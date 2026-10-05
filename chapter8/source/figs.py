import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, Polygon
from math import comb
plt.rcParams.update({'font.family':'serif','font.serif':['DejaVu Serif'],'mathtext.fontset':'dejavuserif',
 'font.size':10,'axes.grid':True,'grid.color':'0.88','axes.linewidth':0.8,'savefig.dpi':220,'legend.fontsize':8.5,'legend.framealpha':0.95})
D=np.deg2rad; out='fig/'
def save(fig,n): fig.tight_layout(); fig.savefig(out+n+'.png',bbox_inches='tight'); plt.close(fig)
def arrow(ax,p0,p1,c='k',lw=1.6,ls='-',ms=12):
    ax.add_patch(FancyArrowPatch(p0,p1,arrowstyle='-|>',mutation_scale=ms,color=c,lw=lw,ls=ls,shrinkA=0,shrinkB=0))

# 1. Pr,Qr vs rho
r=np.linspace(0,360,721)
P=1+0.5*np.sin(D(30+r)); Q=-2*(1-np.cos(D(30)))+0.5*np.cos(D(30+r))
fig,ax=plt.subplots(figsize=(6.4,3.4))
ax.plot(r,P,'k',lw=1.6,label=r'$P_r$'); ax.plot(r,Q,'k--',lw=1.4,label=r'$Q_r$')
ax.axhline(1,color='0.5',lw=0.8,ls=':'); ax.axhline(-0.268,color='0.5',lw=0.8,ls=':')
for x,y,t in [(60,1.5,r'$P_{r,\max}=1.5$ at $\rho=60^\circ$'),(240,0.5,r'$P_{r,\min}=0.5$ at $\rho=240^\circ$')]:
    ax.plot(x,y,'ko',ms=4); ax.annotate(t,(x,y),(x+10,y+0.12) if y>1 else (x-60,y+0.25),fontsize=8.5)
ax.plot(330,0.232,'ko',ms=3); ax.annotate(r'$Q_{r,\max}=+0.232$',(330,0.232),(282,-0.2),fontsize=8.5)
ax.plot(150,-0.768,'ko',ms=3); ax.annotate(r'$Q_{r,\min}=-0.768$',(150,-0.768),(160,-0.95),fontsize=8.5)
ax.set_xlim(0,360); ax.set_xticks(range(0,361,60)); ax.set_ylim(-1.1,1.8)
ax.set_xlabel(r'injection angle $\rho$ (deg, measured from $V_s$)'); ax.set_ylabel('pu'); ax.legend(loc='upper right')
save(fig,'f_pq_rho')

# 2. UPFC modes phasors
fig,axs=plt.subplots(2,2,figsize=(7.0,4.6)); axs=axs.ravel()
titles=['(a) voltage regulation','(b) series-reactance emulation','(c) phase-angle regulation','(d) general P-Q control']
Vs=np.array([1.0,0]); Ia=D(-25); I=0.55*np.array([np.cos(Ia),np.sin(Ia)])
for k,ax in enumerate(axs):
    ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-0.1,1.45); ax.set_ylim(-0.45,0.62); ax.set_title(titles[k],fontsize=10)
    arrow(ax,(0,0),Vs); ax.text(0.45,-0.09,r'$V_s$',fontsize=9)
    arrow(ax,(0,0),I,c='0.45',lw=1.2,ls='--'); ax.text(I[0]*0.6+0.02,I[1]*0.6-0.12,r'$I$',color='0.35',fontsize=9)
    if k==0: v=np.array([0.25,0])
    if k==1: v=0.25*np.array([np.cos(Ia-np.pi/2),np.sin(Ia-np.pi/2)]); v=-v  # capacitive: V_inj leads I by 90 (boost sense)
    if k==2:
        s=D(16); v=np.array([np.cos(s)-1,np.sin(s)])
    if k==3: v=0.25*np.array([np.cos(D(55)),np.sin(D(55))])
    arrow(ax,tuple(Vs),tuple(Vs+v),c='#1f4e79',lw=1.8); 
    arrow(ax,(0,0),tuple(Vs+v),c='0.3',lw=1.0)
    ax.text(*(Vs+v/2+np.array([0.03,0.02])),r'$V_{pq}$',color='#1f4e79',fontsize=9)
    ax.text(*((Vs+v)*0.55+np.array([-0.12,0.07])),r"$V_s'$",color='0.25',fontsize=9)
