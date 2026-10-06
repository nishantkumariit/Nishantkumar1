@@P51

For transient stability, midpoint capacitive support raises the post-fault power-angle curve and enlarges the decelerating area of the equal-area construction; how much it gains depends on the clearing time, the device limits and the post-fault network. For small-signal oscillations, a supplementary controller modulates the reactive output through phase compensation chosen to produce damping torque. The required phase depends on the measured signal and the operating point, and an unshaped speed signal with the wrong phase can reduce damping instead of adding it. Chapter 11 develops these controls.

@@P258

The series branch is resonant at harmonic order $n$. At order $h$ its reactance is $X_{h} = hX_{L} - X_{C}/h = X_{L}(h - n^{2}/h)$, capacitive for $h < n$ and inductive for $h > n$. A branch detuned to $n = 4.5$ is therefore capacitive at the fundamental and inductive at the fifth harmonic. Tuning below the fifth, typically between 4.3 and 4.8, has to be coordinated with network resonances, background harmonics, component tolerances and switching duty. Increasing $L$ lowers $n$ and reduces the initial rate of rise for a given voltage mismatch, at the cost of a larger fundamental magnification.

@@P288

One practical rule uses voltage matching for $|V_{C0}| < V_{m}$ and the same-polarity crest for $|V_{C0}| \ge V_{m}$; in the lossless model these choices minimize the oscillatory amplitude over the feasible closing angles. Another arrangement keeps every disconnected capacitor charged near the supply crest and always fires at the crest. At $|V_{C0}| = V_{m}$ the transient is small but not zero, because the exact steady capacitor crest is $kV_{m}$. Which strategy suits a given installation depends on the charging method, leakage, valve polarity, harmonics and capacitor insulation.

@@P317

Three-phase TSC banks are connected in delta or in ungrounded star. Delta branches see line-to-line voltage and can be switched independently. In an ungrounded star the neutral shifts during switching and couples the phases, so the firing sequence has to be derived from the actual residual and line-to-line voltages rather than from a fixed quarter-cycle delay. Some low-voltage banks replace one thyristor of each valve by a diode, which keeps the capacitor charged to the crest and permits crest firing; the harmonic, polarity and insulation duties of that circuit then need separate checking.

@@P379

Figure 6.29 shows the operating area and the net susceptance versus firing angle. The fixed capacitance stays connected and the TCR varies its fundamental current continuously, so there are no capacitor-switching transients. The TCR still generates harmonics, which the filters reduce but do not eliminate. The weakness is loss: at zero net output the TCR must cancel the full capacitor current, as the simplified comparison of Figure 6.31 shows. Industrial users often accept this for the continuous response, whereas transmission SVCs usually prefer switched stages that avoid circulating current at idle.

@@P448

For this preliminary lag-and-droop model, choose $K_{C} = 1/[2(K_{SL} + K_{N,max})]$ using the largest expected voltage sensitivity; the crossover then lies near $1/(2T_{b})$ at that operating point. This is a starting value, and the final design must include the true firing delay, measurement lags, the current-to-susceptance conversion and the expected topology changes. Within the simplified model,

@@P533

Short-time capacitive and inductive overload limits depend on topology, switching pattern, transistor and diode duty, junction temperature, cooling and protection. Turn-off current capability made some earlier converters stronger in one direction than the other, but modern PWM and multilevel STATCOMs show no general asymmetry by the sign of $Q$, and the manufacturer's complete V-I envelope should be used. Under purely reactive operation, the ideal current-limited comparison is

@@P629

Equation (6.64) assumes small voltage ripple. The exact relation for sinusoidal energy exchange is $V_{dc,max}^{2} - V_{dc,min}^{2} = 2P_{2}/(\omega C)$, where $P_{2}$ is the peak twice-frequency power, and uncompensated DC ripple also produces AC sidebands. Sizing the capacitor from a supposed balanced three-phase reactive energy has no physical basis; for the numbers of Example 6.12 that rule gives 1.125 mF, 2.25 times the transient-deficit value.

@@P639

Balanced fundamental reactive power does not cycle energy through the DC link. If the hypothetical energy $\sqrt{2}Q/(2\omega) = 45.016$ kJ were nevertheless treated as a usable energy excursion, then $C = 2(45.016\ \mathrm{kJ})/[(21\ \mathrm{kV})^{2} - (19\ \mathrm{kV})^{2}] = 1.125$ mF, 2.25 times the 0.50 mF of part (a). The ratio is specific to these numbers; the rule itself is not a valid way to size a balanced common DC link.

