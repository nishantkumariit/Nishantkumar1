import re
p='work/word/document.xml'; x=open(p).read()
order=[1,5,9,11,12,16,18,21,24,26,28,29,32,33,34,35,2,3,4,6,7,8,10,13,14,15,17,19,20,22,23,25,27,30,31]
mp={o:i+1 for i,o in enumerate(order)}
n0=len(re.findall(r'Example 6\.(\d+)',x))
x=re.sub(r'Example 6\.(\d+)',lambda m:'Example ⟪%d⟫'%mp[int(m.group(1))],x)
x=x.replace('⟪','6.').replace('⟫','')
print('renumbered',n0)
def rep(a,b,cnt=1):
    global x
    assert x.count(a)==cnt,(a,x.count(a)); x=x.replace(a,b)
U='</m:oMath><w:r><w:t xml:space="preserve"> A.</w:t></w:r></w:p>'
rep('<m:t>54.02</m:t></m:r></m:oMath></w:p>','<m:t>54.02</m:t></m:r>'+U)
rep('<m:t>652.4</m:t></m:r></m:oMath></w:p>','<m:t>652.4</m:t></m:r>'+U)
rep('<m:t>494.8</m:t></m:r></m:oMath></w:p>','<m:t>494.8</m:t></m:r>'+U)
i=x.find('Radsted, Denmark'); j=x.find('>2006<',i); assert j-i<600; x=x[:j]+'>2007<'+x[j+6:]
j=x.find('>Transmission<',i); assert j-i<1200; x=x[:j]+'>132 kV<'+x[j+14:]
i=x.find('Strathmore, Australia'); j=x.find('>n.a.<',i); assert j-i<600; x=x[:j]+'>2007<'+x[j+6:]
rep(' capacitor is essential: without it the line currents remain balanced in magnitude only if the load is resistive.',
    ' branch is needed only because the load is not resistive: it cancels the load’s own 300 kvar, and without it the line currents would be neither balanced nor at unity power factor.')
open(p,'w').write(x)
