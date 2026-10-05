
## 8.8 Recent Advances and Research Directions

The research question has moved from whether these controllers can regulate power flow to how they should be built, dispatched, stabilized and protected in networks dominated by power electronics. This section surveys the state of the art and develops each research direction from an equation or constraint already introduced in Sections 8.1 to 8.6, so that a research scholar can see precisely which part of the classical model a new contribution must change. Each subsection follows the same pattern: what has been achieved, the governing relations, the limitations of current approaches, and the open problems worth pursuing.

### 8.8.1 State of the art: from multi-pulse GTO converters to modular controllers

The first generation of combined controllers, represented by Inez (1998) and Marcy (2001 to 2004), used GTO converters whose output was synthesized by multi-pulse magnetic summation [3], [11], [16]. The transformers were large, the losses were a few percent of rating, and the converter could not be partitioned easily for redundancy. Three developments have since changed the picture (FIG{timeline}).

![FIGDEF{timeline} Milestones in combined and special-purpose FACTS controllers, from concept to modular and solid-state implementations.](fig/f_timeline.png){width=100%}

The first is the modular multilevel converter (MMC). The 220 kV Nanjing West Ring UPFC, commissioned in 2015, was the first MMC-based UPFC: one shunt converter on the 35 kV tertiary of a 220 kV transformer and two series converters in two parallel 220 kV lines, which makes it a GUPFC-type arrangement in the terminology of Section 8.2.3. The 500 kV UPFC in the southern Suzhou grid entered service at the end of 2017 and was, at that time, the highest-voltage and largest-capacity UPFC in operation [18]. MMC cells replace the multi-pulse transformers, provide near-sinusoidal output without filters, and allow redundant cells to be added at modest cost.

The second is the move toward transformerless and distributed series injection. Divan and Johal proposed distributed FACTS, in which many small, line-mounted modules each inject a modest series voltage [19]; the concept matured into commercial modular SSSCs that are now installed by transmission owners in Europe and the Americas to push power off overloaded circuits [30]. At distribution and medium voltage, a transformerless UPFC built from two cascaded multilevel inverters was demonstrated on a 4.16 kV test system [17].

The third is solid-state isolation. Recent work replaces line-frequency insertion transformers by cascaded modules with high-frequency isolated DC-DC stages (dual-active-bridge cells), so that the series and shunt ports exchange energy through compact medium-frequency magnetics [14]. Direct-injection low-voltage controllers that avoid transformers altogether and process only part of the line power have also been proposed for feeders with high penetration of distributed generation [25]. Reviews of the wider FACTS field confirm that UPFC, IPFC, distributed power-flow control and fault-current limitation remain active areas, with growing attention to optimal placement and stability in renewable-rich grids [13], [15].

Table: TABDEF{installs} Representative field installations and demonstrators discussed in this chapter.

| Year | Installation | Voltage level | Technology | Significance |
|:--|:--|:--|:--|:--|
| 1998 | Inez UPFC, AEP, USA | 138 kV | Two $\pm160$ MVA GTO multi-pulse VSCs | First full-scale UPFC; STATCOM, SSSC and UPFC modes [3], [16] |
| 1998 | Plattsburgh APST, NYPA, USA | Tie to Vermont | Inductors in parallel with an existing PAR | First commercial IPC-family device [28] |
| 2001 to 2004 | Marcy CSC, NYPA, USA | 345 kV | Two 100 MVA VSCs, one shunt and two series transformers | Convertible STATCOM, SSSC, UPFC and IPFC [11] |
| 2015 | Nanjing West Ring, China | 220 kV | Three MMCs, two series and one shunt | First MMC-based UPFC [18] |
| 2017 | Southern Suzhou, China | 500 kV | MMC-based UPFC | Highest voltage UPFC at commissioning [18] |
| 2016 | Transformerless UPFC test system, USA | 4.16 kV | Two cascaded multilevel inverters | Removes insertion and shunt transformers [17] |
| 2020s | Modular SSSC fleets, several utilities | 110 kV to 230 kV class | Line- or substation-mounted single-phase modules | Relocatable, incremental series compensation [19], [30] |

### 8.8.2 Modular multilevel and solid-state UPFC architectures

For a modular series converter with $N$ cells whose fundamental outputs are aligned, the commanded series voltage is the phasor sum

$$\mathbf{V}_{se}=\sum_{k=1}^{N}\mathbf{V}_k$$ EQDEF{cellsum}

Equal sharing gives $V_k=V_{se}/N$ only while every cell has the same available voltage and thermal margin. If $n_b$ cells are bypassed after failures, the survivors must raise their contribution, and the design condition becomes

$$\frac{V_{se}}{N-n_b}\le V_{cell,max}\quad\Longrightarrow\quad N\ge\frac{V_{se}}{V_{cell,max}}+n_b$$ EQDEF{nminus}

FIG{modular}(a) shows how quickly the per-cell requirement rises when the cell count is small. Cell voltage is not the only constraint. Each cell of a series converter carries the full line current, and in a single-phase H-bridge cell the instantaneous power contains a component at twice the line frequency. With RMS cell voltage $V$, RMS current $I$ and phase angle $\varphi$ between them,

$$p(t)=VI\cos\varphi-VI\cos(2\omega t-\varphi)$$

so the stored energy oscillates with a peak-to-peak value $\Delta E=S_{cell}/\omega$, where $S_{cell}=VI$. Since $\Delta E\approx C\,V_{dc}\,\Delta V_{pp}$, the cell capacitance needed to hold the peak-to-peak ripple to $\Delta V_{pp}$ is

$$C_{cell}\ge\frac{S_{cell}}{\omega\,V_{dc}\,\Delta V_{pp}}$$ EQDEF{cellC}

This relation explains why single-phase modular series converters are capacitor-dominated in volume and why ripple-cancelling arrangements, such as three-phase cell groups or active power decoupling, are attractive research topics.

Redundancy is usually expressed as availability. If $N_r$ cells are required, $r$ redundant cells are installed and each cell has availability $A_c$ with independent failures, the converter is available whenever no more than $r$ cells are out:

$$A_{sys}=\sum_{k=0}^{r}\binom{N_r+r}{k}(1-A_c)^{k}A_c^{\,N_r+r-k}$$ EQDEF{avail}

FIG{modular}(b) shows that a single redundant cell typically reduces unavailability by more than an order of magnitude.

![FIGDEF{modular} Modular series converters: (a) required cell voltage after bypass for an 18 kV injection and (b) converter unavailability versus cell availability for 12 required cells with 0, 1 and 2 redundant cells.](fig/f_modular.png){width=96%}

#### EXDEF{ex_nminus}. N-1 voltage margin of a modular UPFC

A modular series converter contains six identical cells, each rated for 4 kV fundamental output, and the operating point requires 18 kV of injection. Find the per-cell voltage before and after one cell is bypassed, and the minimum cell count for operation with two cells bypassed.

**Solution.** Normal sharing is $18/6=3.0$ kV per cell. After one bypass the five survivors supply $18/5=3.6$ kV each, leaving 0.4 kV of margin per cell. With two bypassed cells, EQ{nminus} gives $N\ge18/4+2=6.5$, so seven cells are required.

#### EXDEF{ex_cellC}. Cell capacitor sizing

A single-phase H-bridge cell of a modular SSSC injects 1.2 kV RMS into a line carrying 1.0 kA RMS at 50 Hz. Its DC voltage is 2.0 kV and the peak-to-peak ripple must not exceed 10 %. Find the minimum cell capacitance. Then find the converter availability if 12 such cells are required, one redundant cell is fitted and each cell has $A_c=0.995$.