@@P677

**Advanced reading path.** Sections 6.7.2 to 6.7.6 assume symmetrical components, capacitor energy balance, the swing equation and basic feedback control. A rating study follows the same order: AC current and modulation headroom first, then stored-energy limits, then synchronization and dynamic stability. Readers meeting the material for the first time can start from the worked examples; research students should follow the internal-state derivations and the validation steps.

@@P682

$S_{sc}$ is the three-phase short-circuit MVA of the network, $S_{rated}$ the compensator or plant rating, and $Q_{C}$ the fixed capacitive compensation subtracted in the conventional ESCR. A shunt capacitor changes voltage sensitivity and resonance but adds no short-circuit strength. SCR and ESCR are screening indices rather than stability criteria, and they are least reliable when several converters interact. A PLL-based grid-following STATCOM both supports and perturbs the voltage it synchronizes to, so at low system strength its PLL, outer loops, the network impedance and nearby converters have to be analysed together; no single SCR threshold settles the question.

@@P688

Here $S = 3VI$ is the balanced reactive rating on consistent cluster bases, and $\varepsilon = \Delta V_{cell,pp}/V_{cell,mean}$. Because capacitor energy varies with voltage squared, a fractional peak-to-peak swing $\varepsilon$ corresponds to an energy window of about $2\varepsilon E_{stored}$. Equating that window to the total cluster ripple gives Equation (6.68), whose ideal lower bound at 50 Hz and $\varepsilon = 10\%$ is 15.9 kJ/MVA. Installed energy must also cover overload, negative-sequence duty, bypassed cells, tolerances and control headroom.

@@P696

The envelope follows from the triangle inequality: the left-hand side has magnitude between $|V_{0}|\,\big||I^{+}| - |I^{-}|\big|$ and $|V_{0}|(|I^{+}| + |I^{-}|)$. The upper bound $r/(1-r)$ holds for $0 \le r < 1$, the range plotted in Figure 6.50a. At $r = 1$ the balance equation is singular: some phase relations have no solution and others have infinitely many, so the required voltage does not diverge for every phase as $r \to 1$. If $I^{+} = 0$ and $I^{-} \ne 0$, the equation gives $|V_{0}| = |V^{+}|$. Severe unbalance can exceed the available cell-voltage headroom, but whether it does has to be checked from the actual phasors, cluster voltages and semiconductor limits [42].

@@P726

The magnitude condition in Equation (6.75) sizes the virtual impedance for a bolted terminal fault with fixed $E_{0}$. It does not by itself limit the transient current, because sampling delay, the initial inductor current and modulation saturation are outside it. Figure 6.53 compares the ideal steady currents for aligned $E$ and $V_{g}$. Direct current saturation uses the full current capability but gives up voltage-source behaviour; a static virtual impedance keeps an impedance-shaped source but under-uses the current capability in a shallow sag; a threshold impedance lies between the two. The ratio $X_{vi}/R_{vi}$ affects both damping and transient stability, and neither improves monotonically with it in every grid, so variable-impedance schemes are tested against the actual network and limiter dynamics [24]-[26].

@@P735

Equation (6.76) uses an input-admittance convention, with positive current drawn into the converter. For stable scalar subsystems the Nyquist criterion is applied to $Z_{g}Y_{c}$ with its actual pole count; an intersection of the two magnitude curves alone does not indicate instability. Coupled dq or sequence models need the matrix return ratio with the generalized Nyquist criterion, or an equivalent state-space analysis. A strictly passive converter admittance connected to a passive grid is a sufficient condition for stability, but a scan showing $\mathrm{Re}\,Y_{c} \ge 0$ over a limited band does not prove it [29], [30].

@@P738

For the scalar model of Figure 6.54 ($T_{d} = 1.5T_{s}$, $f_{s} = 5$ kHz, 400 Hz current-loop bandwidth and a 100 Hz first-order voltage-feedforward filter), $\mathrm{Re}\,Y_{c}$ turns negative near 0.84 kHz, close to the familiar $f_{s}/6$ boundary of delay-dominated models; the exact crossing depends on the gains and the feedforward. Negative conductance marks a risk of adverse interaction rather than a proven instability: a grid resonance in this band, such as the 1.2 kHz example, has to be assessed with a return-ratio or coupled-model stability test.

@@P740

