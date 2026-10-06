import numpy as np, math, cmath
def Q(V,I,pf,X):
    ph=math.acos(pf);Vs=V*(1-X);Is=V*I*pf/Vs;U=math.sqrt(V*V-Vs*Vs);d=math.acos(1-X)
    Ish=abs(I*cmath.exp(1j*(d-ph))-Is);return dict(Vs=Vs,Is=Is,U=U,Sse=U*Is,d=math.degrees(d),Ish=Ish,Ssh=V*Ish,tot=U*Is+V*Ish,cos=math.cos(ph-d))
def P(V,I,pf,X):
    ph=math.acos(pf);Vs=V*(1-X);Is=V*I*pf/Vs;U=V*X;Ish=abs(I*cmath.exp(-1j*ph)-Is);return dict(U=U,Sse=U*Is,Ish=Ish,Ssh=V*Ish,tot=U*Is+V*Ish)
print('9.21',Q(230,20,.8,.1))
print('9.22',P(230,25,.8,.2))
print('9.23',Q(230,20,.8,.25))
V=230;I=25;pf=.8;X=.3;Vs=161;Is=4600/161;U=130
c=(V*V-Vs*Vs-U*U)/(2*Vs*U);psi=math.acos(c);Pse=U*Is*c;Qse=U*Is*math.sin(psi)
d=math.atan2(U*math.sin(psi),Vs+U*c);Ish=abs(I*cmath.exp(1j*(d-math.acos(pf)))-Is)
print('9.24',c,math.degrees(psi),Pse,Qse,U*Is,math.degrees(d),Ish,V*Ish,U*Is+V*Ish)
print('  Q',Q(230,25,.8,.3));print('  P',P(230,25,.8,.3))
# DVR comparison 9.21: standalone DVR, 20 A load at 10% sag: smaller root injection 43.17 V *20 A
print('dvr',43.169*20)
# 9.25/9.26
for Vs in (207,253):
    ph=math.acos(.8);a=math.acos(184/Vs)
    for th in (ph-a,ph+a):
        inj=cmath.rect(230,th)-Vs;b=ph-th
        print(Vs,math.degrees(th),abs(inj),math.degrees(cmath.phase(inj)),abs(inj)*25,25*abs(math.sin(b)),Vs*25*abs(math.sin(b)))
