"""Fig 6.3 regenerated: X = 0.5 pu, V = 1 pu, midpoint Thevenin reactance X/4."""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'serif','mathtext.fontset':'dejavuserif','font.size':20})
X=0.5; Xth=X/4; d=np.linspace(0,np.pi,721); deg=np.degrees(d)
P=lambda Vm: 4*Vm*np.sin(d/2)            # P = V Vm sin(d/2)/(X/2)
c=np.cos(d/2)
fig,ax=plt.subplots(figsize=(9.156,5.156),dpi=500)
ax.plot(deg,P(c),'k-',lw=2.2,label='Uncompensated')
ax.plot(deg,P(np.ones_like(d)),'k--',lw=2.2,label='Ideal regulation')
mk=dict(markevery=(260,60),ms=8,lw=1.6)
for I,m in [(0.5,'o'),(1.0,'s')]:
    ax.plot(deg,P(np.minimum(1,c+Xth*I)),'k-',marker=m,mfc='white',label=r'STATCOM: $I_{max}=%g$ pu'%I,**mk)
for B,m in [(0.5,'^'),(1.0,'D')]:
    ax.plot(deg,P(np.minimum(1,c/(1-Xth*B))),'k:',marker=m,mfc='black',label=r'SVC: $B_{max}=%g$ pu'%B,**mk)
ax.set_xlim(0,180); ax.set_ylim(0,4.6); ax.set_xticks(range(0,181,20))
ax.set_xlabel(r'$\delta$ (degrees)'); ax.set_ylabel('Transmitted power (pu)')
ax.grid(alpha=0.3); ax.legend(loc='upper left',fontsize=13,ncol=2,framealpha=0.95,columnspacing=1.0)
fig.tight_layout(); fig.savefig('fig63.png',dpi=500)