**Solution.** $S_{cell}=1.2\times1.0=1.2$ MVA and $\Delta V_{pp}=200$ V, so EQ{cellC} gives $C\ge1.2\times10^6/(314.16\times2000\times200)=9.55$ mF. Without redundancy $A_{sys}=0.995^{12}=0.9416$. With one redundant cell, EQ{avail} gives $A_{sys}=0.995^{13}+13\times0.005\times0.995^{12}=0.9981$, so the unavailability falls from 5.8 % to 0.19 %.

The principal limitations of current architectures are three. Series cells see the full line fault current, so their bypass must act within the first current rise. Floating cells must be insulated to line potential and supplied with gate power. Solid-state designs with medium-frequency isolation add two conversion stages, so their efficiency and fault ride-through have yet to be proven at transmission ratings [14]. Open problems include fault-tolerant capacitor-voltage balancing under unequal cell temperatures, ripple-energy reduction, wide-bandgap cells for medium-voltage series injection, and reliability models that combine cell failure rates with bypass-switch failure modes.

### 8.8.3 Distributed and modular series power-flow control

A modular SSSC injects a voltage in quadrature with the line current, $\mathbf{V}_m=\pm jX_m\mathbf{I}$, so each module emulates a small positive or negative reactance and $n$ modules emulate $\Delta X=nX_m$ [19], [30]. For two parallel paths of reactance $X_1$ and $X_2$ carrying a total $P_T$, adding $\Delta X$ to path 1 gives

$$P_1=P_T\,\frac{X_2}{X_1+X_2+\Delta X},\qquad P_2=P_T-P_1$$ EQDEF{dfacts}

provided the external network holds $P_T$. The attraction is incremental deployment: modules can be added, removed or relocated as congestion patterns change. The limitations follow from the physics. A quadrature-only module exchanges no real power, so it cannot emulate resistance or move power against the natural angle in the way a UPFC can. Each module must bypass itself during faults, and a fleet of modules changes the apparent impedance seen by distance relays (Section 8.8.8).

#### EXDEF{ex_dfacts}. Sizing a fleet of series modules

Two parallel paths of 0.3 pu and 0.6 pu share 2.3 pu (natural sharing 1.533 pu and 0.767 pu). Each series module emulates 0.02 pu of inductive reactance. How many modules must be placed in path 1 to reduce its flow to 1.3 pu or less, and what voltage does each module inject?

**Solution.** From EQ{dfacts}, $0.9+\Delta X\ge2.3\times0.6/1.3=1.0615$, so $\Delta X\ge0.1615$ pu and nine modules are needed ($\Delta X=0.18$ pu). Then $P_1=2.3\times0.6/1.08=1.278$ pu and $P_2=1.022$ pu. Each module injects $V_m=X_mI_1\approx0.02\times1.278=0.026$ pu, a small voltage that is the basis of the low module rating.

### 8.8.4 Coordinated dispatch and optimal placement

Distributed and combined controllers turn a device-design problem into a constrained network-optimization problem. For branch $k$ between buses $i$ and $j$ with series impedance $Z_k$ and a controllable series source $\mathbf{V}_{se,k}$,

$$\mathbf{I}_k=\frac{\mathbf{V}_i+\mathbf{V}_{se,k}-\mathbf{V}_j}{Z_k}$$ EQDEF{opfbranch}

and an AC optimal power flow with power-flow controllers can be written as

$$\min_{x,u}\;F(x,u)\quad\text{s.t.}\quad g(x,u)=0,\;\;h(x,u)\le0,\;\;|\mathbf{V}_{se,k}|\le V_{se,k}^{max},\;\;|\mathbf{I}_k|\le I_k^{max}$$ EQDEF{opf}

where $x$ collects bus voltages, $u$ the generator set points and controller injections, $g$ the AC power-balance equations and $h$ the operating limits. Device-specific couplings are then added. For an IPFC, $\sum_k\mathrm{Re}(\mathbf{V}_{se,k}\mathbf{I}_k^{*})+P_{loss}=0$ from EQ{ipfcbal}. For a UPFC, $\mathrm{Re}(\mathbf{V}_{se}\mathbf{I}^{*})+P_{sh}+P_{loss}=0$ together with the shunt limit of EQ{ratings}.

The bilinear power term $\mathrm{Re}(\mathbf{V}_{se}\mathbf{I}^{*})$ makes the problem nonconvex even where the network part is relaxed. Second-order-cone and semidefinite relaxations of the network equations [23], McCormick envelopes for the bilinear device terms, and mixed-integer formulations for placement are the standard tools; learning-based surrogates are increasingly used to screen many contingencies quickly. A recurring weakness of published work is that the OPF may return an injection inside the ideal control disk that violates the converter current limit in a contingency. A credible formulation enforces converter capability in every post-contingency state, not only in the base case. Security-constrained dispatch of mixed fleets (UPFC, PST and modular SSSC together), stochastic formulations for renewable variability, and exactness conditions for relaxations that include device constraints remain open.

### 8.8.5 Converter-grid interaction and impedance-based stability

Fast converter controls give a converter port a frequency-dependent terminal impedance. A controller that behaves well in one network can interact with another converter, an HVDC station or a weak or resonant network through the PLL, current controller, DC link and outer loops [21]. Represent the converter port by an impedance $Z_c(s)$ and the network seen from it by $Z_g(s)$. For a current-controlled port the interaction is governed by the minor-loop gain

$$L(s)=\frac{Z_g(s)}{Z_c(s)}=Z_g(s)\,Y_c(s)$$ EQDEF{minorloop}

and the interconnection is stable if $L(s)$ satisfies the Nyquist criterion, given that each subsystem is stable on its own [20]. In practice the magnitude crossover $|Z_g|=|Z_c|$ is located and the phase margin $\mathrm{PM}=180^\circ-|\angle Z_g-\angle Z_c|$ is evaluated there. For three-phase studies the scalar test is replaced by the generalized Nyquist criterion applied to dq-frame or sequence-domain matrices,

$$\det\left[\mathbf{I}+\mathbf{Z}_g(s)\,\mathbf{Y}_c(s)\right]=0$$ EQDEF{gnc}

whose roots are the closed-loop interaction modes.

A minimal model that already shows the mechanism is a current-controlled VSC with filter inductance $L_f$, proportional current gain $K_p$ and a computation-plus-PWM delay $T_d$:

$$Z_c(j\omega)=j\omega L_f+K_p\,e^{-j\omega T_d}$$ EQDEF{zc}

Its real part $K_p\cos\omega T_d$ becomes negative above $f=1/(4T_d)$. In that band the converter port is an active, negative-resistance source, and any network inductance that crosses its magnitude there leaves little phase margin (FIG{impedance}). For a UPFC the problem is multi-port: a perturbation at the shunt terminal modulates $V_{dc}$, which changes the voltage available to the series port. Deriving the two converters separately and joining them through an ideal, infinitely stiff DC source hides exactly this coupling, which is one reason three-port impedance models of combined controllers are a worthwhile research topic.

![FIGDEF{impedance} Impedance-based screening for the converter model of EQ{zc} ($L_f=1$ mH, $K_p=15\ \Omega$, $T_d=150\ \mu$s) against two network inductances. The stiffer network crosses inside the negative-resistance band and has a much smaller phase margin.](fig/f_impedance.png){width=82%}

#### EXDEF{ex_impedance}. Phase-margin screen

