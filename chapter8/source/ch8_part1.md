# Chapter 8 Combined and Special-Purpose FACTS Controllers: UPFC, IPFC, Phase-Angle Regulators, IPC, Current Limiters and Voltage Limiters

## Learning Objectives

After working through this chapter, the reader should be able to:

- derive the active and reactive power delivered by a line equipped with a unified power flow controller (UPFC), construct its circular control region, and compare it with the regions attainable with series compensation or a phase-angle regulator of the same voltage rating;
- explain the real-power exchange between the shunt and series converters of the UPFC, size both converters, model the DC-link energy, and describe the control modes, control structure and the Inez installation;
- analyse the interline power flow controller (IPFC), including the prime-converter constraint, real-power transfer between lines, voltage-margin sharing and the generalized multi-converter controllers;
- derive the behaviour of in-phase voltage regulators, quadrature boosters and ideal phase shifters, and analyse thyristor tap-changers, including their waveforms, harmonics, commutation constraints and ternary winding arrangements;
- derive the power characteristics of the interphase power controller (IPC), its design equations and operating region, and explain the assisted phase-shifting transformer and the decoupling interconnector;
- explain series-resonant, bridge-type and transformer-coupled solid-state fault current limiters, solid-state breakers and transfer switches, and estimate symmetrical and peak fault currents with and without them;
- describe the metal-oxide varistor law and the thyristor-controlled voltage limiter, and calculate clamping levels, inrush transients and absorbed energy;
- formulate research problems on modular converter architectures, coordinated dispatch, impedance-based stability, current-limited operation and protection interaction, and choose a validation method that matches the claim being made.

## 8.1 The Unified Power Flow Controller (UPFC)

### 8.1.1 Concept and circuit

Gyugyi proposed the UPFC in 1991 as a controller that can, within its ratings, act simultaneously or selectively on all the parameters that govern power flow in a line: voltage, impedance and phase angle [1], [2], [6]. FIG{upfc_ckt} shows its circuit. Two voltage-source converters (VSCs) share a DC capacitor. Converter 2 is connected in series with the line through an insertion transformer and injects a voltage $V_{pq}$ of controllable magnitude $0\le V_{pq}\le V_{pq,max}$ and controllable angle $0\le\rho<2\pi$. Converter 1 is connected in shunt through a coupling transformer. Its first task is to supply or absorb, through the DC link, the real power that converter 2 exchanges with the line. It can also generate or absorb reactive power independently, exactly as a STATCOM does, to regulate the bus voltage.

![FIGDEF{upfc_ckt} UPFC circuit: shunt and series voltage-source converters sharing a DC link.](fig/rId22.png){width=88%}

The UPFC is best understood as an energy-coupled combination of the shunt VSC of Chapter 6 and the series VSC of Chapter 7. If the two converters were electrically independent, the series converter could exchange with the line only the real power available from its own DC source, which in practice means none in steady state. Connecting the DC terminals changes this. The shunt converter draws real power from the AC bus, passes it through the DC link, and allows the series converter to inject a voltage at any angle with respect to the line current. This is the physical origin of the two-dimensional P-Q control capability.

The important point is what passes through the DC link and what does not. The commanded series voltage can be resolved into a component in phase with the line current and a component in quadrature with it. The quadrature component exchanges reactive power that is generated or absorbed inside converter 2, as in an SSSC. The in-phase component exchanges real power, and only this average real power, together with converter losses and the small change in capacitor energy during transients, travels through the DC link to converter 1 and from there back to the AC system (FIG{upfc_energy}). Seen from the line, the UPFC is therefore an ideal series voltage source of any phase angle. It can emulate a capacitive or inductive series reactance, an in-phase voltage regulator, a phase shifter, or any combination, and it can move between these functions within a few cycles.

![FIGDEF{upfc_energy} Energy and control paths in a UPFC. Only the real-power imbalance is exchanged through the common DC link; reactive power is handled locally at each converter.](fig/image1.png){width=80%}

The shunt converter therefore has two simultaneous duties. The first is energetic: it regulates the DC-link voltage by supplying the real power demanded by the series converter plus the losses. The second is local AC support: within its current rating it injects or absorbs reactive current to regulate the sending-bus voltage. Both duties share one current limit, so they cannot be treated as independent, unlimited services.

### 8.1.2 Power-flow equations

Consider the two-machine system with the UPFC at the sending end of a lossless line of reactance $X$. Take the receiving voltage as the reference, $\mathbf{V}_r=V_r\angle 0$, the sending voltage as $\mathbf{V}_s=V_s\angle\delta$, and write the series injection as $\mathbf{V}_{pq}=V_{pq}\angle(\delta+\rho)$, so that $\rho$ is measured from the sending-end voltage. Kirchhoff's voltage law around the line gives

$$\mathbf{I}=\frac{\mathbf{V}_s+\mathbf{V}_{pq}-\mathbf{V}_r}{jX}$$ EQDEF{upfcI}

where $\mathbf{I}$ is the line current phasor. The complex power delivered to the receiving end, $S_r=\mathbf{V}_r\mathbf{I}^{*}$, separates into

$$P_r=\frac{V_sV_r}{X}\sin\delta+\frac{V_rV_{pq}}{X}\sin(\delta+\rho),\qquad Q_r=\frac{V_sV_r\cos\delta-V_r^{2}}{X}+\frac{V_rV_{pq}}{X}\cos(\delta+\rho)$$ EQDEF{upfcPQ}

where $P_r$ and $Q_r$ are the active and reactive power delivered to the receiving bus. For $V_s=V_r=V$ the uncompensated values are $P_0=(V^2/X)\sin\delta$ and $Q_0=-(V^2/X)(1-\cos\delta)$, and EQ{upfcPQ} can be written as

$$(P_r-P_0)^2+(Q_r-Q_0)^2=\left(\frac{VV_{pq}}{X}\right)^2$$ EQDEF{upfcCircle}

As $\rho$ sweeps a full turn at fixed $V_{pq}$, the operating point traces a circle centred on the uncompensated point $(P_0,Q_0)$ with radius $VV_{pq}/X$. Allowing any magnitude up to $V_{pq,max}$ fills the disk. The centre slides along the uncompensated locus as $\delta$ changes, but the radius does not depend on $\delta$ (FIG{upfc_regions}). Even at $\delta=0$, where an uncompensated line carries nothing, the UPFC can drive up to $VV_{pq,max}/X$ of active power in either direction.

![FIGDEF{upfc_regions} UPFC control regions in the $P_r$-$Q_r$ plane at $\delta=0^\circ$, $30^\circ$, $60^\circ$ and $90^\circ$ ($V=1$ pu, $X=0.5$ pu, $V_{pq,max}=0.25$ pu).](fig/rId26.png){width=62%}

The attainable active power at any angle therefore lies in the band $P_0\pm VV_{pq,max}/X$ (FIG{upfc_band}). Maximum power at a given angle is obtained with $\sin(\delta+\rho)=1$, that is, with $\mathbf{V}_{pq}$ leading the receiving voltage by $90^\circ$; at that point the reactive power is unchanged from $Q_0$. FIG{pq_rho} shows how both receiving-end powers vary as the injection angle rotates. The active and reactive responses are in quadrature, which is the reason a single-angle device cannot set both of them independently.

![FIGDEF{upfc_band} Range of transmittable active power with a UPFC versus transmission angle ($V=1$ pu, $V_{pq,max}=0.25$ pu, $X=0.5$ pu).](fig/rId29.png){width=78%}

![FIGDEF{pq_rho} Receiving-end active and reactive power versus injection angle for $V=1$ pu, $X=0.5$ pu, $\delta=30^\circ$ and $V_{pq}=0.25$ pu. The two curves are the projections of the control circle of EQ{upfcCircle}.](fig/f_pq_rho.png){width=82%}

The disk is a kinematic result for an ideal, lossless network. A real UPFC occupies only the part of it that also satisfies the series-voltage limit, the line-current limit, the series- and shunt-converter MVA limits, the DC-link voltage band and the semiconductor thermal limits. These constraints are introduced in Sections 8.1.4 and 8.1.6.

