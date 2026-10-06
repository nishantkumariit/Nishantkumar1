import numpy as np, math
w=2*math.pi*50; Vm=math.sqrt(2)*11000/math.sqrt(3)
# bridge
Rs=0.2;Ls=2e-3;Ld=20e-3;Rl=8.75946
Z=Rs+Rl+1j*w*Ls;Ih=Vm/Z;print('prefault',abs(Ih),math.degrees(-np.angle(Ih)))
def sim(h):
    i=Ih.real;idc=1500.0;t=0;mx=0;n=int(0.12/h)
    for k in range(n):
        t=k*h;vs=Vm*math.cos(w*t);R=Rs+(Rl if t<0.04 else 0)
        if abs(i)<idc-1e-9:
            i_new=i+h*(vs-R*i)/Ls
            if abs(i_new)>idc: i_new=math.copysign(idc,i_new)
            i=i_new
        else:
            sg=math.copysign(1,i)
            # try inside
            di=(vs-R*i)/Ls
            if sg*di<0: i=i+h*di
            else:
                idc=idc+h*(sg*vs-R*idc)/(Ls+Ld); i=sg*idc
        if t>=0.04: mx=max(mx,abs(i))
    return mx,idc
a=sim(2e-6);b=sim(1e-6);print('bridge',a,b,(a[0]-b[0])/b[0]*100)
