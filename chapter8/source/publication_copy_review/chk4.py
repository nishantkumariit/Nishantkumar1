import numpy as np, math
def clamp(h,dt=1e-6):
    q=-1.0;u=0.0;E=0;th=0;n=int(2*math.pi/dt);qmax=0
    for k in range(n):
        th=k*dt
        if abs(q)>=h and q*u>0:
            # clamped: q fixed, u evolves via inductor with source - h
            du=64*(math.cos(th)-q)
            E+=q*u*dt  # MOV current = u (capacitor current zero)
            u+=du*dt
            if q*u<=0: u=0.0 if False else u
        else:
            # RK2 midpoint
            k1q=u;k1u=64*(math.cos(th)-q)
            qm=q+0.5*dt*k1q;um=u+0.5*dt*k1u
            q+=dt*um;u+=dt*64*(math.cos(th+0.5*dt)-qm)
            if abs(q)>h: q=math.copysign(h,q)
        qmax=max(qmax,abs(q))
    return E,qmax
for h in (1.7,1.3): print(h,clamp(h),clamp(h,5e-7))
# unclamped peak
th=np.linspace(0,2*np.pi,200001);v=64/63*np.cos(th)-127/63*np.cos(8*th);print('unclamped max',abs(v).max())
# delay
from scipy.special import lambertw
Lf=1e-3;Kp=15;Td=150e-6;Rg=0.05
for Lg in (0.5e-3,2e-3):
    L=Lf+Lg;wh=math.sqrt(Kp**2-Rg**2)/L;Tc=math.acos(-Rg/Kp)/wh
    roots=[lambertw(-(Kp*Td/L)*math.exp(Rg*Td/L),k)/Td-Rg/L for k in range(-50,51)]
    r=max(roots,key=lambda s:s.real)
    print(Lg,Tc*1e6,r,-r.real/abs(r))
    f=np.linspace(100,5000,2000001);s=1j*2*np.pi*f
    Zg=Rg+s*Lg;Zc=s*Lf+Kp*np.exp(-s*Td);Lm=Zg/Zc;m=abs(Lm)
    idx=np.where(np.diff(np.sign(m-1)))[0]
    for i in idx:
        ang=np.degrees(np.angle(Lm[i]));print('  cross',f[i],ang,180-abs(ang))
print('KpTd/Lf',Kp*Td/Lf)
