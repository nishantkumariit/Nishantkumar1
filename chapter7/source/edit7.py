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


# ---------- 1. content rewrites ----------
replace_content(E[109], 'P109')
replace_content(E[129], 'P129', 'FirstParagraph')
replace_content(E[168], 'P168', 'FirstParagraph')
replace_content(E[171], 'P171', 'FirstParagraph')
replace_content(E[209], 'P209')
replace_content(E[224], 'P224')
replace_content(E[345], 'P345', 'BodyText')
replace_content(E[351], 'P351', 'BodyText')
replace_content(E[352], 'P352', 'BodyText')
replace_content(E[322], 'P322', 'BodyText')
replace_content(E[356], 'P356', 'BodyText')
replace_content(E[468], 'P468')
replace_content(E[569], 'P569')
replace_content(E[597], 'P597')
replace_content(E[608], 'P608')
replace_content(E[611], 'P611')
replace_content(E[763], 'P763', 'BodyText')
append_content(E[679], 'P679A')

# restyle the remaining later-added "Normal" paragraphs
for i in [130, 131, 169, 172, 265, 266, 267, 269, 270, 346, 348, 349, 354, 355]:
    set_style(E[i], 'BodyText')

# ---------- 2. text corrections ----------
treplace(E[37], 'give numerical examples', 'work through these relations numerically')
treplace(E[77], 'Vithayathil and co-workers proposed rapid adjustment of network impedance with a thyristor-controlled series capacitor in 1986 [1].',
         'Vithayathil and co-workers conceived the rapid adjustment of network impedance in the mid-1980s, a scheme in which a thyristor-controlled reactor in parallel with a series capacitor varies the line reactance, and reported system case studies at CIGRE in 1988 [1].')
treplace(E[77], 'and Gyugyi introduced the SSSC in 1989 as part of the voltage-source family that also includes the STATCOM and UPFC [4].',
         'and Gyugyi proposed the SSSC in 1989 as part of the voltage-source family that also includes the STATCOM and UPFC; its full analysis appeared later [4].')
treplace(E[215], 'reaches more than twice the peak line current and flows against it, so the capacitor current is boosted during the reversal',
         'reaches about 1.7 times the peak line current and flows against it, so during the reversal the capacitor current is boosted to about 2.7 times the peak line current')
treplace(E[420], 'at about 180 ms', 'at about 190 ms')
treplace(E[647], '14.65', '14.64')
treplace(E[799], 'is SSR-neutral but only raises flow;', 'is SSR-neutral, but it can reduce flow only within its limited inductive vernier;')

treplace(E[348], 'Early high-power SSSC concepts used two-level or three-level voltage-source converters with multi-pulse transformer arrangements. Modern multilevel approaches synthesize', 'Multilevel converters synthesize')
treplace(E[265], 'The complete TCSC controller contains an external and an internal problem.', 'The complete TCSC controller solves two problems, an external one and an internal one.')

# Table 7.2 rows (Kanpur-Ballabhgarh, Rourkela-Raipur)
tbl72 = E[181]
rows = tbl72.findall('w:tr', ns)
for r in rows:
    cells = r.findall('w:tc', ns)
    c0 = text_of(cells[0])
    if c0.startswith('Kanpur'):
        treplace(cells[1].find('.//w:p', ns), '2000s (commissioned in two phases)', '2000s, in two phases')
        treplace(cells[3].find('.//w:p', ns), 'First indigenous TCSC (BHEL with PGCIL)',
                 'First indigenous TCSC (BHEL with POWERGRID); a thyristor-controlled section varies an 8% fixed segment up to 20%')
    if c0.startswith('Rourkela'):
        treplace(cells[3].find('.//w:p', ns), 'Inter-regional power transfer and damping',
                 'First TCSC in India; East-West inter-regional transfer and damping')

# ---------- 3. Table 7.1 caption and introduction ----------
cap72 = E[180]
cap71 = copy.deepcopy(cap72)
for t in cap71.iter(q('w:t')):
    t.text = ''
cap71.findall('.//w:t', ns)[0].text = 'Table 7.1 Series FACTS controllers at a glance.'
intro = copy.deepcopy(B['T71INTRO'])
set_style(intro, 'BodyText')
E[14].addprevious(intro)
E[14].addprevious(cap71)

# ---------- 4. Table 7.4: caption above, borders like Table 7.3 ----------
cap74 = E[367]
for ch in list(cap74):
    cap74.remove(ch)
for ch in copy.deepcopy(cap72):
    cap74.append(ch)
for t in cap74.iter(q('w:t')):
    t.text = ''
