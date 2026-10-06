import copy, re
from lxml import etree
exec(open('../../c7b/edit7b.py').read().split('import re as _re')[0])
Mt='{%s}t'%M

def allreplace(p, old, new, count=None):
    n=0
    for t in list(p.iter(q('w:t')))+list(p.iter(Mt)):
        if t.text and old in t.text:
            n+=t.text.count(old); t.text=t.text.replace(old,new)
    assert n>0,(old,text_of(p)[:80])
    if count: assert n==count,(old,n)

T=[
 (237,'The former 700-to-644 V window fails even the zero-inductor SPWM bound, and its 8.61 mH inductor would require about 310 V converter RMS: correct capacitor arithmetic alone did not make that design feasible.',
      'For comparison, a 700 V bus with the same 8% droop falls to 644 V, below even the 677.7 V zero-drop SPWM bound, and a larger 8.61 mH inductor would need about 310 V converter RMS. A correct capacitor-energy calculation alone does not make a design feasible.'),
 (478,'The former 150-to-142.5 V window lacked filter-voltage headroom. ',''),
 (572,' and is not constrained to an invented ±2 kW bound',''),
 (785,'there is no universal 25% crossover.','no single sag depth marks a general crossover between the two arrangements.'),
 (422,'Consequently the calculated AC export approaches, but is not identically, the ideal 4.8 kW sag and −3.2 kW swell values.',
      'Consequently the calculated mean AC export is about 5.0 kW during the sag and −3.5 kW during the swell, rather than the ideal 4.8 kW and −3.2 kW: the 5° phase lag of H at 50 Hz turns part of the injection toward the lagging load current.'),
 (468,' At 95 % conversion efficiency the battery delivers 1.89 kJ.',''),
 (183,'a numerical range is not universal.','no single numerical range suits every design.'),
 (210,'These are declared allowances, not universal safe ratings.','These are declared screening allowances, not safe ratings in themselves.'),
 (384,'adding a positive global d-axis voltage is not universally a loss-absorption command.','a positive d-axis voltage absorbs real power only when it opposes the load current.'),
 (387,'No universal 1 to 2 ms response should be assigned to an algorithm name.','An algorithm name alone does not imply a 1 to 2 ms response.'),
 (649,'A small rating is possible when the required harmonic voltage is small, but is not universal.','A small rating follows only when the required harmonic voltage is small.'),
 (657,'Virtual damping is not proof of zero energy exchange or stability under delay.','Virtual damping implies neither zero energy exchange nor stability under delay.'),
 (791,'Duration alone does not establish a universal capacitor, supercapacitor, flywheel or battery boundary.','Duration alone does not decide between capacitor, supercapacitor, flywheel and battery storage.'),
 (793,'not universal storage-technology boundaries','not storage-technology boundaries'),
 (801,'a universal percentage of kVA rating','a fixed percentage of kVA rating'),
 (838,'they are not universal requirements for every custom-power device','they do not automatically apply to every custom-power device'),
]
def findp(o):
    hits=[p for p in body.iter(q('w:p')) if o in text_of(p)]
    assert len(hits)==1,(o,len(hits))
    return hits[0]
for i,o,n in T: treplace(findp(o),o,n)

# Example 9.28 denominators
allreplace(E[668],'0.3506','0.3523',2); allreplace(E[668],'1.078','1.097',2); allreplace(E[668],'0.0093','0.0091',1)

# Section 9.9.8 heading and its three figures
h=E[866]; set_style(h,'Heading3')
for r in h.iter(q('w:r')):
    rp=r.find('w:rPr',ns)
    if rp is not None: r.remove(rp)
for i in (868,871,874): set_style(E[i],'CaptionedFigure')
for i in (869,872,875): set_style(E[i],'ImageCaption')

# run-in subheads: chapter style is italic; convert bold leads to italic
for i,p in enumerate(E):
    if p.tag!=q('w:p'): continue
    st=p.find('w:pPr/w:pStyle',ns)
    if st is None or st.get(q('w:val')) not in ('BodyText','FirstParagraph'): continue
    r=p.find('w:r',ns)
    if r is None or r.find('w:rPr/w:b',ns) is None: continue
    t=''.join(x.text or '' for x in r.iter(q('w:t')))
    if t.endswith('.') and len(t.split())<=7 and t.strip()!='Solution.':
        rp=r.find('w:rPr',ns)
        for tag in ('w:b','w:bCs'):
            for e in rp.findall(tag,ns): rp.remove(e)
        etree.SubElement(rp,q('w:i')); etree.SubElement(rp,q('w:iCs'))
        print('italic lead',i,t)

# key-equation table order
tbl=E[881]
rows=tbl.findall('w:tr',ns)
def row(label): return [r for r in rows if text_of(r).strip().startswith(label)][0]
row('(9.45)').addprevious(row('(9.44)'))
row('(9.57)').addprevious(row('(9.55)'))

# redrawn Fig 9.33
from PIL import Image
import shutil
A='http://schemas.openxmlformats.org/drawingml/2006/main';WP='http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing';R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
for rid,fn in {'rId206':'fig9_33.png'}.items():
    shutil.copy('../figs/'+fn,'work/word/media/%s.png'%rid)
    w,hh=Image.open('../figs/'+fn).size
    for blip in body.iter('{%s}blip'%A):
        if blip.get('{%s}embed'%R)==rid:
            inl=blip
            while inl.tag!='{%s}inline'%WP: inl=inl.getparent()
            ext=inl.find('{%s}extent'%WP); cx=int(int(ext.get('cx'))*0.75); cy=int(cx*hh/w)
            ext.set('cx',str(cx)); ext.set('cy',str(cy))
            for x in inl.iter('{%s}ext'%A):
                if x.get('cx'): x.set('cx',str(cx)); x.set('cy',str(cy))
exec(open('refedits.py').read())
nb=0
for p in body.iter(q('w:p')):
    r=p.find('w:r',ns)
    if r is None: continue
    t=r.find('w:t',ns)
    if t is None or not (t.text or '').startswith('Solution.'): continue
    if r.find('w:rPr/w:b',ns) is not None: continue
    if t.text!='Solution.':
        r2=copy.deepcopy(r); r.addnext(r2)
        r2.find('w:t',ns).text=t.text[len('Solution.'):]
        r2.find('w:t',ns).set('{http://www.w3.org/XML/1998/namespace}space','preserve')
        t.text='Solution.'
    rp=r.find('w:rPr',ns)
    if rp is None: rp=etree.Element(q('w:rPr')); r.insert(0,rp)
    for e in rp.findall('w:i',ns)+rp.findall('w:iCs',ns): rp.remove(e)
    etree.SubElement(rp,q('w:b')); nb+=1
print('bolded Solution labels',nb)
for mc in body.iter('{%s}mcPr'%M):
    c=mc.find('{%s}count'%M)
    if c is not None: mc.remove(c); mc.insert(0,c)
tree.write(DOC, xml_declaration=True, encoding='UTF-8', standalone=True)
print('edits applied')