#### EXDEF{ex_circle}. UPFC control circle

For $V=1.0$ pu, $X=0.5$ pu, $\delta=30^\circ$ and $V_{pq,max}=0.25$ pu, find the uncompensated operating point, the radius of the ideal control circle and the attainable range of $P_r$.

**Solution.** $P_0=(V^2/X)\sin\delta=2\sin 30^\circ=1.00$ pu and $Q_0=-2(1-\cos 30^\circ)=-0.268$ pu. The radius is $R=VV_{pq,max}/X=0.25/0.5=0.50$ pu. The extreme active powers lie at the horizontal ends of the disk, so $P_{r,max}=1.50$ pu and $P_{r,min}=0.50$ pu. Every point of the disk is geometrically reachable, but converter current, series-transformer voltage and shunt-converter real-power capability must still be checked before a point is accepted as feasible.

### 8.1.3 Comparison with single-parameter controllers

FIG{upfc_compare} compares, at $\delta=30^\circ$, the operating points that three controllers with the same injected-voltage limit can reach. A controllable series reactance (TCSC or SSSC) injects voltage in quadrature with the current, so it can only move the operating point along a curve through $(P_0,Q_0)$. A phase-angle regulator injects voltage in quadrature with the bus voltage and moves the point along a different curve. Only the UPFC, free to choose the angle of injection, fills the whole disk. It can therefore set active and reactive flow independently, which no single-parameter device can do [7], [9].

![FIGDEF{upfc_compare} Attainable $P_r$-$Q_r$ at $\delta=30^\circ$: UPFC, controllable series compensation and phase-angle regulator with the same injected-voltage limit.](fig/rId33.png){width=66%}

The same hardware reproduces these familiar controllers simply by constraining the direction of $\mathbf{V}_{pq}$ (FIG{upfc_modes}). For voltage regulation the injection is aligned with $\mathbf{V}_s$. For series-reactance emulation it is tied to the line current and kept in quadrature with it, leading the current (in the boosting sense) for capacitive compensation. For phase-angle regulation it is chosen so that the line-side voltage $\mathbf{V}_s'$ rotates by a commanded angle with unchanged magnitude. Automatic power-flow control removes all directional restrictions and computes whatever phasor drives the measured P and Q to their references.

