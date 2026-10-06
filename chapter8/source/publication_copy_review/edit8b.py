import copy, re
from lxml import etree
exec(open('../../c7b/edit7b.py').read().split('import re as _re')[0])
Mt = '{%s}t' % M

def mreplace(p, old, new):
    for t in p.iter(Mt):
        if t.text and old in t.text:
            t.text = t.text.replace(old, new); return
    raise AssertionError(old)

def boldlead(p, lead):
    r = p.find('w:r', ns); t = r.find('w:t', ns)
    assert t.text.startswith(lead), t.text[:50]
    r2 = copy.deepcopy(r); r.addnext(r2)
    t.text = lead
    r2.find('w:t', ns).text = t.text and r2.find('w:t', ns).text[len(lead):]
    r2.find('w:t', ns).set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    rPr = r.find('w:rPr', ns)
    if rPr is None: rPr = etree.Element(q('w:rPr')); r.insert(0, rPr)
    if rPr.find('w:b', ns) is None: etree.SubElement(rPr, q('w:b'))

# ---------- paragraph rewrites ----------
replace_content(E[13], 'P13')
append_content(E[461], 'P461A')

T = [
 (23, 'rather than a universal number of cycles.', 'and cannot be summarized by a fixed number of cycles.'),
 (111, 'Figure 8.10 is an explicit mathematical response sketch, not a measured trace or a validated UPFC simulation. It illustrates', 'Figure 8.10 is an analytical sketch rather than a measured or simulated trace. It illustrates'),
 (113, 'Analytical response sketch, not a validated UPFC simulation. At', 'Analytical response sketch. At'),
 (128, 'Ratings, energy balance and transformer/protection duties must be distinguished from the choice of semiconductor and waveform synthesis.', 'Its rating, energy-balance and transformer-protection lessons remain relevant whichever semiconductor and waveform-synthesis method a newer design adopts.'),
 (182, ' These are different milestones.', ''),
 (32, ', separates into', ', follows from the expanded current:'),
 (140, 'Their sum supplies neither an external energy source nor independent commands: it must cover', 'Their sum is not an external energy source: it must cover'),
 (128, 'entered test operation in May 1998 [6], [7].', 'was commissioned in mid-1998, after its shunt STATCOM stage had entered service in 1997 [6], [7].'),
 (211, 'This is a mathematical selector model; ordinary SCR gating alone does not realize an interior-angle transfer.', 'This is a mathematical selector model, not a thyristor-circuit simulation.'),
 (212, 'A nonoverlap instruction by itself supplies no current-transfer path.', 'Blocking the outgoing valve before the incoming path conducts would simply interrupt the load current.'),
 (263, 'it does not universally eliminate fault contribution.', 'it does not in general eliminate the fault contribution.'),
 (277, '“A few milliseconds” alone is not a universal first-peak guarantee.', 'A quoted operating time of a few milliseconds therefore does not by itself guarantee a lower first peak.'),
 (295, ' They are illustrative circuit results, not equipment certification.', ''),
 (317, 'rather than a universal quarter-cycle.', 'so a quarter-cycle figure is not a general rating.'),
 (317, 'between feeders', 'between feeders [17]'),
 (321, 'so no universal reset time should be assigned.', 'so no single reset time applies to all designs.'),
 (339, 'There is no universal clamping level of 1.7 times normal peak.', 'The protective level is therefore a design result; a ratio such as 1.7 times the normal peak is an example, not a standard value.'),
 (394, 'a single percentage cannot characterize all first-generation converters.', 'loss and footprint comparisons are meaningful only for specific designs.'),
 (463, 'Local crossing angles alone are not a stability proof.', 'Model parameters: Lf = 1 mH, Kp = 15 Ω, Td = 150 μs, Rg = 0.05 Ω. Local crossing angles alone do not establish stability.'),
 (533, 'These are an outlook, not proof of novelty or a guarantee of publication. A project-specific current literature review and reproducible comparison with established methods remain necessary.', 'They are an outlook: novelty still has to be established through a current literature review and a reproducible comparison with established methods.'),
 (644, 'Assume an ideal selector able to realize it; ordinary SCR gate withdrawal alone cannot. Find', 'Assume an ideal selector that can realize it. Find'),
 (699, 'No device can honestly be declared', 'No device can be declared'),
 (19, 'phase angle [1], [2], [3].', 'phase angle [1], [2], [3], [9], [10].'),
 (234, 'phase-shifted voltages [13].', 'phase-shifted voltages [13], [14].'),
 (391, 'dominated by power electronics.', 'dominated by power electronics [25].'),
 (454, 'outer loops [27].', 'outer loops [27], [28].'),
 (741, 'Interphase Power Controllers — complementing', 'Interphase Power Controllers: complementing'),
]
for i, o, n in T:
    treplace(E[i], o, n)

