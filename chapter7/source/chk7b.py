import numpy as np
from scipy.optimize import brentq
from tcsc import Xexact, Xsimp_alpha, wave, fund, harm
w=2*np.pi*50; d=np.pi/180; s3=np.sqrt(3)
F=lambda g: 1-2*g/np.pi-np.sin(2*g)/np.pi
def Vrms(g): return np.sqrt(((np.pi-2*g)*(0.5+np.sin(g)**2)-1.5*np.sin(2*g))/np.pi)
def Vn(g,n): return abs(4/np.pi*(np.sin(g)*np.cos(n*g)-n*np.cos(g)*np.sin(n*g))/(n*(n*n-1)))
ginv=lambda r: brentq(lambda g:F(g)-r,0,np.pi/2)/d
V=400/s3; I=2*V*np.sin(15*d)/80; print('7.1',V,I*1e3,400**2*.5/80,400**2*(1-np.cos(30*d))/80,I*1.5e3,3*(1.5*I)**2*80/3, 2*400**2/80*0.5/(4/9)*(1-np.cos(30*d)))
I=2*220/s3*np.sin(22.5*d)/30; print('7.2',I*1e3,220**2*np.sin(45*d)/30,I*20,3*I**2*20)
for dl in [30,60,90]: print('7.3',np.cos(dl/2*d),np.sin(dl*d)/.35,np.sin(dl*d)/.5)
for XC in [0,.3,.4,.5,.6,.7]:
    Xn=1.2-XC; V1=np.exp(1j*30*d); Ic=(V1-1)/(1j*Xn); VF=V1-1j*Ic*(0.1-XC); print('7.4',XC,round(abs(Ic),3),round(abs(VF),3))
print('7.5',50*np.sqrt(.4),50-50*np.sqrt(.4),(18/50)**2,(30/50)**2)
def cca(Pm,Pmax,Pf):
    d0=np.arcsin(Pm/Pmax); dm=np.pi-d0
    c=(Pm*(dm-d0)+Pmax*np.cos(dm)-Pf*np.cos(d0))/(Pmax-Pf); return d0/d,dm/d,np.arccos(c)/d,c
print('7.6',cca(.6,1,.4),cca(.6,1.5,.4),cca(.6,1.5,.6))
k=1-1/1.3; XC=k*50; I0=2*220/s3*np.sin(22.5*d)/50; I1=I0*1.3; print('7.7',k,XC,I1*1e3,3*I1**2*XC,2*np.sin(22.5*d)/np.sin(45*d),1.3*np.cos(22.5*d))
XC=1/(w*1500e-6); print('7.8',XC,[ (F(g*d),XC*F(g*d),1e6/(w*XC*F(g*d))) for g in (20,50,70)])
b=20/(w*1000e-6); print('7.9 base',b)
for g in (10,25,45,60):
    gg=g*d; f1=b*F(gg)/np.sqrt(2); vr=b*Vrms(gg); h=[b*Vn(gg,n)/np.sqrt(2) for n in (3,5,7)]
    print(g,round(f1,2),round(vr,2),[round(x,2) for x in h],'THD %.1f'%(100*np.sqrt(vr**2-f1**2)/f1))
XC=1/(w*1e-3); r=1.5/XC; g=ginv(r); print('7.10',XC,r,g,180-2*g)
print('7.11',1e6/(w*50),ginv(.25))
print('7.12',1e6/(w*32),ginv(.25),(1000/s3*s3/np.sqrt(2))**2*32/1e6,[160000*.5/80/(1-k) for k in (0,.1,.4)],100*Vn(ginv(.25)*d,3),Vn(ginv(.25)*d,3)*32/np.sqrt(2))
g45=45*d; Xs=3*F(g45); print('7.13',Xs,Xs/.75,ginv(Xs/.75), 400*3*Vn(g45,3)/np.sqrt(2), 400*.75*Vn(ginv(Xs/.75)*d,3)/np.sqrt(2))
print('7.14',[(800/np.sqrt(2))**2*5*n/1e6 for n in range(5)])
for I in (400,600,800,1000,1200):
    n=min(5,int(16000/(I*8)+1e-9)); print('7.15',I,n,n*8*I/1e3)