For the converter of FIG{impedance}, find the frequency above which the port becomes active, and compare the interaction margins for $L_g=0.5$ mH and $L_g=2$ mH ($R_g=0.05\ \Omega$).

**Solution.** $1/(4T_d)=1/(4\times150\times10^{-6})=1667$ Hz. Solving $|Z_g|=|Z_c|$ numerically gives a crossover at 903 Hz for $L_g=2$ mH, where $\angle Z_c\approx-30^\circ$, $\angle Z_g\approx+90^\circ$ and $\mathrm{PM}\approx61^\circ$. For $L_g=0.5$ mH the crossover moves to 1598 Hz, close to the active band, where $\angle Z_c\approx-78^\circ$ and $\mathrm{PM}\approx12^\circ$, a poorly damped harmonic resonance. The result shows that "stronger" is not always "safer" for delay-dominated interactions, and it identifies the frequency at which an EMT study should look first.

### 8.8.6 Wide-area damping control and communication delay

Supplementary damping loops on a UPFC or IPFC are increasingly driven by remote phasor measurements. The communication and processing delay $T_d$ adds a phase lag

$$\phi_d=-360\,f\,T_d\ \text{degrees},\qquad e^{-sT_d}\approx\frac{1-sT_d/2}{1+sT_d/2}$$ EQDEF{delay}

at the mode frequency $f$; the first-order Padé form on the right is used when the delay must appear in a state-space model. A delay that looks small in milliseconds can consume much of the phase lead designed into a damping controller (FIG{delay}). If the uncompensated lag rotates the damping torque far enough, a loop designed to damp a mode can excite it.

![FIGDEF{delay} Phase lag introduced by end-to-end delay in a wide-area damping loop.](fig/f_delay.png){width=74%}

#### EXDEF{ex_delay}. Communication delay in supplementary damping

A wide-area UPFC damping loop acts on a 0.8 Hz inter-area mode. Find the phase lag caused by delays of 40 ms and 120 ms.

**Solution.** $\phi_d=-360\times0.8\times0.040=-11.5^\circ$ and $-360\times0.8\times0.120=-34.6^\circ$. The second value is comparable to the lead normally provided by one compensation stage, so delay must be included in the design and its worst-case value used in robustness checks.

Research directions here include delay-robust and adaptive damping controllers, coordination of several FACTS damping loops so that they do not compete for the same mode, and cyber-physical resilience when measurements are lost or spoofed.

### 8.8.7 Grid-forming concepts and current-limited operation

A conventional UPFC is synchronized to the network through a PLL and regulates power flow; it does not establish frequency. Grid-forming control is now central to converter-dominated systems, and a combined controller could in principle let its shunt port form a local voltage angle while the series port shapes corridor flow. The difficulty is energy and current coordination. Both ports draw on one DC store and on semiconductor current limits, and during a fault the shunt port's apparent-power capability shrinks with the voltage:

$$P_{sh}^{2}+Q_{sh}^{2}\le\left(V I_{sh,max}\right)^{2}\quad\Longrightarrow\quad |Q_{sh}|\le\sqrt{\left(VI_{sh,max}\right)^{2}-P_{sh}^{2}}$$ EQDEF{capab}

Once the current limit is active, the pre-fault P-Q references cannot all be satisfied, and the priority rule decides the outcome (FIG{capability}). Grid-forming literature shows that the choice among current-reference saturation, virtual impedance and voltage limiting changes fault contribution, synchronization stability and recovery [22]. For a virtual-impedance limiter with internal voltage $E$ and a worst-case terminal voltage $V_{min}$, the impedance needed to respect the current limit is $|Z_v|\ge(E-V_{min})/I_{max}$.

![FIGDEF{capability} Shunt-converter capability at normal and depressed voltage with 0.3 pu of real power reserved for DC-link support.](fig/f_capability.png){width=58%}

#### EXDEF{ex_capab}. Reactive capability during a voltage dip

A UPFC shunt converter has $I_{sh,max}=1.0$ pu and must keep drawing 0.3 pu of real power to support the series converter. Find its reactive capability at $V=1.0$ pu and during a fault that depresses the bus to 0.5 pu.

**Solution.** From EQ{capab}, $|Q_{sh}|\le\sqrt{1-0.09}=0.954$ pu at 1.0 pu voltage, and $|Q_{sh}|\le\sqrt{0.25-0.09}=0.400$ pu at 0.5 pu. The dip removes 58 % of the reactive support exactly when it is most needed, unless the series converter is bypassed so that the real-power reservation can be released. A study should state this priority explicitly.

### 8.8.8 Protection-aware design and solid-state interruption

Series and combined controllers change the voltages and currents measured by distance, differential and overcurrent protection. Let a series source inject $\mathbf{V}_{inj}$ between the relay location and the line, so that the line-side voltage is $\mathbf{V}_{relay}+\mathbf{V}_{inj}$. For a bolted fault at a fraction $m$ of a line of impedance $Z_L$,

$$Z_{app}=\frac{\mathbf{V}_{relay}}{\mathbf{I}}=mZ_L-\frac{\mathbf{V}_{inj}}{\mathbf{I}}$$ EQDEF{zapp}

Capacitive emulation ($\mathbf{V}_{inj}=+jX_c\mathbf{I}$) shortens the apparent impedance and makes zone 1 overreach; inductive emulation makes it underreach. Because the converter saturates, blocks and bypasses during the fault, $\mathbf{V}_{inj}$ itself changes within the relay measurement window, so the study must reproduce those transitions rather than assume instantaneous removal of the controller.

#### EXDEF{ex_zapp}. Distance-relay overreach

A line has $Z_L=j0.50$ pu and a zone-1 reach of 80 % ($j0.40$ pu). A series converter between the relay and the line emulates 0.15 pu of capacitive reactance during the fault. Up to what fraction of the line does zone 1 now operate?

**Solution.** From EQ{zapp}, $Z_{app}=j(0.50m-0.15)$. Zone 1 operates while $0.50m-0.15\le0.40$, that is, for $m\le1.10$. Zone 1 now reaches 10 % into the adjacent line, so either the reach must be reduced while the converter is active or the converter must bypass before the zone-1 decision is made.

Solid-state interruption raises a related energy problem. When a semiconductor breaker turns off current $I_0$ in a loop of inductance $L$ against a driving voltage $V_s$, the current commutates into a surge arrester clamping at $V_c=kV_s$. The current then falls linearly, and

$$t_f=\frac{LI_0}{V_c-V_s},\qquad E_{MOV}=\frac12LI_0^{2}\,\frac{k}{k-1}$$ EQDEF{sscb}

so a low clamping ratio shortens neither the stress nor the energy: both the fall time and the absorbed energy grow without bound as $k\to1$ (FIG{sscb}). The same trade-off between clamping level and energy governs the TCVL (Section 8.6.2), and it is why hybrid breakers, which combine a mechanical path with a semiconductor commutation branch, are the preferred architecture for HVDC grids [29].

![FIGDEF{sscb} Normalized MOV energy and current fall time of a solid-state breaker versus clamping ratio.](fig/f_sscb.png){width=74%}

#### EXDEF{ex_sscb}. Solid-state breaker energy

A semiconductor breaker interrupts 5 kA in a 10 kV DC feeder with 1 mH of loop inductance. The arrester clamps at 15 kV. Find the current fall time and the energy the arrester absorbs.

**Solution.** $k=1.5$, so $t_f=10^{-3}\times5000/(15\,000-10\,000)=1.0$ ms and $E_{MOV}=0.5\times10^{-3}\times5000^2\times1.5/0.5=37.5$ kJ, three times the magnetic energy stored in the loop.

