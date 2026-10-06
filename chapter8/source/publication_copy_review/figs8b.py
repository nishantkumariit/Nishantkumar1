import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Serif','mathtext.fontset':'dejavuserif','font.size':12})
DPI=300
def arrow(ax,p0,p1,ls='-',lw=1.6):
    ax.annotate('',xy=p1,xytext=p0,arrowprops=dict(arrowstyle='->',lw=lw,ls=ls,color='k',shrinkA=0,shrinkB=0,mutation_scale=14))
# ---------- Fig 8.7
fig,axs=plt.subplots(2,2,figsize=(8.4,5.6))
th_i=np.deg2rad(-25); I=0.55*np.exp(1j*th_i); Vs=1.0+0j
cases=[('(a) Bus-aligned rise',0.22+0j),
       ('(b) Capacitive rise (leads $\\underline{I}$ by 90°)',0.22*np.exp(1j*(th_i+np.pi/2))),
       ('(c) Constant-magnitude phase shift',np.exp(1j*np.deg2rad(16))-1),
       ('(d) General injection',0.22*np.exp(1j*np.deg2rad(50)))]
for ax,(title,V) in zip(axs.flat,cases):
    Vp=Vs+V
    arrow(ax,(0,0),(Vs.real,Vs.imag))
    arrow(ax,(Vs.real,Vs.imag),(Vp.real,Vp.imag),lw=2.0)
    arrow(ax,(0,0),(Vp.real,Vp.imag),ls='--',lw=1.3)
    arrow(ax,(0,0),(I.real,I.imag),ls=':',lw=1.4)
    ax.text(Vs.real-0.02,-0.09,'$\\underline{V}_s$',ha='center')
    ax.text(Vp.real+0.03,Vp.imag+0.03,"$\\underline{V}_s'$",ha='left')
    m=Vs+V/2; ax.text(m.real+0.05,m.imag-0.02,'$\\underline{V}_{pq}$',ha='left',va='top')
    ax.text(I.real+0.02,I.imag-0.07,'$\\underline{I}$',ha='left')
    ax.set_title(title,fontsize=12,loc='left')
    ax.set_xlim(-0.08,1.45);ax.set_ylim(-0.36,0.42);ax.set_aspect('equal');ax.axis('off')
fig.tight_layout();fig.savefig('fig8_7.png',dpi=DPI);plt.close()
# ---------- box helpers
def box(ax,x,y,w,h,txt,fs=13):
    ax.add_patch(plt.Rectangle((x-w/2,y-h/2),w,h,fill=False,lw=1.4))
    ax.text(x,y,txt,ha='center',va='center',fontsize=fs,linespacing=1.25)
# ---------- Fig 8.29
fig,ax=plt.subplots(figsize=(8.2,1.75))
labels=['Normal\nlow-Z path','Detection\ncurrent and\nlogic','Limitation\ncommutate or\ninsert Z','Clearance\nbreaker\ninterrupts','Recovery\nenergy and\nreclose checks']
w,h,g=2.05,1.15,0.32
for k,l in enumerate(labels):
    x=k*(w+g); box(ax,x,0,w,h,l,fs=12)
    if k<4: arrow(ax,(x+w/2,0),(x+w/2+g,0))
ax.set_xlim(-w/2-0.1,4*(w+g)+w/2+0.1);ax.set_ylim(-0.6,0.6);ax.axis('off')
fig.tight_layout();fig.savefig('fig8_29.png',dpi=DPI);plt.close()
# ---------- Fig 8.42
fig,ax=plt.subplots(figsize=(11,4.6))
ax.text(5.5,4.35,'Choose the model and the real hardware required by the claim',ha='center',fontsize=12.5)
top=[(1.6,'Steady-state\nnetwork model'),(5.5,'RMS dynamics and\nsmall-signal models'),(9.4,'Switching EMT with\nprotection logic')]
for x,t in top: box(ax,x,3.2,2.9,1.0,t)
arrow(ax,(3.05,3.2),(4.05,3.2));arrow(ax,(6.95,3.2),(7.95,3.2))
bot=[(1.8,'Controller HIL\nreal controller,\nsimulated plant'),(5.5,'Protection HIL\nreal relay,\nsimulated faults'),(9.2,'Power HIL or prototype\nreal power hardware,\ninterface stability')]
for x,t in bot:
    box(ax,x,0.9,3.2,1.35,t); arrow(ax,(9.4,2.7),(x,1.575))
ax.set_xlim(0,11);ax.set_ylim(0,4.7);ax.axis('off')
fig.tight_layout();fig.savefig('fig8_42.png',dpi=DPI);plt.close()
# ---------- Fig 8.35
fig,ax=plt.subplots(figsize=(8,6))
pts={'IPC':(0.10,0.45),'TCPAR':(0.52,0.52),'IPFC':(0.70,0.74),'UPFC':(0.74,0.87),'SSCL':(0.83,0.20),'TCVL':(0.83,0.08)}
for k,(x,y) in pts.items():
    ax.plot(x,y,'ko',ms=7);ax.text(x-0.015,y+0.03,k,ha='right',fontsize=12)
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.set_xticks([]);ax.set_yticks([])
ax.set_xlabel('Slower  ←  application response  →  faster',fontsize=13)
ax.set_ylabel('Less  ←  steady flow-control freedom  →  more',fontsize=13)
fig.tight_layout();fig.savefig('fig8_35.png',dpi=DPI);plt.close()
# ---------- Fig 8.38
Lf=1e-3;Kp=15;Td=150e-6;Rg=0.05
f=np.logspace(2,np.log10(5000),4000);w=2*np.pi*f
Zc=1j*w*Lf+Kp*np.exp(-1j*w*Td)
fig,(a1,a2)=plt.subplots(2,1,figsize=(9,7.4),sharex=True)
a1.loglog(f,abs(Zc),'k-',lw=1.8,label='$|Z_c|$')
for Lg,ls in ((0.5e-3,'--'),(2e-3,':')):
    a1.loglog(f,abs(Rg+1j*w*Lg),'k'+ls,lw=1.6,label=f'$|Z_g|$, $L_g$ = {Lg*1e3:g} mH')
cr=[(903.93,2e-3,(420,30)),(1598.19,0.5e-3,(1150,1.4)),(2165.92,0.5e-3,(2500,2.2))]
for fc,Lg,(tx,ty) in cr:
    z=abs(Rg+1j*2*np.pi*fc*Lg); a1.plot(fc,z,'ko',ms=5)
    a1.annotate(f'{fc:.2f} Hz',xy=(fc,z),xytext=(tx,ty),fontsize=11,arrowprops=dict(arrowstyle='-',lw=0.8))
a1.set_ylabel('|Z| (Ω)');a1.grid(True,which='both',alpha=0.3);a1.legend(loc='upper left',fontsize=10.5)
a2.semilogx(f,Zc.real,'k-',lw=1.8);a2.axhline(0,color='k',lw=0.8)
a2.axvspan(1666.67,5000,fill=False,hatch='///',lw=0.8)
a2.text(2050,9.5,'First negative-\nresistance band',fontsize=11,bbox=dict(fc='white',ec='none'))
a2.set_ylabel('Re $Z_c$ (Ω)');a2.set_xlabel('Frequency (Hz)');a2.grid(True,which='both',alpha=0.3)
a2.set_xlim(100,5000)
a1.set_title('$L_f$ = 1 mH, $K_p$ = 15 Ω, $T_d$ = 150 μs, $R_g$ = 0.05 Ω',fontsize=11)
fig.tight_layout();fig.savefig('fig8_38.png',dpi=DPI);plt.close()
