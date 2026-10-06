import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Serif','mathtext.fontset':'dejavuserif','font.size':13})
fig,ax=plt.subplots(figsize=(9,6.2));lw=1.8
def coil(x0,y,n=4,r=0.17,up=True):
    for k in range(n):
        th=np.linspace(0,np.pi,40);xc=x0+r+2*r*k
        ax.plot(xc+r*np.cos(th),y+(1 if up else -1)*r*np.sin(th),'k',lw=lw)
def box(x,y,w,h,t):
    ax.add_patch(plt.Rectangle((x-w/2,y-h/2),w,h,fill=False,lw=lw));ax.text(x,y,t,ha='center',va='center')
def L(xs,ys): ax.plot(xs,ys,'k',lw=lw)
xc0=3.3;n=4;r=0.17;wc=2*r*n
for yline,sec,name,ld,vsc in ((8.0,-1,'feeder 1','load 1','VSC1'),(1.0,1,'feeder 2','load 2','VSC2')):
    box(1.0,yline,1.4,0.7,name);box(8.6,yline,1.4,0.7,ld)
    L([1.7,xc0],[yline,yline]);L([xc0+wc,7.9],[yline,yline])
    coil(xc0,yline,up=(sec<0))
    yc=yline+sec*0.32
    for dy in (0.04,0.11): L([xc0,xc0+wc],[yc+sec*dy*0+sec*(dy-0.04)-sec*0.02]*2) if False else None
    L([xc0,xc0+wc],[yline+sec*0.30]*2);L([xc0,xc0+wc],[yline+sec*0.38]*2)
    ys=yline+sec*0.68;coil(xc0,ys,up=(sec>0))
    yv=yline+sec*2.1
    L([xc0,xc0],[ys,yv-sec*0.35]);L([xc0+wc,xc0+wc],[ys,yv-sec*0.35])
    box(xc0+wc/2,yv,1.5,0.7,vsc)
# DC link between VSC1 (y=5.9) and VSC2 (y=3.1)
xv=xc0+wc/2+0.75
for yv,s in ((5.9,1),(3.1,-1)):
    L([xv,6.0],[yv+0.15,yv+0.15]);L([xv,6.6],[yv-0.15,yv-0.15])
L([6.0,6.0],[3.25,6.05]);L([6.6,6.6],[2.95,5.75])
ax.plot([6.0,6.6],[4.55,4.55],alpha=0)
L([6.0,6.18],[4.5,4.5]);L([6.42,6.6],[4.5,4.5]);L([6.18,6.18],[4.2,4.8]);L([6.42,6.42],[4.2,4.8])
for x,y in ((6.0,6.05),(6.6,5.75),(6.0,3.25),(6.6,2.95),(6.0,4.5),(6.6,4.5)): ax.plot(x,y,'ko',ms=5)
ax.text(6.85,4.5,'$C_{dc}$ (shared DC link)',va='center')
ax.text(5.85,6.2,'+',ha='center');ax.text(6.8,5.85,'−',ha='center')
ax.text(5.1,7.1,'real power from a healthy feeder\nsupports the sagged one',ha='left',fontsize=12)
ax.set_xlim(0,9.5);ax.set_ylim(0.3,8.7);ax.set_aspect('equal');ax.axis('off')
fig.tight_layout();fig.savefig('fig9_33.png',dpi=300)