### 8.8.9 Data-driven methods and digital twins

Machine learning is most defensible here as a computational aid that accelerates a physics-constrained task: estimating uncertain parameters, screening many contingencies, constructing an OPF surrogate, detecting oscillatory modes or predicting converter thermal margin. The network equations and converter capability limits should remain explicit. A common way to keep a learned model physically consistent is to penalize violations of the governing equations during training:

$$\mathcal{L}=\mathcal{L}_{data}+\lambda_1\left\Vert g(x,u)\right\Vert ^{2}+\lambda_2\sum_{i}\max\left(0,h_i(x,u)\right)^{2}$$ EQDEF{pinn}

where $g$ and $h$ are the equality and inequality constraints of EQ{opf}. Even then, a learned controller that violates $V_{se,max}$, converter current, DC-link energy or arrester energy is not physically valid, however small its training error. A digital twin of a UPFC or IPFC corridor should state what it synchronizes (line parameters, transformer data, converter loss coefficients, capacitor condition, valve temperature, protection status), which decision improves because of that synchronization, and over what operating range the model has been validated against measurements. Its contribution should be judged by measurable improvement in prediction, control or maintenance, not by the label.

### 8.8.10 Validation hierarchy and publishable evidence

A research claim must be matched to a model that preserves the phenomenon being claimed (FIG{ladder}). Power-flow redistribution can be established with a validated steady-state model. Oscillation damping needs eigenvalue or time-domain evidence over several operating points. Harmonic, switching and impedance-interaction claims require EMT or switching models. Fault-current, bypass and relay claims require EMT with protection logic. Claims about implementation delay, sampling and gate logic are strongest when supported by controller or protection hardware-in-the-loop tests. A sound workflow is therefore to derive the reduced model, identify the expected mechanism, test sensitivity analytically, verify with EMT, and move to HIL only for claims that depend on real controller or relay timing. This avoids both extremes: a very detailed model used without understanding the mechanism, and implementation claims drawn from an oversimplified model.

![FIGDEF{ladder} Model hierarchy for research on combined and special-purpose FACTS controllers. Fidelity increases from steady-state dispatch to switching, protection and hardware validation.](fig/image25.png){width=96%}

### 8.8.11 Open problems and potential contributions

TAB{research} links each open problem to the equation it modifies, the reason current methods fall short, a contribution that would be publishable, and the evidence a reviewer will expect.

Table: TABDEF{research} Research map for combined and special-purpose FACTS controllers.

| Research problem | Governing relation | Limitation of current practice | Potential contribution | Minimum evidence |
|:--|:--|:--|:--|:--|
| Fault-tolerant modular series converters | EQ{nminus}, EQ{cellC}, EQ{avail} | Equal-sharing assumptions; ripple energy sizes the cells | Thermal-aware balancing, ripple cancellation, wide-bandgap cells | Switching model, loss and reliability analysis, prototype |
| Security-constrained dispatch of mixed fleets | EQ{opfbranch}, EQ{opf} | Converter limits checked only in the base case | Contingency-aware formulations with exactness guarantees | Benchmark networks, N-1 validation, solver statistics |
| Multi-port interaction of UPFC and IPFC | EQ{gnc} with DC-link coupling | Converters modelled separately with a stiff DC source | Three-port impedance models and design rules | Frequency scans validated against EMT |
| Delay-robust wide-area damping | EQ{delay} | Fixed-delay designs; no coordination among devices | Robust or adaptive coordinated damping | Eigenvalue studies, real-time HIL with delay |
| Grid-forming combined controllers | EQ{capab}, EQ{dcdyn} | Priority rules unstated; DC energy shared implicitly | Current-limited dual-port control with explicit priority | EMT fault studies, synchronization-stability analysis |
| Protection with series injection | EQ{zapp} | Instantaneous bypass assumed in relay studies | Adaptive relay settings, converter-aware protection logic | EMT plus protection HIL |
| Energy-aware solid-state limiters and breakers | EQ{sscb}, EQ{movE} | Current peak or clamp level optimized alone | Co-design of clamp level, MOV energy and recovery | EMT, thermal model, high-power test |
| Physics-constrained learning | EQ{pinn} | Black-box models extrapolate poorly | Hybrid models with certified constraint satisfaction | Out-of-distribution tests, constraint-violation statistics |

The industrial relevance is direct. Transmission owners need incremental, relocatable ways to release capacity faster than new lines can be built, and every item in TAB{research} either lowers the cost of such control, makes it safer to operate, or makes its benefit easier to prove to a regulator.

## Key Equations

Table: TABDEF{keyeq} Key equations of Chapter 8.

| Equation | Expression | Conditions |
|:--|:--|:--|
| EQ{upfcPQ} | $P_r=\frac{V_sV_r}{X}\sin\delta+\frac{V_rV_{pq}}{X}\sin(\delta+\rho)$ | UPFC at sending end, $\rho$ measured from $\mathbf{V}_s$ |
| EQ{upfcCircle} | $(P_r-P_0)^2+(Q_r-Q_0)^2=(VV_{pq}/X)^2$ | Control circle, $V_s=V_r=V$ |
| EQ{dcbal} | $P_{sh}+P_{se}=0$ | Lossless UPFC, steady state |
| EQ{dcdyn} | $\frac{d}{dt}\left(\frac12C_{dc}V_{dc}^2\right)=-(P_{sh}+P_{se}+P_{loss})$ | DC-link dynamics |
| EQ{ipfc2bal} | $P_{1pq}+P_{2pq}=0$ | Two-converter IPFC |
| EQ{ipfcmargin} | $\lvert V_{2q}\rvert\le\sqrt{V_{2,max}^2-V_{2p}^2}$ | Supporting-converter margin |
| EQ{ideal_ps} | $\lvert V_\sigma\rvert=2V_s\sin(\sigma/2)$ | Ideal phase shifter |
| EQ{par_power} | $P=\frac{V^2}{X}\sin(\delta\pm\sigma)$ | Phase shifter on a lossless line |
| EQ{ternary} | $N=3^L$, $\Delta V_{max}=\frac{3^L-1}{2}V_{step}$ | Ternary windings |
| EQ{ipc120} | $P=P_{max}\cos\left(\delta_{SR}-\frac{\psi_1+\psi_2}{2}\right)\sin\frac{\psi_2-\psi_1}{2}$ | IPC, $\lvert B_1\rvert=\lvert B_2\rvert$ |
| EQ{xlim} | $X_{lim}=V_{ph}/I_{f,lim}-X_s$ | Limiting reactance, inductive source |
| EQ{kappa} | $i_p=\kappa\sqrt2I_k''$, $\kappa\approx1.02+0.98e^{-3R/X}$ | First fault-current peak |
| EQ{mov} | $I=kV^\alpha$ | Metal-oxide varistor |
| EQ{tcvl} | $V_{lim}=(1-f_b)V_{clamp}$ | TCVL |
| EQ{inrush} | $f_0=1/(2\pi\sqrt{LC})$, $\hat I\approx\Delta V/Z_0$ | Capacitor energization |
| EQ{nminus} | $N\ge V_{se}/V_{cell,max}+n_b$ | Modular converter with bypassed cells |
| EQ{cellC} | $C_{cell}\ge S_{cell}/(\omega V_{dc}\Delta V_{pp})$ | Single-phase cell ripple |
| EQ{minorloop} | $L(s)=Z_g(s)/Z_c(s)$ | Impedance-based stability |
| EQ{capab} | $\lvert Q_{sh}\rvert\le\sqrt{(VI_{sh,max})^2-P_{sh}^2}$ | Current-limited shunt port |
| EQ{zapp} | $Z_{app}=mZ_L-\mathbf{V}_{inj}/\mathbf{I}$ | Relay with series injection |
| EQ{sscb} | $E_{MOV}=\frac12LI_0^2\,k/(k-1)$ | Solid-state interruption |