![FIGDEF{upfc_modes} Phasor interpretation of four UPFC series-injection modes. $\mathbf{V}_s'=\mathbf{V}_s+\mathbf{V}_{pq}$ is the line-side voltage and $\mathbf{I}$ the line current.](fig/f_modes.png){width=78%}

### 8.1.4 Internal power exchange and ratings

The complex power supplied by the series converter to the line is

$$S_{se}=P_{se}+jQ_{se}=\mathbf{V}_{pq}\mathbf{I}^{*}$$ EQDEF{Sse}

where $P_{se}$ and $Q_{se}$ are the real and reactive power delivered by the series converter. In a lossless UPFC in steady state the DC link must balance:

$$P_{sh}+P_{se}=0$$ EQDEF{dcbal}

where $P_{sh}$ is the real power delivered by the shunt converter to the AC system. The shunt converter therefore draws $P_{se}$ from the bus (or returns it) in addition to its own reactive output $Q_{sh}$, and its rating must satisfy

$$S_{sh}=\sqrt{P_{se}^{2}+Q_{sh}^{2}}\le V_{bus}I_{sh,max},\qquad S_{se}=V_{pq}I\le V_{pq,max}I_{max}$$ EQDEF{ratings}

FIG{upfc_internal} plots $P_r$, $P_{se}$ and $Q_{se}$ against $\rho$ for a representative case. The real power circulated through the link is small compared with the change in line power it produces (0.067 pu of link power for a 0.5 pu increase in line power in Example EX{pr_maxmin}), while the series converter's reactive power is considerably larger. The series converter rating is set by $V_{pq,max}I_{max}$. The shunt converter is often rated similarly, so that it can operate as a full STATCOM when the series converter is out of service.

![FIGDEF{upfc_internal} Receiving-end power and series-converter real and reactive power versus injection angle ($\delta=30^\circ$, $V_{pq}=0.25$ pu, $X=0.5$ pu).](fig/rId37.png){width=82%}

#### EXDEF{ex_series_power}. Series-converter real-power requirement

A UPFC series converter injects 0.12 pu at an angle of $30^\circ$ with respect to a 0.90 pu line current. Find the converter real and reactive power on the same three-phase base.

**Solution.** With the current as reference, $S_{se}=\mathbf{V}_{pq}\mathbf{I}^{*}=0.12\times0.90\angle30^\circ=0.108\angle30^\circ$ pu. Hence $P_{se}=0.108\cos30^\circ=0.0935$ pu and $Q_{se}=0.108\sin30^\circ=0.0540$ pu. The shunt converter must supply about 0.0935 pu of real power through the DC link, plus losses. The 0.054 pu of reactive power is produced inside the series converter and does not cross the link.

#### EXDEF{ex_shunt_alloc}. Shunt-converter current allocation

A shunt VSC connected to a 1.0 pu bus must draw 0.18 pu of real power to support the UPFC DC link and inject 0.24 pu of reactive power for voltage support. Determine its apparent-power duty and current.

**Solution.** $S_{sh}=\sqrt{0.18^2+0.24^2}=0.30$ pu. At $V=1.0$ pu the current magnitude is also 0.30 pu. Once the converter reaches its current limit, real-power balancing and reactive support compete for the same current and cannot be allocated independently.

### 8.1.5 Operating and control modes

The shunt converter operates in one of two modes. In VAR control it follows a reactive power (or reactive current) reference. In automatic voltage control, the usual mode, it adjusts reactive current to regulate the bus voltage at the point of connection along a droop characteristic. In either mode a DC-voltage regulator adds the active-current component that balances the series-converter real power and the losses.

The series converter offers five functional modes. They are control objectives, not different power circuits:

- *Direct voltage injection.* The converter injects the commanded $V_{pq}$ and $\rho$ directly. Special cases are an injection in quadrature with the current (SSSC-like reactive compensation) and an injection in phase with the bus voltage (voltage regulation).
- *Bus voltage regulation.* The injection is kept in phase with the sending-end voltage and its magnitude regulates the voltage at the line-side terminal.
- *Line impedance compensation.* The injection is made proportional to the line current with a chosen phase, emulating a series reactance and, if desired, a series resistance.
- *Phase-angle regulation.* The injection is chosen so that the line-side voltage is shifted by a commanded angle without change of magnitude.
- *Automatic power-flow control.* The most general mode, in which closed outer loops around the measured line P and Q compute the series voltage, so that the commanded flows are maintained in spite of network changes.

### 8.1.6 Dynamic model, control structure and limits

For dynamic studies the DC capacitor cannot be treated as an algebraic power-transfer path. Its stored energy is $W_{dc}=\tfrac12C_{dc}V_{dc}^{2}$. With positive $P_{sh}$ and $P_{se}$ denoting real power delivered from the converters to the AC system, the energy balance is

$$\frac{dW_{dc}}{dt}=\frac{d}{dt}\left(\tfrac12C_{dc}V_{dc}^{2}\right)=-\left(P_{sh}+P_{se}+P_{loss}\right)$$ EQDEF{dcdyn}

and for small deviations about the operating voltage $V_{dc0}$,

$$C_{dc}V_{dc0}\frac{d\,\Delta V_{dc}}{dt}\approx-\left(\Delta P_{sh}+\Delta P_{se}\right)$$ EQDEF{dclin}

EQ{dcbal} is therefore valid only after the energy transient has settled. A temporary mismatch moves $V_{dc}$, and the shunt-converter DC-voltage loop supplies the active current that restores it.

#### EXDEF{ex_dc_dev}. DC-link energy deviation

A 20 mF UPFC DC capacitor operates at 20 kV. For 15 ms the series converter draws 6 MW more real power from the link than the shunt converter supplies. Neglect losses and find the DC voltage after the event.

**Solution.** Initial energy $W_1=\tfrac12CV_1^2=0.5\times0.020\times(20\,000)^2=4.00$ MJ. The deficit is $6\times10^6\times0.015=0.09$ MJ, so $W_2=3.91$ MJ and $V_2=\sqrt{2W_2/C}=19.77$ kV, a 1.1 % dip. The linearized EQ{dclin} gives $\Delta V_{dc}\approx-0.09\times10^6/(0.020\times20\,000)=-225$ V, which agrees closely.

FIG{upfc_ctrl} shows a typical vector-control structure. A phase-locked loop provides the reference angle for both converters. For the series converter, $P_{ref}$ and $Q_{ref}$ are converted into $d$- and $q$-axis line-current references, and a current controller with decoupling computes the series voltage, limited to $V_{pq,max}$. For the shunt converter, a DC-voltage regulator produces the active-current reference that keeps the link charged, and an AC-voltage (or VAR) regulator produces the reactive-current reference. Supplementary loops add power-oscillation damping and transient-stability functions to the series reference.

![FIGDEF{upfc_ctrl} UPFC control structure: series converter in automatic power-flow control, shunt converter regulating DC and AC voltage.](fig/rId42.png){width=96%}

The inner current or voltage loops must be appreciably faster than the outer power, AC-voltage and DC-voltage loops. Bandwidth separation reduces interaction, but it does not remove the coupling that exists through the network and the DC link. Anti-windup is required wherever a reference saturates.

The ideal control disk is not a converter capability curve. At every requested operating point the controller must check series-voltage magnitude, line current, series-converter MVA, shunt-converter current, transformer MVA, DC-link voltage and semiconductor temperature. In normal operation the outer P-Q loop may have full authority. During a severe voltage depression or fault, current limiting overrides it, because semiconductor survival has priority over tracking a power-flow reference. A common priority order is converter protection and DC-link energy first, then the remaining current margin for reactive support. The exact order is manufacturer and application dependent and should be represented explicitly in EMT studies.

A UPFC is not energized by simply enabling both PWM bridges. A typical sequence precharges the DC link, verifies transformer and bus conditions, synchronizes the converter reference frame, enables the shunt converter to establish $V_{dc}$, and only then releases the series converter from bypass. Shutdown reverses the sequence. During an internal converter fault or a severe external fault, the series converter is blocked and a thyristor bypass across the insertion-transformer secondary carries the line current, so the transmission line stays in service even though the power-flow controller is unavailable.

FIG{upfc_resp} shows the qualitative response to a step in the automatic power-flow references. P and Q move to their new values with a controlled transient while $V_{dc}$ is disturbed only temporarily. A sustained drift of $V_{dc}$ indicates a real-power imbalance or shunt-converter saturation. Large oscillations in P or Q point to inadequate damping, loop interaction, measurement delay or an operating point near a limit.

![FIGDEF{upfc_resp} Illustrative UPFC response to a power-flow reference change (normalized). The curves show the expected relationship among P, Q and DC-link voltage, not a universal tuning.](fig/image12.png){width=78%}

Two dynamic duties deserve separate mention. During electromechanical oscillations, the supplementary controller modulates the series-voltage command so that the resulting electrical-power component opposes the speed or angle deviation. During a line fault, the objective changes at once from power-flow tracking to converter protection: series injection is limited, blocked or bypassed according to current and voltage stress, and normal control is restored only after the post-fault network is judged stable. A simulation that keeps enforcing $P_{ref}$ and $Q_{ref}$ through a severe fault produces unrealistically large converter commands and overstates the transient-stability benefit.

### 8.1.7 UPFC with a fixed phase shifter

A UPFC can be combined with a fixed, mechanically tapped phase-shifting transformer. The fixed shifter moves the centre of the control circle to the point that corresponds to the shifted angle, and the UPFC provides fast control around that new centre. The motivation is rating reduction. If the steady requirement is $V_{fix}$ and the dynamic correction is $\Delta V$, the converter need only be rated for the envelope of $\Delta V$ rather than for $V_{fix}+\Delta V$. The price is flexibility, because the fixed component cannot be removed electronically during an emergency.

#### EXDEF{ex_fixed_ps}. Fixed phase shifter plus UPFC

A corridor requires a steady $12^\circ$ phase shift but only $\pm4^\circ$ of fast modulation for damping and dispatch. If an ideal fixed phase shifter supplies $12^\circ$, what range must the UPFC series converter provide, and what is the approximate rating saving on a 1 pu voltage base?

**Solution.** The converter needs to cover only $-4^\circ$ to $+4^\circ$ about the fixed point, giving a total controllable shift of $8^\circ$ to $16^\circ$. From $|V_\sigma|=2V\sin(\sigma/2)$, a $16^\circ$ shift needs 0.278 pu of injection whereas $4^\circ$ needs 0.070 pu, so the series-converter voltage rating falls to roughly one quarter.

### 8.1.8 Field experience: the Inez UPFC

The first UPFC was installed at the Inez substation of American Electric Power in eastern Kentucky and entered test operation in May 1998 [3], [16]. It was a joint project of AEP, EPRI and Westinghouse (later Siemens). It consists of two identical $\pm160$ MVA GTO-thyristor voltage-sourced converters with harmonic-neutralizing multi-pulse transformer arrangements, which can be configured as a STATCOM, an SSSC or a UPFC. Its purpose was to support the voltage of a heavily loaded 138 kV area and to control power flow on a new high-capacity line. Inez established the practicality of converter-based power-flow control, and the same converter building blocks were later used in the NYPA convertible static compensator at Marcy (Section 8.2.4). Present installations use modular multilevel converters instead (Section 8.8.1), but the energy-balance and series-injection principles are unchanged.

## 8.2 The Interline Power Flow Controller (IPFC)

### 8.2.1 Concept

Gyugyi, Sen and Schauder proposed the IPFC to compensate several lines leaving one substation [4]. Each line is given its own series converter, and all converters share a common DC link (FIG{ipfc2}). Each converter can provide reactive series compensation to its own line, as an SSSC would. In addition, because the converters share the DC link, any converter can deliver real power to its line provided another converter draws the same real power from its own line. The IPFC can therefore transfer real power between lines: it can relieve an overloaded line by shifting active power to an underloaded one, equalize both active and reactive flows, and compensate resistive as well as reactive voltage drops.

![FIGDEF{ipfc2} Two-converter IPFC with series converters in two lines and a common DC link.](fig/rId49.png){width=88%}

The common DC link creates no energy. In an IPFC without a shunt converter or storage, the algebraic sum of the average real powers exchanged by all series converters must be zero apart from losses and transient changes of capacitor energy. For $N$ series converters (FIG{ipfcN})

$$\sum_{k=1}^{N}P_{k,pq}+\frac{dW_{dc}}{dt}+P_{loss}=0$$ EQDEF{ipfcbal}

with signs defined at the converter AC terminals. This single constraint distinguishes an IPFC from several independent SSSCs and explains why the individual line commands are coupled.

![FIGDEF{ipfcN} Generalized IPFC with several series converters sharing one DC link at a common substation.](fig/f_ipfc_general.png){width=80%}

### 8.2.2 Constrained operation of the prime converter

In a two-converter IPFC, converter 1 (the prime converter) is chosen to control line 1 fully, with its injected voltage $\mathbf{V}_{1pq}$ free in magnitude and angle. Its line then follows EQ{upfcPQ} and EQ{upfcCircle} exactly as with a UPFC. The difference lies in where the real power comes from. The series power supplied by converter 1 to line 1 must be absorbed by converter 2:

$$P_{1pq}=\mathrm{Re}\left(\mathbf{V}_{1pq}\mathbf{I}_1^{*}\right),\qquad P_{1pq}+P_{2pq}=0$$ EQDEF{ipfc2bal}

where $P_{1pq}$ and $P_{2pq}$ are the real powers delivered to lines 1 and 2 by their converters and $\mathbf{I}_1$ is the current of line 1. Converter 2 must therefore inject into line 2 a voltage whose component in phase with $\mathbf{I}_2$ absorbs exactly $P_{1pq}$. That fixes one degree of freedom of converter 2. The other, its quadrature component, remains free for reactive compensation of line 2, but only within the voltage margin left inside its circular limit (FIG{prime_support}):

$$V_{2p}=-\frac{P_{1pq}}{I_2},\qquad |V_{2q}|\le\sqrt{V_{2,max}^{2}-V_{2p}^{2}}$$ EQDEF{ipfcmargin}

![FIGDEF{prime_support} Voltage decomposition of (a) the prime converter and (b) the supporting converter, each referred to its own line current. Real-power support consumes part of the supporting converter's voltage capability.](fig/f_prime_support.png){width=88%}

The operating region of line 1 is a full disk only if line 2 can supply the required real power within its converter rating. Otherwise line 1's region is clipped to the band $|P_{1pq}|\le V_{2,max}I_2$ (FIG{ipfc_region}). Example EX{ipfc_upf} works through a typical case: at $\delta=30^\circ$, $X=0.5$ pu and $V_{pq,max}=0.25$ pu, holding $Q_{1r}=0$ while raising $P_{1r}$ to 1.42 pu requires converter 1 to supply 0.19 pu of real power. Converter 2, with the same voltage rating, can absorb it in two ways, one of which also raises the power in line 2 to 1.23 pu.

![FIGDEF{ipfc_region} Prime-line operating region of an IPFC at $\delta=30^\circ$ ($V=1$ pu, $X=0.5$ pu, $V_{1pq,max}=0.25$ pu). Only the shaded band is reachable when the supporting converter can exchange at most 0.10 pu or 0.05 pu of real power.](fig/f_ipfc_region.png){width=64%}

In a multi-line installation the prime role need not be permanently assigned. A supervisory controller can redistribute real-power duty according to line loading, converter temperature and remaining voltage margin (FIG{ipfc_bar}).

![FIGDEF{ipfc_bar} Illustrative redistribution of active power among three lines by coordinated IPFC control. The total transfer is unchanged; the overloaded corridor is relieved.](fig/image13.png){width=70%}

#### EXDEF{ex_ipfc3}. Real-power redistribution in a three-converter IPFC

Three series converters share a common DC link. Converter 1 delivers 0.18 pu of real power to line 1 and converter 2 absorbs 0.07 pu from line 2. Neglecting losses and DC-energy change, find the real power of converter 3.

**Solution.** From EQ{ipfcbal}, $P_1+P_2+P_3=0$. Taking delivery to a line as positive, $P_3=-(0.18-0.07)=-0.11$ pu: converter 3 must absorb 0.11 pu from line 3. An IPFC can redistribute real power, but it cannot supply net real power to all lines at once unless a shunt converter, storage or another real-power port is added.

#### EXDEF{ex_ipfc_margin}. Remaining quadrature margin of a supporting converter

A supporting converter is limited to $V_{2,max}=0.20$ pu and carries $I_2=1.0$ pu. It must absorb 0.12 pu of real power for the prime line. Find the largest quadrature component it can still inject, and repeat for a line current of 1.5 pu.

**Solution.** At $I_2=1.0$ pu, $V_{2p}=-0.12$ pu and $|V_{2q}|\le\sqrt{0.20^2-0.12^2}=0.16$ pu. At $I_2=1.5$ pu the same power needs only $V_{2p}=-0.08$ pu, leaving $\sqrt{0.04-0.0064}=0.183$ pu. A heavily loaded supporting line is therefore the better donor, because it can exchange the same real power with a smaller in-phase voltage.

### 8.2.3 Generalized and multi-converter controllers

The UPFC and the IPFC are special cases of a family built from voltage-source converters on a common DC bus. A generalized UPFC (GUPFC) adds a shunt converter to an IPFC: the shunt converter regulates the bus voltage and supplies the net real-power imbalance of the series converters, so that each line can be controlled fully. A generalized IPFC with $n$ series converters satisfies the single steady-state constraint

$$\sum_{k=1}^{n}P_{k,pq}=P_{sh}+P_{storage}-P_{loss}$$ EQDEF{gipfc}

where $P_{k,pq}$ is the real power delivered by the $k$th series converter, $P_{sh}$ that drawn by any shunt converter from its bus, $P_{storage}$ that drawn from any energy store and $P_{loss}$ the converter losses. Each converter adds two degrees of freedom and the DC balance removes one. Converter count alone does not define capability; the connection topology and the DC-link energy paths do [8], [10].

#### EXDEF{ex_ipfc_dc}. IPFC DC-link voltage drift

A 10 mF DC capacitor operates at 15 kV. For 20 ms the algebraic converter-power imbalance removes 3 MW from the capacitor. Neglect losses and find the final DC voltage.

**Solution.** Initial energy $0.5\times0.010\times15\,000^2=1.125$ MJ. The energy removed is $3\times10^6\times0.020=0.060$ MJ, leaving 1.065 MJ, so $V_{dc2}=\sqrt{2\times1.065\times10^6/0.010}=14.59$ kV. Even a short mismatch produces a visible DC excursion, which is why dynamic IPFC models must not replace the capacitor by a constant-voltage source.

### 8.2.4 The convertible static compensator

The New York Power Authority's convertible static compensator (CSC) at the Marcy 345 kV substation made this flexibility practical [11]. Two 100 MVA converters, a shunt transformer and two series transformers in different lines can be configured by switching as one or two STATCOMs, one or two SSSCs, a UPFC or an IPFC. The STATCOM stage was placed in commercial operation in April 2001 and the full CSC was completed in July 2004. Functional convertibility means that a single investment provides a STATCOM today and a power-flow controller tomorrow, as system needs change.

## 8.3 Voltage and Phase-Angle Regulators (TCVR and TCPAR)

### 8.3.1 Principle

A voltage regulator adds an in-phase voltage $\Delta V$ to the bus voltage, changing its magnitude. A phase-angle regulator (PAR) adds a voltage that shifts its phase. FIG{par_phasors} shows the three common forms. The in-phase regulator changes only magnitude. The quadrature booster adds a voltage $V_\sigma$ at $90^\circ$, which shifts the phase by $\sigma=\tan^{-1}(V_\sigma/V_s)$ but also raises the magnitude to $\sqrt{V_s^2+V_\sigma^2}$. The ideal phase shifter adds a voltage at an angle $(\pi+\sigma)/2$ to $\mathbf{V}_s$, so that the magnitude is unchanged and the phase shifts by $\sigma$, with

$$|V_\sigma|=2V_s\sin\frac{\sigma}{2}$$ EQDEF{ideal_ps}

Geometrically, the injection is the chord between two equal-radius phasors separated by $\sigma$.

![FIGDEF{par_phasors} Phasor diagrams of (a) an in-phase voltage regulator, (b) a quadrature booster and (c) an ideal phase shifter ($\sigma=20^\circ$).](fig/f_par_phasors.png){width=96%}

With an ideal phase shifter at the sending end of a lossless line, the transmitted power becomes

$$P=\frac{V^{2}}{X}\sin(\delta\pm\sigma)$$ EQDEF{par_power}

where $\sigma$ is the phase shift and the sign depends on the boost convention. The power-angle curve is shifted sideways rather than scaled (FIG{par_curves}). A phase shifter therefore does not raise the maximum transmissible power of a single line. It lets the operator choose the power at a given network angle, which is exactly what is needed to control loop flows in meshed networks, to keep a heavily loaded line within its limit, or to pick up power on an underused path. In transients, rapidly increasing $\sigma$ after a fault keeps the electrical power high while the machine accelerates, which enlarges the decelerating area, and modulating $\sigma$ with speed deviation adds damping.

![FIGDEF{par_curves} Power-angle curves with a phase-angle regulator: the curve shifts sideways by $\sigma$ without change of peak.](fig/rId60.png){width=74%}

A quadrature booster on a lossless line delivers $P=(V_{s,eff}V_r/X)\sin(\delta+\sigma)$ with $V_{s,eff}=\sqrt{V_s^2+V_\sigma^2}$, so it slightly raises the reactive power flow as well. For small $V_\sigma/V_s$ the magnitude error is second order, which is why the approximation is acceptable at modest angles, but the difference matters for rating and reactive-power calculations. In meshed networks with $X\gg R$, an in-phase regulator mainly controls reactive loop flow and a quadrature regulator mainly controls active loop flow.

#### EXDEF{ex_qb}. Quadrature-booster magnitude error

A 1.0 pu bus receives a quadrature injection of 0.20 pu. Find the resulting voltage magnitude and phase shift, and the injection an ideal phase shifter needs for the same angle.

**Solution.** $|V'|=\sqrt{1+0.2^2}=1.0198$ pu and $\sigma=\tan^{-1}0.2=11.31^\circ$. The shift is accompanied by a 1.98 % magnitude rise. An ideal phase shifter needs $2\sin(5.655^\circ)=0.197$ pu at an angle of $95.7^\circ$ to $\mathbf{V}_s$ and leaves the magnitude at 1.0 pu.

### 8.3.2 Thyristor tap-changers

The classical PAR or voltage regulator is a transformer with a mechanical on-load tap changer, which is slow and wears with every operation. Replacing the mechanical changer by thyristor switches makes the device fast enough for dynamic control. In its simplest form, two taps $V_1$ and $V_2$ of a winding are each connected to the output through an antiparallel thyristor pair. With a resistive load, firing the upper-tap switch at a delay $\alpha$ in each half cycle produces the output waveform of FIG{tap_wave}. The output follows $v_1$ up to $\alpha$ and $v_2$ afterwards, so its fundamental varies continuously between $V_1$ and $V_2$. Because the waveform jumps at $\alpha$, the output contains odd harmonics whose amplitude depends on $V_2-V_1$ and $\alpha$.

![FIGDEF{tap_wave} Thyristor tap-changer with a resistive load: output voltage for $V_1=0.9$ pu, $V_2=1.1$ pu and $\alpha=60^\circ$ (left), and fundamental, 3rd and 5th harmonics versus $\alpha$ (right).](fig/rId64.png){width=96%}

Commutation deserves explicit attention. With an inductive load the current continues after the voltage zero, and with a capacitive load it leads the voltage, so the commutation instants move. The tap-changing circuit must never connect two unequal taps together through conducting valves, because the resulting circulating current is limited only by the leakage impedance of the tap section. Safe transfer therefore requires that the outgoing thyristor has stopped conducting before the incoming one fires, which is why practical gate logic uses current polarity and tap-voltage polarity rather than voltage phase alone, together with interlocks and timed transfer states.

To avoid harmonics altogether, the tap-changer can be operated in discrete steps by switching whole cycles; a transient then occurs only when the tap changes. With identical windings the number of levels grows only linearly with the number of switches. With windings proportioned in a ternary ratio $1:3:9:\dots$, each connected through a bridge that can add it with positive or negative polarity or bypass it, $L$ windings give $3^L$ levels (FIG{ternary}):

$$N_{levels}=3^{L},\qquad \Delta V_{max}=\frac{3^{L}-1}{2}V_{step}$$ EQDEF{ternary}

where $L$ is the number of winding sections, $V_{step}$ the voltage of the smallest section and $\Delta V_{max}$ the largest injected voltage in each direction. Applied to an in-phase winding, this gives a thyristor-controlled voltage regulator (TCVR); applied to a quadrature winding excited from the other two phases, a thyristor-controlled phase-angle regulator (TCPAR).

![FIGDEF{ternary} Injected-voltage levels of a ternary-proportioned three-winding regulator.](fig/rId67.png){width=70%}

#### EXDEF{ex_ternary}. Ternary regulator

A three-section ternary regulator has $V_{step}=4$ kV. Find the section voltages, the number of levels and the maximum positive injection.

**Solution.** The sections are 4, 12 and 36 kV. The number of levels is $3^3=27$, and the maximum positive injection is $4\times(27-1)/2=52$ kV. Ternary proportioning obtains many levels with few sections, but insulation, transformer complexity and valve coordination still govern the practical design.

### 8.3.3 Converter-based regulators

A voltage-source converter connected in series through a transformer can inject a voltage of any phase. If it is used as a voltage regulator or phase-angle regulator, it must exchange real power with the line, because the injected voltage is not in quadrature with the current. That real power has to come from a shunt converter or an energy store: a converter-based PAR is, in effect, a UPFC operated in phase-angle regulation mode. Hybrid schemes combine a mechanically tapped phase shifter for the bulk angle with a small converter for fast trimming and damping. A transformer-only alternative is the Sen transformer, which synthesizes a series voltage of selectable magnitude and angle from tapped windings of a shunt-connected unit [24]; it gives UPFC-like steady-state control at transformer cost but with tap-changer speed.

## 8.4 The Interphase Power Controller (IPC)

### 8.4.1 Motivation and concept

Interconnecting two strong networks raises short-circuit levels, often beyond the ratings of existing breakers. The conventional remedies are to leave bus-tie breakers open, to operate subtransmission radially or to split substation buses, all of which sacrifice flexibility and sometimes reliability. The interphase power controller, developed in Canada in the 1990s [5], offers a passive alternative. Each phase of the tie consists of two parallel branches, one inductive and one capacitive, connected to voltages that are phase-shifted by angles $\psi_1$ and $\psi_2$ (FIG{ipc_ckt}). The phase shifts are obtained either from phase-shifting transformers or by connecting the branches to other phases of the sending network, hence the name. The basic IPC uses only reactors, capacitors and transformers: it generates no harmonics, has no switching losses and needs little maintenance. Power electronics can be added where fast control is needed.

![FIGDEF{ipc_ckt} IPC equivalent circuit: inductive and capacitive branches fed from phase-shifted voltages.](fig/rId73.png){width=80%}

### 8.4.2 Power characteristics

Let the branch susceptances be $B_1$ (inductive, $B_1=-1/X_L<0$) and $B_2$ (capacitive, $B_2=+1/X_C>0$). Branch $k$ sees an angle $\delta_{Bk}=\delta_{SR}-\psi_k$, where $\delta_{SR}=\delta_S-\delta_R$. Summing the two branch flows gives

$$P=-V_SV_R\left(B_1\sin\delta_{B1}+B_2\sin\delta_{B2}\right)$$ EQDEF{ipcP}

$$-Q_S=\sum_{k=1,2}\left(V_S^{2}-V_SV_R\cos\delta_{Bk}\right)B_k,\qquad Q_R=\sum_{k=1,2}\left(V_R^{2}-V_SV_R\cos\delta_{Bk}\right)B_k$$ EQDEF{ipcQ}

where $P$ is the transmitted active power and $Q_S$ and $Q_R$ are the reactive powers at the sending and receiving ends. Subtracting the two reactive equations gives $-Q_S=(B_1+B_2)(V_S^2-V_R^2)+Q_R$, so that with $B_1=-B_2$ the reactive powers at the two ends are equal and opposite whatever the voltages.

In the IPC120 the branches of each phase are connected, through a Y-y6 transformer, to the inverted voltages of the two other phases, which lie at $\psi_1=-60^\circ$ and $\psi_2=+60^\circ$ from the phase voltage; the two connection points are thus $120^\circ$ apart. With $|B_1|=|B_2|=1/X$ and $V_S'=V_S/n$ for transformer ratio $n$, EQ{ipcP} and EQ{ipcQ} combine into

$$\begin{aligned}P&=P_{max}\cos\left(\delta_{SR}-\frac{\psi_1+\psi_2}{2}\right)\sin\frac{\psi_2-\psi_1}{2}\\ Q_R&=-P_{max}\sin\left(\delta_{SR}-\frac{\psi_1+\psi_2}{2}\right)\sin\frac{\psi_2-\psi_1}{2}\end{aligned}$$ EQDEF{ipc120}

with $P_{max}=2V_S'V_R/X$. For the symmetric IPC120 this is $P=0.866P_{max}\cos\delta_{SR}$. The power is a cosine of the angle and is flat near $\delta_{SR}=0$: over $\pm25^\circ$ it changes by less than 10 % (FIG{ipc120}). An ordinary tie line, whose power is a sine of the angle, would swing from strong forward to strong reverse flow over the same range. The IPC also delivers non-zero power at zero angle, because its branches see the phase-shifted voltages.

![FIGDEF{ipc120} Active and receiving-end reactive power of an IPC120 versus angle, compared with an ordinary tie.](fig/rId77.png){width=82%}

The flat characteristic is not produced by feedback control. It results from superposing the powers of an inductive branch and a capacitive branch whose applied voltages are displaced in phase (FIG{ipc_branches}). As the external angle increases, the inductive-branch power $\sin(\delta_{SR}+60^\circ)$ rises while the capacitive-branch power $\sin(60^\circ-\delta_{SR})$ falls, and around the design point their first-order changes cancel. The reactive powers do not cancel in the same way, so branch reactive circulation can be substantial even when the net active power is well behaved. Component ratings must be based on branch current and voltage, not on the net MW transfer alone.

![FIGDEF{ipc_branches} Exact decomposition of IPC120 active power into inductive- and capacitive-branch contributions ($V_S=V_R=1$ pu, $|B_k|=1$ pu). Their opposing slopes produce the flat total $\sqrt3\cos\delta_{SR}$.](fig/f_ipc_branches.png){width=78%}

#### EXDEF{ex_ipc_branch}. IPC branch-current rating

An IPC transfers 300 MW at unity net power factor on a 230 kV three-phase link, but internal branch currents are 1.35 times the line current because of reactive circulation. Estimate the line current and the branch-current rating.

**Solution.** $I=300\times10^6/(\sqrt3\times230\times10^3)=753$ A. Each branch should be rated for at least $1.35\times753=1017$ A before overload margin is added. The net terminal power factor reveals nothing about this internal circulation; branch equipment must be rated from the branch phasors.

### 8.4.3 Design equations, fault behaviour and variants

For a specified $P$ and $Q_R$ at a given angle, EQ{ipcP} and EQ{ipcQ} are linear in $B_1$ and $B_2$ and can be solved directly. For the IPC120 the solution is

$$B_1=\frac{P\left(2V_R-V_S\cos\delta_{SR}-\sqrt3V_S\sin\delta_{SR}\right)-Q_RV_S\left(\sqrt3\cos\delta_{SR}-\sin\delta_{SR}\right)}{\sqrt3V_SV_R\left(V_S-2V_R\cos\delta_{SR}\right)}$$ EQDEF{ipcB1}

$$B_2=\frac{-P\left(2V_R-V_S\cos\delta_{SR}+\sqrt3V_S\sin\delta_{SR}\right)-Q_RV_S\left(\sqrt3\cos\delta_{SR}+\sin\delta_{SR}\right)}{\sqrt3V_SV_R\left(V_S-2V_R\cos\delta_{SR}\right)}$$ EQDEF{ipcB2}

where $B_1$ and $B_2$ are the required branch susceptances. Substituting the results of Example EX{ex_ipc120} ($P=1.673$ pu, $Q_R=-0.448$ pu at $\delta_{SR}=15^\circ$) returns $B_1=-1.00$ pu and $B_2=+1.00$ pu, which is a useful check. The IPC limits its own fault contribution because a fault at one terminal leaves the other terminal feeding through one branch impedance, never through the parallel combination.

The IPC family should be separated into variants because their objectives differ [5], [28]. The IPC120 uses $\pm60^\circ$ internal shifts and matched susceptances to obtain the flattest characteristic. An injection IPC uses smaller shifts produced by series injection transformers, reducing transformer voltage rating. The decoupling interconnector (DI) tunes the two branches to parallel resonance at system frequency; its terminal voltages are then decoupled, and it contributes almost nothing to faults on either side, which allows ties that would otherwise be impossible because of short-circuit levels. The fault-current-limiting transformer (FCLT) is a DI simplified for use in parallel with conventional transformers, raising a station's capacity without raising its short-circuit level. For transmission, where complete decoupling would harm stability, the parallel circuit is detuned. The simplest version is the assisted phase-shifting transformer (APST): an existing PST with a reactive impedance in parallel. The first APST entered service in June 1998 at Plattsburgh, New York, on the tie to Vermont, where inductors were added in parallel with an existing phase-angle regulator to raise its transfer capacity.

### 8.4.4 Operating region and retrofitting of PSTs

Seen from the network, a PST with leakage reactance $X_T$ transfers $P\approx(\delta_{SR}-\psi)/X_T$ for small angles. Its operating region in the $P$-$\delta_{SR}$ plane is a band of slope $1/X_T$ bounded by the tap limits $\psi_{min}$ and $\psi_{max}$ and by winding-current limits. Adding a parallel branch of reactance $X_p$ adds $\delta_{SR}/X_p$ to the power. With an inductor ($X_p>0$) the band becomes steeper and the capacity rises; with a capacitor ($X_p<0$) the slope falls, and with $X_p=-X_T$ the characteristic becomes flat, which is the IPC behaviour. FIG{pst_region} compares the two operating regions.

![FIGDEF{pst_region} Operating regions of a PST alone and of the same PST with a parallel capacitor (IPC), small-angle approximation.](fig/rId82.png){width=92%}

## 8.5 Solid-State Current Limiters, Breakers and Transfer Switches

### 8.5.1 Fault current limitation

Growing generation and interconnection raise fault levels above the interrupting ratings of existing breakers. Fault-current-limiting devices fall into two broad classes (FIG{fcl_class}) [13]. Single-shot devices, such as current-limiting fuses and pyrotechnic limiters, must be replaced after each operation. Multi-operation devices include solid-state, hybrid, saturable-core and superconducting limiters. A solid-state current limiter (SSCL) inserts an impedance into the faulted circuit within a few milliseconds, before the first current peak, so that the downstream breaker sees a reduced current.

![FIGDEF{fcl_class} Classification of fault-current-limiting technologies. This chapter concentrates on solid-state and hybrid implementations and retains superconducting limiters for comparison.](fig/image6.png){width=82%}

A good limiter presents very small impedance and loss in normal operation, responds before the prospective current reaches its first peak, inserts enough impedance during the fault, coordinates with relays and breakers, withstands the associated energy and recovery voltage, and returns to service quickly after clearance. These requirements conflict. A large limiting impedance improves current reduction but raises recovery voltage and stored energy; a semiconductor path improves speed but adds conduction loss and thermal stress.

For preliminary design the symmetrical fault current follows from the Thevenin equivalent, $I_f=V_{ph}/|Z_{th}+Z_{lim}|$. For a predominantly inductive source the required limiting reactance is

$$X_{lim}=\frac{V_{ph}}{I_{f,lim}}-X_s$$ EQDEF{xlim}

where $X_{lim}$ is the reactance the limiter must insert, $V_{ph}$ the phase voltage, $I_{f,lim}$ the permitted symmetrical RMS fault current and $X_s$ the source reactance. This is only an RMS screen. The first asymmetrical peak depends on the fault inception angle and the $X/R$ ratio. IEC 60909 estimates it as

$$i_p=\kappa\sqrt2\,I_k'',\qquad \kappa\approx1.02+0.98\,e^{-3R/X}$$ EQDEF{kappa}

so that for $X/R=15$ the peak is $1.82\sqrt2=2.58$ times the symmetrical RMS value [27]. A limiter intended to relieve breaker making duty or semiconductor stress must therefore be checked in the time domain.

#### EXDEF{ex_xlim}. Required limiter impedance and peak current

A 33 kV system has a per-phase Thevenin impedance of $0.127+j1.90\ \Omega$ ($X/R=15$). Find the additional reactance that reduces the symmetrical three-phase fault current to 5 kA, and compare the first peaks with and without the limiter.

**Solution.** $V_{ph}=33/\sqrt3=19.05$ kV. Neglecting $R$, $X_{tot}=19.05/5=3.81\ \Omega$ and $X_{lim}=3.81-1.90=1.91\ \Omega$. Without the limiter $I_k''=19.05/1.904=10.0$ kA and $i_p=1.82\sqrt2\times10.0=25.7$ kA. With a reactive limiter the $X/R$ ratio of the loop rises to about 30, so $\kappa\approx1.91$ and $i_p\approx1.91\sqrt2\times5.0=13.5$ kA. Limiter insertion transients, breaker recovery voltage and energy duty still require an EMT study.

### 8.5.2 Series-resonant SSFCL

The simplest SSCL places a reactor $L_1$ in series with a capacitor $C_1$ tuned to the fundamental, $\omega^2L_1C_1=1$, so that in normal operation the series impedance is nearly zero (FIG{ssfcl_ckt}). A GTO or thyristor switch across $C_1$ closes within about 3 ms when a fault is detected, removing the capacitor and leaving $X_{L1}$ in the circuit. An MOV across the capacitor limits its overvoltage while the switch closes, and a small reactor in the bypass limits the capacitor discharge current. FIG{ssfcl_sim} shows a simulated 11 kV, 50 Hz case: the prospective peak of 16.3 kA is held to about 4.1 kA.

![FIGDEF{ssfcl_ckt} Series-resonant solid-state fault current limiter.](fig/rId88.png){width=80%}

![FIGDEF{ssfcl_sim} Simulated fault current without limiter and with a series-resonant SSFCL ($L_1=10$ mH, $C_1=1013\ \mu$F, 11 kV, 50 Hz, fault at 40 ms).](fig/rId91.png){width=80%}

### 8.5.3 Bridge-type and transformer-coupled limiters

In the bridge-type SSCL (FIG{bridge_ckt}), a diode or thyristor bridge in series with each phase carries a DC reactor $L_d$ biased with a current $i_d$ larger than the peak load current. In normal operation all bridge arms conduct and the bridge is effectively a short circuit. When a fault drives the line current above $i_d$, the bridge forces the line current to equal the reactor current, and $L_d$ appears in series with the line, limiting $di/dt$ to approximately $V_m/L_d$. FIG{bridge_sim} shows the line and reactor currents. The DC reactor current ratchets upward each half cycle, so a downstream breaker, or gate blocking of the thyristors, must clear the fault within a few cycles.

![FIGDEF{bridge_ckt} Single-phase bridge-type SSCL with DC reactor.](fig/rId95.png){width=74%}

![FIGDEF{bridge_sim} Simulated line and DC-reactor currents of a bridge-type SSCL during a fault at 40 ms.](fig/rId98.png){width=78%}

In the transformer-coupled version, the bridge is connected to the secondary of a series transformer whose primary is in the line. In normal operation the secondary is short-circuited by the thyristors, and the transformer presents only its leakage impedance. On a fault the thyristors are blocked, and the transformer magnetizing impedance, together with a secondary reactor, limits the current. Its control sequence is as important as the power circuit. During start-up the controller verifies voltage magnitude, phase and frequency on both sides, establishes a synchronization reference and energizes the DC reactor before closing the synchronizing path. During a fault the gating is removed or reconfigured, and freewheeling devices provide a path for the reactor energy. Reclosing is permitted only after voltage recovery, phase and frequency checks and confirmation of the bypass state, because an incorrect transition can create severe overvoltage or inrush.

Regardless of topology, the protection sequence has five recognizable states: normal conduction, fault detection, impedance insertion, fault clearing and recovery (FIG{fcl_states}). Detection must be fast but secure. Instantaneous current, $di/dt$, voltage depression, differential quantities or combinations can be used. A very low threshold risks operation during transformer energization or motor starting; a high threshold sacrifices the first-peak benefit. Coordination with downstream relays and breakers therefore belongs in the limiter design, not in a later protection review.

![FIGDEF{fcl_states} Generic operating sequence of a fast solid-state fault current limiter.](fig/image16.png){width=90%}

### 8.5.4 Solid-state breakers and transfer switches

A mechanical breaker cannot influence the first current peak, interrupts only at a current zero after several cycles, and tolerates a limited number of full-rated fault interruptions before contact maintenance. A solid-state breaker (SSB) built from GTOs, IGCTs, IGBTs or thyristors with forced commutation interrupts within a fraction of a cycle and without contact wear. SSBs are used for fast load and fault interruption, as fault-current limiters (with a reactor inserted when the switch opens), and as bus-tie breakers that separate a faulted section before its neighbours see a deep sag.

A limiter and a breaker solve different parts of the protection problem: the limiter reduces the magnitude and rate of rise of current, while the breaker establishes isolation. A solid-state transfer switch (SSTS) does neither; it commutates a sensitive load from a failing preferred feeder to an alternate feeder within about a quarter cycle [12]. Thyristor SSTS designs are efficient because they exploit natural current zeros, while fully controllable devices interrupt more freely but need greater semiconductor and surge-energy capability. Hybrid designs keep a mechanical contact in parallel to carry the load current in normal operation, so that the semiconductor conducts only during the transition and its conduction losses are avoided.

### 8.5.5 Comparison with superconducting limiters

A superconducting fault current limiter (SCFCL) presents near-zero impedance until the current exceeds the critical value, at which the superconductor quenches and a high impedance appears. It acts intrinsically, without detection electronics. Its drawbacks are the cryogenic plant and the recovery time after a quench, which ranges from about a second to tens of seconds depending on design and on the energy dissipated. Solid-state limiters reset faster and are fully controllable, but they carry on-state losses in normal operation unless bypassed.

## 8.6 The Thyristor-Controlled Voltage Limiter (TCVL)

### 8.6.1 Metal-oxide varistors

Zinc-oxide varistors protect equipment against overvoltages because their V-I characteristic is extremely nonlinear:

$$I=kV^{\alpha}\quad\Longleftrightarrow\quad V=C\,I^{1/\alpha}$$ EQDEF{mov}

where $I$ is the varistor current, $V$ its voltage, $k$ and $C$ constants of the material and geometry, and $\alpha$ the nonlinearity exponent, typically 20 to 50 for ZnO against about 5 for the older silicon-carbide arresters. Over many decades of current the voltage changes by only a few tens of percent (FIG{mov_vi}). Varistors are rated by their continuous operating voltage, by their residual (clamping) voltage at a specified impulse current, and by the energy or charge they can absorb [26]. The energy limit follows from thermal stability: a block that absorbs too much energy heats, its leakage current rises, and thermal runaway can follow.

![FIGDEF{mov_vi} Normalized V-I characteristics of metal-oxide varistors for several nonlinearity exponents.](fig/rId105.png){width=72%}

The power law is valuable for understanding but not sufficient for arrester design. Manufacturer data specify residual voltage at standardized current impulses, temporary-overvoltage capability and energy withstand. During a transient the absorbed energy is

$$E=\int_{t_1}^{t_2}v(t)\,i(t)\,dt$$ EQDEF{movE}

Lowering the clamping level reduces insulation stress but generally increases arrester current and absorbed energy, so TCVL design is an insulation-coordination and thermal problem as much as a voltage-threshold problem.

### 8.6.2 Principle of the TCVL

A gapless MOV arrester is designed so that it does not conduct significantly at the highest continuous voltage; its clamping level is therefore around 1.7 times the normal peak voltage. Many temporary and switching overvoltages that harm equipment lie below that level. The TCVL (FIG{tcvl_ckt}) connects an antiparallel thyristor switch across a lower section of the arrester stack. When an overvoltage is detected, the thyristors short that section, and the remaining section clamps at a lower level:

$$V_{lim}=(1-f_b)\,V_{clamp}$$ EQDEF{tcvl}

where $f_b$ is the fraction of the stack bypassed and $V_{clamp}$ the clamping voltage of the full stack. The thyristors are fired only for the duration of the disturbance, so the full stack withstands normal voltage continuously. Once the current through the bypass reaches a natural zero after gating stops, the thyristors recover and the full stack resumes the continuous-voltage duty. The reduced protective level is used to limit dynamic overvoltages after load rejection, overvoltages during capacitor energization, and the voltage across series capacitors (FIG{tcvl_action}). In a three-phase installation each phase has its own voltage measurement, gate isolation and energy check, so that an unsymmetrical disturbance does not force identical action in all phases.

![FIGDEF{tcvl_ckt} Thyristor-controlled voltage limiter: thyristor switch across a section of an MOV stack.](fig/rId109.png){width=40%}

![FIGDEF{tcvl_action} Idealized TCVL action during a temporary overvoltage. The full stack would not conduct below about 1.7 pu; bypassing part of it lowers the limiting level to 1.25 pu only while the thyristors are gated.](fig/f_tcvl_action.png){width=82%}

A practical controller must distinguish a short surge from a temporary overvoltage that justifies controlled bypass. The trigger can use instantaneous voltage, a filtered envelope, event classification or a combination, and the firing decision must respect thyristor polarity (FIG{tcvl_states}). The principal design trade-off is between protective level and energy: bypassing more discs lowers the clamping voltage but forces larger current through the remaining discs and increases their absorbed energy.

![FIGDEF{tcvl_states} State sequence of a thyristor-controlled voltage limiter.](fig/image17.png){width=90%}

#### EXDEF{ex_mov_energy}. MOV energy check

A TCVL clamps a transient at 45 kV while the average arrester current during the main conduction interval is 1.8 kA for 3 ms. Estimate the absorbed energy with a rectangular-pulse approximation.

**Solution.** $E\approx V_{clamp}I_{avg}\Delta t=45\,000\times1\,800\times0.003=243$ kJ. The rectangular approximation is adequate for a first sizing check; final selection should integrate the actual $v(t)i(t)$ waveform with EQ{movE} and compare it with the manufacturer's single-event and repetitive energy capability.

#### EXDEF{ex_bypass}. TCVL bypass fraction

A full MOV stack has an effective clamping level of 90 kV. A controlled event requires about 63 kV. Using the proportional stack model of EQ{tcvl}, estimate the fraction of the stack to bypass.

**Solution.** $f_b=1-63/90=0.30$, so about 30 % of the stack is bypassed. This first-order voltage-sharing model must be confirmed with the actual residual-voltage characteristic, disc tolerances and energy distribution.

### 8.6.3 Capacitor-switching transients

Energizing a capacitor bank through a mechanical switch forms an LC circuit with the source inductance. The inrush oscillates at the natural frequency

$$f_0=\frac{1}{2\pi\sqrt{LC}},\qquad Z_0=\sqrt{\frac{L}{C}},\qquad \hat I_{inrush}\approx\frac{\Delta V}{Z_0}$$ EQDEF{inrush}

where $L$ is the source inductance, $C$ the bank capacitance, $Z_0$ the characteristic impedance and $\Delta V$ the voltage difference at closing. The capacitor voltage can overshoot to 2 pu, or to 3 pu if a charged bank is re-energized at the opposite supply peak. FIG{cap_reenerg} shows this worst case, the effect of an MOV clamping at $1.7V_m$, and the further reduction obtained when a TCVL lowers the clamping level to $1.3V_m$. The energy the MOV must absorb is the integral of $vi$ over the clamping intervals, and it grows sharply as the clamping level is lowered, which is the main design trade-off.

![FIGDEF{cap_reenerg} Re-energization of a capacitor bank charged to $-V_m$: no limiter, MOV clamping at $1.7V_m$, and TCVL clamping at $1.3V_m$ (normalized, natural frequency eight times fundamental, damping neglected).](fig/rId113.png){width=82%}

### 8.6.4 Protection coordination and limitations

TCVL action must be coordinated with conventional surge arresters, breaker switching, capacitor discharge devices and insulation withstand. Triggering too early increases MOV energy and thyristor duty; triggering too late sacrifices the insulation benefit. The device is most attractive where a temporarily lower protective level is valuable but cannot be tolerated continuously because of leakage current and thermal constraints.

## 8.7 Comparison and Selection

The technologies in this chapter should not be ranked on a single scale. UPFC and IPFC are power-flow controllers; TCPAR and TCVR are specialized regulators; the IPC is principally a passive network-shaping device; SSCL and SSB are protection devices; the TCVL is an insulation-protection device. TAB{compare} summarizes their attributes.

Table: TABDEF{compare} Comparison of the controllers of this chapter.

| Attribute | UPFC | IPFC / GUPFC | TCPAR / TCVR | IPC / APST | SSCL / SSB | TCVL |
|:--|:--|:--|:--|:--|:--|:--|
| Parameters controlled | $V$, $X_{eff}$, $\delta_{eff}$ | Flows in several lines | Angle or magnitude | Shape of $P$-$\delta$ curve | Fault current | Overvoltage level |
| Independent $P$ and $Q$ | Yes | Yes in prime line | No | No (passive) | Not applicable | Not applicable |
| Power stage | Two VSCs | $n$ VSCs (plus shunt in GUPFC) | Thyristor tap-changer or VSC | Reactors, capacitors, transformers | Thyristors/GTOs/IGBTs and reactors | Thyristors and MOV |
| External real-power port | Yes, shunt VSC | No in pure IPFC | Not needed (transformer type) | None | Not a dispatch device | None |
| Speed | Sub-cycle | Sub-cycle | About one cycle (thyristor) | Inherent | 1 to 3 ms | Sub-cycle |
| Harmonics | Low (multi-pulse or multilevel) | Low | Some (phase control) or none (stepped) | None | None in normal state | None |
| Normal-state loss | Converter and transformer loss | Converter loss | Low to moderate | Low | Topology dependent | Very low |
| Main limitation | Cost, losses, two ratings | DC balance, supporting margin | Range set by windings, valve duty | Fixed characteristic, branch circulation | Energy, recovery voltage | MOV energy, thyristor duty |
| Best-fit application | Critical corridor needing fast multi-variable control | Several lines at one substation | Fast loop-flow or voltage regulation | Tie with short-circuit constraint | Excess fault level, fast isolation | Dynamic insulation coordination |

Selection should begin with the constrained state variable, not with the device name: active power, reactive power, voltage magnitude, phase angle, fault current or transient overvoltage. The next layer is the dynamic requirement: steady-state dispatch, electromechanical damping, sub-cycle protection or insulation coordination. Only then should topology, rating, redundancy, loss and cost be compared. A UPFC is the most general controller in this chapter, but it is not automatically the best choice. If the requirement is only slow loop-flow control, a phase-shifting transformer may provide the service with much lower loss and complexity. If several lines at one substation must exchange controllable real power, the IPFC is structurally better matched. If short-circuit level is the binding constraint, neither a UPFC nor an IPFC substitutes for a properly designed fault current limiter, and if insulation stress from a switching event is the problem, a TCVL addresses a different physical quantity altogether.

A second useful distinction is the energy path. The UPFC has an AC real-power port through its shunt converter. A pure IPFC redistributes real power among series converters but has no external real-power source. The IPC needs no semiconductor DC link. SSCL and TCVL are designed around transient energy and protection duty. FIG{map} places the devices on a qualitative map of response speed and steady-state controllability.

![FIGDEF{map} Qualitative map of response speed and steady-state power-flow controllability. Positions are indicative only and must not be read as equipment ratings.](fig/image24.png){width=72%}

#### EXDEF{ex_select}. Selecting the controller by the binding constraint

A substation has three outgoing lines. One line is overloaded, a second has spare transfer capability, bus voltage is acceptable, and the short-circuit level is already close to the breaker rating. Which controller family is the natural first candidate if the objective is to redistribute steady line flows without increasing bus fault contribution?

**Solution.** An IPFC (or a set of SSSCs, if real-power exchange between lines is not needed) is the natural FACTS candidate. Its series converters reshape line flows directly, the common DC link lets it exchange real power among lines, and, unlike a shunt converter, series converters behind a fast bypass add little to the bus fault level. A UPFC could control one corridor strongly but does not coordinate several lines, and its shunt converter contributes fault current. The final decision still requires a short-circuit and protection study.
