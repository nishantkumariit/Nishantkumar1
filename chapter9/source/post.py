import re, copy, sys, os, shutil
from lxml import etree
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
M='http://schemas.openxmlformats.org/officeDocument/2006/math'
R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
ns={'w':W,'m':M}
q=lambda t:'{%s}%s'%(ns[t.split(':')[0]],t.split(':')[1])
d='raw/'
tree=etree.parse(d+'word/document.xml'); root=tree.getroot(); body=root.find('w:body',ns)
_sp0=body.find('w:sectPr',ns)
TW0=int(_sp0.find('w:pgSz',ns).get(q('w:w')))-int(_sp0.find('w:pgMar',ns).get(q('w:left')))-int(_sp0.find('w:pgMar',ns).get(q('w:right')))
EQW=(900,TW0-1800,900)
def E(tag,**attrs):
    e=etree.Element(q(tag))
    for k,v in attrs.items(): e.set(q('w:'+k),str(v))
    return e
def text(el): return ''.join(t.text or '' for t in el.iter(q('w:t')))
# 1. equations
cnt=0
for p in list(body.iter(q('w:p'))):
    t=text(p).strip()
    m=re.fullmatch(r'⟦\((9\.\d+)\)⟧',t)
    if not m: continue
    prev=p.getprevious()
    while prev is not None and prev.tag!=q('w:p'): prev=prev.getprevious()
    assert prev is not None and prev.find('.//m:oMathPara',ns) is not None, t
    assert text(prev).strip()=='', ('text in eq para',text(prev)[:80])
    num=m.group(1)
    tbl=E('w:tbl'); tp=E('w:tblPr'); tbl.append(tp)
    tw=E('w:tblW',w=TW0,type='dxa'); tp.append(tw); tp.append(E('w:jc',val='center'))
    b=E('w:tblBorders')
    for side in ('top','left','bottom','right','insideH','insideV'): b.append(E('w:'+side,val='nil'))
    tp.append(b); tp.append(E('w:tblLayout',type='fixed'))
    lk=E('w:tblLook',val='0000'); tp.append(lk)
    g=E('w:tblGrid')
    for wdt in EQW: g.append(E('w:gridCol',w=wdt))
    tbl.append(g); tr=E('w:tr'); tbl.append(tr)
    tr.append(E('w:trPr')); tr[-1].append(E('w:cantSplit'))
    for k,wdt in enumerate(EQW):
        tc=E('w:tc'); tcp=E('w:tcPr'); tcp.append(E('w:tcW',w=wdt,type='dxa')); tcp.append(E('w:vAlign',val='center')); tc.append(tcp)
        if k==1:
            mp=copy.deepcopy(prev); 
            ppr=mp.find('w:pPr',ns)
            if ppr is not None: mp.remove(ppr)
            ppr=E('w:pPr'); ppr.append(E('w:spacing',before=60,after=60)); ppr.append(E('w:jc',val='center')); mp.insert(0,ppr)
            tc.append(mp)
        else:
            pp=E('w:p'); ppr=E('w:pPr'); ppr.append(E('w:spacing',before=60,after=60)); ppr.append(E('w:jc',val='right' if k==2 else 'left')); pp.append(ppr)
            if k==2:
                r=E('w:r'); tt=E('w:t'); tt.text='(%s)'%num; r.append(tt); pp.append(r)
            tc.append(pp)
        tr.append(tc)
    prev.addprevious(tbl); prev.getparent().remove(prev); p.getparent().remove(p); cnt+=1
