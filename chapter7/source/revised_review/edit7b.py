"""Apply the Chapter 7 corrections to work/word/document.xml (after merge_runs).
Indices are body-child positions of the ORIGINAL document (same as orig.txt P-numbers)."""
import copy, re
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
M = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
ns = {'w': W, 'm': M}
q = lambda t: '{%s}%s' % ((W if t.split(':')[0] == 'w' else M), t.split(':')[1])

DOC = 'work/word/document.xml'
tree = etree.parse(DOC)
body = tree.getroot().find('w:body', ns)
E = list(body)                       # original indices

# ---------- pandoc blocks ----------
bl = list(etree.parse('bl/word/document.xml').getroot().find('w:body', ns))
B = {}
cur = None
for el in bl:
    if el.tag != q('w:p'):
        continue
    txt = ''.join(t.text or '' for t in el.iter(q('w:t')))
    if txt.startswith('@@'):
        cur = txt[2:].strip()
        continue
    if cur:
        B[cur] = el
        cur = None


def text_of(p):
    return ''.join(t.text or '' for t in p.iter(q('w:t')))


def set_style(p, style):
    pPr = p.find('w:pPr', ns)
    if pPr is None:
        pPr = etree.SubElement(p, q('w:pPr'))
        p.insert(0, pPr)
    for ch in list(pPr):
        if ch.tag != q('w:numPr'):
            pPr.remove(ch)
    ps = etree.Element(q('w:pStyle'))
    ps.set(q('w:val'), style)
    pPr.insert(0, ps)
    # drop run-level font overrides so the style governs
    for r in p.iter(q('w:r')):
        rPr = r.find('w:rPr', ns)
        if rPr is not None:
            for f in rPr.findall('w:rFonts', ns):
                rPr.remove(f)


def replace_content(p, key, style=None):
    src = B[key]
    for ch in list(p):
        if ch.tag != q('w:pPr'):
            p.remove(ch)
    for ch in src:
        if ch.tag != q('w:pPr'):
            p.append(copy.deepcopy(ch))
    if style:
        set_style(p, style)


def append_content(p, key):
    sp = etree.SubElement(p, q('w:r'))
    t = etree.SubElement(sp, q('w:t'))
    t.text = ' '
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    for ch in B[key]:
        if ch.tag != q('w:pPr'):
            p.append(copy.deepcopy(ch))


def treplace(p, old, new, count=1):
    """replace text spanning consecutive w:t nodes of a paragraph (math excluded)"""
    ts = [t for t in p.iter(q('w:t'))]
    s = ''.join(t.text or '' for t in ts)
    k = s.find(old)
    assert k >= 0, (old, s[:200])
    pos = 0
    first = True
    end = k + len(old)
    for t in ts:
        a, b = pos, pos + len(t.text or '')
        pos = b
        if b <= k or a >= end:
            continue
        txt = t.text or ''
        lo, hi = max(k, a) - a, min(end, b) - a
        if first:
            t.text = txt[:lo] + new + txt[hi:]
            first = False
        else:
            t.text = txt[:lo] + txt[hi:]
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')



import re as _re
keys=['P15','P43','P47','P69','P76','P184','P216','P232','P245','P250','P293','P298','P300','P362','P396','P418','P447','P513','P549','P647','P755']
for k in keys:
    replace_content(E[int(k[1:])], k)
append_content(E[80], 'P80A')

treplace(E[214], 'Example 7.31 provides numerical values beside this derivation through the cross-reference; Example 7.33 connects angle, waveform stress and reactor selection.', 'Example 7.31 gives numerical values for this derivation, and Example 7.33 connects angle, waveform stress and reactor selection.')
treplace(E[181], 'omission of a separate triggered gap is a design-specific decision, not a consequence that every fast valve permits.', 'whether a separate triggered gap can be omitted depends on the design.')
treplace(E[234], 'A ±2° gap around the first pole is genuinely excluded.', 'A ±2° band around the first pole is excluded.')
treplace(E[450], 'damping ratios 12.6635% at 150 ms and 9.8303% at 200 ms, printed as 12.7% and 9.8%.', 'damping ratios of 12.7% at 150 ms and 9.8% at 200 ms.')
treplace(E[693], 'The capacitor and reactor component reactances at 33 Hz are 15.15 Ω and 0.88 Ω. These do not determine', 'These component reactances do not determine')
treplace(E[763], 'Find XC, electrical', 'Find the capacitor reactance, the electrical')

# Rourkela-Raipur row and reference [26]
for tbl in body.iter(q('w:tbl')):
    for r in tbl.findall('w:tr', ns):
        cells = r.findall('w:tc', ns)
        if len(cells) >= 4 and text_of(cells[0]).startswith('Rourkela'):
            treplace(cells[1].find('.//w:p', ns), 'Reported in early project literature', '2004')
            p3 = cells[3].find('.//w:p', ns)
            treplace(p3, text_of(p3), 'First TCSC in India; two banks at the Raipur end for East–West transfer and inter-area damping [26]')
treplace(E[829], 'historical customer case, technical configuration and damping application.', 'historical customer case: TCSC installed 2004, first in India; configuration and damping application.')

# move angle-reference guide to the end of Section 7.1.7
cap, tab = E[85], E[86]
E[80].addnext(cap); cap.addnext(tab)

# renumber tables 7.2..7.8 -> 7.3..7.9 (text and alt-text captions)
def rt(s):
    return _re.sub(r'(Tables?\s+)7\.(\d+)', lambda m: m.group(1)+'7.'+(str(int(m.group(2))+1) if int(m.group(2))>=2 else m.group(2)), s)
for t in body.iter(q('w:t')):
    if t.text and 'Table' in t.text: t.text = rt(t.text)
for c in body.iter(q('w:tblCaption')):
    c.set(q('w:val'), rt(c.get(q('w:val'))))
for t in body.iter(q('w:t')):
    if t.text and '7.Z' in t.text: t.text = t.text.replace('7.Z','7.2')

# style the new caption and table like the others
proto_cap = E[16]
for ch in list(cap): cap.remove(ch)
for ch in copy.deepcopy(proto_cap): cap.append(ch)
for t in cap.iter(q('w:t')): t.text=''
cap.findall('.//w:t', ns)[0].text = 'Table 7.2 Angle references used in this chapter (radians in derivations, degrees in numerical results).'
new = copy.deepcopy(E[17].find('w:tblPr', ns))
new.find('w:tblCaption', ns).set(q('w:val'), 'Table 7.2 Angle references used in this chapter.')
tab.replace(tab.find('w:tblPr', ns), new)
for tc in tab.iter(q('w:tc')):
    tcPr = tc.find('w:tcPr', ns)
    if tcPr is None:
        tcPr = etree.Element(q('w:tcPr')); tc.insert(0, tcPr)
    if tcPr.find('w:vAlign', ns) is None:
        va = etree.SubElement(tcPr, q('w:vAlign')); va.set(q('w:val'), 'center')

# normalize the one oversized cell in the model-fidelity table
for t in body.iter(q('w:t')):
    if t.text and t.text.startswith('Linearized converter and network over a'):
        rPr = t.getparent().find('w:rPr', ns)
        for e in rPr.findall('w:sz', ns): e.set(q('w:val'), '19')
        if rPr.find('w:szCs', ns) is None:
            e = etree.SubElement(rPr, q('w:szCs')); e.set(q('w:val'), '19')

tree.write(DOC, xml_declaration=True, encoding='UTF-8', standalone=True)
print('edits applied')
