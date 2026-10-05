exec(open('chk.py').read().split("print('=== examples')")[0].split('# numeric check')[0])
s2=np.sqrt(2)
d=np.linspace(0,np.pi,1000001)
P=2*np.sin(d)+0.5*np.sin(d/2); k=np.argmax(P); print('6.30f',P[k],np.degrees(d[k]))
# 6.26e
for p in (6,12,24,48):
    ns=[kk*p+s for kk in range(1,3000) for s in (-1,1)]; ns=np.array(ns,float)
    print(p,np.sqrt(np.sum(1/ns**2))*100, np.sqrt(np.sum(1/ns[:4]**2))*100, np.sqrt(np.sum((1/(ns**2*0.2))**2))*100)
# 6.31
Zs=0.8+4j; ZL=35+27j; V=415/np.sqrt(3); I=V/abs(Zs+ZL); print('6.31',I,I*abs(ZL),I*abs(ZL)*np.sqrt(3),I*abs(Zs))
def VL(B):
    Y=1/ZL+1j*B; Zp=1/Y; return abs(V*Zp/(Zs+Zp))
B=brentq(lambda b:VL(b)-V,0,0.1); print(B*1e3,B*V**2,3*B*V**2,B*V,V**2*(1/ZL).real, 3*V**2*(1/ZL).real)
# answers
X=3*400**2/35e3; print('A6.1',X,X/w*1e3,400/X,np.sqrt(3)*400/X,afor(0.4))
a=D(130); I1=F(a); print('A6.2',[In(a,n)/s2/(1/s2)*100 for n in (3,5,7)])
base=1; Ib=Ir(a); trip=np.sqrt(sum(In(a,n)**2/2 for n in range(3,600,6))); I1r=F(a)/s2
print(' THD',np.sqrt((Ib/I1r)**2-1),np.sqrt((np.sqrt(Ib**2-trip**2)/I1r)**2-1))
X=w*0.02; base=s2*230/X; a=D(140); print('A6.3',Ir(a)*base,F(a)*base/s2,230**2*F(a)/X,base*(1+np.cos(a)))
a=D(135); print('A6.4',[In(a,n)*100 for n in (11,13,23,25)])
for Q in (25e3,50e3,100e3): X=3*415**2/Q; print('A6.5',X,X/w*1e3)
n=4.8;k=n*n/(n*n-1); Xn=3*415**2/60e3; XC=k*Xn; print('A6.6',Xn,XC,1/(w*XC)*1e6,XC/n**2/w*1e3,k,k*415*s2,(1+k)*415*s2)
n=4; rho=0.3; print('A6.7',np.degrees(np.arcsin(rho)),np.sqrt(1-rho**2*(1-1/n**2)),n*abs((1-1/n**2)*rho-1))
for E in (1.04,0.95): I=(E-1)/(0.12); V=1+0.04*I; print('A6.9',I,V,V*I)
X=3*13.8**2/90; print('A6.10',X,X/w*1e3, 13.8e3**2/60e6, 1/(w*13.8e3**2/60e6)*1e6, afor(60/90))
for q,N in ((10,1),(55,3),(90,4)): print('A6.11',N*25-q,afor((N*25-q)/30))
print(afor(20/30))
for B in (1.0,-0.4): print('A6.12',B/(1-B/6))
print('A6.13',1+0.06,0.85,1-0.04)
X=0.6; Im=1.5; c=1-Im*X/4; dl=2*np.arccos(c); P=lambda dd:np.sin(dd)/X+Im/2*np.sin(dd/2)
dd=np.linspace(0,np.pi,1000001); kk=np.argmax(P(dd)); print('A6.14',np.degrees(dl),2/X*np.sin(dl/2),P(D(120)),2/X,P(dd[kk]),np.degrees(dd[kk]))
print('A6.15',2*1.5e6*0.015/((18e3**2-16e3**2))*1e3, 0.6e6/(w*0.662e-3*17e3))
print('A6.16',[100/(n*n*0.15) for n in (23,25)])
G=10e3/415**2; Bc=G/np.sqrt(3); print('A6.17',G*1e3,Bc*1e3,Bc/w*1e6,1/(w*Bc)*1e3,Bc*415**2,10e3/(np.sqrt(3)*415))
