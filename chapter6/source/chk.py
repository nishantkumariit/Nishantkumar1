import numpy as np
from scipy.optimize import brentq
D=np.deg2rad; w=2*np.pi*50
F=lambda a:(2*(np.pi-a)+np.sin(2*a))/np.pi
Ir=lambda a:np.sqrt(((np.pi-a)*(1+2*np.cos(a)**2)+1.5*np.sin(2*a))/np.pi)  # times Vm/wL
def In(a,n): return 4/np.pi*abs((np.cos(a)*np.sin(n*a)-n*np.sin(a)*np.cos(n*a))/(n*(n*n-1)))  # pk, times Vm/wL
afor=lambda q:np.degrees(brentq(lambda a:F(a)-q,D(90),D(180)))
# numeric check of formulas
th=np.linspace(0,2*np.pi,400001)[:-1]
def wave(a):
    i=np.zeros_like(th); m=(th>=a)&(th<=2*np.pi-a); i[m]=np.cos(a)-np.cos(th[m])
    i2=np.zeros_like(th); t2=(th-np.pi)%(2*np.pi); m2=(t2>=a)&(t2<=2*np.pi-a); i2[m2]=-(np.cos(a)-np.cos(t2[m2])); return i+i2
for ad in (100,120,130,150):
    a=D(ad); x=wave(a); 
    print(ad,'Irms',np.sqrt(np.mean(x**2)),Ir(a),'F',F(a),'fund',abs(2*np.mean(x*np.exp(-1j*th))),'I3',abs(2*np.mean(x*np.exp(-3j*th))),In(a,3),'THD',np.sqrt((Ir(a)/(F(a)/np.sqrt(2)))**2-1))
# table 6.3
for n in (3,5,7,9,11,13,15,17,19,21,23,25):
    aa=np.linspace(D(90.001),D(179.999),200001); v=In(aa,n); k=np.argmax(v); print(n,round(v[k]*100/1,2),round(np.degrees(aa[k]),1))
print('=== examples')
s2=np.sqrt(2)
# Ex6.1
X=3*415**2/50000; L=X/w; base=s2*415/X; a=D(afor(0.5)); print('6.1',X,L*1e3,415/X,s2*0+np.sqrt(3)*415/X,np.degrees(a),base,Ir(a)*base, 0.5*base/s2, np.sqrt((Ir(a)/(0.5/s2))**2-1),[In(a,n)*base/s2 for n in (3,5,7)],[In(a,n)*base/s2*np.sqrt(3) for n in (5,7)])
# 6.2
X=w*0.01; base=s2*240/X; a=D(120); print('6.2',X,240**2/X,base,Ir(a)*base,F(a)/X,240*F(a)/X,240**2*F(a)/X,[In(a,n)*base/s2 for n in (3,5,7)],base*(1+np.cos(a)),s2*240*np.sin(a))
# 6.3
X=w*0.005; base=s2*415/X; a=D(105); print('6.3',X,3*415**2/X,base,Ir(a)*base,F(a),F(a)*base/s2,3*415**2*F(a)/X,[In(a,n)*base/s2 for n in (3,5,7,9,11,13)])
trip=np.sqrt(sum((In(a,n)*base/s2)**2 for n in range(3,400,6))); Ib=Ir(a)*base; I1=F(a)*base/s2
print(' trip',trip,np.sqrt(3)*np.sqrt(Ib**2-trip**2),np.sqrt(3)*I1,np.sqrt((np.sqrt(Ib**2-trip**2)/I1)**2-1),[np.sqrt(3)*In(a,n)*base/s2 for n in (5,7,11,13)])
# 6.4
for q in (.2,.4,.6,.8): aa=afor(q); print('6.4',q,aa,aa-90,-4*np.sin(D(aa))**2/np.pi*np.pi/180)
a=D(120); a1=a-(F(a)-0.4)/(-4*np.sin(a)**2/np.pi); print(np.degrees(a1), -4*np.sin(a)**2/np.pi, F(D(30)))
# 6.5
X=w*0.015; base=s2*415/X; a=D(120); print('6.5',X,3*415**2/X,base,F(a)*base/s2,Ir(a)*base,np.sqrt(3)*F(a)*base/s2,2*3*415*F(a)*base/s2,[np.sqrt(3)*In(a,n)*base/s2 for n in (5,7,11,13)])
# 6.6
Xs=3*415**2/25000; bs=s2*415/Xs; print('6.6',Xs,Xs/w*1e3,In(D(120),3)*bs/s2,4*In(D(120),3)*bs/s2)
a=D(afor(0.4)); print(np.degrees(a),In(a,3)*bs/s2,In(a,5)*bs/s2); Xf=Xs/4; bf=s2*415/Xf; a6=D(afor(0.6)); print(np.degrees(a6),In(a6,3)*bf/s2,In(a6,5)*bf/s2)
# 6.7
X=3*13.8e3**2/60e6; Ib=13800/X; print('6.7',X,X/w*1e3,Ib,Ib*s2,Ib*s2/2,Ib*s2/np.pi,1.1*s2*13.8,X/80,Ib**2*X/80/1e3)
# 6.8
X=w*0.018; base=s2*230/X; a=D(120); print('6.8',X,base,base*.5,Ir(a)*base,F(a)*base/s2,230**2*F(a)/X,X/60,(Ir(a)*base)**2*X/60)
# 6.10
for Q in (50e3,100e3,200e3): X=3*415**2/Q; print('6.10',X,X/w*1e3,415/X,415/X*s2,415/X*s2/2,415/X*s2/np.pi)
# 6.14
Xn=33**2/20; n=4.5;k=n*n/(n*n-1); XC=k*Xn; XL=XC/n**2; C=1/(w*XC); Lh=XL/w; Vm=33e3*s2/np.sqrt(3); print('6.14',Xn,XC,XL,C*1e6,Lh*1e3,s2*20e6/(3*19.053e3),np.sqrt(Lh/C),Vm,(1+k)*Vm,(1+k)*Vm/Lh/1e6,(1+k)*Vm/20e6*1e3)
# 6.15
for Q in (25e3,50e3,100e3,200e3): Xn=3*415**2/Q; C=1/(w*k*Xn); Lh=k*Xn/(n*n*w); print('6.15',C*1e6,Lh*1e3,415/Xn,np.sqrt(3)*415/Xn)
# 6.17
for h,Q in ((4.9,25e6),(6.9,15e6)): XC=h*h/(h*h-1)*11e3**2/Q; XL=XC/h/h; print('6.17',XC,1/(w*XC)*1e6,XL,XL/w*1e3)
print([afor(q) for q in (40/60,20/60,50/60)])
# 6.19
print('6.19',afor(45/60),afor(20/60))
# 6.20
X=3*121/100; n=4.3;k=n*n/(n*n-1); Xn=121/50; XC=k*Xn; XL=XC/n**2; print('6.20',X,X/w*1e3,k,XC,1/(w*XC)*1e6,XL,XL/w*1e3)
for h,Q in ((4.9,40),(6.9,10)): XC=h*h/(h*h-1)*121/Q; print(XC,1/(w*XC)*1e6,XC/h/h/w*1e3)
Vm=11e3*s2/np.sqrt(3); print(Vm,(1+k)*Vm)
