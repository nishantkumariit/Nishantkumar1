import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
plt.rcParams.update({'font.family':'serif','font.serif':['DejaVu Serif'],'mathtext.fontset':'dejavuserif','font.size':10,'axes.grid':True,'grid.color':'0.88','savefig.dpi':220,'legend.fontsize':8.5})
D=np.deg2rad; out='fig/'
def save(f,n): f.tight_layout(); f.savefig(out+n+'.png',bbox_inches='tight'); plt.close(f)
def box(ax,x,y,w,h,t,fs=8.5,fc='#f2f2f2'):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.02',fc=fc,ec='k',lw=1)); ax.text(x,y,t,ha='center',va='center',fontsize=fs)
def arr(ax,p,q,**k): ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=11,color='k',lw=1,**k))

# 1. DSTATCOM vs SVC V-I (corrected slope)
f,ax=plt.subplots(figsize=(6,4.2)); I=np.linspace(-1,1,10)
ax.plot([-1,1],[0.98,1.02],'k',lw=2,label='regulation slope (droop): $V=V_{ref}+X_{sl}I$')
ax.plot([-1,-1],[0,0.98],color='0.35',lw=1.6,label='DSTATCOM: rated current held at low voltage'); ax.plot([1,1],[0,1.02],color='0.35',lw=1.6)
v=np.linspace(0,1.15,50); ax.plot(-v,v,'k--',lw=1.2,label=r'SVC capacitive limit: $I=B_{C,max}V$'); ax.plot(v*0.95,v,'k:',lw=1.4,label=r'SVC inductive limit: $I=B_{L,max}V$')
ax.axvline(0,color='0.6',lw=0.8); ax.set_xlim(-1.3,1.3); ax.set_ylim(0,1.2)
ax.set_xlabel(r'compensator current (pu):  capacitive $\leftarrow$ 0 $\rightarrow$ inductive'); ax.set_ylabel('bus voltage (pu)'); ax.legend(loc='lower center',fontsize=7.8)
ax.annotate('at 0.4 pu voltage: DSTATCOM 1.0 pu,\nSVC 0.4 pu capacitive current',(-1,0.4),(-0.55,0.6),fontsize=8,arrowprops=dict(arrowstyle='->',lw=0.7))
save(f,'f9_vi')

# 2. UPQC control hierarchy
f,ax=plt.subplots(figsize=(8.6,3.6)); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,4.4)
layers=[('Supervisor: mode (UPQC-P/Q/S), limits, priority, protection',3.9),('Reference extraction: PLL, sequence/harmonic separation ($v_L^*$, $i_s^*$)',3.05),('Outer loops: DC-link energy, load-voltage magnitude',2.2),('Inner loops: series voltage, shunt current, active damping',1.35),('Modulation, current/voltage saturation, anti-windup',0.5)]
for i,(t,y) in enumerate(layers):
    box(ax,4.3,y,7.6,0.6,t,fs=9,fc=['#dfe7f0','#eef2f7','#f2f2f2','#f7f7f7','#ffffff'][i])
    if i<4: arr(ax,(4.3,y-0.3),(4.3,y-0.55))
ax.text(8.55,3.9,'seconds',fontsize=8.5,va='center'); ax.text(8.55,2.2,'10-100 ms',fontsize=8.5,va='center'); ax.text(8.55,1.35,'< 1 ms',fontsize=8.5,va='center'); ax.text(8.55,0.5,'switching',fontsize=8.5,va='center')
ax.annotate('',(9.6,0.4),(9.6,4.0),arrowprops=dict(arrowstyle='<->',lw=0.8)); ax.text(9.7,2.2,'bandwidth',rotation=90,va='center',fontsize=8.5)
save(f,'f9_upqc_ctrl')

# 3. J(delta) UPQC-S
f,ax=plt.subplots(figsize=(6,3.6)); d=np.linspace(-10,60,700)
for pf,ls in [(0.8,'-'),(0.95,'--')]:
    phi=np.arccos(pf); Vs=184; I=25; Is=230*I*pf/Vs; dd=D(d)
    J=Is*abs(230*np.exp(1j*dd)-Vs)+230*abs(I*np.exp(1j*(dd-phi))-Is); k=np.argmin(J)
    ax.plot(d,J/1e3,'k',ls=ls,lw=1.6,label=f'pf = {pf}'); ax.plot(d[k],J[k]/1e3,'ko',ms=5); ax.annotate(f'min {J[k]:.0f} VA at δ = {d[k]:.1f}°',(d[k],J[k]/1e3),(d[k]-14 if pf>0.9 else d[k]-2,J[k]/1e3+(4.2 if pf>0.9 else 2.6)),fontsize=8.5,arrowprops=dict(arrowstyle='->',lw=0.7))
