import numpy as np
from scipy.optimize import brentq
from tcsc import *
w=2*np.pi*50; d=np.pi/180
F=lambda g: 1-2*g/np.pi-np.sin(2*g)/np.pi
def Vrms(g): return np.sqrt(((np.pi-2*g)*(0.5+np.sin(g)**2)-1.5*np.sin(2*g))/np.pi)
def Vn(g,n): return abs(4/np.pi*(np.sin(g)*np.cos(n*g)-n*np.cos(g)*np.sin(n*g))/(n*(n*n-1)))
# numeric GCSC waveform check
def gcsc_num(g,N=400000):
    th=np.linspace(0,2*np.pi,N,endpoint=False); v=np.zeros(N)
    for s,off in [(1,0),(-1,np.pi)]:
        x=th-off; m=(x>=g)&(x<=np.pi-g); v[m]=s*(np.sin(x[m])-np.sin(g))
    i=np.cos(th)
    fund=2*np.mean(v*np.sin(th))  # v fundamental in phase with sin (lags cos current)
    rms=np.sqrt(np.mean(v**2))
    h=lambda n: np.hypot(2*np.mean(v*np.cos(n*th)),2*np.mean(v*np.sin(n*th)))
    return fund,rms,[h(n) for n in (3,5,7)]
print('GCSC formula check')
for g in [0,10,25,30,45,60,80]:
    fn,rm,hh=gcsc_num(g*d)
    print(g, 'F %.5f/%.5f rms %.5f/%.5f h3 %.5f/%.5f h5 %.5f/%.5f'%(F(g*d),fn,Vrms(g*d),rm,Vn(g*d,3),hh[0],Vn(g*d,5),hh[1]))
gs=np.linspace(0,90,9001)*d; v3=[Vn(g,3) for g in gs]; k=np.argmax(v3); print('max V3 %.4f at %.2f'%(v3[k],gs[k]/d))
# wrong formula sin^2 2g
g=60*d; print('wrong rms',np.sqrt(((np.pi-2*g)*(0.5+np.sin(2*g)**2)-1.5*np.sin(2*g))/np.pi), 'fund rms',F(g)/np.sqrt(2))
print('--- 7.A', 220**2*0.5/40, 220**2*0.5/24)
print('7.B',F(30*d),8*F(30*d))
a=brentq(lambda a: np.pi-2*a-np.sin(2*a)-np.pi/5,0,np.pi/2); print('7.D simp alpha',a/d,'exact br',90/np.sqrt(5),90-90/np.sqrt(5))
print('7.J'); c=0.8*(0.05+0.5j)/2; r=abs(c); print(abs(c),np.angle(c)/d,c, abs(0.85*(0.05+0.5j)-0.08j-c), abs(0.7*(0.05+0.5j)+0.08j-c))
fe=brentq(lambda f:0.02+0.005*f/(f-50),1,49.9); print('7.K fe',fe,(fe/50)**2)
# 7.L and fig 7.34
def damp(f,Td,z0=0.02,zt=0.15):
    wn=2*np.pi*f; K=2*(zt-z0)*wn
    from scipy.optimize import fsolve
    s0=-zt*wn+1j*wn*np.sqrt(1-zt**2)
    best=None
    for Tdi in np.linspace(0,Td,60)[1:]:
        g=lambda x: [np.real((x[0]+1j*x[1])**2+2*z0*wn*(x[0]+1j*x[1])+wn**2+K*(x[0]+1j*x[1])*np.exp(-(x[0]+1j*x[1])*Tdi)), np.imag((x[0]+1j*x[1])**2+2*z0*wn*(x[0]+1j*x[1])+wn**2+K*(x[0]+1j*x[1])*np.exp(-(x[0]+1j*x[1])*Tdi))]
        x=fsolve(g,[s0.real,s0.imag]); s0=x[0]+1j*x[1]
    return -s0.real/abs(s0)
for f in [0.4,0.7,1.0]:
    print('mode',f,[round(100*damp(f,T),2) for T in [0.15,0.18,0.2,0.25]])
# find 5% and 0% crossing for 1 Hz
for f in [1.0]:
    Ts=np.arange(0.10,0.30,0.005); z=[damp(f,T) for T in Ts]
    for T,zz in zip(Ts,z): print(round(T,3),round(100*zz,2),end='; ')
    print()
print('7.24 fig: X1=.3 X2=.4 Pt=1.6',1.6*.4/.7, (1.6*.4/.85)-.7, ((1.6*.4/.85)-.7)*0.85)
