@@P15

**Conventions.** Network phasors are RMS fundamental quantities. $X_{C} > 0$ denotes a capacitor-reactance magnitude, whereas a signed device reactance is negative in capacitive operation. Waveform equations state explicitly where a current is a peak value. A per-phase power becomes a balanced three-phase power on multiplication by 3, and per-unit formulas use one common three-phase base. Angles inside derivatives and integrals are in radians even when results are quoted in degrees. Sections 7.1 to 7.3 and 7.5 form the core of the chapter; the exact TCSC waveform, the impedance-based stability tests and the delayed-damping models are intended for advanced and research study.

@@P43

Series and shunt ratings must be compared for the same transfer objective, angle, voltage and device limits. A series capacitor changes the transfer reactance and supplies $I^{2}X_{C}$ per phase, whereas a shunt device changes the voltage profile by supplying bus current. In the ideal equal-end-voltage model, series compensation achieves a given transfer increase at a moderate angle with less installed var duty than an equally constrained midpoint shunt scheme (Example 7.19). Voltage support, losses, congestion, protection and contingencies can still favour a different solution in a particular network.

@@P47

For a radial lossless line feeding a constant-power load, reducing the series reactance moves the nose of the static P-V curve outward (Figure 7.4). With sending voltage $E$, receiving voltage $V_{r}$ and load $Q = P\tan\varphi$, the power-flow equation is $E^{2}V_{r}^{2} = (V_{r}^{2} + X_{eff}Q)^{2} + (X_{eff}P)^{2}$, and the two voltage branches merge where its discriminant vanishes. The capacitor output rises as $I^{2}X_{C}$, which helps exactly when it is needed, but only within the capacitor, MOV, line-current and protection limits. Load recovery and motor stalling are dynamic phenomena, so a larger static nose has to be confirmed by a dynamic voltage-stability study.

@@P69

Fixed compensation near turbine-generators is chosen from frequency scans, coupled torsional studies and contingency cases rather than from a fixed percentage. A TCSC can reshape its subsynchronous impedance through suitable firing control, and an SSSC produces its fundamental injection without a physical series capacitor, but both still require SSR, SSCI and control-interaction studies. Examples 7.17 and 7.30 show the frequency screening that starts such a study.

@@P76

Higher compensation reduces the net reactance and can raise the current, the local capacitor-terminal voltage and the sensitivity to outages. It also affects distance protection and subsynchronous interactions. Installations at 70% to 75% are demanding designs rather than general limits; the permissible range follows from the complete network, equipment and protection study.

@@P184

Table 7.2 gives selected historical installations, each with its own source. Dates are reported commissioning or test-commissioning dates, and ratings are omitted where the cited record does not state them. The table illustrates applications; it is not an equipment specification or a claim of precedence.

@@P216

As a numerical check, the waveform integrals were evaluated separately on each switching interval, with tolerances of $10^{-10}$, at 180 values of $\beta$ for $X_{L}/X_{C}$ = 0.133, 0.15 and 0.20, excluding the immediate neighbourhood of the poles. Equation (7.16) agreed with the integrated waveforms to within $10^{-10}$. This confirms the analytical result for the ideal periodic waveform; it is not a substitute for EMT or hardware validation.

@@P232

The imposed-current model predicts capacitor-voltage harmonics and internal circulating-current pulses. In a real network these voltage harmonics drive line-current harmonics through the frequency-dependent network impedance, so the line current is not perfectly sinusoidal. Figure 7.19 plots peak harmonic voltage on the fixed base $I_{m}X_{C}$, with the region around the first pole excluded. At $\beta = 25^{\circ}$ and $X_{L}/X_{C} = 0.133$ the third harmonic is 17.3% of that base, or 10.8% of the actual fundamental. Harmonic duty grows rapidly towards resonance, so the capacitive vernier cannot be assumed to produce only a few percent of harmonic voltage.

@@P245

The internal controller estimates the fundamental current and capacitor voltage, forms a signed reactance estimate and maps a limited order to synchronized valve pulses. Current synchronization needs filtering that preserves the intended firing phase, and capacitor-voltage prediction uses both measured voltage and current. Suitable firing can improve subsynchronous behaviour, although equally spaced reversals do not by themselves ensure positive damping. The reactance estimator must use phase as well as magnitude, for example $\mathrm{Im}(\bar{V}_{C1}/\bar{I}_{1})$ with consistent terminal polarity, and must be disabled or conditioned near zero current.

@@P250