ax.set_xlabel('restored load-voltage angle δ (deg)'); ax.set_ylabel(r'$J=S_{se}+S_{sh}$ (kVA)'); ax.legend()
save(f,'f9_J')

# 4. Harmonic source types
f,axs=plt.subplots(1,2,figsize=(8.6,2.9))
for ax,t in zip(axs,['(a) current-source type: thyristor rectifier, large $L_{dc}$','(b) voltage-source type: diode rectifier, large $C_{dc}$']):
    ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,5); ax.set_title(t,fontsize=9)
    ax.plot([0.5,9],[4,4],'k'); ax.plot([0.5,9],[1,1],'k'); ax.add_patch(Circle((0.5,2.5),0.5,fill=False)); ax.text(0.5,2.5,'$V_{sh}$',ha='center',va='center',fontsize=8)
    ax.plot([0.5,0.5],[3,4],'k'); ax.plot([0.5,0.5],[1,2],'k'); ax.add_patch(Rectangle((2,3.75),1.2,0.5,fill=False)); ax.text(2.6,4.45,'$Z_s$',ha='center',fontsize=9)
    ax.text(4.3,4.3,'PCC',fontsize=8)
for ax in axs: ax.plot([4.5,4.5],[3.95,4.05],'k')
ax=axs[0]; ax.plot([7,7],[4,3.4],'k'); ax.add_patch(Circle((7,2.5),0.55,fill=False)); ax.annotate('',(7,3.0),(7,2.0),arrowprops=dict(arrowstyle='->')); ax.text(7.75,2.5,'$I_{Lh}$',fontsize=9); ax.plot([7,7],[1.95,1],'k')
ax.plot([8.6,8.6],[4,3.4],'k'); ax.add_patch(Rectangle((8.35,1.8),0.5,1.4,fill=False)); ax.text(9.0,2.5,'$Z_L$ large',fontsize=8); ax.plot([8.6,8.6],[1.8,1],'k'); ax.text(5.6,0.3,'Norton: shunt APF suitable',fontsize=8.5,ha='center')
ax=axs[1]; ax.plot([7,7],[4,3.6],'k'); ax.add_patch(Rectangle((6.75,3.0),0.5,0.6,fill=False)); ax.text(7.4,3.2,'$Z_L$ small',fontsize=8); ax.add_patch(Circle((7,2.2),0.5,fill=False)); ax.text(7,2.2,'$V_{Lh}$',ha='center',va='center',fontsize=8); ax.plot([7,7],[3.0,2.7],'k'); ax.plot([7,7],[1.7,1],'k'); ax.text(5.6,0.3,'Thevenin: series APF suitable',fontsize=8.5,ha='center')
save(f,'f9_hsources')

# 5. series hybrid frequency response
h=np.linspace(1,25,2000); Xs=0.06; Rs=0.006
ht=4.8; Q=30; XL=1/ht**2*1  # filter with Xc at fund = 1/... choose Xc1=2 pu (0.5 pu var)
Xc1=2.0; XL1=Xc1/ht**2; R=XL1*ht/Q
ZF=R+1j*(h*XL1-Xc1/h); Zs=Rs+1j*h*Xs
f,axs=plt.subplots(1,2,figsize=(8.8,3.4))
for K,ls,lab in [(0,'-','passive filter only'),(0.5,'--','with series APF, K = 0.5 pu'),(2,':','with series APF, K = 2 pu')]:
    axs[0].semilogy(h,abs(ZF/(Zs+ZF+K)),'k',ls=ls,lw=1.4,label=lab); axs[1].semilogy(h,abs(1/(Zs+ZF+K)),'k',ls=ls,lw=1.4,label=lab)
axs[0].set_title(r'(a) load-harmonic sharing $|I_{sh}/I_{Lh}|$',fontsize=9); axs[1].set_title(r'(b) background-voltage admittance $|I_{sh}/V_{sh}|$ (pu)',fontsize=9)
for ax in axs: ax.set_xlabel('harmonic order h'); ax.axvline(5,color='0.6',lw=0.7); ax.axvline(7,color='0.6',lw=0.7)
axs[0].legend(fontsize=7.6); axs[1].text(2.0,40,'parallel resonance\nof $C_F$ with $L_s$',fontsize=8)
save(f,'f9_hybrid_resp')