## Common Misconceptions

- *"The UPFC's DC link carries the reactive power of the series converter."* Only real power, plus losses, passes through the link. The reactive power of each converter is generated internally at its AC terminals.
- *"An IPFC can supply net real power to all its lines from the DC capacitor."* A capacitor is not a continuous energy source. Without storage or a shunt real-power port, the series-converter real powers must balance apart from losses.
- *"A phase shifter raises the maximum power of a line."* An ideal phase shifter shifts the power-angle curve sideways. It raises the power at a given network angle, but the peak $V^2/X$ is unchanged.
- *"A quadrature booster is an ideal phase shifter."* A quadrature injection changes both angle and magnitude. An ideal phase shifter preserves magnitude by a different phasor geometry and needs a slightly different injection.
- *"A capacitor in parallel with a PST carries power in the same direction as the PST."* A capacitive branch has negative reactance, so at a positive angle it carries power in the opposite direction. That is exactly what flattens the IPC characteristic.
- *"A current limiter replaces the breaker."* A limiter changes the current trajectory; the breaker (or an SSB) still establishes isolation. Hybrid devices may combine both functions, but their ratings and timing requirements remain distinct.
- *"Lowering the clamping level is free."* The energy the varistor absorbs rises steeply as the clamping level falls, which is why a TCVL bypasses part of the stack only for the duration of a disturbance.
- *"A controller that can set P and Q always improves damping."* The sign and phase of the supplementary path, measurement delay, current limiting and the operating point decide whether a mode is damped or excited.

## Chapter Summary

The UPFC injects a series voltage of any magnitude and phase, supplied with real power by a shunt converter through a common DC link, so it can move the operating point of a line anywhere inside a circle of radius $VV_{pq,max}/X$ around its uncompensated point. Its practical region is the part of that disk that satisfies converter current, voltage and DC-energy limits. The IPFC extends the idea to several lines, transferring real power between them under a single DC-balance constraint that also consumes part of each supporting converter's voltage margin; generalized and convertible arrangements extend it further. Thyristor-controlled voltage and phase-angle regulators provide fast magnitude or angle control with tap-changer windings, continuously with phase control or in ternary steps. The IPC flattens the power-angle characteristic of a tie and limits its fault contribution with passive components alone. Solid-state current limiters, breakers and transfer switches insert impedance or interrupt current within milliseconds, and the thyristor-controlled voltage limiter lowers the protective level of a varistor stack only when needed. Present research concentrates on modular and solid-state converters, coordinated dispatch, impedance-based stability, current-limited and grid-forming operation, and protection-aware design, each of which modifies a specific equation of the classical theory.

## Solved Numerical Practice Problems

Unless stated otherwise, per-unit quantities use a common three-phase base, line-to-line kilovolts and ohms give three-phase megawatts directly when both end voltages are balanced line-to-line RMS values, trigonometric angles are in degrees, and the UPFC injection angle $\rho$ is measured from the sending-end voltage. Lossless formulas are not applied to problems that include line resistance.

#### EXDEF{ex_upfc_basic}. UPFC uncompensated point and control circle

A UPFC is installed on a lossless line with $V_s=V_r=1$ pu, $X=0.5$ pu, $\delta=30^\circ$ and $V_{pq,max}=0.25$ pu. Find (a) $P_0$; (b) $Q_0$; (c) the total reactive power absorbed by the line; (d) the centre and radius of the control circle; (e) the range of $P_r$.

**Solution.** (a) $P_0=2\sin30^\circ=1.0$ pu. (b) $Q_0=-2(1-\cos30^\circ)=-0.268$ pu. (c) $|I|=2\sin15^\circ/0.5=1.035$ pu, so $I^2X=0.536$ pu, half supplied by each end. (d) Centre $(1.0,-0.268)$, radius $0.25/0.5=0.5$ pu. (e) 0.5 to 1.5 pu.

#### EXDEF{pr_maxmin}. Maximum and minimum power and converter duty

For Example EX{ex_upfc_basic} find (a) $\rho$ for maximum power; (b) $P_r$ and $Q_r$; (c) the line current; (d) the series-converter real and reactive power; (e) the same quantities at minimum power.

**Solution.** (a) $\sin(\delta+\rho)=1$, so $\rho=60^\circ$. (b) $P_r=1.5$ pu and $Q_r=-0.268$ pu (unchanged). (c) From EQ{upfcI}, $\mathbf{I}=1.524\angle10.13^\circ$ pu. (d) $S_{se}=\mathbf{V}_{pq}\mathbf{I}^{*}$: $P_{se}=0.067$ pu, $Q_{se}=0.375$ pu, $|S_{se}|=0.381$ pu. (e) $\rho=240^\circ$: $P_r=0.5$ pu, $Q_r=-0.268$ pu, $I=0.567$ pu, $P_{se}=-0.067$ pu, $Q_{se}=-0.125$ pu. The real power through the link is small in both cases; the series-converter rating is governed by $V_{pq}I$, which depends on the line current as well as on the injected voltage.

#### EXDEF{ex_two_angles}. Two injection angles for the same active power

On the line of Example EX{ex_upfc_basic}, $V_{pq}=0.45$ pu and the target is $P_r=1.4$ pu. Find (a) both values of $\rho$; (b) $Q_r$ for each; (c) the currents; (d) the series-converter apparent powers; (e) the better choice.

**Solution.** (a) $\sin(30^\circ+\rho)=0.4/0.9$, so $\rho=-3.61^\circ$ or $123.61^\circ$. (b) $Q_r=+0.538$ pu or $-1.074$ pu. (c) 1.500 pu or 1.765 pu. (d) 0.675 pu or 0.794 pu. (e) The first: it delivers reactive power to the receiving end with less current and less converter duty.

#### EXDEF{ex_lossy}. UPFC on a line with resistance

A 132 kV line has $X=175\ \Omega$ and $R=70\ \Omega$, with equal end voltages at $\delta=45^\circ$. The UPFC can inject up to 45 kV (line-to-line equivalent). Find (a) $P$, $Q_r$ and current without the UPFC; (b) the maximum receiving-end power and the injection angle; (c) the minimum injection that raises power by 50 % when placed at its best angle.

**Solution.** The exact complex calculation with $Z=70+j175\ \Omega$ gives: (a) $P_0=50.64$ MW, $Q_r=-49.42$ Mvar and $I_0=309.5$ A. (b) Optimizing $\rho$ gives $P_{max}=82.15$ MW at $\rho=23.2^\circ$, an increase of 62 %, with $I=419.3$ A. (c) $V_{pq}=36.15$ kV line-to-line. Approximate formulas that ignore $R$, or that force the injection into quadrature, overestimate the voltage needed.

#### EXDEF{ex_zero_angle}. Power transfer at zero angle

With $V_s=V_r=1$ pu, $X=0.5$ pu, $\delta=0$ and $V_{pq}=0.4$ pu, find (a) the uncompensated power; (b) $P_r$ and $Q_r$ at $\rho=90^\circ$; (c) the current; (d) the series-converter power.

