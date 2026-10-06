import numpy as np, cmath, math
d=np.deg2rad
# Ex 8.25
V=1;X=0.5;de=d(30);Vpq=0.25
for rho in (60,240):
    I=(cmath.rect(1,de)+cmath.rect(Vpq,de+d(rho))-1)/(1j*X)
    S=1*I.conjugate(); Sse=cmath.rect(Vpq,de+d(rho))*I.conjugate()
    print('8.25',rho,abs(I),np.rad2deg(cmath.phase(I)),S,Sse,abs(Sse))
# 8.27
Vll=132;R=70;Xl=175;de=d(45);Z=R+1j*Xl
I0=(cmath.rect(Vll,de)-Vll)/Z; S=Vll*I0.conjugate()
print('8.27a',S, abs(I0)/math.sqrt(3)*1000)
th=math.atan2(Xl,R); inc=Vll*45/abs(Z)
I1=(cmath.rect(Vll,de)+cmath.rect(45,th)-Vll)/Z
print('8.27b',np.rad2deg(th)-45,inc,(Vll*I1.conjugate()).real,abs(I1)/math.sqrt(3)*1000,0.5*S.real*abs(Z)/Vll)
# 8.30
Vs=1;Vr=0.95;X=0.5;de=d(25);Vpq=0.2;rho=d(50)
P0=Vs*Vr*math.sin(de)/X;Q0=(Vs*Vr*math.cos(de)-Vr**2)/X
I=(cmath.rect(Vs,de)+cmath.rect(Vpq,de+rho)-Vr)/(1j*X);S=Vr*I.conjugate();Sse=cmath.rect(Vpq,de+rho)*I.conjugate()
Ve=cmath.rect(Vs,de)+cmath.rect(Vpq,de+rho)
print('8.30',P0,Q0,S,abs(Ve),np.rad2deg(cmath.phase(Ve)),Sse)
# 8.31
P0=138**2*math.sin(d(35))/80;pt=138*28/80;s=(180-P0)/pt;a=np.rad2deg(math.asin(s))
print('8.31',P0,pt,P0-pt,P0+pt,s,a-35,180-a-35)
# 8.32
V=1;X=0.5;de=d(30);Vpq=0.25;Q0=-(1-math.cos(de))/X
c=-Q0*X/(V*Vpq);th=math.acos(c);rho1=th-de
V1=cmath.rect(Vpq,th);I1=(cmath.rect(1,de)+V1-1)/(1j*X);S1=I1.conjugate();Sp=V1*I1.conjugate()
print('8.32',c,np.rad2deg(rho1),S1,Sp)
P1=Sp.real
# converter 2 on line 2 (identical uncompensated line), injection Vpq2=0.25 at angle de+rho2 ; absorb P1
from scipy.optimize import brentq
def f(r):
    V2=cmath.rect(0.25,de+r);I2=(cmath.rect(1,de)+V2-1)/(1j*X);return (V2*I2.conjugate()).real+P1
rs=np.linspace(-np.pi,np.pi,3601);vals=[f(r) for r in rs]
for i in range(len(rs)-1):
    if vals[i]*vals[i+1]<0:
        r=brentq(f,rs[i],rs[i+1]);V2=cmath.rect(0.25,de+r);I2=(cmath.rect(1,de)+V2-1)/(1j*X);S2=I2.conjugate()
        print('  rho2',np.rad2deg(r),S2,abs(I2),(V2*I2.conjugate()))
# 8.36
Vp=127.0;P0=3*Vp**2*math.sin(d(25))/50;Ve=math.hypot(127,20);sg=math.degrees(math.atan(20/127))
print('8.36',sg,Ve,P0,3*Ve*Vp*math.sin(d(25+sg))/50,3*128.6*127*math.sin(d(33.95))/50)
# 8.40 fourier
from scipy.integrate import quad
V1,V2,al=10,12,d(60)
def v(t): return V1*math.sin(t) if t<al else V2*math.sin(t)
for n in (1,3,5,7):
    a=2/math.pi*(quad(lambda t:v(t)*math.cos(n*t),0,al)[0]+quad(lambda t:v(t)*math.cos(n*t),al,math.pi)[0])
    b=2/math.pi*(quad(lambda t:v(t)*math.sin(n*t),0,al)[0]+quad(lambda t:v(t)*math.sin(n*t),al,math.pi)[0])
    print('8.40',n,a,b,math.hypot(a,b),math.degrees(math.atan2(a,b)))
vr2=(quad(lambda t:v(t)**2,0,al)[0]+quad(lambda t:v(t)**2,al,math.pi)[0])/math.pi
A1=11.6188;print(' rms',math.sqrt(vr2),math.sqrt(2*vr2/A1**2-1)*100, math.sqrt(0.477465**2+0.275664**2+0.137832**2)/A1*100)
# 8.29
print('8.29',math.hypot(0.06699,0.3))