# 6. TDD vs load fraction
f,ax=plt.subplots(figsize=(5.8,3.4)); lf=np.linspace(0.1,1,200)
for thd,ls in [(0.1,':'),(0.2,'--'),(0.3,'-.'),(0.5,'-')]:
    ax.plot(lf*100,thd*lf*100,'k',ls=ls,lw=1.4,label=f'THD = {int(thd*100)} %')
for lim in (5,8,12): ax.axhline(lim,color='0.6',lw=0.8); ax.text(101,lim,f'{lim} %',va='center',fontsize=8)
ax.set_xlabel(r'fundamental current as % of maximum demand ($I_1/I_L$)'); ax.set_ylabel('TDD (%)'); ax.legend(fontsize=8,loc='upper left'); ax.set_xlim(10,108); ax.set_ylim(0,32)
save(f,'f9_tdd_thd')

# 7. spectrum vs limits
hh=np.array([5,7,11,13,17,19]); I=np.array([40,25,12,8,5,4.])/5; lim=np.array([4,4,2,2,1.5,1.5]); R=I*0.40209636589962455
f,ax=plt.subplots(figsize=(6.2,3.4)); x=np.arange(len(hh))
ax.bar(x-0.2,I,0.38,color='0.55',label='before compensation'); ax.bar(x+0.2,R,0.38,color='#1f4e79',label='after APF (uniform 60 % reduction)')
ax.step(np.r_[x-0.5,x[-1]+0.5],np.r_[lim,lim[-1]],'k--',where='post',lw=1.2,label=r'IEEE 519-2022 limit, $I_{sc}/I_L<20$')
ax.set_xticks(x); ax.set_xticklabels([str(i) for i in hh]); ax.set_xlabel('harmonic order'); ax.set_ylabel(r'$I_h$ (% of $I_L$)'); ax.legend(fontsize=8)
ax.text(1.6,7.4,'TDD: 9.95 % → 4.0 % (limit 5 %)',fontsize=8.5)
save(f,'f9_spectrum')

# 8. statistical assessment (illustrative)
rng=np.random.default_rng(3); t=np.arange(0,7*24*6)/6.0
base=3.2+1.4*np.sin(2*np.pi*(t-8)/24)+0.6*(t%168>120)*-1
tdd=np.clip(base+rng.normal(0,0.45,len(t)),0.3,None)
f,axs=plt.subplots(1,2,figsize=(9,3.2),gridspec_kw={'width_ratios':[2,1]})
axs[0].plot(t,tdd,color='0.4',lw=0.6); p95=np.percentile(tdd,95); p99=np.percentile(tdd,99)
axs[0].axhline(5,color='k',ls='--',lw=1); axs[0].text(2,5.15,'table limit 5 %',fontsize=8); axs[0].axhline(7.5,color='k',ls=':',lw=1); axs[0].text(2,7.65,'1.5 × limit',fontsize=8)
axs[0].set_xlabel('time (h), one week of 10-min values'); axs[0].set_ylabel('TDD (%)'); axs[0].set_title('(a) short-time (10 min) TDD record',fontsize=9)
s=np.sort(tdd); c=np.arange(1,len(s)+1)/len(s); axs[1].plot(s,c*100,'k',lw=1.4)
for p,v in [(95,p95),(99,p99)]: axs[1].plot([v,v],[0,p],'k:',lw=0.8); axs[1].text(0.3,p-(8 if p==95 else -2),f'{p}th percentile: {v:.2f} %',fontsize=7.5)
axs[1].axvline(5,color='k',ls='--',lw=1); axs[1].set_xlabel('TDD (%)'); axs[1].set_ylabel('cumulative probability (%)'); axs[1].set_title('(b) weekly distribution',fontsize=9)
save(f,'f9_stat'); print('p95',p95,'p99',p99)

# 9. compliance workflow
f,ax=plt.subplots(figsize=(8.6,3.0)); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,3)
steps=['1. Define PCC\n(utility interface)','2. Obtain $I_{sc}$ and\nmaximum demand $I_L$','3. Select limits\n(IEEE 519 tables)','4. Measure or\nsimulate $I_h$, $V_h$','5. Statistical\nassessment','6. Mitigate and\nre-verify']
for i,s in enumerate(steps):
    x=0.85+i*1.66; box(ax,x,1.8,1.45,1.0,s,fs=8)
    if i<5: arr(ax,(x+0.73,1.8),(x+0.93,1.8))
ax.text(5,0.5,'Voltage limits (Table of voltage distortion) are checked separately from current limits at every step.',ha='center',fontsize=8.5)
save(f,'f9_workflow')