print('equations',cnt)
# 2. data tables
_sp=body.find('w:sectPr',ns); _pg=_sp.find('w:pgSz',ns); _mg=_sp.find('w:pgMar',ns)
TW=int(_pg.get(q('w:w')))-int(_mg.get(q('w:left')))-int(_mg.get(q('w:right')))
for tbl in body.iter(q('w:tbl')):
    tp=tbl.find('w:tblPr',ns)
    if tp.find('w:tblStyle',ns) is None: continue
    rows=tbl.findall('w:tr',ns); ncol=len(rows[0].findall('w:tc',ns))
    L=[0]*ncol
    for r in rows:
        for j,c in enumerate(r.findall('w:tc',ns)):
            words=text(c).split(); L[j]=max(L[j], min(len(text(c)),60), max([len(w) for w in words]+[4])*1.6)
    tot=sum(L); widths=[max(700,int(TW*l/tot)) for l in L]
    hdr=text(rows[0].findall('w:tc',ns)[0]).strip()
    if hdr=='Equation': widths=[1250,4900,2876]
    elif hdr=='Attribute' and ncol==7: widths=[1400]+[int((TW-1400)/6)]*6
    sc=TW/sum(widths); widths=[int(w*sc) for w in widths]
    tw=tp.find('w:tblW',ns); tw.set(q('w:type'),'dxa'); tw.set(q('w:w'),str(TW))
    lay=tp.find('w:tblLayout',ns)
    if lay is None:
        lay=E('w:tblLayout'); tw.addnext(lay)
    lay.set(q('w:type'),'fixed')
    b=E('w:tblBorders')
    for side,sz in (('top',8),('left',4),('bottom',8),('right',4),('insideH',4),('insideV',4)):
        b.append(E('w:'+side,val='single',sz=sz,space=0,color='808080'))
    lay.addprevious(b)
    cm=E('w:tblCellMar'); cm.append(E('w:top',w=30,type='dxa')); cm.append(E('w:left',w=70,type='dxa')); cm.append(E('w:bottom',w=30,type='dxa')); cm.append(E('w:right',w=70,type='dxa')); lay.addnext(cm)
    g=tbl.find('w:tblGrid',ns)
    for gc in list(g): g.remove(gc)
    for wd in widths: g.append(E('w:gridCol',w=wd))
    small = ncol>=5
    for i,r in enumerate(rows):
        for j,c in enumerate(r.findall('w:tc',ns)):
            tcp=c.find('w:tcPr',ns)
            if tcp is None: tcp=E('w:tcPr'); c.insert(0,tcp)
            for x in list(tcp): tcp.remove(x)
            tcp.append(E('w:tcW',w=widths[j],type='dxa'))
            if i==0:
                tcp.append(E('w:shd',val='clear',color='auto',fill='E7E6E6'))
            for rr in c.iter(q('w:r')):
                rp=rr.find('w:rPr',ns)
                if rp is None: rp=E('w:rPr'); rr.insert(0,rp)
                if i==0 and rp.find('w:b',ns) is None: rp.append(E('w:b'))
                if small:
                    rp.append(E('w:sz',val=18)); rp.append(E('w:szCs',val=18))
            for pp in c.findall('w:p',ns):
                ppr=pp.find('w:pPr',ns)
                if ppr is None: ppr=E('w:pPr'); pp.insert(0,ppr)
                jc=ppr.find('w:jc',ns)
                if jc is not None: jc.set(q('w:val'),'left')
# 3. footer with page numbers
sect=body.find('w:sectPr',ns)
HAS_FOOTER=sect.find('w:footerReference',ns) is not None
if not HAS_FOOTER:
    fr=E('w:footerReference',type='default'); fr.set('{%s}id'%R,'rIdFooter1'); sect.insert(0,fr)

for tbl in body.findall('w:tbl',ns):
    if tbl.find('w:tblPr/w:tblStyle',ns) is None: continue
    nx=tbl.getnext()
    if nx is not None and nx.tag==q('w:p'):
        ppr=nx.find('w:pPr',ns)
        if ppr is None: ppr=E('w:pPr'); nx.insert(0,ppr)
        sp=ppr.find('w:spacing',ns)
        if sp is None: sp=E('w:spacing'); 
        sp.set(q('w:before'),'160'); 
        if sp.getparent() is None:
            st=ppr.find('w:pStyle',ns); (st.addnext(sp) if st is not None else ppr.insert(0,sp))
