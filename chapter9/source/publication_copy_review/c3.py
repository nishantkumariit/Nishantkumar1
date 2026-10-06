import math, cmath, numpy as np
V=415/math.sqrt(3);w=2*math.pi*50
# 9.37
Zs=0.3+1.8j;ZL=18+12j;VM=0.75*V
I=VM/abs(Zs+ZL);print('9.37a',VM,I,I*abs(ZL),I*abs(ZL)*math.sqrt(3))
IL=V/abs(ZL);print('b',IL,IL**2*18.3,VM*IL)
k=abs(1+Zs/ZL);inj=V*k-VM;print('c',k,inj)
# aligned: VL(1+Zs/ZL) aligned with VM; Vinj = (k V - VM) along VM; current IL = VL/ZL; P = Re(Vinj I*) per phase
VL=V*cmath.exp(-1j*cmath.phase(1+Zs/ZL));Il=VL/ZL;P=3*(inj*Il.conjugate()).real;print(P,3*inj*abs(Il),math.sqrt(V*V-VM*VM))
# 9.41
Vinj=0.3*V;n=3;Vc=n*Vinj;Ideep=30000/(3*0.7*V);Ic=Ideep/n;print('9.41',Vinj,Vc,Ideep,Ic,3*Vinj*Ideep)
Isw=30000/(3*1.3*V);dl=0.1*Isw;Lc=n*math.sqrt(3)*800/(12*1.2*1e4*dl);print(Isw,dl,Lc*1e3,Lc/n**2*1e3)
Vt=math.hypot(Vc,w*Lc*Ic);print(Vt,760/(2*math.sqrt(2)),3*Vt*Ic,1.25*(math.sqrt(2)*Ic+0.1*Ideep/n),2*600/(800**2-760**2))
# answers
def Q(V,I,pf,X):
    ph=math.acos(pf);Vs=V*(1-X);Is=V*I*pf/Vs;U=math.sqrt(V*V-Vs*Vs);d=math.acos(1-X)
    Ish=abs(I*cmath.exp(1j*(d-ph))-Is);return Vs,Is,U,U*Is,math.degrees(d),Ish,U*Is+V*Ish
print('P9.1-4',Q(230,18,.75,.18))
Vs=230*.82;Is=230*18*.75/Vs;print('P9.2',230*.18,230*.18*Is)
Vp=400/math.sqrt(3);I=15000/(math.sqrt(3)*400*.85);print('P9.5',Vp,0.25*Vp,I,3*0.25*Vp*I*.85,0.25*15000*.18)
print('P9.6',2*675/(650**2-600**2))
print('P9.8',math.hypot(7,3.5)/45*100,math.hypot(7,3.5))
print('P9.9',math.sqrt(144+64+16+9)/350*100,[x/350*100 for x in (12,8,4,3)])
print('P9.11')
a=cmath.rect(1,math.radians(120))
for t,s in ((1,0.8+0.12),(a*a,a*a*0.8+a*0.12),(a,a*0.8+a*a*0.12)):print(abs(t-s))
print('P9.13',0.25*10000/12000)
print('P9.14',Q(230,18,.75,.15)[2],Q(230,18,.75,.15)[3],230*.15,230*.15*230*18*.75/(230*.85))
print('P9.15',6000*.18/.95)
Ib=40000/(math.sqrt(3)*415*.75);Ia=40000/(math.sqrt(3)*415);Qv=40*math.tan(math.acos(.75));print('P9.16',Ib,Ia,Qv*1000/(math.sqrt(3)*415),Qv)
Vdc=2*math.sqrt(2)*415/math.sqrt(3);Lr=math.sqrt(3)*700/(12*1.2*1e4*2.5);E=3*V*1.2*50*0.01;C=2*E/(700**2-665**2);print('P9.17',Vdc,Lr*1e3,E,C*1e3)
print('P9.18',30000/415,30000/(3*V))
h=math.sqrt(.18**2+.12**2+.06**2);print('P9.19',h*100,60*h,3*V*60*h)
ph=math.acos(.75);print('P9.20',1-.75,230*math.sin(ph),math.degrees(ph))
print('P9.21',0.4*50*.9,0.4*45*0.3/.95,0.4*45*0.3/.95/3.6)
Vi=0.35*V;I=30000/(math.sqrt(3)*415);print('P9.22',Vi,100/Vi,3*Vi*I,I*Vi/100)
V2=230;I2=20;pf=.85;X=.25;Vs=V2*(1-X);Is=V2*I2*pf/Vs;U=110
c=(V2*V2-Vs*Vs-U*U)/(2*Vs*U);psi=math.acos(c);d=math.atan2(U*math.sin(psi),Vs+U*c);Ish=abs(I2*cmath.exp(1j*(d-math.acos(pf)))-Is)
print('P9.23',math.degrees(psi),math.degrees(d),U*Is*c,U*Is,V2*Ish,U*Is+V2*Ish)
Vs=230*.92;ph=math.acos(.9);al=math.acos(230*.9/Vs);th=ph-al;inj=abs(cmath.rect(230,th)-Vs);b=ph-th
print('P9.24',math.degrees(th),inj,inj*20,20*math.sin(b),Vs*20*math.sin(b),Vs)
In=30+cmath.rect(20,math.radians(-150))+cmath.rect(25,math.radians(100));print('P9.25',abs(In),math.degrees(cmath.phase(In)))
print('P9.26',math.sqrt(15/.25),1/math.sqrt(.0567))
Zs=0.02+0.3j;ZF=0.02+0.05j;d=abs(Zs+ZF+2);print('P9.27',abs(ZF)/d*0.2,0.01/d,abs(ZF)/d*0.2+0.01/d)