save(fig,'f_modes')

# 3. Generalized IPFC schematic
fig,ax=plt.subplots(figsize=(7.2,3.6)); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,6)
ax.plot([1,1],[0.6,5.4],'k',lw=3); ax.text(0.55,5.6,'common bus',fontsize=8.5)
ys=[4.8,3.2,1.6]
for i,y in enumerate(ys):
    ax.plot([1,4.1],[y,y],'k',lw=1.2); ax.plot([5.3,9.4],[y,y],'k',lw=1.2)
    for j in range(4): ax.add_patch(Circle((4.25+j*0.3,y),0.15,fill=False,lw=1))
    ax.text(9.45,y-0.08,f'line {i+1}',fontsize=8.5)
    ax.add_patch(Rectangle((4.2,y-1.05),0.9,0.55,fill=False,lw=1)); ax.text(4.65,y-0.78,f'VSC{i+1}',ha='center',va='center',fontsize=8)
    ax.plot([4.65,4.65],[y-0.5,y-0.15],'k',lw=0.8)
    ax.plot([5.1,6.6],[y-0.78,y-0.78],'k',lw=0.8)
    ax.text(5.6,y+0.25,f'$V_{{{i+1},pq}}$',fontsize=8.5)
ax.plot([6.6,6.6],[ys[2]-0.78,ys[0]-0.78],'k',lw=2)
ax.plot([6.6,7.4],[2.4,2.4],'k',lw=0.8); ax.plot([7.4,7.4],[2.15,2.65],'k',lw=1.5); ax.plot([7.55,7.55],[2.15,2.65],'k',lw=1.5)
ax.text(7.75,2.3,r'$C_{dc}$',fontsize=9); ax.text(6.7,1.0,'common DC link',fontsize=8.5)
ax.text(6.75,0.35,r'$\sum_k P_{k,pq}+dW_{dc}/dt+P_{loss}=0$',fontsize=9)
save(fig,'f_ipfc_general')

# 4. prime / supporting decomposition
fig,axs=plt.subplots(1,2,figsize=(7.6,3.4))
ax=axs[0]; ax.set_aspect('equal'); ax.set_title('(a) prime converter, line 1',fontsize=9)
arrow(ax,(0,0),(0.3,0),c='0.4',ls='--',lw=1.2); ax.text(0.31,-0.02,r'$I_1$',fontsize=9)
v=0.25*np.array([np.cos(D(40)),np.sin(D(40))])
arrow(ax,(0,0),tuple(v),c='#1f4e79',lw=1.8); ax.text(v[0]-0.02,v[1]+0.015,r'$V_{1pq}$',color='#1f4e79')
ax.plot([v[0],v[0]],[0,v[1]],'k:',lw=1); ax.text(v[0]/2-0.04,-0.035,r'$V_{1p}$ (real power)',fontsize=8)
ax.text(v[0]+0.01,v[1]/2,r'$V_{1q}$',fontsize=8.5)
ax.add_patch(Circle((0,0),0.25,fill=False,ls='--',color='0.6')); ax.set_xlim(-0.3,0.38); ax.set_ylim(-0.3,0.3)
ax.set_xlabel('in phase with $I_1$ (pu)'); ax.set_ylabel('quadrature (pu)')
ax=axs[1]; ax.set_aspect('equal'); ax.set_title('(b) supporting converter, line 2',fontsize=9)
Vm=0.20; Vp=-0.12; Vq=np.sqrt(Vm**2-Vp**2)
ax.add_patch(Circle((0,0),Vm,fill=False,color='k',lw=1.2)); arrow(ax,(0,0),(0.28,0),c='0.4',ls='--',lw=1.2); ax.text(0.285,-0.02,r'$I_2$',fontsize=9)
ax.plot([Vp,Vp],[-Vq,Vq],color='#1f4e79',lw=3,alpha=0.8); ax.plot([0,Vp],[0,0],'k',lw=1.4)
ax.text(Vp-0.02,0.025,r'$V_{2p}=-0.12$',fontsize=8,ha='right')
ax.annotate(r'usable $|V_{2q}|\leq\sqrt{V_{max}^2-V_{2p}^2}=0.16$',(Vp,Vq*0.6),(-0.05,0.24),fontsize=8,arrowprops=dict(arrowstyle='->',lw=0.8))
ax.text(0.09,-0.19,r'$V_{max}=0.20$',fontsize=8); ax.set_xlim(-0.3,0.36); ax.set_ylim(-0.27,0.3)
ax.set_xlabel('in phase with $I_2$ (pu)')
save(fig,'f_prime_support')