# Example 8.15: answer the question that is asked
p = E[386]
treplace(p, text_of(p), 'Solution. The natural first candidate is a series-only arrangement: an IPFC if controllable real-power exchange between the overloaded and the underloaded line is needed, or independent quadrature SSSC modules if reactance-based redistribution is enough. Neither adds a shunt energy source at the bus, so the controller itself adds little steady fault infeed, although its transformers, control and bypass sequence still alter fault currents and relay measurements. A UPFC could also redistribute the flow, but its shunt converter contributes rating-limited current during faults, which is unwelcome when the fault level is already close to the breaker rating. Load-flow, contingency and switching/protection studies make the final choice.')

# numerical corrections found in the review
mreplace(E[625], '409.1', '409.0')
mreplace(E[645], '5.4512', '5.4532')

boldlead(E[400], 'Important topology distinctions.')

# ---------- replaced figures (rId -> new file); keep width, adjust height ----------
from PIL import Image
NEWFIG = {'rId144': 'fig8_7.png', 'rId244': 'fig8_29.png', 'rId273': 'fig8_35.png', 'rId291': 'fig8_38.png', 'rId313': 'fig8_42.png'}
import shutil
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
WP = 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
for rid, fn in NEWFIG.items():
    shutil.copy('../figs/' + fn, 'work/word/media/%s.png' % rid)
    w, h = Image.open('../figs/' + fn).size
    for blip in body.iter('{%s}blip' % A):
        if blip.get('{%s}embed' % R) == rid:
            inl = blip
            while inl.tag != '{%s}inline' % WP: inl = inl.getparent()
            ext = inl.find('{%s}extent' % WP)
            cx = int(ext.get('cx')); cy = int(cx * h / w)
            if cy > 5.4e6:  # keep tall figures within the page
                cy = int(5.4e6); cx = int(cy * w / h)
            ext.set('cx', str(cx)); ext.set('cy', str(cy))
            for x in inl.iter('{%s}ext' % A):
                if x.get('cx'): x.set('cx', str(cx)); x.set('cy', str(cy))

# ---------- renumber citations in order of first appearance ----------
refhead = E[705]
kids = list(body)
cut = kids.index(refhead)
order = []
cite = re.compile(r'\[(\d+)\]')
for el in kids[:cut]:
    for t in el.iter(q('w:t')):
        if t.text:
            for n in cite.findall(t.text):
                n = int(n)
                if n not in order: order.append(n)
refps = [el for el in kids[cut+1:] if el.tag == q('w:p') and re.match(r'\[(\d+)\]', text_of(el))]
nums = [int(re.match(r'\[(\d+)\]', text_of(el)).group(1)) for el in refps]
missing = [n for n in nums if n not in order]
assert not missing, missing
assert len(order) == len(nums), (order, nums)
mp = {old: k + 1 for k, old in enumerate(order)}
for el in kids[:cut]:
    for t in el.iter(q('w:t')):
        if t.text and cite.search(t.text):
            t.text = cite.sub(lambda m: '[%d]' % mp[int(m.group(1))], t.text)
contents = {}
for el, n in zip(refps, nums):
    contents[mp[n]] = [copy.deepcopy(c) for c in el if c.tag != q('w:pPr')]
for k, el in enumerate(refps, 1):
    for c in list(el):
        if c.tag != q('w:pPr'): el.remove(c)
    for c in contents[k]: el.append(c)
    t0 = el.find('.//w:t', ns)
    t0.text = re.sub(r'^\[\d+\]', '[%d]' % k, t0.text)
    for t in el.iter(q('w:t')):
        if t is not t0 and t.text and cite.search(t.text):
            t.text = cite.sub(lambda m: '[%d]' % mp[int(m.group(1))], t.text)
    rest = t0.text[len('[%d]' % k):]
    if cite.search(rest):
        t0.text = '[%d]' % k + cite.sub(lambda m: '[%d]' % mp[int(m.group(1))], rest)
# figure alt texts / docPr descr do not carry citations
for mc in body.iter('{%s}mcPr' % M):
    c = mc.find('{%s}count' % M)
    if c is not None:
        mc.remove(c); mc.insert(0, c)
open('refmap.txt', 'w').write(repr(mp))
tree.write(DOC, xml_declaration=True, encoding='UTF-8', standalone=True)
print('edits applied', mp)