tree.write(d+'word/document.xml',xml_declaration=True,encoding='UTF-8',standalone=True)
if not HAS_FOOTER: open(d+'word/footer1.xml','w').write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr xmlns:w="%s"><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:sz w:val="20"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:rPr><w:sz w:val="20"/></w:rPr><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r><w:r><w:rPr><w:sz w:val="20"/></w:rPr><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:rPr><w:sz w:val="20"/></w:rPr><w:t>1</w:t></w:r><w:r><w:rPr><w:sz w:val="20"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>'%W)
rel=open(d+'word/_rels/document.xml.rels').read()
rel=rel if HAS_FOOTER else rel.replace('</Relationships>','<Relationship Id="rIdFooter1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/></Relationships>')
open(d+'word/_rels/document.xml.rels','w').write(rel)
ct=open(d+'[Content_Types].xml').read()
if 'Extension="png"' not in ct:
    ct=ct.replace('<Default Extension="xml"','<Default Extension="png" ContentType="image/png" /><Default Extension="xml"')
if 'footer1.xml' not in ct and not HAS_FOOTER:
    ct=ct.replace('</Types>','<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/></Types>')
open(d+'[Content_Types].xml','w').write(ct)
# 4. styles: keep figure with caption, heading4 keepNext already
st=open(d+'word/styles.xml').read()
pass
open(d+'word/styles.xml','w').write(st)
# core props
cp=open(d+'docProps/core.xml').read()
cp=re.sub(r'<dc:title>.*?</dc:title>','<dc:title>Chapter 9 Custom Power Devices for Distribution Power Quality</dc:title>',cp)
open(d+'docProps/core.xml','w').write(cp)
dx=open(d+'word/document.xml').read().replace('<m:nor/><m:sty m:val="p"/>','<m:nor/>')
import re as _re
dx=_re.sub(r'<m:mcPr>(<m:mcJc [^>]*/>)(<m:count [^>]*/>)</m:mcPr>',r'<m:mcPr>\2\1</m:mcPr>',dx)
open(d+'word/document.xml','w').write(dx)
# reorder style children to schema order
SO=['name','aliases','basedOn','next','link','autoRedefine','hidden','uiPriority','semiHidden','unhideWhenUsed','qFormat','locked','personal','personalCompose','personalReply','rsid','pPr','rPr','tblPr','trPr','tcPr','tblStylePr']
PO=['pStyle','keepNext','keepLines','pageBreakBefore','framePr','widowControl','numPr','suppressLineNumbers','pBdr','shd','tabs','suppressAutoHyphens','kinsoku','wordWrap','overflowPunct','topLinePunct','autoSpaceDE','autoSpaceDN','bidi','adjustRightInd','snapToGrid','spacing','ind','contextualSpacing','mirrorIndents','suppressOverlap','jc','textDirection','textAlignment','textboxTightWrap','outlineLvl','divId','cnfStyle','rPr','sectPr','pPrChange']
st=etree.parse(d+'word/styles.xml'); sr=st.getroot()
def reorder(el,order):
    kids=list(el)
    for k in kids: el.remove(k)
    key=lambda k:(order.index(etree.QName(k).localname) if etree.QName(k).localname in order else 999)
    for k in sorted(kids,key=key): el.append(k)
for s_ in sr.iter(q('w:style')):
    reorder(s_,SO)
    for ppr in s_.findall('w:pPr',ns): reorder(ppr,PO)
TO=['cnfStyle','tcW','gridSpan','hMerge','vMerge','tcBorders','shd','noWrap','tcMar','textDirection','tcFitText','vAlign','hideMark']
for t_ in sr.iter(q('w:tcPr')): reorder(t_,TO)
for r_ in sr.iter(q('w:rPr')):
    if r_.text and r_.text.strip(): r_.text=None
    for c in r_: 
        if c.tail and c.tail.strip(): c.tail=None
st.write(d+'word/styles.xml',xml_declaration=True,encoding='UTF-8',standalone=True)