# 5. IPFC prime-line region clipped
V=1;X=0.5;dl=D(30);Vm=0.25
mags=np.linspace(0,Vm,120); angs=np.linspace(0,2*np.pi,720)
Mg,An=np.meshgrid(mags,angs)
vs=np.exp(1j*dl); vpq=Mg*np.exp(1j*(dl+An)); I=(vs+vpq-1)/(1j*X); Sr=np.conj(I); Pse=np.real(vpq*np.conj(I))
fig,ax=plt.subplots(figsize=(5.2,4.6))
th=np.linspace(0,2*np.pi,400); ax.plot(1+0.5*np.cos(th),-0.268+0.5*np.sin(th),'k',lw=1.4,label='ideal disk (UPFC-like)')
for lim,col,lab in [(0.10,'0.55',r'$|P_{1pq}|\leq0.10$ pu'),(0.05,'#1f4e79',r'$|P_{1pq}|\leq0.05$ pu')]:
    m=np.abs(Pse)<=lim
    ax.scatter(Sr.real[m],Sr.imag[m],s=0.6,color=col,alpha=0.35,rasterized=True)
    ax.plot([],[],'s',color=col,label=lab+' (support limit)')
ax.plot(1,-0.268,'ko',ms=4); ax.set_aspect('equal'); ax.set_xlabel(r'$P_{1r}$ (pu)'); ax.set_ylabel(r'$Q_{1r}$ (pu)')
ax.legend(loc='lower left',fontsize=7.8); ax.set_xlim(0.4,1.6); ax.set_ylim(-0.85,0.35)
save(fig,'f_ipfc_region')

# 6. PAR phasors
fig,axs=plt.subplots(1,3,figsize=(8.4,2.8)); s=D(20)
tit=['(a) in-phase regulator','(b) quadrature booster','(c) ideal phase shifter']
for k,ax in enumerate(axs):
    ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-0.05,1.3); ax.set_ylim(-0.15,0.5); ax.set_title(tit[k],fontsize=9)
    arrow(ax,(0,0),(1,0)); ax.text(0.45,-0.1,r'$V_s$')
    if k==0: arrow(ax,(1,0),(1.2,0),c='#1f4e79',lw=2); ax.text(1.03,0.04,r'$\Delta V$',color='#1f4e79')
    if k==1:
        t=np.tan(s); arrow(ax,(1,0),(1,t),c='#1f4e79',lw=2); arrow(ax,(0,0),(1,t),c='0.35',lw=1.1)
        ax.text(1.03,t/2,r'$V_\sigma$',color='#1f4e79'); ax.text(0.35,0.2,r"$V_s'=\sqrt{V_s^2+V_\sigma^2}$",fontsize=8)
        a=np.linspace(0,s,30); ax.plot(0.3*np.cos(a),0.3*np.sin(a),'k',lw=0.7); ax.text(0.32,0.03,r'$\sigma$',fontsize=8)
    if k==2:
        e=np.array([np.cos(s),np.sin(s)]); arrow(ax,(1,0),tuple(e),c='#1f4e79',lw=2); arrow(ax,(0,0),tuple(e),c='0.35',lw=1.1)
        ax.text(1.0,0.16,r'$V_\sigma$',color='#1f4e79'); ax.text(0.2,0.28,r"$|V_s'|=|V_s|$",fontsize=8)
        a=np.linspace(0,np.pi,60); ax.plot(np.cos(a*s/np.pi),np.sin(a*s/np.pi),'k:',lw=0.7)
        a=np.linspace(0,s,30); ax.plot(0.3*np.cos(a),0.3*np.sin(a),'k',lw=0.7); ax.text(0.32,0.03,r'$\sigma$',fontsize=8)
        ax.text(0.55,-0.13,r'$|V_\sigma|=2V_s\sin(\sigma/2)$',fontsize=8)
