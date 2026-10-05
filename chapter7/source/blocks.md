@@T71INTRO

Table 7.1 summarizes the four controllers treated in this chapter, together with the fixed series capacitor from which they all derive.

@@P109

where $V_{C,rms}$ is the total RMS capacitor voltage and $V_{Cn}$ the peak $n$th harmonic voltage (its magnitude is used). The third harmonic reaches its largest value of 13.8% of $IX_{C}$ at $\gamma = 30^{\circ}$, mirroring the TCR at $\alpha = 120^{\circ}$. The RMS expression contains $\sin^{2}\gamma$, not $\sin^{2}2\gamma$. The two forms agree only at $\gamma = 60^{\circ}$, where $\sin 2\gamma = \sin\gamma$. Elsewhere the second form is wrong: it gives more than twice the true RMS voltage at $\gamma = 30^{\circ}$, and its radicand becomes negative beyond about $60^{\circ}$ (Example 7.9).

@@P129

The GCSC control variable is not a conventional thyristor firing delay. The bidirectional turn-off valve conducts while the capacitor is bypassed and is commanded off after the selected current crest. From that instant until the valve turns on again at zero capacitor voltage, the line current charges the capacitor. A practical controller therefore begins with current synchronization, calculates the requested fundamental reactance, converts it into a turn-off delay through the inverse of Equation (7.8), and issues turn-off commands under protection supervision. The current reference must be filtered enough to reject harmonics without introducing a phase error large enough to shift the intended insertion interval.

@@P168

Equal TSSC stages are easy to manufacture and share voltage uniformly, but $n$ equal stages provide only $n+1$ distinct reactance levels. Binary-weighted reactances $X$, $2X$, $4X$ and so on provide $2^{n}$ levels with the same number of valves. Because capacitor reactance is inversely proportional to capacitance, the capacitances are weighted in the opposite order, $C$, $C/2$, $C/4$ and so on. This is the reverse of a binary shunt capacitor bank, in which the capacitance (susceptance) itself is weighted.

@@P171

Each inserted capacitor carries full line current and must be rated for steady-state voltage, insertion offset and temporary overload. Each bypass valve carries full line current while its stage is out of service and must withstand the capacitor voltage while the stage is inserted. A small reactor in the valve branch limits the discharge current and $di/dt$ when a charged stage is bypassed (Equation (7.12)). MOV protection and a mechanical bypass path are coordinated with the series-capacitor protection described in Section 7.1.6.

@@P209

For $1 < \varpi < 3$ ($1/9 < X_{L}/X_{C} < 1$) exactly one resonance lies between blocking and full conduction, so the characteristic has one capacitive and one inductive branch. Practical modules use $\varpi$ between about 2 and 3 ($0.11 \le X_{L}/X_{C} \le 0.25$). For $\varpi > 3$ a second resonance, at $\beta = 3\pi/(2\varpi)$, falls inside the control range close to full conduction (Example 7.21). We verified Equation (7.16) against a direct time-domain solution of Equation (7.15) over the full range of $\beta$; the two agree to better than 0.01%. Figure 7.16 compares the exact and simplified characteristics for $X_{L}/X_{C} = 0.133$.

@@P224

The ratio $X_{L}/X_{C}$ is a central design decision. A small reactor gives a fast, well-defined charge reversal and an effective protective bypass, because the valve then forms a low-impedance path around the capacitor. A larger reactor reduces the peak and RMS thyristor current and the harmonics injected into the line, and widens the usable angle range, but it slows the reversal. Prototype installations used $X_{L}/X_{C} \approx 0.13$, and practical values lie between about 0.11 and 0.25 ($\varpi$ between 2 and 3); below $X_{L}/X_{C} = 1/9$ a second resonance appears near full conduction. The resonance angle $\beta_{r}$ of Equation (7.18) must sit well inside the control range, with an exclusion band around it.

@@P345