C=1/(w*12); Z0=np.sqrt(.5e-3/C); print('7.16',C*1e6,Z0,1/(2*np.pi*np.sqrt(.5e-3*C)),8000/Z0,8000/.5e-3/1e6)
print('7.17',[(600*40/(100-10*n),600-600*40/(100-10*n)) for n in range(5)])
print('7.18',[(50*np.sqrt(n*10/80),50-50*np.sqrt(n*10/80)) for n in range(1,5)])
XC=1/(w*1e-3); XL=w*1.5e-3; wr=np.sqrt(XC/XL); print('7.19',XC,XL,wr,90/wr,90-90/wr)
ar=brentq(lambda a: XL*np.pi/(np.pi-2*a-np.sin(2*a))-XC,1e-3,np.pi/2-1e-3); print(' simp res',ar/d)
for a in (20,50,60): print(' a',a,'simp',Xsimp_alpha(a*d,XC,XL),'exact',Xexact((90-a)*d,XC,XL))
XC=1;XL=.15; b=brentq(lambda b: Xexact(b,XC,XL)+3,1e-3,90/np.sqrt(1/.15)*d-1e-6); print('7.20',b/d,90-b/d,90/np.sqrt(1/.15))
for r in (.1,.15,.2):
    br=90/np.sqrt(1/r); b=brentq(lambda b: Xexact(b,10,10*r)+20,1e-3,br*d-1e-6)/d; print('7.21',r,b,10*r/w*1e3,br,br-b, '2nd res',3*br)
th,i,v,iT=wave(28.53*d,10,1.5,Im=1200*np.sqrt(2)); print(' wave', fund(th,v,1200*np.sqrt(2)), v.max(), np.sqrt(np.mean(iT**2)), abs(iT).max())
b=brentq(lambda b: Xexact(b,10,1.5)+20,1e-3,34*d); th,i,v,iT=wave(b,10,1.5,Im=1200*np.sqrt(2)); print(' wave exact b',b/d, v.max(), np.sqrt(np.mean(iT**2)), abs(iT).max())
print('7.22',250000*.5/85,250000*np.sin(35*d)/(250000*.5/85))
print('7.23',.45*60,50*np.sqrt(.45),50-50*np.sqrt(.45),10*50/33,1.333*33/50)
XC=5;XL=.667; br=90/np.sqrt(XC/XL); Im=800*np.sqrt(2); th,i,v,iT=wave(25*d,XC,XL,Im=Im); X=fund(th,v,Im); iC=i-iT
print('7.24',br,X,Xexact(25*d,XC,XL),800*abs(X)/1e3,np.sqrt(np.mean(v**2))/1e3,np.sqrt(np.mean(iT**2)),abs(iT).max(),np.sqrt(np.mean(iC**2)),np.mean(iT**2)*.05/1e3, 800**2*abs(X)/1e6)
# fig 7.17 claim (Xl/Xc=0.133, beta 25): peak iT / Im
th,i,v,iT=wave(25*d,1,.133); print('fig7.17 peak iT/Im',abs(iT).max(),'iC peak',abs(i-iT).max(),'X',fund(th,v))
th,i,v,iT=wave(55*d,1,.133); print('fig7.18 beta55 X',fund(th,v),'iT peak',abs(iT).max())
print('7.25',400**2/100,60/1600,-20/1600,1/.0375,1/.025,100*np.sin(10*d)/.0375,100*np.sin(10*d)/.025)
I=(2*np.sin(10*d)+.6); print('7.26',np.sin(20*d),np.sin(20*d)+.6*np.cos(10*d),I,.6/I,np.sin(20*d)/(1-.6/I))
P0=np.sin(40*d)/1.2; dP=.5*np.cos(20*d)/1.2; print('7.27',P0,P0+dP,P0-dP,dP/P0,2*np.arcsin(.25)/d)
P0=400**2*np.sin(45*d)/100; dP=400*30*np.cos(22.5*d)/100; I=(2*400/s3*np.sin(22.5*d)+30/s3)/100; print('7.28',P0,dP,P0-dP,P0+dP,I*1e3,2*400/s3*np.sin(22.5*d)/100*1e3,3*30/s3*I)
V=275/s3; dl=35*d
def line(R,X):
    Vs=V*np.exp(1j*dl); Vr=V; I=(Vs-Vr)/(R+1j*X); Sr=3*Vr*np.conj(I); Ss=3*Vs*np.conj(I); return Sr,Ss,abs(I)