save(fig,'f_par_phasors')

# 7. IPC branch decomposition (exact, IPC120, |B|=1, V=1)
d=np.linspace(-40,40,400)
PL=np.sin(D(d+60)); PC=np.sin(D(60-d)); fig,ax=plt.subplots(figsize=(6.0,3.4))
ax.plot(d,PL,'k--',lw=1.3,label=r'inductive branch, $\sin(\delta_{SR}+60^\circ)$')
ax.plot(d,PC,'k:',lw=1.6,label=r'capacitive branch, $\sin(60^\circ-\delta_{SR})$')
ax.plot(d,PL+PC,'k',lw=1.8,label=r'total, $\sqrt{3}\cos\delta_{SR}$')
ax.plot(d,2*np.sin(D(d)),color='0.6',lw=1.2,label=r'ordinary tie, $X=0.5$ pu')
ax.set_xlabel(r'$\delta_{SR}$ (deg)'); ax.set_ylabel(r'$P$ (pu, $V_S=V_R=1$, $|B_k|=1$)'); ax.legend(fontsize=7.8,loc='lower center',ncol=2); ax.set_ylim(-1.5,2.1)
save(fig,'f_ipc_branches')

# 8. TCVL action
t=np.linspace(0,0.12,4000); env=np.where((t>0.03)&(t<0.09),1.55,1.0); v=env*np.sin(2*np.pi*50*t)
vt=np.clip(v,-1.25,1.25); vt=np.where((t>0.03)&(t<0.09),vt,v)
fig,ax=plt.subplots(figsize=(6.4,3.0))
ax.plot(t*1e3,v,'k:',lw=1.1,label='temporary overvoltage (full stack conducts only above 1.7 pu)')
ax.plot(t*1e3,vt,'k',lw=1.5,label='terminal voltage with TCVL clamp at 1.25 pu')
for y,l in [(1.7,'full-stack level 1.7 pu'),(1.25,'TCVL level 1.25 pu')]:
    ax.axhline(y,color='0.5',ls='--',lw=0.8); ax.axhline(-y,color='0.5',ls='--',lw=0.8); ax.text(1,y+0.04,l,fontsize=7.5)
ax.axvspan(30,90,color='0.93'); ax.text(52,-1.95,'thyristors gated',fontsize=8)
ax.set_xlabel('time (ms)'); ax.set_ylabel('voltage (pu of normal peak)'); ax.set_ylim(-2.05,2.15); ax.legend(loc='upper right',fontsize=7.5)
save(fig,'f_tcvl_action')

# ---- Section 8.8 figures
# 9. timeline
ev=[(1991,'UPFC concept\n(Gyugyi)'),(1998,'Inez UPFC (AEP);\nPlattsburgh APST'),(1999,'IPFC concept\npublished'),(2004,'Marcy CSC\ncompleted (NYPA)'),
    (2007,'Distributed FACTS\nconcept'),(2015,'Nanjing 220 kV\nMMC-UPFC'),(2016,'Transformerless\nUPFC (4.16 kV test)'),(2017,'Suzhou 500 kV\nMMC-UPFC'),(2020,'m-SSSC fleets in\nseveral grids'),(2025,'Solid-state and direct-\ninjection UPFC research')]
