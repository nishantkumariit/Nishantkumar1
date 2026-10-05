"""Bring work/ into OOXML schema order (pre-existing issues of the source file plus pandoc math)."""
import re
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
M = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
ns = {'w': W, 'm': M}
q = lambda t: '{%s}%s' % ((W if t.split(':')[0] == 'w' else M), t.split(':')[1])

SO = ['name', 'aliases', 'basedOn', 'next', 'link', 'autoRedefine', 'hidden', 'uiPriority', 'semiHidden', 'unhideWhenUsed', 'qFormat', 'locked', 'personal', 'personalCompose', 'personalReply', 'rsid', 'pPr', 'rPr', 'tblPr', 'trPr', 'tcPr', 'tblStylePr']
PO = ['pStyle', 'keepNext', 'keepLines', 'pageBreakBefore', 'framePr', 'widowControl', 'numPr', 'suppressLineNumbers', 'pBdr', 'shd', 'tabs', 'suppressAutoHyphens', 'kinsoku', 'wordWrap', 'overflowPunct', 'topLinePunct', 'autoSpaceDE', 'autoSpaceDN', 'bidi', 'adjustRightInd', 'snapToGrid', 'spacing', 'ind', 'contextualSpacing', 'mirrorIndents', 'suppressOverlap', 'jc', 'textDirection', 'textAlignment', 'textboxTightWrap', 'outlineLvl', 'divId', 'cnfStyle', 'rPr', 'sectPr', 'pPrChange']
RO = ['rStyle', 'rFonts', 'b', 'bCs', 'i', 'iCs', 'caps', 'smallCaps', 'strike', 'dstrike', 'outline', 'shadow', 'emboss', 'imprint', 'noProof', 'snapToGrid', 'vanish', 'webHidden', 'color', 'spacing', 'w', 'kern', 'position', 'sz', 'szCs', 'highlight', 'u', 'effect', 'bdr', 'shd', 'fitText', 'vertAlign', 'rtl', 'cs', 'em', 'lang', 'eastAsianLayout', 'specVanish', 'oMath']
TBO = ['tblStyle', 'tblpPr', 'tblOverlap', 'bidiVisual', 'tblStyleRowBandSize', 'tblStyleColBandSize', 'tblW', 'jc', 'tblCellSpacing', 'tblInd', 'tblBorders', 'shd', 'tblLayout', 'tblCellMar', 'tblLook', 'tblCaption', 'tblDescription']
TCO = ['cnfStyle', 'tcW', 'gridSpan', 'hMerge', 'vMerge', 'tcBorders', 'shd', 'noWrap', 'tcMar', 'textDirection', 'tcFitText', 'vAlign', 'hideMark']
DPO = ['begChr', 'sepChr', 'endChr', 'grow', 'shp', 'ctrlPr']
SETO = 'writeProtection view zoom removePersonalInformation removeDateAndTime doNotDisplayPageBoundaries displayBackgroundShape printPostScriptOverText printFractionalCharacterWidth printFormsData embedTrueTypeFonts embedSystemFonts saveSubsetFonts saveFormsData mirrorMargins alignBordersAndEdges bordersDoNotSurroundHeader bordersDoNotSurroundFooter gutterAtTop hideSpellingErrors hideGrammaticalErrors activeWritingStyle proofState formsDesign attachedTemplate linkStyles stylePaneFormatFilter stylePaneSortMethod documentType mailMerge revisionView trackRevisions doNotTrackMoves doNotTrackFormatting documentProtection autoFormatOverride styleLockTheme styleLockQFSet defaultTabStop autoHyphenation consecutiveHyphenLimit hyphenationZone doNotHyphenateCaps showEnvelope summaryLength clickAndTypeStyle defaultTableStyle evenAndOddHeaders bookFoldRevPrinting bookFoldPrinting bookFoldPrintingSheets drawingGridHorizontalSpacing drawingGridVerticalSpacing displayHorizontalDrawingGridEvery displayVerticalDrawingGridEvery doNotUseMarginsForDrawingGridOrigin drawingGridHorizontalOrigin drawingGridVerticalOrigin doNotShadeFormData noPunctuationKerning characterSpacingControl printTwoOnOne strictFirstAndLastChars noLineBreaksAfter noLineBreaksBefore savePreviewPicture doNotValidateAgainstSchema saveInvalidXml ignoreMixedContent alwaysShowPlaceholderText doNotDemarcateInvalidXml saveXmlDataOnly useXSLTWhenSaving saveThroughXslt showXMLTags alwaysMergeEmptyNamespace updateFields hdrShapeDefaults footnotePr endnotePr compat docVars rsids mathPr attachedSchema themeFontLang clrSchemeMapping doNotIncludeSubdocsInStats doNotAutoCompressPictures forceUpgrade captions readModeInkLockDown smartTagType schemaLibrary shapeDefaults doNotEmbedSmartTags decimalSymbol listSeparator'.split()


def reorder(el, order):
    kids = list(el)
    for k in kids:
        el.remove(k)
    key = lambda k: order.index(etree.QName(k).localname) if etree.QName(k).localname in order else 999
    for k in sorted(kids, key=key):
        el.append(k)


def clean_text(el):
    if el.text and el.text.strip():
        el.text = None
    for c in el:
        if c.tail and c.tail.strip():
            c.tail = None


def fix_tree(root):
    for s in root.iter(q('w:style')):
        reorder(s, SO)
    for p in root.iter(q('w:pPr')):
        reorder(p, PO)
    for r in root.iter(q('w:rPr')):
        clean_text(r)
        reorder(r, RO)
    for t in root.iter(q('w:tblPr')):
        reorder(t, TBO)
    for t in root.iter(q('w:tcPr')):
        reorder(t, TCO)
    for d in root.iter(q('m:dPr')):
        reorder(d, DPO)
    for r in root.iter(q('m:rPr')):
        if r.find('m:nor', ns) is not None:
            for s in r.findall('m:sty', ns) + r.findall('m:scr', ns):
                r.remove(s)
        reorder(r, ['lit', 'nor', 'scr', 'sty', 'brk', 'aln'])


for f in ['styles', 'document', 'numbering']:
    path = 'work/word/%s.xml' % f
    t = etree.parse(path)
    root = t.getroot()
    fix_tree(root)
    if f == 'numbering':
        for n in root.iter(q('w:nsid')):
            n.set(q('w:val'), n.get(q('w:val')).rjust(8, '0'))
    if f == 'document':
        # unique bookmark ids
        seen = {}
        nxt = 10000
        for bs in root.iter(q('w:bookmarkStart')):
            i = bs.get(q('w:id'))
            if i in seen:
                seen[i] += 1
                new = str(nxt); nxt += 1
                bs.set(q('w:id'), new)
                # matching end: next bookmarkEnd with old id after this start
                for be in bs.itersiblings():
                    if be.tag == q('w:bookmarkEnd') and be.get(q('w:id')) == i:
                        be.set(q('w:id'), new)
                        break
            else:
                seen[i] = 0
        for wt in root.iter(q('w:t')):
            if wt.text and (wt.text != wt.text.strip()):
                wt.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    t.write(path, xml_declaration=True, encoding='UTF-8', standalone=True)

st = etree.parse('work/word/settings.xml')
reorder(st.getroot(), SETO)
st.write('work/word/settings.xml', xml_declaration=True, encoding='UTF-8', standalone=True)
print('schema order fixed')