cap74.findall('.//w:t', ns)[0].text = 'Table 7.4 Service-oriented comparison of the four series FACTS controller families.'
E[366].addprevious(cap74)
old = E[366].find('w:tblPr', ns)
new = copy.deepcopy(E[362].find('w:tblPr', ns))
new.find('w:tblCaption', ns).set(q('w:val'), 'Table 7.4 Service-oriented comparison of the four series FACTS controller families.')
E[366].replace(old, new)
for tc in E[366].iter(q('w:tc')):
    tcPr = tc.find('w:tcPr', ns)
    if tcPr.find('w:vAlign', ns) is None:
        va = etree.SubElement(tcPr, q('w:vAlign'))
        va.set(q('w:val'), 'center')

# ---------- 5. moves ----------
def move_after(anchor, items):
    a = anchor
    for it in items:
        a.addnext(it)
        a = it

move_after(E[299], [E[351]])                    # rating -> 7.5.3
move_after(E[319], [E[352], E[348], E[349]])    # protection, topologies -> 7.5.5
move_after(E[328], [E[322]])                    # SSCI caveat -> end of 7.5.6
move_after(E[334], [E[345], E[346], E[354], E[355]])   # control -> 7.5.7
move_after(E[363], [E[356]])                    # selection -> 7.6 (before Table 7.4)
move_after(E[241], [E[265]])                    # TCSC control chain -> 7.4.8
move_after(E[244], [E[266]])                    # POD channel -> 7.4.8
move_after(E[260], [E[267]])                    # fault behaviour -> 7.4.11
move_after(E[256], [E[269], E[270]])            # model hierarchy -> 7.4.10

# ---------- 6. deletions (duplicates, empty paragraphs, merged headings) ----------
for i in [264, 268, 314, 315, 316, 317, 323, 324, 325, 326, 337, 338, 344, 347, 350, 353]:
    p = E[i]
    p.getparent().remove(p)

# ---------- 7. Section 7.7 examples: separate heading paragraphs ----------
hdr_proto = E[47]
for i in [440, 443, 446, 449, 452]:
    p = E[i]
    rs = [r for r in p if r.tag == q('w:r')]
    lab = text_of(rs[0]).strip()              # 'Example 7.H.'
    body_run = rs[1]
    bt = text_of(body_run)
    m = re.match(r'\s*([^.]*\.)\s*(.*)', bt, re.S)
    title, rest = m.group(1)[:-1], m.group(2)
    h = copy.deepcopy(hdr_proto)
    hr = h.findall('w:r', ns)
    hr[0].find('w:t', ns).text = 'Example'
    hr[1].find('w:t', ns).text = ' ' + lab.split()[1] + ' ' + title
    p.addprevious(h)
    p.remove(rs[0])
    ts = body_run.findall('w:t', ns)
    ts[0].text = rest
    for t in ts[1:]:
        body_run.remove(t)
    set_style(p, 'FirstParagraph')

# ---------- 8. example renumbering ----------
order = []
for p in body.iter(q('w:p')):
    s = text_of(p).strip()
    m = re.match(r'Example\s+7\.([A-L]|\d+)[ .]', s)
    if m and (p.find('w:pPr/w:pStyle', ns) is None or p.find('w:pPr/w:pStyle', ns).get(q('w:val')) in ('Heading3',)):
        order.append(m.group(1))
EMAP = {old: str(k + 1) for k, old in enumerate(order)}
assert len(EMAP) == len(order) == 43, (len(order), order)

tok = r'7\.(?:[A-L]|\d+)'
def ren_ex(s):
    def fix(m):
        return re.sub(r'7\.([A-L]|\d+)', lambda n: '7.' + EMAP[n.group(1)], m.group(0))
    s = re.sub(r'Examples?\s+' + tok + r'(?:\s*(?:,|and|to)\s*' + tok + r')*', fix, s)
    return s

for t in body.iter(q('w:t')):
    if t.text and '7.' in t.text:
        t.text = ren_ex(t.text)
# lettered headings: "Example" bold run + " 7.A. Title"
for p in body.iter(q('w:p')):
    rs = p.findall('w:r', ns)
    if len(rs) >= 2 and text_of(rs[0]) == 'Example':
        t = rs[1].find('w:t', ns)
        t.text = re.sub(r'^\s*7\.([A-L]|\d+)\.?\s*', lambda n: ' 7.%s. ' % EMAP[n.group(1)], t.text)

# ---------- 9. figure renumbering (Figures 7.27 and 7.28 removed) ----------
def fmap(n):
    n = int(n)
    assert n not in (27, 28), n
    return str(n - 2 if n >= 29 else n)
def ren_fig(s):
    def fix(m):
        return re.sub(r'7\.(\d+)', lambda n: '7.' + fmap(n.group(1)), m.group(0))
    return re.sub(r'Figures?\s+7\.\d+(?:\s*(?:,|and|to)\s*7\.\d+)*', fix, s)
for t in body.iter(q('w:t')):
    if t.text and 'Figure' in t.text:
        t.text = ren_fig(t.text)

tree.write(DOC, xml_declaration=True, encoding='UTF-8', standalone=True)
print('examples mapped:', EMAP)
