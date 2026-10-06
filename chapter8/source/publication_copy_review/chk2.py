import numpy as np, math
from scipy.integrate import solve_ivp
w=2*math.pi*50; Vm=math.sqrt(2)*11000/math.sqrt(3)
# series resonant
Rs=0.12;Ls=2e-3;Rl=20;L1=10e-3;C1=1013.21e-6;Lb=0.1e-3;Rb=0.1
Ih=Vm/(Rs+Rl+1j*w*Ls);Vc=Ih/(1j*w*C1)
def rhs(t,y,lim=True):
    i,vc,ib=y
    R=Rs+(Rl if t<0.04 else 0)
    if lim:
        di=(Vm*math.cos(w*t)-R*i-vc)/(Ls+L1)
        if t>=0.043: dib=(vc-Rb*ib)/Lb
        else: dib=0;ib=0
        dvc=(i-ib)/C1
        return [di,dvc,dib]
    else:
        return [(Vm*math.cos(w*t)-R*i)/Ls,0,0]
def run(lim):
    ts=[];ys=[]
    segs=[(0,0.04),(0.04,0.043),(0.043,0.12)] if lim else [(0,0.04),(0.04,0.12)]
    y0=[Ih.real,Vc.real,0] if lim else [Ih.real,0,0]
    for a,b in segs:
        s=solve_ivp(lambda t,y:rhs(t,y,lim),(a,b),y0,max_step=1e-6,rtol=1e-9,atol=1e-9,dense_output=True)
        ts.append(s.t);ys.append(s.y);y0=s.y[:,-1]
    t=np.concatenate(ts);i=np.concatenate([y[0] for y in ys])
    m=t>=0.04;return abs(i[m]).max()
print('SR limited',run(True)/1e3,'prosp',run(False)/1e3)
# prospective with limiter omitted: initial condition: same prefault line current -> but prefault model without limiter? text: "omits the limiter but retains the same prefault line-current initial condition"
