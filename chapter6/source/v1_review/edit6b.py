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



for k in ['P51','P258','P288','P317','P379','P448','P533','P629','P639','P677','P682','P688','P696','P726','P735','P738','P740','P741','P743','P285','P113','P125','P126','P128','P443','P444','P693','P705']:
    replace_content(E[int(k[1:])], k)

treplace(E[22], 'a weak bus has greater voltage sensitivity. This does not make a weak network easier to stabilize: its control interactions and fault limits must also be checked.',
         'a weak bus has greater voltage sensitivity, and for the same reason its voltage-control loop is more prone to interaction.')
treplace(E[42], 'without an underline', 'without an overbar')
treplace(E[953], 'The unequal b-c and c-a reactive currents', 'The equal and opposite b-c and c-a reactive currents')
treplace(E[728], '; it is an illustrative static law, not transient protection certification.', ', an illustrative static law.')
treplace(E[488], 'and the Hitachi Energy Gerdau case [43].', 'and the Hitachi Energy Gerdau case [43]. Years are in-service years, which can differ by a year from the contract years in supplier lists.')

treplace(E[283], 'Figure 6.21 shows simulated closing transients', 'Figure 6.21 shows the computed closing transients')
treplace(E[488], 'from the Siemens reference list [41]', 'from the Siemens reference list [41], with the Devers data from [40],')
E[114].addnext(E[113])          # derivation note after Equation (6.16)

for tbl in body.iter(q('w:tbl')):
    for r in tbl.findall('w:tr', ns):
        cells = r.findall('w:tc', ns)
        if len(cells) < 2: continue
        c0 = text_of(cells[0])
        if c0.startswith('Radsted'): treplace(cells[1].find('.//w:p', ns), '2006', '2007')
        if c0.startswith('Islington'): treplace(cells[1].find('.//w:p', ns), '2009', '2010')

tree.write(DOC, xml_declaration=True, encoding='UTF-8', standalone=True)
print('edits applied')