**Solution.** (a) Zero. (b) $P_r=0.4\times1/0.5=0.8$ pu and $Q_r=0$. (c) 0.8 pu. (d) $P_{se}=0$ and $Q_{se}=0.32$ pu. Series injection alone establishes power transfer where an uncompensated line carries none.

#### EXDEF{ex_shunt_rating}. Shunt-converter rating

In Example EX{pr_maxmin}(a) the shunt converter must also supply 0.3 pu of reactive power to the bus. Find (a) its real power; (b) its apparent power.

**Solution.** (a) $P_{sh}=-P_{se}=-0.067$ pu, drawn from the bus. (b) $\sqrt{0.067^2+0.3^2}=0.307$ pu. Shunt converters are normally rated close to the series converter so that they can operate as a STATCOM.

#### EXDEF{ex_unequal}. UPFC with unequal end voltages

$V_s=1.0$ pu, $V_r=0.95$ pu, $X=0.5$ pu, $\delta=25^\circ$, $V_{pq}=0.2$ pu and $\rho=50^\circ$. Find (a) $P_0$ and $Q_r$ without injection; (b) $P_r$ and $Q_r$ with it; (c) the effective sending voltage; (d) the series-converter power.

**Solution.** (a) $P_0=0.803$ pu and $Q_{r0}=-0.083$ pu. (b) From EQ{upfcPQ}, $P_r=1.170$ pu and $Q_r=+0.015$ pu. (c) $|\mathbf{V}_s+\mathbf{V}_{pq}|=1.139\angle32.7^\circ$ pu. (d) $P_{se}=0.061$ pu and $Q_{se}=0.239$ pu.

#### EXDEF{ex_138}. A 138 kV UPFC

A 138 kV line has $X=80\ \Omega$ and operates at $35^\circ$; the UPFC can inject 28 kV. Find (a) $P_0$; (b) the UPFC power term; (c) the power range; (d) $\rho$ for 180 MW.

**Solution.** (a) $138^2\sin35^\circ/80=136.5$ MW. (b) $138\times28/80=48.3$ MW. (c) 88.2 to 184.8 MW. (d) $\sin(35^\circ+\rho)=(180-136.5)/48.3=0.900$, so $\rho=29.1^\circ$ (the other root, $80.9^\circ$, gives a more negative $Q_r$). A target of 260 MW is outside the range and is physically infeasible even though a controller would accept the reference.

#### EXDEF{ipfc_upf}. IPFC: unity power factor at the receiving end of line 1

Two identical lines have $V=1$ pu, $X=0.5$ pu and $\delta=30^\circ$; both IPFC converters can inject 0.25 pu. Converter 1 must hold $Q_{1r}=0$ while maximizing $P_{1r}$. Find (a) $\rho_1$; (b) $P_{1r}$; (c) $P_{1pq}$ and $Q_{1pq}$; (d) the injection angles of converter 2; (e) the resulting power in line 2.

**Solution.** (a) $\cos(\delta+\rho_1)=-Q_0X/(VV_{pq})=0.536$, so $\rho_1=27.60^\circ$. (b) 1.422 pu. (c) $P_{1pq}=0.191$ pu and $Q_{1pq}=0.300$ pu. (d) Converter 2 must absorb 0.191 pu: $\rho_2=-152.4^\circ$ or $122.4^\circ$. (e) $P_{2r}=0.578$ pu ($Q_{2r}=-0.536$ pu) or 1.232 pu ($Q_{2r}=-0.711$ pu). The second choice raises the flow in both lines; the first transfers power from line 2 to line 1.

#### EXDEF{ex_hdc}. IPFC DC-link dynamics

An IPFC DC capacitor has an energy-storage constant $H_{dc}=0.01$ s, defined as the stored DC energy at $V_{dc}=1$ pu divided by the three-phase power base. Converter 2 supplies 0.25 pu to the DC link while converter 1 absorbs 0.20 pu from it. Find (a) the net power into the link; (b) the exact DC voltage after 10 ms, neglecting losses; (c) the small-signal approximation; (d) the conclusion.

**Solution.** (a) $0.25-0.20=0.05$ pu. (b) Stored energy is proportional to $V_{dc}^2$, so the normalized energy rises from 1.0 to $1+0.05\times0.010/0.010=1.05$ and $V_{dc}=\sqrt{1.05}=1.0247$ pu. (c) Linearizing $W_{dc}=H_{dc}V_{dc}^2$ about 1 pu gives $d\Delta V_{dc}/dt=\Delta P/(2H_{dc})=2.5$ pu/s, so $\Delta V_{dc}\approx0.025$ pu after 10 ms, in close agreement. (d) A 0.05 pu imbalance moves the DC voltage by about 2.5 % in 10 ms, so the DC-voltage controller must act quickly. Using $\Delta V_{dc}=\Delta P\,\Delta t/H_{dc}$ would overestimate the excursion by a factor of two.

#### EXDEF{ex_parallel}. Balancing two parallel lines

Two parallel lines of 0.3 pu and 0.6 pu share 2.3 pu. Find (a) the natural sharing; (b) the series reactance that equalizes the flows; (c) the approximate series voltage needed in line 1.

**Solution.** (a) 1.533 pu and 0.767 pu. (b) Line 1 must look like 0.6 pu, so 0.3 pu is added. (c) $V_q\approx0.3\times1.15=0.345$ pu at the equalized current, a substantial injection at high current.

#### EXDEF{ex_gipfc}. Generalized IPFC power balance

Four converters share a DC link. Converters 1, 2 and 3 deliver $+0.15$, $-0.08$ and $-0.04$ pu to their lines. Converter 4 injects 0.1 pu into a line carrying 0.9 pu. Find (a) $P_{4pq}$; (b) the angle between $\mathbf{V}_{4pq}$ and $\mathbf{I}_4$.

**Solution.** (a) From EQ{ipfcbal}, $P_{4pq}=-(0.15-0.08-0.04)=-0.03$ pu (converter 4 absorbs). (b) $\cos\phi=-0.03/(0.1\times0.9)=-0.333$, so $\phi=109.5^\circ$.

#### EXDEF{ex_qb220}. Quadrature booster on a 220 kV line

A quadrature booster injects 20 kV (phase) into a 220 kV line ($V_{ph}=127.0$ kV) of $X=50\ \Omega$ at $\delta=25^\circ$. Find (a) the phase shift; (b) the effective voltage; (c) the power before and after.

**Solution.** (a) $\tan^{-1}(20/127)=8.95^\circ$. (b) $\sqrt{127^2+20^2}=128.6$ kV. (c) $P_0=3V_{ph}^2\sin25^\circ/X=409.1$ MW and $P=3\times128.6\times127.0\times\sin33.95^\circ/50=547.2$ MW. Part of the increase comes from the 1.2 % magnitude rise, which an ideal phase shifter would not produce.

#### EXDEF{ex_tcpar132}. TCPAR on a 132 kV line

A lossless 132 kV line has $X=40\ \Omega$ and operates at $30^\circ$. Find $P$ and the reactive power supplied at each end for $\sigma=0$, $+10^\circ$ and $-10^\circ$.

**Solution.** $P=V^2\sin(\delta+\sigma)/X$: 217.8, 280.0 and 149.0 MW. With equal end voltages each end supplies $V^2(1-\cos(\delta+\sigma))/X$: 58.4, 101.9 and 26.3 Mvar, so the line absorbs twice these values in total.

#### EXDEF{ex_ideal_ps}. Ideal phase shifter

An ideal phase shifter injects 0.4 pu. Find (a) $\sigma$; (b) the injection angle relative to $\mathbf{V}_s$; (c) the power at $\delta=30^\circ$ on a 0.3 pu line ($V=1$ pu) when the shift opposes the angle.

