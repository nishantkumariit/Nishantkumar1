# Chapter 4 – Final review notes

**Chapter:** Mathematical Modeling for Digital Twins
**Revised file:** `Chapter-4_Mathematical-Modeling-for-Digital-Twins_revised.docx` (45 pages, validated)

## What was checked

Every worked example and table was recomputed independently in Python:

- **Examples 4.1 to 4.16:** all reproduce. This covers:
  - the RC, RL and RLC responses and the capacitor-ageing inversion;
  - the two-node thermal modal solution;
  - the DC-bus consistent initialization and Newton iterations;
  - the DC machine eigenvalues;
  - the Park transformation;
  - the induction-motor direct-on-line start (95.8 A peak, 222 N·m, 1440 r/min, 49.75 N·m) and its Thévenin check;
  - the PV model (MPP 306.6 W) and its temperature dependence;
  - the battery pulse and identification;
  - the PV linearization range;
  - Table 4.4 (all five methods at all five steps);
  - the stiffness, Tustin warping, Lyapunov and observability-Gramian results;
  - the balanced truncation and residualization (Table 4.5);
  - the Cramér-Rao bounds (Table 4.6).
- **Example 4.17 (adaptive fidelity switching):** reproduces exactly (158.3 °C, 10.9 K, 2.5 K, 55 %, cost 3.73), but only with the timing shown in Figure 4.24. The text was wrong about the profile; see correction 2.
- **Example 4.18 (co-simulation, Table 4.8):** reproduces exactly.
- **Example 4.19 (Monte Carlo):** reproduces with seed 1.
- **Example 4.20 (validation):** reproduces with Ĉ = 4467.6 J/K, the 157.1 °C twin peak against the 172.5 °C plant, and the forecast RMSE and bias. Two of the original's unstated settings were found and are now written into the text: the plant starts from its steady state without the loss feedback, and it is integrated with 1 s steps.
- **Answer key:** all 31 original answers were recomputed and are correct.

## Corrections

1. **Example 4.5:** the steady armature current is Bω/K_t = 2.60 A, not 2.62 A.
2. **Example 4.17:** the text said "a six-hour load profile in 30-minute blocks". The stated results and Figure 4.24 correspond to a four-hour profile in 20-minute blocks, starting from 100 °C (winding) and 76 °C (frame). Corrected, and the initial state is now stated.
3. **Table 4.11:** the BESS filter time constants were given as "0.2 ms / 0.2 ms". The filter decays with 1/(ζω_n) = 0.75 ms and rings with a 1.2 ms period; the 0.2 ms figure belongs to the DC bus (R₀C_bus).
4. **Example 4.20:** the initial state and the integration step of the synthetic plant are now stated, so the example can be reproduced.
5. **Figures:**
   - Figure 4.10 now draws ambient temperature as a temperature (voltage-type) source.
   - Figure 4.28 labels the two-node twin as "within 0.1 K of the plant", which is what the example reports.
   - Figure 4.27 now shows the actual calibration, validation and out-of-domain conditions of Example 4.20 and its stated envelope.

## Additions

- **Introduction** (about 960 words) replaces the numbered Learning outcomes list. It covers:
  - the role of the model in a twin;
  - the history from Kirchhoff and Park to state space, stiff solvers and balanced truncation;
  - what changes when a model runs continuously against a deadline;
  - the chapter plan.

  Its last paragraph states the learning outcomes in sentence form. The "How to read this chapter" box is kept.
- **New Advanced box (Section 4.11): the port-Hamiltonian form.**
  - It derives the passivity inequality.
  - It writes the RLC filter in that form, recovering (4.11).
  - It explains why assemblies of passive sub-models are stable by construction.
  - It shows that the implicit midpoint (trapezoidal) rule preserves the discrete energy balance, which gives a stronger verification test.
  - Reference: van der Schaft and Jeltsema, 2014.
- **Section 4.17, new verified literature:**
  - PINNs for power systems (Misyris et al., IEEE PES GM 2020);
  - PINNSim (Stiasny, Zhang and Chatzivasileiadis, Electr. Power Syst. Res., vol. 235, 2024);
  - HELICS co-simulation (Palmintier et al., MSCPES 2017);
  - SSP 2.0 (Modelica Association, December 2024).
- **Exercises:** 31 exercises and 10 review questions were merged into 15 exercises with linked conceptual, derivation and numerical parts. Complete solutions to all 15 are in the Answer key. New parts include:
  - capacitor and resistance recovery from a measured ringing;
  - the Newton wrong-root demonstration;
  - observability Gramian eigenvalues;
  - a Fisher-information singularity;
  - post-pulse relaxation.
- **Figures:** all 28 redrawn at 600 dpi, generated from the same computations that verify the examples.
- **References:** renumbered in order of first citation (26 in total); a DOI was added for Manimaran et al. (2026).

## Items for the author to confirm

1. Section 4.17 status labels ("research", "emerging", "testing use") reflect 2026 practice as I understand it. Adjust them if your own field experience differs.
2. The illustrative M-07 motor, PV module and LFP cell parameters are labelled as illustrative. Keep that label unless you substitute measured data.
3. eFMI (FMI for embedded systems) is not mentioned. As of this review it has beta releases but no final 1.0, so it was deliberately left out.
4. As in the earlier chapters, the Review questions section was folded into the 15 exercises.
5. Equations do not render in LibreOffice (the same is true of the original file). They were verified by converting the document back to LaTeX; please glance at them once in Word.