Figure 7.22 compares two ideal SMIB simulations that the reader can reproduce. The model is $\dot{\delta} = \omega_{b}\Delta\omega$, $2H\Delta\dot{\omega} = P_{m} - P_{e} - D\Delta\omega$, with $H = 4$ s, $f_{0} = 50$ Hz, $P_{m} = 0.6$ pu, $D = 0$, $V = 1$ pu and total uncompensated $X = 1$ pu. Initially $x_{C} = 0.25$ pu and $\delta_{0} = \sin^{-1}[P_{m}(1 - x_{C})]$. During an 80 ms fault $P_{e} = 0$ and the device is bypassed; afterwards $P_{e} = \sin\delta/(1 - x_{C})$. The damping case uses $x_{C}^{*} = 0.25 + 8\Delta\omega$, limited to 0.10 to 0.40 pu, through a 20 ms lag. The damping shown follows from these assumptions and is not a prediction of field performance.

@@P293

**Symmetric voltage range.** The ideal converter can command either voltage polarity within its voltage, current and MVA envelope, so it can increase or decrease corridor flow. The resulting flow-control range depends on the transfer sensitivity, angle, current and limits; it is not simply twice the converter rating.

@@P298

In constant-voltage mode the SSSC commands a quadrature voltage up to its voltage ceiling; in reactance mode its magnitude is $|V_{q}| = |X_{q}|\,|I|$ until that ceiling is reached. Unlike a capacitor of finite reactance, it can hold a finite voltage at light load, provided the current stays above the synchronization threshold. At zero current the current angle is undefined, and charging, losses and auxiliary supply then need a defined operating strategy. Converter and transformer losses depend on topology, switching and loading, so their light-load behaviour has to be taken from the actual design.

@@P300

Figure 7.25. SSSC constant-voltage and constant-reactance envelopes. Capacitive and inductive labels refer to forward current; the minimum-current threshold shown is an example value.

@@P362

Sections 7.1 to 7.5 establish the circuit physics. Recent work extends them to modular power-flow routing, converter-related subsynchronous interactions, communication delay and protection-aware validation, issues that matter most where inverter-based generation and conventional machines share series-compensated networks. The models below are entry points for quantitative research, and their limitations matter as much as their numerical results. Table 7.5 summarizes the main gaps before they are examined in turn.

@@P396

The screening model treats the machine as a simple induction equivalent with a nearly synchronous rotor, neglecting the magnetizing branch and frequency-dependent parameters. At stator frequency $f_{e}$ the slip is $s = (f_{e} - f_{0})/f_{e}$, so the rotor contributes $R_{r}'/s = R_{r}'f_{e}/(f_{e} - f_{0})$, which is negative for $0 < f_{e} < f_{0}$. The converter term is an illustrative scalar resistance rather than a property of any particular controller. A positive $R_{net}$ at one resonance is a screening result only; torsional modes, frequency coupling and contingencies require coupled models. Figure 7.31 uses $R_{c}(f) = -0.004(f/50)^{4}$ pu so that the example can be reproduced, and Example 7.11 gives the boundary without the converter term.

@@P418

Model fidelity follows from the phenomenon being claimed (Figure 7.33 and Table 7.6). IEC 60143-4:2023 replaces the earlier network-simulator test of TCSC control and protection with a hardware-in-the-loop test [13]. Published M-SSSC EMT models support offline and real-time studies [14], although a published model is not automatically a validated replica of a given commercial unit. Controller HIL and protection HIL answer different questions and are complementary rather than ranked.

@@P447

**Note.** Converter control can move this boundary; with the illustrative contribution of Figure 7.31 it falls to about 62%.

@@P513

At 70% compensation of the line alone the current rises by 140% and the line-side capacitor terminal reaches 1.307 pu. These figures flag the insulation and current duty; the permissible compensation still has to come from a full study. Relative to the entire 1.2 pu path, the compensation is only 58.3%.

@@P549

**Note.** The comparison holds the end voltages, the angle and the shunt-voltage target fixed. It explains the series advantage for this transfer objective, not a general economic preference.

@@P647

**Note.** Frequency separation is a screening requirement. Before the switching protocol is chosen, the unsuitable steady settings are excluded and the transition duration, control, torsional damping and contingencies are assessed.

@@P755

**Solution.** (a) $P_{0} = 213.9$ MW. (b) $k = 1/3$, $X_{C} = 13.33\ \Omega$. (c) The compensated current is 1822.8 A and the capacitor duty 132.9 Mvar. (d) The required SSSC voltage is 42.10 kV line-to-line. (e) Its fundamental rating is $\sqrt{3}(42.10)(1.8228) = 132.9$ MVA, equal at this operating point because both devices produce the same fundamental voltage and current. (f) At smaller angles a constant-voltage SSSC contributes relatively more, and it can also command the opposite polarity. Which solution is more economical depends on installed equipment, losses, protection and service value. A hybrid has to be sized separately.

@@P80A

Table 7.Z collects the angle reference used for each device in the rest of the chapter.
