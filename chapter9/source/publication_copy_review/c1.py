import numpy as np, cmath, math
r=lambda m,a: cmath.rect(m,math.radians(a))
pol=lambda z:(round(abs(z),3),round(math.degrees(cmath.phase(z)),2))
V=415/math.sqrt(3); a=r(1,-120)
# 9.3
Zb=9.15; Z=[ (9+3j)*Zb,(3+1.5j)*Zb,(7.5+1.5j)*Zb]; Vs=[V,V*a,V*a*a]
IL=[v/z for v,z in zip(Vs,Z)]; P=sum((v*i.conjugate()).real for v,i in zip(Vs,IL))
Is=P/(3*V); IS=[Is,Is*a,Is*a*a]; IC=[l-s for l,s in zip(IL,IS)]
print('9.3',[pol(i) for i in IL],P,Is,[pol(i) for i in IC],pol(sum(IL)),V*sum(abs(i) for i in IC),V/Is,3*V*max(abs(i) for i in IC))
# 9.4
Zs=1+3j;Za=10+5j
print('9.4a',pol(V*Za/(Za+Zs)))
ILa=V/Za;PL=abs(ILa)**2*10;Ip=PL/3/V
A=V+1*Ip;B=3*Ip;co=[10,2*(B*1-A*3),A*A+B*B-V*V];roots=np.roots(co)
print('9.4',pol(ILa),PL,Ip,A,B,co,roots)
Iq=min(roots);Isa=Ip+1j*Iq;print(pol(Isa));Vsrc=V+Zs*Isa;print('Vs',pol(Vsrc),'Q',V*Iq)
IC=[ILa-Isa,-Isa*a,-Isa*a*a];print([pol(i) for i in IC],V*sum(abs(i) for i in IC),abs(Zs*Isa),3*V*abs(IC[0]),abs(IC[0])*math.sqrt(2),abs(ILa)*math.sqrt(2))
# 9.2
IL=r(415,30)/(415**2/50000);print('9.2',pol(IL),50000/(3*V))