# 10. normalized rating comparison vs sag depth
X=np.linspace(0,0.5,200); phi=np.arccos(0.8); thd=0.25
dst=np.sqrt(np.sin(phi)**2+thd**2)*np.ones_like(X); dvr=X
upP=X*np.cos(phi)/(1-X)+np.sqrt(np.sin(phi)**2+thd**2+(np.cos(phi)*X/(1-X))**2)
d=np.arccos(1-X); upQse=np.cos(phi)*np.tan(d); IL=np.exp(1j*(d-phi)); Is=np.cos(phi)/(1-X); upQsh=np.sqrt(np.abs(IL-Is)**2+thd**2)
upQ=upQse+np.maximum(upQsh,dst)
f,ax=plt.subplots(figsize=(6.2,3.6))
ax.plot(X*100,dst,'k:',lw=1.6,label='DSTATCOM (reactive + harmonic duty)'); ax.plot(X*100,dvr,'k--',lw=1.4,label='DVR, in-phase (plus storage)')
ax.plot(X*100,dvr+dst,color='0.5',lw=1.2,label='DVR + DSTATCOM (separate units)'); ax.plot(X*100,upP,'k',lw=1.8,label='UPQC-P, series + shunt'); ax.plot(X*100,upQ,'k-.',lw=1.4,label='UPQC-Q, series + installed shunt')
ax.set_xlabel('design sag depth X (%)'); ax.set_ylabel('converter rating / load kVA'); ax.legend(fontsize=7.8); ax.set_ylim(0,2.2)
save(f,'f9_rating')

# 11. sag depth-duration with storage energy
f,ax=plt.subplots(figsize=(6.2,3.8)); t=np.logspace(-2,1,300)
for E,ls in [(10,':'),(50,'--'),(200,'-.'),(1000,'-')]:
    x=E/(1.0*t)  # kJ per (P_L=1 MW): X = E/(P t) with P=1000 kW -> X = E/(1000 t)
    ax.plot(t,np.minimum(E/(1000*t),1)*100,'k',ls=ls,lw=1.2,label=f'{E} kJ per MW of load')
ax.axvspan(0.01,1,color='0.95'); ax.text(0.012,104,'supercapacitor / DC capacitor',fontsize=8); ax.axvspan(1,10,color='0.88'); ax.text(1.2,104,'battery / flywheel',fontsize=8)
ax.set_xscale('log'); ax.set_xlabel('sag duration (s)'); ax.set_ylabel('sag depth X (%)'); ax.set_ylim(0,110); ax.legend(fontsize=7.8,loc='center left')
save(f,'f9_storage')

# 12. economics
N=np.linspace(0,40,200); f,ax=plt.subplots(figsize=(6,3.4))
ax.plot(N,N*0.6*40,'k',lw=1.6,label='expected loss, no mitigation (60 % trip, 40 k$/trip)')
ax.plot(N,N*0.05*40+41.05,'k--',lw=1.4,label='with DVR: residual loss + annualized cost')
ax.plot(N,N*0.03*40+70,'k:',lw=1.4,label='with UPQC: residual loss + annualized cost (illustrative)')
ax.axvline(41.05/(0.55*40),color='0.6',lw=0.8); ax.text(2.2,300,'DVR break-even\n≈ 1.9 events/yr',fontsize=8)
ax.set_xlabel('sag events per year causing exposure'); ax.set_ylabel('annual cost (k$)'); ax.legend(fontsize=7.6)
save(f,'f9_econ')

# 13. selection map (corrected)
f,ax=plt.subplots(figsize=(7.6,3.8)); ax.set_xlim(0,3); ax.set_ylim(0,3); ax.grid(False)
cols=['supply-voltage\ndisturbance','load-current\ndisturbance','both']; rows=['fundamental\n(sag, swell, pf)','harmonic /\nunbalance','interruption /\nsevere event']
cells=[['DVR (sag/swell)\nDSTATCOM (ZVR, weak feeder)','DSTATCOM\n(UPF, balancing)','UPQC'],['DVR / series APF','shunt APF / DSTATCOM\nhybrid filter','UPQC\nor hybrid + DVR'],['UPS, island-capable\nstorage (not a DVR)','SSCL / breaker\n(fault current)','UPS or storage-backed\nUPQC with isolation']]
for i in range(3):
    for j in range(3):
        ax.add_patch(Rectangle((j,i),1,1,fc=['#ffffff','#f2f2f2','#e6e6e6'][i],ec='k',lw=0.8)); ax.text(j+0.5,i+0.5,cells[i][j],ha='center',va='center',fontsize=8.3)
ax.set_xticks([0.5,1.5,2.5]); ax.set_xticklabels(cols); ax.set_yticks([0.5,1.5,2.5]); ax.set_yticklabels(rows)
save(f,'f9_map')
print('ok')
