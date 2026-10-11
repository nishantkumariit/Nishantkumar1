# Chapter 7 – Final review notes

**Chapter:** Digital Twins of Power Electronic Converters and Electrical Machines
**Revised file:** `Chapter-7_Digital-Twins-of-Power-Electronic-Converters-and-Electrical-Machines_revised.docx` (60 pages, validated)

## What was checked

Every worked example and every answer was recomputed independently. Results:

**Converters**
- **Examples 7.1 to 7.6:** buck and boost ripples, the DCM ratio 0.438, the 1.714 mH boundary inductance, flyback, dual active bridge and LLC.
  - DAB phase shifts are 18.86° and 21.98°.
  - DAB RMS currents (13.5 A and 15.4 A) were confirmed by simulation.
  - The 5.47 kW soft-switching boundary was confirmed.
  - LLC gains were confirmed for all nine operating points.
- **Cascaded H-bridge THD:** 31.1 / 10.1 / 6.9 / 3.8 %.
- **Kolar DC-link ripple formula (7.15):** confirmed against a switching simulation (17.44 A both ways).
- **Example 7.10:** the buck switching simulation reproduces 11.950 V, 4.09 A and 51 mV.
- **Converter twin:** Examples 7.11 and 7.13 and Table 7.6 (all loss terms, 16.3 / 18.1 W) are correct.

**Devices, losses and lifetime**
- **Table 7.8 and Example 7.14:** R_on,sp, BFOM, drift thickness, doping and die areas are correct.
- **Example 7.15:** electrothermal fixed point 51.1 °C, 8.92 W, 25 °C error 7.8 %, loop gain 0.033.
- **Table 7.10:** a Foster-network simulation gives 1.81 / 3.57 / 5.33 / 6.45 / 7.78 K.
- **Example 7.16:** lifetime damage shares 76.4 / 22.5 / 1.1 %, 0.015 %/year, ×2.1 for a hotter heatsink.
- **Example 7.17:** capacitor ageing is correct.

**Machines**
- **Examples 7.18 to 7.20:** frames, PMSM torque and the three other machine families are correct.
- **Examples 7.25 to 7.27:** field weakening, MTPA and the sensorless limit are correct.
- **Example 7.29:** reflected wave and bearing voltage are correct.
- **Example 7.30:** HIL sizing is correct.
- **Example 7.24:** the SRM fit reproduces exactly with seed 4: 8.015 ± 0.051 mH, 80.3 ± 0.7 mH, 0.547 ± 0.003 Wb.

**Case study (Section 7.18)**
- The plant model reproduces exactly: 102.7 °C before the fault and 137.6 °C after it. Two details not stated in Table 7.15 are needed for this:
  - iron loss is injected at the housing node;
  - each speed step is drawn before its duration.
- The estimator chain agrees within noise realization:
  - winding error 2.7 K RMS;
  - magnet bias −1.08 K against the stated −1.03 K;
  - alarm 61 to 66 s after onset against the stated 59 s;
  - R_ha 0.0719 K/W;
  - torque scale 0.961 against the stated 0.959;
  - lead time 40 min.
- The original values are kept.

**Answer key:** all 38 answers recomputed and correct.

## Corrections

1. **Example 7.23 (SRM):** the power figures did not follow from the example's own torque and currents. 29.7 N·m at 1500 r/min is 4.67 kW, not 4.51 kW, and copper loss at 13.8 A RMS is 380 W, not 365 W. A re-simulation of the stated model reproduces the torque, ripple and currents exactly. Corrected values:
   - (i) 1.29 kW, 287 W, 1.58 kW (81 %);
   - (ii) 4.67 kW, 380 W, 5.06 kW (92 %).

   A consistency check is added: the loop of Figure 7.28 encloses 7.78 J per stroke, and 7.78 × 24 / 2π = 29.7 N·m.
2. **Example 7.22:** the bracket is 4.42 A (printed as 4.12 in the torque product).
3. **Section 7.4.3 and Figure 7.9 (dead time):** for negative current, the pole voltage stays high t_d longer than commanded. The original figure had both pole-voltage traces wrong; it is redrawn.
4. **Figure 7.35:** the motor-terminal voltage settled at about 740 V instead of 650 V. It is redrawn with a reflection model that settles at the DC-link voltage.
5. **Figure 7.23:** the dq values did not match Example 7.18. They now show 17.3 A and 10.0 A.
6. **Figure 7.4:** quadrant I was labelled "buck-boost"; it now reads discharge (I) and charge (II).
7. **Figure 7.32:** the efficiency map has been redrawn with a stated loss model. Contours now run from 80 to 94 %, and the caption is updated to match.
8. **Chapter summary:** a garbled sentence with a doubled comma is rewritten.

## Additions

- **Introduction** (about 970 words) replaces the numbered Learning outcomes list. It covers:
  - the history of devices and of field-oriented control;
  - the multi-time-scale problem;
  - the chapter's arc;
  - drive D-3.

  Its last paragraph states the learning outcomes in sentence form.
- **New Advanced box (Section 7.3.2): deriving the DAB power, soft-switching boundary and RMS current.**
  - It derives the corner currents, (7.7) and the ZVS condition.
  - It gives an exact RMS formula that reproduces Example 7.5's 13.5 A and 15.4 A.
- **Verified literature added:**
  - Peng, Zhao and Wang, DC-DC digital twin health indicators (IEEE TPEL 2021);
  - A. Kumar and N. Kumar, real-time digital twin of a two-stage converter (IEEE TIM 2025);
  - Bayerer et al., power-cycling lifetime model (CIPS 2008);
  - JEDEC JEP184 for SiC bias-temperature instability and JEP173 for GaN dynamic R_ds,on;
  - Kirchgässner et al., thermal neural networks (Eng. Appl. AI 2023).
- **Exercises:** 38 exercises and 10 review questions were merged into 15 linked exercises with complete solutions. New numerical parts include:
  - DAB corner and RMS currents at 7.5 kW;
  - field weakening at 4000 r/min;
  - LC filter damping;
  - edge-timestamp error;
  - a reflected-wave and bearing-voltage problem.
- **Figures:** 30 of 38 were redrawn at 600 dpi, regenerated from the chapter's own models: the buck simulation, loss curves, Foster swing, SRM simulation, field-weakening curves and MTPA.
- **Figures kept as in the original:** 7.14, 7.16, 7.17, 7.18, 7.22, 7.26, 7.37 and 7.38. Six of these plot results of the original identification and simulation runs, which depend on unstated random-number details, and 7.14 and 7.16 needed no change.
- **References:** 27, renumbered in order of first citation.

## Items for the author to confirm

1. References [4] to [7] (Dutt and Kumar; Pandey and Kumar) could not be checked against an accessible index. Please confirm the volumes, pages and DOIs, especially the December 2026 TPEL entry.
2. Table 7.15 should state that iron loss enters the housing node and that the speed level is drawn before the duration in each step; the case study reproduces only with these choices.
3. Figure 7.17 (right) is captioned "absolute correlations" but shows signed values. Consider changing the caption to "correlations".
4. As in the earlier chapters, the Review questions section was folded into the 15 exercises.
5. Equations do not render in LibreOffice (the same is true of the original file). They were verified by converting the document back to LaTeX; please glance at them once in Word.