In both schemes the power-system controller should be kept separate from the fast converter controller. The former requests a series voltage, a power flow or an equivalent reactance; the latter produces a feasible voltage vector within modulation, current, DC-voltage and semiconductor limits. With indirect control, the switching pattern and the DC-link voltage set the synthesized AC voltage, and a small phase displacement from exact quadrature supplies the converter losses and regulates the DC-link energy. With direct control, PWM or multilevel modulation sets the output-voltage vector explicitly.

@@P351

For balanced operation the converter rating is $S_{SSSC} = \sqrt{3}\,V_{q,LL}\,I$, where $V_{q,LL}$ is the injected line-to-line RMS voltage and $I$ the line RMS current. This is a converter MVA rating, not a capacitor kvar rating. In constant-voltage mode the MVA demand grows in proportion to the line current. In constant-reactance mode $V_{q} = X_{q}I$, so the demand grows with $I^{2}$ until the voltage ceiling is reached; beyond that point the controller leaves the ideal constant-reactance characteristic and operates on its voltage limit. The same converter therefore follows different V-I trajectories under the two commands, a distinction that matters in both rating and power-flow studies.

@@P352

The converter cannot carry the prospective line fault current, so the fast thyristor bypass and the mechanical bypass breaker are an essential part of its protection, and the series transformer must survive the fault current until they operate. Transformerless modular designs remove the series transformer but not the need for fault bypass, insulation coordination and protection-interaction studies (Section 7.7.2).

@@P322

The absence of classical series resonance must not be read as immunity from every subsynchronous phenomenon. The converter, its synchronization loop, DC-link dynamics, modulation and limiters, together with the surrounding network, form a controlled dynamic system. That system can take part in subsynchronous or supersynchronous control interactions even though no physical capacitor reactance crosses the line inductive reactance. Section 7.7.3 develops the impedance-based analysis used to screen such interactions.

@@P356

Selection should be based on the required service rather than on a simple ranking, and Table 7.4 reorganizes the comparison in that way. The decisive questions are whether compensation must be continuous or stepped, whether the controller must both increase and decrease corridor flow, whether a classical series capacitor is acceptable from the SSR perspective, how much fault-current duty the series equipment must survive, and whether converter losses and protection complexity are justified by the additional controllability.

@@P468

*“The SSSC power term needs a unit conversion factor.”* With line-to-line kilovolts and ohms, both $V^{2}/X$ and $VV_{q}/X$ come out directly in megawatts for the three-phase system. An extra factor, as in some worked solutions, overstates the SSSC contribution tenfold (1108.7 MW instead of 110.9 MW in Example 7.28).

@@P569

A numerical RMS of the waveform of Equation (7.6) gives the same values to five figures. With $\sin^{2}2\gamma$ in place of $\sin^{2}\gamma$ the formula would give 41.2 V instead of 22.45 V at $25^{\circ}$, and its radicand turns negative beyond about $60^{\circ}$; the two forms coincide only at $60^{\circ}$, which is why a check at that single angle cannot expose the error.

@@P597

32 kV, reached at full insertion ($IX_{C}$).

@@P608

Single: 90.0 V RMS. Sequential: 18.1 V RMS, a five-fold reduction. It exceeds the nominal factor $m = 4$ because the controlled module sits near full insertion, where its harmonics are small.

@@P611

**Note.** The fundamental reactance is the same in both realizations; only the harmonic content and the voltage that each valve must block change.

@@P679A

With $X_{L}/X_{C} = 0.1$ ($\varpi = 3.16 > 3$) a second resonance also lies at $\beta = 85.4^{\circ}$, close to full conduction, so the transition to bypass must cross it quickly.

@@P763

**Numerical consistency note.** All SSSC examples use three-phase quantities. With line-to-line RMS voltage and line current the converter rating is $S = \sqrt{3}\,V_{LL}I$; with per-phase voltage it is $S = 3V_{ph}I$. Per-unit calculations use one declared three-phase base and need no additional $\sqrt{3}$.