**Solution.** (a) From EQ{ideal_ps}, $\sigma=2\sin^{-1}(0.2)=23.07^\circ$. (b) $(180^\circ+23.07^\circ)/2=101.5^\circ$. (c) $P=\sin6.93^\circ/0.3=0.402$ pu.

#### EXDEF{ex_tcvr}. Ternary TCVR

A TCVR has three ternary windings with a smallest step of 5 kV. Find (a) the number of levels; (b) the maximum boost and buck; (c) the winding voltages; (d) the resolution.

**Solution.** (a) 27. (b) $\pm13\times5=\pm65$ kV. (c) 5, 15 and 45 kV. (d) 5 kV per step.

#### EXDEF{ex_tap_harm}. Thyristor tap-changer harmonics

Taps of 10 kV and 12 kV (peak) feed a resistive load; the upper switch fires at $\alpha=60^\circ$ in each half cycle. Find (a) the fundamental amplitude; (b) its phase shift; (c) the 3rd, 5th and 7th harmonics; (d) the THD of these three.

**Solution.** Fourier analysis of the switched waveform gives (a) 11.62 kV; (b) $-2.36^\circ$; (c) 0.477, 0.276 and 0.138 kV; (d) $\sqrt{0.477^2+0.276^2+0.138^2}/11.62=4.9$ %.

#### EXDEF{ex_loopflow}. Loop-flow control with a PAR

Two parallel paths of 0.3 pu and 0.6 pu carry 2.3 pu in total. Find the phase shift in the 0.6 pu path that equalizes the flows (a) if the total transfer of 2.3 pu is maintained; (b) if instead the angle across the corridor is held at its original value.

**Solution.** The original angle is $\theta=2.3/(1/0.3+1/0.6)=0.46$ rad. (a) For 1.15 pu in each path, line 1 needs $\theta=0.345$ rad, so the corridor angle falls to 0.345 rad, and line 2 needs $(0.345+\sigma)/0.6=1.15$, giving $\sigma=0.345$ rad ($19.8^\circ$). (b) With $\theta=0.46$ rad held, $\sigma=0.23$ rad ($13.2^\circ$) raises line 2 to 1.15 pu while line 1 stays at 1.533 pu, so the total rises to 2.68 pu. The network angle is generally part of the solution, not a fixed input.

#### EXDEF{ex_vsc_reg}. VSC-based regulator power exchange

A series VSC injects 5 kV in phase with the bus voltage into a line carrying 500 A at 0.866 power factor lagging. Find, per phase, (a) the real power; (b) the reactive power; (c) the converter rating.

**Solution.** (a) $5\times500\cos30^\circ=2.17$ MW. (b) $5\times500\sin30^\circ=1.25$ Mvar. (c) 2.5 MVA. The real power must be supplied by a shunt converter or a store.

#### EXDEF{ex_ipc120}. IPC120 powers

An IPC120 with $B_1=-1$ pu and $B_2=+1$ pu connects buses with $V_S=V_R=1$ pu at $\delta_{SR}=15^\circ$. Find (a) $\delta_{B1}$ and $\delta_{B2}$; (b) $P$; (c) $Q_S$ and $Q_R$.

**Solution.** (a) $75^\circ$ and $-45^\circ$. (b) From EQ{ipcP}, $P=0.966+0.707=1.673$ pu, which equals $2\times0.866\cos15^\circ$ from EQ{ipc120}. (c) From EQ{ipcQ}, $-Q_S=Q_R=-(1-\cos75^\circ)+(1-\cos45^\circ)=-0.448$ pu. Terminal powers alone do not reveal the internal branch currents.

## Unsolved Practice Problems

**Problem 8.1** A UPFC on a line with $V=1$ pu, $X=0.4$ pu, $\delta=45^\circ$ and $V_{pq,max}=0.2$ pu must deliver $P_r=1.8$ pu. Find $P_0$, $Q_0$, the circle radius, the maximum power, and the injection angle (with the corresponding $Q_r$) that gives 1.8 pu with the larger reactive delivery.

**Problem 8.2** For $V=1$ pu, $X=0.6$ pu and $\delta=60^\circ$, find the centre and radius of the UPFC control circle for $V_{pq,max}=0.3$ pu.

**Problem 8.3** A 400 kV line of $100\ \Omega$ operates at $40^\circ$ with a UPFC injecting up to 30 kV. Find the power range.

**Problem 8.4** Explain, with the DC-balance equation, why an IPFC cannot supply net real power to all its lines simultaneously without a shunt converter or storage.

**Problem 8.5** A ternary TCPAR has four windings with a 3 kV smallest step. Find the number of levels and the maximum injection.

**Problem 8.6** An injection IPC has $\psi_1=-20^\circ$, $\psi_2=+20^\circ$, $X=0.5$ pu and $V_S=V_R=1$ pu. Find $P$ at $\delta_{SR}=10^\circ$ and $25^\circ$.

**Problem 8.7** Find the phase shift produced by an ideal phase shifter injecting 0.25 pu.

**Problem 8.8** A quadrature booster injects 0.15 pu. Find the phase shift and the magnitude of the effective sending voltage.

**Problem 8.9** A 33 kV network has a symmetrical fault current of 12 kA; the breakers are rated 8 kA. Find the reactance a current limiter must add.

**Problem 8.10** A series-resonant SSFCL at 11 kV, 50 Hz uses $L_1=20$ mH with a source reactance of $0.5\ \Omega$. Find $C_1$ and the limited symmetrical fault current.

**Problem 8.11** A 400 kV arrester clamps at 1.7 pu of the peak phase voltage. Find the clamping voltage, and the TCVL level if 25 % of the stack is bypassed.

**Problem 8.12** A 66 kV capacitor bank of $60\ \mu$F per phase is energized through 1.5 mH. Find $f_0$, $Z_0$ and the inrush peak for a discharged bank closed at the voltage peak.

**Problem 8.13** By what factor does the current of a ZnO block rise when its voltage rises by 10 %, for $\alpha=25$ and $\alpha=40$?

**Problem 8.14** Compare a UPFC, an IPFC, a TCPAR and an APST for relieving a congested 400 kV corridor with a parallel underused path, a weak voltage at the receiving bus, and a tight budget.

**Problem 8.15** A modular series converter must inject 24 kV with cells rated 3.2 kV and must tolerate two bypassed cells. Find the minimum number of cells and the per-cell voltage in normal operation.

**Problem 8.16** A converter port with $Z_c=j\omega L_f+K_pe^{-j\omega T_d}$ has $T_d=100\ \mu$s. Above what frequency is its real part negative?

**Problem 8.17** A series converter emulates 0.10 pu of capacitive reactance on a line of $Z_L=j0.40$ pu protected by a zone 1 set at 85 %. Find the effective zone-1 reach while the converter is active.

## Answer Key (Unsolved Problems)

**8.1** 1.768 pu; $-0.732$ pu; 0.5 pu; 2.268 pu; $\rho=-41.3^\circ$ with $Q_r=-0.233$ pu (the other root, $131.3^\circ$, gives $Q_r=-1.231$ pu).

**8.2** $(1.443,\,-0.833)$ pu; 0.5 pu.

**8.3** $P_0=1028.5$ MW; range 908.5 to 1148.5 MW.

**8.4** $\sum P_{k,pq}=0$ without a shunt converter or store, so power delivered to some lines must be drawn from others.

**8.5** 81 levels; $\pm120$ kV.

