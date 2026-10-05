import numpy as np
from scipy.optimize import brentq
d=np.pi/180
def Xexact(beta,XC,XL):
    w=np.sqrt(XC/XL); XLC=XC*XL/(XC-XL); C1=(XC+XLC)/np.pi; C2=4*XLC**2/(np.pi*XL)
    return -XC+C1*(2*beta+np.sin(2*beta))-C2*np.cos(beta)**2*(w*np.tan(w*beta)-np.tan(beta))
def Xsimp_alpha(a,XC,XL):
    XLa=XL*np.pi/(np.pi-2*a-np.sin(2*a)); return XC*XLa/(XC-XLa)
def wave(beta,XC,XL,Im=1.0,N=200000):
    """analytic periodic steady state; i=Im cos th, conduction centred on th=0 and pi"""
    w2=XC/XL; w=np.sqrt(w2)
    A=-XC*Im/(w2-1); B=(Im*XC-A)*np.cos(beta)/(w*np.cos(w*beta))
    th=np.linspace(-np.pi/2,3*np.pi/2,N,endpoint=False)
    v=np.zeros(N); iT=np.zeros(N)
    vb=A*np.sin(beta)+B*np.sin(w*beta)
    for k,t in enumerate(th):
        s=1; x=t
        if t>np.pi/2: x=t-np.pi; s=-1
        if abs(x)<=beta:
            v[k]=s*(A*np.sin(x)+B*np.sin(w*x)); iT[k]=s*(Im*np.cos(x)-(A*np.cos(x)+B*w*np.cos(w*x))/XC)
        else:
            # blocked: for x in (beta, pi/2]: v=vb+XC Im (sin x - sin beta); for x<-beta symmetric odd
            if x>0: v[k]=s*(vb+XC*Im*(np.sin(x)-np.sin(beta)))
            else: v[k]=-s*(vb+XC*Im*(np.sin(-x)-np.sin(beta)))
    i=Im*np.cos(th)
    return th,i,v,iT
def fund(th,v,Im=1.0):
    X=-np.mean(v*np.sin(th))*2/Im
    return X
def harm(th,v,n):
    a=2*np.mean(v*np.cos(n*th)); b=2*np.mean(v*np.sin(n*th)); return np.hypot(a,b)
if __name__=='__main__':
    XC=1.0
    for r in [0.133,0.1,0.15,0.2,0.25]:
        XL=r
        for b in [10,20,25,30,50,55,60,80]:
            bb=b*d
            if abs(np.cos(np.sqrt(XC/XL)*bb))<0.05: continue
            th,i,v,iT=wave(bb,XC,XL)
            ok = iT[(np.abs(((th+np.pi/2)%np.pi)-np.pi/2)<=bb-1e-3)].min()
            print(r,b,'formula %.5f numeric %.5f  min iT in conduction %.3f'%(Xexact(bb,XC,XL),fund(th,v),ok))
