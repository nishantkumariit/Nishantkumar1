# Chapters 11 to 14: final review notes

All four revised files pass the Word-format validator.

| Chapter | Revised file | Pages |
|---|---|---|
| 11 | `Chapter-11_Digital-Twins-for-Microgrids-Smart-Grids-and-Power-Systems_revised.docx` | 88 |
| 12 | `Chapter-12_Condition-Monitoring-Fault-Diagnosis-and-Prognostics_revised.docx` | 69 |
| 13 | `Chapter-13_Digital-Twin-based-Control-Optimization-and-Energy-Management_revised.docx` | 63 |
| 14 | `Chapter-14_Cybersecurity-Privacy-Trust-and-Resilient-Digital-Twins_revised.docx` | 75 |

## What was done in all four chapters

- **Introductions.** The numbered learning-outcome list is replaced by an Introduction of about 1130 to 1230 words. It covers context and history, a map of the chapter, the general lessons of the running example and the scope of standards, and ends with the learning outcomes written as sentences.
- **Exercises.** About 40 to 51 exercises per chapter, plus the design project, are merged into 15 themed exercises with complete solutions to all fifteen. The old answer key in Chapter 11 was out of order and is now in sequence. The conceptual and review questions are kept.
- **Checking.** Every worked example, every numerical claim, every answer-key entry and every figure was recomputed or inspected independently in Python.
- **Packaging defect fixed.** The original files did not declare PNG as a content type, which can make Word report "unreadable content". They also carried 21 to 29 unused image files each. Both are fixed.

## Chapter 11: corrections

1. **Example 11.2.** The intermediate step for V2 is (−0.1a)/3, not (1 − 0.1a)/3. The final value 0.0333∠−60° was already right.
2. **Example 11.3.** Unit A's overload relative to its share is 3.6 %. The 7 % figure was unit B's shortfall; both are now stated.
3. **Example 11.12.** With refrigeration doubled, the motor-start step reaches 0.81 MVA, which is 112 % of the limit, not 99 %.
4. **Section 11.10.4.** An unfinished sentence is completed with a reference to (11.53).
5. **Section 11.12.7.** The stale-PMU effect now uses the values of Table 11.9: about 6 mpu for WLS, LNR and Huber, 2.7 mpu for the learned estimator, and coverage of at most 11 %.
6. **Example 11.20.** THD_V numerator corrected to 18.2 V. The result, 0.29 %, is unchanged.
7. **Figure 11.29 caption.** The voltage harmonics do not rise with order. The caption now says V_h = h X_s I_h.
8. **Example 11.22.** The 124 and 240 kW figures are reserves, not standard deviations, and are now labelled as reserves.
9. **Application D.** The reductions are now stated per formulation, from Table 11.11.
10. **Example 11.23.** DER-only reactive absorption is 4.3 Mvar, not 4.1, so the over-promise is about 60 %, not 50 %.
11. **Example 11.26.** The 2.20 h SAIDI of Example 11.24 assumes no tie, so the text no longer says the tie is its source.
12. **Figures 11.15 and 11.25.**
    - Figure 11.15: the QSTS step is "1 s to 1 h", as in the text and Table 11.7, and the coverage arrow now points down.
    - Figure 11.25: the band is relabelled "±0.15 Hz acceptance band"; it is not a 95 % band.

## Chapter 12: corrections

1. **PSD paragraph.** The ENBW correction applies when an amplitude spectrum is converted to a PSD, not when a PSD is converted to band power.
2. **Example 12.13.** In the periodic steady state the junction swings between 51 and 118 °C, with a largest swing of 67 K. The 44 °C and 74 K values came from the cold start. The damage and the 8.9-year life were already correct. The Figure 12.30 caption now notes the start-up transient.
3. **Figure 12.11 text.** The frozen twin's residual is about 0.20, not 0.15.
4. **Wrong figure reference.** The method ladder is Table 12.4, not Figure 12.1.
5. **Answers.**
   - Ramp-fault derivation: the residual is now defined consistently, so the fixed point ρτ_a follows.
   - Cell-capacity exercise: the weakest cell falls short of the others by 2 to 4 Ah, not 3 to 4 Ah.
   - 118 Hz envelope line: the answer now notes that it is 3.5 % below BPFI, more than the usual 1 to 2 % slip, so the speed must be checked first.
6. **Captions.**
   - Figure 12.12 draws only one mode-conditioned limit, and the caption now says so.
   - Figure 12.13 marks no alarm times, so the caption no longer promises them.