fig,ax=plt.subplots(figsize=(9.6,3.6)); ax.axis('off'); ax.set_xlim(1988,2028); ax.set_ylim(-2.4,2.4)
ax.plot([1989,2027],[0,0],'k',lw=1.5)
for i,(y,l) in enumerate(ev):
    s=[1,-1,1,-1,1,-1,1,-1,1,-1][i]; h=[0.4,0.4,0.4,0.4,0.4,0.4,1.25,1.25,0.4,0.4][i]; ax.plot([y,y],[0,h*s],'k',lw=0.8); ax.plot(y,0,'ko',ms=4)
    ax.text(y,(h+0.05)*s,f'{y}\n{l}' if s>0 else f'{l}\n{y}',ha='center',va='bottom' if s>0 else 'top',fontsize=8)
save(fig,'f_timeline')

# 10. modular N-1 and availability
fig,axs=plt.subplots(1,2,figsize=(8.6,3.3))
ax=axs[0]; nb=np.arange(0,4)
for N,m in [(6,'o'),(8,'s'),(12,'^')]:
    ax.plot(nb,18/(N-nb),'k-',marker=m,ms=4,lw=1,label=f'$N={N}$')
ax.axhline(4,color='0.4',ls='--',lw=1); ax.text(2.2,4.08,'cell rating 4 kV',fontsize=8)
ax.set_xlabel('bypassed cells $n_b$'); ax.set_ylabel('required cell voltage (kV)'); ax.set_xticks(nb); ax.legend(title=r'$V_{se}=18$ kV',fontsize=8); ax.set_title('(a) voltage sharing after bypass',fontsize=9)
ax=axs[1]; A=np.linspace(0.98,0.9999,200)
for r,ls in [(0,'-'),(1,'--'),(2,':')]:
    N=12+r; As=[sum(comb(N,k)*(1-a)**k*a**(N-k) for k in range(r+1)) for a in A]
    ax.plot(A,1-np.array(As),'k',ls=ls,lw=1.4,label=f'{r} redundant')
ax.set_yscale('log'); ax.set_xlabel('cell availability $A_c$'); ax.set_ylabel('unavailability $1-A_{sys}$'); ax.legend(title='12 required cells',fontsize=8); ax.set_title('(b) effect of cell redundancy',fontsize=9)
save(fig,'f_modular')

# 11. impedance Bode
f=np.logspace(np.log10(100),np.log10(4000),3000); w=2*np.pi*f
Zc=1j*w*1e-3+15*np.exp(-1j*w*150e-6)
fig,axs=plt.subplots(2,1,figsize=(6.4,4.8),sharex=True)
axs[0].loglog(f,abs(Zc),'k',lw=1.6,label=r'converter port $Z_c$')
for Lg,ls,lab in [(0.5e-3,'--',r'stiff grid, $L_g=0.5$ mH'),(2e-3,':',r'weaker grid, $L_g=2$ mH')]:
    Zg=0.05+1j*w*Lg; axs[0].loglog(f,abs(Zg),'k',ls=ls,lw=1.3,label=lab); axs[1].semilogx(f,np.degrees(np.angle(Zg)),'k',ls=ls,lw=1.3)
    i=np.where(np.diff(np.sign(abs(Zg)-abs(Zc))))[0][0]; axs[0].plot(f[i],abs(Zg[i]),'ko',ms=4)
    pm=180-abs(np.degrees(np.angle(Zg[i])-np.angle(Zc[i]))); axs[0].annotate(f'{f[i]:.0f} Hz, PM = {pm:.0f}°',(f[i],abs(Zg[i])),(f[i]*(0.45 if Lg>1e-3 else 1.15),abs(Zg[i])*(2.6 if Lg>1e-3 else 0.35)),fontsize=8,arrowprops=dict(arrowstyle='->',lw=0.6))
