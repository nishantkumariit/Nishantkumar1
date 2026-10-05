"""Widen the expression column of Table 7.8 so Equation (7.16) is not clipped."""
from lxml import etree
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; ns={'w':W}
q=lambda n:'{%s}%s'%(W,n)
P='work/word/document.xml'
d=etree.parse(P); b=d.getroot().find('w:body',ns)
WID=[760,5560,1598]
for t in b.iter(q('tbl')):
    cap=t.find('w:tblPr/w:tblCaption',ns)
    if cap is None or 'Table 7.8' not in cap.get(q('val')): continue
    for g,wd in zip(t.find('w:tblGrid',ns).findall('w:gridCol',ns),WID): g.set(q('w'),str(wd))
    tp=t.find('w:tblPr',ns)
    lay=etree.SubElement(tp,q('tblLayout')); lay.set(q('type'),'fixed')
    for r in t.findall('w:tr',ns):
        for c,wd in zip(r.findall('w:tc',ns),WID):
            tcPr=c.find('w:tcPr',ns)
            for o in tcPr.findall('w:tcW',ns): tcPr.remove(o)
            tw=etree.Element(q('tcW')); tw.set(q('w'),str(wd)); tw.set(q('type'),'dxa'); tcPr.insert(0,tw)
d.write(P,xml_declaration=True,encoding='UTF-8',standalone=True); print('table 7.8 widened')