Figure 6.54. Scalar grid impedances and converter input conductance from Equation (6.77): $f_{s} = 5$ kHz, $T_{d} = 1.5T_{s}$, coupling $X = 0.15$ pu at 50 Hz, 400 Hz proportional current-loop bandwidth and 100 Hz first-order feedforward. The hatched band marks negative conductance.

@@P741

Figure 6.55 places typical phenomena on a frequency axis. Fundamental-frequency phasor models suit electromechanical and outer voltage-control studies but cannot resolve switching harmonics or fast current-loop interactions. Average-value EMT models can represent fast controls if their states, delays and bandwidth are included, and switching EMT models are needed for switching ripple and device stress. The frequency boundaries between these model classes are approximate.

@@P743

Figure 6.55. Indicative frequency ranges of shunt-compensator phenomena and the model classes suited to them; the boundaries are approximate.

@@P285

Figure 6.20. Oscillatory current amplitude for voltage-matching and positive-crest firing at three tuning ratios. The curves starting at 1.0 are voltage matching, which exists only for $|\rho| \le 1$; the V-shaped lines are crest firing, with zero transient at $\rho = k$.

@@P113

To evaluate it, expand $(\cos\alpha-\cos\theta)^{2} = \cos^{2}\alpha - 2\cos\alpha\cos\theta + (1+\cos 2\theta)/2$; half-wave symmetry makes the two pulses contribute equally, which gives the factor $1/\pi$ and the limits $\alpha$ to $2\pi-\alpha$.

@@P125

For odd $n \ge 3$ the cosine coefficient is obtained exactly as for the fundamental, now with $\cos n\theta$ inside the integral.

@@P126

Here $a_{n}$ is $2V_{m}/(\pi\omega L)$ times the integral of $(\cos\alpha-\cos\theta)\cos n\theta$ from $\alpha$ to $2\pi-\alpha$. With the product-to-sum identity $\cos\theta\cos n\theta = [\cos(n-1)\theta + \cos(n+1)\theta]/2$, each term integrates directly over these limits, giving

@@P128

where $a_{n}$ is the signed peak cosine coefficient of the $n$th harmonic; a harmonic rating uses its magnitude. Combining the terms over the common denominator $n(n^{2}-1)$ and taking the magnitude gives

@@P443

Here $K_{N}$ is the network gain and $ESCR$ the effective short-circuit ratio at the SVC bus, expressed on the SVC rating. The approximation comes from the lossless steady relation $V = E_{th}/(1 - X_{th}B)$, whose sensitivity at an operating point $B_{0}$ is $K_{N} = \partial V/\partial B = E_{th}X_{th}/(1 - X_{th}B_{0})^{2}$, evaluated at $B = B_{0}$; it reduces to $X_{th}$ for $V \approx E_{th} \approx 1$ pu and small $X_{th}B_{0}$. With consistent uncompensated short-circuit and MVA bases $X_{th} = 1/SCR$; using $1/ESCR$ instead is an effective-strength approximation, and the fixed capacitance must then not be counted a second time as an explicit controlled branch.

@@P444

The thyristor actuator is modelled as a transport delay of mean value $T_{b} \approx T/4$ (5 ms at 50 Hz), approximated by $1/(1+sT_{b})$. The slope feedback contributes a further gain $K_{SL}$ around the loop. With the regulator

@@P693

Under these assumptions the magnitude result is exact for every current ratio, and the worst-case cluster current over all negative-sequence angles is $|I^{+}| + 2|I^{-}|$. When negative-sequence voltage is also present, the complete cluster-power equations have to be solved and their solvability checked.

@@P705

Positive $P_{ES}$ withdraws energy from the store and negative $P_{ES}$ charges it, within $-P_{ch,max} \le P_{ES} \le P_{dis,max}$. The current limit is written with AC-terminal $P$ and $Q$ on common per-unit bases, whereas the energy equation uses the actual stored energy. If $P_{ES}$ is measured at the external storage port rather than at the stored-energy boundary, use $dE/dt = -P_{ES}/\eta_{dis}$ for discharge and $dE/dt = -\eta_{ch}P_{ES}$ for charge, with auxiliaries added separately. For a supercapacitor $E_{usable} = \tfrac{1}{2}C(V_{max}^{2} - V_{min}^{2})$, so a 2:1 voltage window uses 75% of the maximum stored energy. Power and energy ratings are separate design variables (Figure 6.51a).