axs[1].semilogx(f,np.degrees(np.unwrap(np.angle(Zc))),'k',lw=1.6); axs[1].axhline(-90,color='0.6',lw=0.8); axs[1].axhline(90,color='0.6',lw=0.8)
axs[1].axvline(1/(4*150e-6),color='0.5',ls='-.',lw=0.9); axs[1].text(1720,30,r'$\mathrm{Re}\{Z_c\}<0$ above $1/(4T_d)$',fontsize=7.8)
axs[0].set_ylabel(r'$|Z|$ ($\Omega$)'); axs[1].set_ylabel(r'$\angle Z$ (deg)'); axs[1].set_xlabel('frequency (Hz)'); axs[0].legend(fontsize=7.8,loc='upper left')
save(fig,'f_impedance')

# 12. delay
f=np.linspace(0.1,2.5,300); fig,ax=plt.subplots(figsize=(5.6,3.1))
for Td,ls in [(0.02,'-'),(0.05,'--'),(0.1,'-.'),(0.2,':')]:
    ax.plot(f,-360*f*Td,'k',ls=ls,lw=1.4,label=f'$T_d={int(Td*1e3)}$ ms')
ax.axvspan(0.1,0.8,color='0.93'); ax.text(0.18,10,'inter-area band',fontsize=8); ax.axvspan(0.8,2.5,color='0.97'); ax.text(1.3,10,'local-mode band',fontsize=8)
ax.set_xlabel('mode frequency (Hz)'); ax.set_ylabel('phase lag (deg)'); ax.legend(fontsize=8,loc='lower left'); ax.set_ylim(-185,22)
save(fig,'f_delay')

# 13. capability
fig,ax=plt.subplots(figsize=(4.8,4.4)); th=np.linspace(0,2*np.pi,400)
for V,ls,lab in [(1.0,'-',r'$V=1.0$ pu'),(0.5,'--',r'$V=0.5$ pu (fault)')]:
    ax.plot(V*np.cos(th),V*np.sin(th),'k',ls=ls,lw=1.4,label=lab+r', $|S|\leq V I_{max}$')
ax.axvline(-0.3,color='#1f4e79',lw=1.2); ax.text(-0.27,-1.08,r'$P_{sh}=-0.3$ pu (DC-link support)',fontsize=7.6,color='#1f4e79')
for V in (1,0.5):
    q=np.sqrt(V**2-0.09); ax.plot([-0.3,-0.3],[-q,q],color='#1f4e79',lw=3,alpha=0.5); ax.plot(-0.3,q,'ko',ms=3); ax.text(-0.27,q-0.08,f'$Q_{{max}}={q:.3f}$',fontsize=7.6)
ax.set_aspect('equal'); ax.set_xlabel(r'$P_{sh}$ (pu)'); ax.set_ylabel(r'$Q_{sh}$ (pu)'); ax.legend(fontsize=7.5,loc='upper right'); ax.set_xlim(-1.15,1.15); ax.set_ylim(-1.15,1.35)
save(fig,'f_capability')

# 14. SSCB MOV energy
k=np.linspace(1.15,2.5,200); fig,ax=plt.subplots(figsize=(5.6,3.1))
ax.plot(k,k/(k-1),'k',lw=1.6,label=r'energy ratio $E_{MOV}/(\frac{1}{2}LI_0^2)=k/(k-1)$')
ax.plot(k,1/(k-1),'k--',lw=1.3,label=r'normalized fall time $t_f\,V_s/(LI_0)=1/(k-1)$')
ax.set_xlabel(r'clamping ratio $k=V_{c}/V_s$'); ax.set_ylabel('normalized value'); ax.set_ylim(0,8); ax.legend(fontsize=8)
save(fig,'f_sscb')
print('done')