Sr,Ss,I0=line(10,75); print('7.29',Sr,Ss,I0*1e3)
R=brentq(lambda R: line(R,7.5*R)[0].real-1.25*Sr.real,1,10); Sr2,Ss2,I2=line(R,7.5*R); print('  R',R,7.5*R,I2*1e3,(75-7.5*R)*I2,(10-R)*I2,3*np.hypot((75-7.5*R)*I2,(10-R)*I2)*I2,3*(10-R)*I2*I2)
Vq=80/s3; Imax=Vq/50; I30=2*500/s3*np.sin(15*d)/150; print('7.30',Imax*1e3,3*Vq*Imax,I30*1e3,2*np.arcsin(Imax*150/(2*500/s3))/d)
P0=110**2*np.sin(45*d)/40; I=2*110/s3*np.sin(22.5*d)/(40*2/3); print('7.31',P0,I*1e3,3*I**2*40/3,0.5*P0*40/(110*np.cos(22.5*d)), s3*0.5*P0*40/(110*np.cos(22.5*d))*I)
print('--- answers')
k=1-1/1.4; I=2*345/s3*np.sin(17.5*d)/(100*(1-k)); print('P7.1',k,100*k,I*1e3,3*I**2*100*k)
print('P7.2',.35*70,50*np.sqrt(.35),50-50*np.sqrt(.35),(25/50)**2)
print('P7.3',cca(.7,1.2,.3),cca(.7,1.6,.3))
XC=1/(w*800e-6); print('P7.4',XC,XC*F(30*d),XC*F(60*d),ginv(1/XC))
b=300/(w*600e-6); f1=b*F(40*d)/np.sqrt(2); vr=b*Vrms(40*d); print('P7.5',f1,vr,b*Vn(40*d,3)/np.sqrt(2),100*np.sqrt(vr**2-f1**2)/f1)
print('P7.6',8000/200,1e6/(w*40),ginv(8000/(600*40)))
C=1/(w*10); Z0=np.sqrt(.3e-3/C); print('P7.8',2*1500*10,Z0,6000/Z0)
XC=12;XL=1.6; wr=np.sqrt(XC/XL); print('P7.9',90/wr,90-90/wr,Xexact(20*d,XC,XL),Xexact(20*d,XC,XL)/-12,Xexact(60*d,XC,XL),'simp a30',Xsimp_alpha(30*d,XC,XL))
b=brentq(lambda b: Xexact(b,9,1.35)+18,1e-3,34*d); print('P7.11',b/d,90-b/d,1e6/(w*9),1.35/w*1e3,90/np.sqrt(9/1.35))
P0=.5/.9; dP=.3*np.cos(15*d)/.9; print('P7.12',P0,P0+dP,P0-dP,(2*np.sin(15*d)+.3)/.9,(2*np.sin(15*d)-.3)/.9)
P0=500**2*np.sin(40*d)/150; dP=500*50*np.cos(20*d)/150; print('P7.13',P0,P0-dP,P0+dP)
print('P7.15',100*np.sin(10*d)/.0375,100*np.sin(10*d)/(48/1600))