**8.6** 1.347 pu; 1.240 pu.

**8.7** $14.36^\circ$.

**8.8** $8.53^\circ$; 1.011 pu.

**8.9** $0.794\ \Omega$.

**8.10** $506.6\ \mu$F; 936 A.

**8.11** 555.2 kV; 416.4 kV.

**8.12** 530.5 Hz; $5.0\ \Omega$; 10.8 kA.

**8.13** 10.8 and 45.3.

**8.14** Open-ended. A TCPAR or APST solves the flow sharing at low cost; the weak receiving voltage favours a UPFC (or a TCPAR plus a STATCOM); the APST is the cheapest if the required angle range is predictable.

**8.15** 10 cells; 2.4 kV per cell.

**8.16** 2.5 kHz.

**8.17** $m\le(0.34+0.10)/0.40=1.10$, that is, 110 % of the line.

## References

[1] L. Gyugyi, "Unified power-flow control concept for flexible AC transmission systems," *IEE Proceedings C*, vol. 139, no. 4, pp. 323-331, 1992.

[2] L. Gyugyi, C. D. Schauder, S. L. Williams, T. R. Rietman, D. R. Torgerson and A. Edris, "The unified power flow controller: a new approach to power transmission control," *IEEE Transactions on Power Delivery*, vol. 10, no. 2, pp. 1085-1097, 1995.

[3] C. Schauder et al., "Operation of the unified power flow controller (UPFC) under practical constraints," *IEEE Transactions on Power Delivery*, vol. 13, no. 2, pp. 630-639, 1998.

[4] L. Gyugyi, K. K. Sen and C. D. Schauder, "The interline power flow controller concept: a new approach to power flow management in transmission systems," *IEEE Transactions on Power Delivery*, vol. 14, no. 3, pp. 1115-1123, 1999.

[5] J. Brochu, *Interphase Power Controllers*. Montréal: Polytechnic International Press, 1999.

[6] N. G. Hingorani and L. Gyugyi, *Understanding FACTS: Concepts and Technology of Flexible AC Transmission Systems*. New York: IEEE Press, 2000.

[7] K. K. Sen and M. L. Sen, *Introduction to FACTS Controllers: Theory, Modeling, and Applications*. Hoboken, NJ: Wiley-IEEE Press, 2009.

[8] Y. H. Song and A. T. Johns (Eds.), *Flexible AC Transmission Systems (FACTS)*. London: IEE, 1999.

[9] K. R. Padiyar, *FACTS Controllers in Power Transmission and Distribution*. New Delhi: New Age International, 2007.

[10] X.-P. Zhang, C. Rehtanz and B. Pal, *Flexible AC Transmission Systems: Modelling and Control*. Berlin: Springer, 2006.

[11] B. Fardanesh, M. Henderson, B. Shperling, S. Zelingher, L. Gyugyi, B. Lam, R. Adapa, C. Schauder, J. Mountford and A. Edris, "Convertible static compensator: application to the New York transmission system," CIGRE Session, Paper 14-103, Paris, 1998.

[12] A. Ghosh and G. Ledwich, *Power Quality Enhancement Using Custom Power Devices*. Boston: Kluwer, 2002.

[13] A. Safaei, M. Zolfaghari, M. Gilvanejad and G. B. Gharehpetian, "A survey on fault current limiters: development and technical aspects," *International Journal of Electrical Power & Energy Systems*, vol. 118, Art. no. 105729, 2020, doi: 10.1016/j.ijepes.2019.105729.

[14] A. Mandal, K. M. Muttaqi, M. R. Islam and D. Sutanto, "A novel architecture of the solid-state unified power flow controller and its integration into the power grid," *Electric Power Systems Research*, vol. 241, Art. no. 111296, 2025, doi: 10.1016/j.epsr.2024.111296.

[15] B. H. Alajrash, M. Salem, M. Swadi, T. Senjyu, M. Kamarol and S. Motahhir, "A comprehensive review of FACTS devices in modern power systems: addressing power quality, optimal placement, and stability with renewable energy penetration," *Energy Reports*, vol. 11, pp. 5350-5371, 2024, doi: 10.1016/j.egyr.2024.05.011.

[16] B. A. Renz, A. Keri, A. S. Mehraban, C. Schauder, E. Stacey, L. Kovalsky, L. Gyugyi and A. Edris, "AEP unified power flow controller performance," *IEEE Transactions on Power Delivery*, vol. 14, no. 4, pp. 1374-1381, 1999.

[17] S. Yang, Y. Liu, X. Wang, D. Gunasekaran, U. Karki and F. Z. Peng, "Modulation and control of transformerless UPFC," *IEEE Transactions on Power Electronics*, vol. 31, no. 2, pp. 1050-1063, 2016.

[18] X. Wang, H. Wang, J. Yang, Z. Xu, W. Sun, C. Wu and C. Li, "Application of 500 kV UPFC in Suzhou southern power grid," *The Journal of Engineering*, vol. 2019, no. 16, pp. 2580-2584, 2019, doi: 10.1049/joe.2018.8556.

[19] D. Divan and H. Johal, "Distributed FACTS: a new concept for realizing grid power flow control," *IEEE Transactions on Power Electronics*, vol. 22, no. 6, pp. 2253-2260, 2007.

[20] J. Sun, "Impedance-based stability criterion for grid-connected inverters," *IEEE Transactions on Power Electronics*, vol. 26, no. 11, pp. 3075-3078, 2011.

[21] X. Wang and F. Blaabjerg, "Harmonic stability in power electronic-based power systems: concept, modeling, and analysis," *IEEE Transactions on Smart Grid*, vol. 10, no. 3, pp. 2858-2870, 2019.

[22] B. Fan, T. Liu, F. Zhao, H. Wu and X. Wang, "A review of current-limiting control of grid-forming inverters under symmetrical disturbances," *IEEE Open Journal of Power Electronics*, vol. 3, pp. 955-969, 2022.

[23] D. K. Molzahn and I. A. Hiskens, "A survey of relaxations and approximations of the power flow equations," *Foundations and Trends in Electric Energy Systems*, vol. 4, no. 1-2, pp. 1-221, 2019.

[24] K. K. Sen and M. L. Sen, "Introducing the family of 'Sen' transformers: a set of power flow controlling transformers," *IEEE Transactions on Power Delivery*, vol. 18, no. 1, pp. 149-157, 2003.

[25] D. Keshavarzi, A. Koehler, W. H. Wellssow and S. M. Goetz, "Entirely transformerless universal direct-injection power-flow controller," arXiv:2511.14209, 2025.

[26] IEC 60099-4:2014, *Surge arresters, Part 4: Metal-oxide surge arresters without gaps for a.c. systems*. Geneva: IEC, 2014.

[27] IEC 60909-0:2016, *Short-circuit currents in three-phase a.c. systems, Part 0: Calculation of currents*. Geneva: IEC, 2016.

[28] "Operational aspects and benefits of interphase power controllers with conventional or electronically switched phase-shifting devices: a robust FACTS application," CIGRE Session, Paper 38-101, Paris, 1998.

[29] J. Häfner and B. Jacobson, "Proactive hybrid HVDC breakers: a key innovation for reliable HVDC grids," in *Proc. CIGRE Symposium*, Bologna, 2011.

[30] F. Kreikebaum, D. Das, Y. Yang, F. Lambert and D. Divan, "Smart Wires: a distributed, low-cost solution for controlling power flows and monitoring transmission lines," in *Proc. IEEE PES Innovative Smart Grid Technologies Conference Europe*, Gothenburg, 2010.
