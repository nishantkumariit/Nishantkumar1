import re,sys
s=open('p1.md').read()+'\n'+open('p2.md').read()+'\n'+open('p3.md').read()
# numbering
for kind,prefix in [('FIG','Figure 9.'),('TAB','Table 9.'),('EX','Example 9.'),('EQ','')]:
    keys=[]; 
    for m in re.finditer(kind+r'DEF\{([^}]+)\}',s):
        if m.group(1) in keys: sys.exit('dup '+m.group(1))
        keys.append(m.group(1))
    num={k:i+1 for i,k in enumerate(keys)}
    if kind=='EQ':
        s=re.sub(r'EQDEF\{([^}]+)\}',lambda m:'⟦(9.%d)⟧'%num[m.group(1)],s)
        s=re.sub(r'EQ\{([^}]+)\}',lambda m:'Equation (9.%d)'%num[m.group(1)],s)
    elif kind=='EX':
        s=re.sub(r'EXDEF\{([^}]+)\}',lambda m:'Example 9.%d'%num[m.group(1)],s)
        s=re.sub(r'Example EX\{([^}]+)\}',lambda m:'Example 9.%d'%num[m.group(1)],s)
        s=re.sub(r'EX\{([^}]+)\}',lambda m:'Example 9.%d'%num[m.group(1)],s)
    else:
        s=re.sub(kind+r'DEF\{([^}]+)\}',lambda m:prefix+'%d.'%num[m.group(1)],s)
        s=re.sub(kind+r'\{([^}]+)\}',lambda m:prefix+'%d'%num[m.group(1)],s)
    print(kind,len(keys))
left=re.findall(r'(?:FIG|TAB|EX|EQ)(?:DEF)?\{',s); assert not left,left
# Key-equation table: 'Equation (9.n)' -> '(9.n)' inside table rows
s=re.sub(r'^\| Equation \((9\.\d+)\) \|',r'| (\1) |',s,flags=re.M)
# Fix "Example 9.n(a)" fine. Equation refs at sentence start fine.
# citations renumber
body,refs=s.split('## References')
order=[]
for m in re.finditer(r'\[(\d+)\]',body):
    n=int(m.group(1))
    if n not in order: order.append(n)
reflines=re.findall(r'^\[(\d+)\] (.*)$',refs,flags=re.M)
refd={int(a):b for a,b in reflines}
missing=set(refd)-set(order); print('uncited',missing); assert not (set(order)-set(refd))
order+= sorted(missing)
newnum={o:i+1 for i,o in enumerate(order)}
body=re.sub(r'\[(\d+)\]',lambda m:'[%d]'%newnum[int(m.group(1))],body)
refs='\n\n'.join('[%d] %s'%(newnum[o],refd[o]) for o in order)
s=body+'## References\n\n'+refs+'\n'

def fixmath(seg):
    seg=seg.replace('\\left|','\\lvert ').replace('\\right|','\\rvert ')
    seg=seg.replace('\\lvert','\\left\\vert{}').replace('\\rvert','\\right\\vert{}')
    out=[];k=0
    for ch in seg:
        if ch=='|':
            out.append('\\left\\vert{}' if k%2==0 else '\\right\\vert{}'); k+=1
        else: out.append(ch)
    assert k%2==0, seg
    o=''.join(out).replace('\\left\\vert{}','\\left\\vert ').replace('\\right\\vert{}','\\right\\vert ')
    return re.sub(r'\s+(\$+)$',r'\1',o)
parts=re.split(r'(\$\$.*?\$\$|\$[^$\n]+?\$)',s,flags=re.S)
s=''.join(fixmath(p) if p.startswith('$') else p for p in parts)
open('ch9.md','w').write(s)
print('refs',len(order))