7. **Figure 12.5 redrawn.** The 4.4 kHz alias curve was phase-inverted and did not pass through the samples.

## Chapter 13: corrections

1. **Warm-start formula (Section 13.20.1).** The last element is −K x_{N|k−1}, with the minus sign restored.
2. **Equation (13.38).** u_k = v_k − K e_k. The sign is now consistent with A − BK.
3. **Equation (13.37).** The left side is |x_j|, not |x_k|.
4. **Example 13.1.**
   - The 10.8 % overshoot is the peak before the reference steps down at 3 s; the saturated actuator allows at most 11.1 %.
   - The Figure 13.6 caption now mentions the reference step.
5. **Example 13.8.** The night tariff runs to 08:00. The stated results reproduce only with this tariff.
6. **Example 13.13.** The cascaded-PI overshoot is 3.0 %, and the start-up current peak is 16.9 A; the 20.3 A peak occurs after the load step.
7. **Example 13.12.** One seed lost the optimum at 750 episodes and then regained it.
8. **Design project.** Duplicated item letters are removed in the merged exercise 13.15.
9. **Figures redrawn.**
   - Figure 13.8: the buck circuit had no input source and the diode had no cathode bar.
   - Figure 13.13: the tube plot was inconsistent with its own limits and with the stated 0.256 tube. It is now computed from the chapter's scalar plant.
   - Figure 13.31: the explicit-MPC curve is now computed from (13.25) and coincides with saturated LQR, as it should.
   - Figure 13.18: the caption now says PV and wind are drawn as a small step.

## Chapter 14: corrections

Every calculation in Chapter 14 was correct. Only small inconsistencies were found:

1. **Example 14.7.** A nadir cannot sit above the value frequency then falls to. The text now says frequency falls below 49 Hz to 48.75 Hz.
2. **Example 14.5.** The difference is 0.31, not 0.30, computed from unrounded values.
3. **Section 14.18.3.** The contributions now match Figure 14.29: 17.4 and 10.1.
4. **Answer key.** The justification for the seven-sensor cosine array now says that every pair of rows has rank 2. The original said three rows, which does not support the answer of 2.
5. **Captions.**
   - Figure 14.27: channels 1 and 3 share a vendor, and the caption now says so.
   - Figure 14.32: the caption now includes the degraded → safe-stop transition.
6. **Figure 14.45.** The evidence box said "HIL caps test", but the chapter's evidence is simulation. It now reads "simulated cap test".

## Items for the art editor (not changed; source scripts are not available)

- **Chapter 11**
  - Figure 11.18: the current-limiter arrow should point to the current loop, not to PWM.
  - Figures 11.4 and 11.9: small label clipping.
  - Figures 11.33 and 11.34: the last hour of the step plots is not drawn.
  - Figure 11.43: a label runs past the frame.
  - Figure 11.44: the Volt/VAR bar should span about 60 to 300 s.
  - Figure 11.27: the loop arrow targets step 3, while Algorithm 11.1 says step 4.
- **Chapter 12**
  - Figures 12.2 and 12.16: overlapping labels.
  - Figure 12.28: the legend shows "$" as math.
  - Figure 12.38: plotting floor not stated, and the legend hides a marker.
  - Figure order: 12.8 is cited before 12.7, and 12.27 before 12.26.
- **Chapter 13**
  - Figure 13.4: the legend hides the pole marker.
  - Figures 13.1, 13.2, 13.28, 13.32 and 13.35: label overlaps.
- **Chapter 14**
  - Literal underscores (for example "P_k", "d_max") in Figures 14.13, 14.22, 14.24, 14.28, 14.32, 14.33, 14.34 and 14.43.
  - Figure 14.5: conduits missing for vendor access and the EV backend.
  - Figure 14.14: the rollback arrow points to the wrong stage.
  - Figure 14.44: the legend says 3.6 % where the text says 3.7 % (a rerun gives 3.68 %), and tick labels overlap.
  - Figure 14.18: the legend hides a marker.

## Points for the author to decide

- **Example 11.21 and Application C.** The 94 A island fault current uses 1.5 MVA of inverter capacity, while Table 11.14 lists 1.8 MVA installed. The text now states 1.5 MVA as an assumption about the capacity in service. If all 1.8 MVA is meant, the current becomes 113 A, and Figure 11.30 and Tables 11.10, 11.17 and 11.18 would need updating.
- **Example 12.8.** The fused classification accuracy (79.8 %) is about 2.7 standard errors above the analytic expectation (79.0 %). This is plausible for one seed, but worth re-running.
