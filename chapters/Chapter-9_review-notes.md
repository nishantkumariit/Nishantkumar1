# Chapter 9 – Final review notes

**Chapter:** Digital Twins for Battery Energy Storage Systems
**Revised file:** `Chapter-9_Digital-Twins-for-Battery-Energy-Storage-Systems_revised.docx` (41 pages, validated)

## What was checked

Every worked example, table entry and answer that can be recomputed was recomputed independently.

**Correct as written**
- **System and precharge:** rack 240 cells and 768 V (600 to 876 V); 1.075 MWh; τ 0.5 s; 99.3 % at 2.5 s; 16 A; 3.2 kJ.
- **Models (Examples 9.1 to 9.4):**
  - residuals of the one- and two-branch models;
  - Arrhenius factors ×2.06 (5 °C) and ×3.08 (−5 °C);
  - hysteresis rate (γh = 36);
  - SPM surface gap;
  - coulomb-counting errors (1.7, 0.009 and 3.6 points);
  - the EKF update.
- **Health and power (Examples 9.6 and 9.7):**
  - capacity and its uncertainty;
  - R_eq 0.326, 0.673 and 1.006 mΩ, with voltage-limited currents 1470, 713 and 477 A;
  - 1.73 kW per cell, about 2 MW for the system.
- **Ageing (Example 9.9):** calendar and cycle losses after 1, 5 and 10 years; end of life 12.0 years (25 °C), 4.9 years (35 °C), 30 years (15 °C).
- **Thermal (Examples 9.10 to 9.12):**
  - heat 6.1 W; time constant 1.7 h;
  - module temperatures 29.8 to 37.4 °C; half flow 45 °C; 0.136 kg/s;
  - Semenov 13.3 K.
- **Pack and faults (Examples 9.13 and 9.16):** 43.1 %, 7.56, 27.5 and 21.6 %; internal-short current, lag and detection times.
- **Fast charge (Example 9.18):** re-simulated.
  - 25 °C: 49.6 min, with the taper reaching 156 A.
  - 5 °C: 199.6 min, tapering from 89 to 37 A.
  - Anode potentials 27, −36, −178 and −446 mV; 21 K rise.
- **Dispatch (Example 9.19):**
  - 15.4 USD per cycle at 25 °C;
  - profits 49.3 and −0.7 USD;
  - marginal losses 0.0019 and 0.0028 % per EFC confirmed from (9.17).
- **Embedded arithmetic (Section 9.12):** a float32 accumulator over one hour counts 1.20 times the true charge.
- **Figures:** all 26 were checked against the text; data figures 9.6, 9.10 to 9.17, 9.22, 9.24 and 9.25 match the stated parameters.

## Errors corrected

1. **Equation (9.23), balancing charge.** The original subtracted the minimum headroom, which gives the wrong cells and amounts. The correct form bleeds every cell down to the largest headroom: ΔQ_i = max_j[(1−z_j)Q_j] − (1−z_i)Q_i. This form reproduces the book's own Example 9.15 numbers (3.8, 0.2, 7.3, 0 A·h).
2. **Example 9.9:** equivalent full cycles at end of life corrected to 6020 (25 °C) and 2460 (35 °C).
3. **Example 9.19:** degradation cost at 35 °C corrected to 22.6 USD (161 250 × 0.0028/20).
4. **Example 9.10:** at 10 % SOC the reversible heat (3.0 W) is half the irreversible heat, not "half as much again".
5. **Example 9.5 and the Figure 9.13 caption:** the filter with an unknown hysteresis branch converges about an hour into the charge. By then the current has reset the hysteresis state and the SOC has crossed the OCV step near 60 %. It does not wait for "the steep upper end" as the text said; the figure shows this.
6. **Answer-key fixes** (old numbering):
   - 9.3: the ambiguity is ±22 points, a 45-point band.
   - 9.8: two years is 730 days, not 720.
   - 9.17: the arithmetic average SOC is 58.4 %; 58.6 % is the capacity-weighted value. Both are now given.

## Figures redrawn (600 dpi)

- **9.1, cell schematic:** labels overlapped the electron arrow and the separator hatching.
- **9.4, precharge circuit:** the PCS hung from the middle of the capacitor. It is now connected across the DC rails, with contactor symbols.
- **9.7, resistances:** the log axis had a single tick label. Readable ticks were added; the data are unchanged.
- **9.19, thermal network:** the heat input was drawn as a voltage source and Tₐ was left floating. Redrawn with a heat-flow source and an ambient source; the simulation panel is kept.
- **9.20, coolant loop:** only 8 modules were drawn. Redrawn with all 15; the temperature panel is recomputed exactly from Example 9.12 and shows the 5 K limit.
- **9.21, thermal runaway:**
  - Left panel: the old trace jumped from 60 °C straight to 650 °C. It is replaced by an adiabatic two-reaction Arrhenius model that passes through the stated stages.
  - Right panel: in the old Semenov diagram both loss lines still crossed the heating curve. It now shows stable, critical (tangent, 14.3 K exact against 13.3 K from (9.21)) and runaway cases. The caption is updated.

## Added

- **Introduction:** about 1230 words, with history (Goodenough 1980, Sony 1991, LFP 1997, Nobel 2019), the twin's questions, a chapter map, recurring lessons and the learning outcomes in sentence form. Section 9.1 is renamed "Battery storage inside the plant-wide twin".
- **[Advanced] box: Bernardi's heat equation from the first law and Gibbs–Helmholtz.** It introduces the enthalpy potential, states the assumptions, and checks the result numerically against Example 9.10.
- **Research paragraph (Section 9.14)** with verified results.
- **Exercises:** 15 merged exercises, replacing 31 plus the mini-project, with complete solutions. New material includes:
  - a scalar Kalman update showing why hysteresis hides SOC on the plateau;
  - a closed-form plating-limited charge time, which reproduces Example 9.18 exactly;
  - the exact Semenov root;
  - float32 underflow at 0.02 A, where the counter stops counting.

## References added (all verified)

- Plett 2004, EKF Part 3 (J. Power Sources 134)
- Birkl et al. 2017 (J. Power Sources 341)
- Dubarry et al. 2012 (J. Power Sources 219)
- Naumann et al. 2018, LFP calendar ageing (J. Energy Storage 17)
- Waldmann et al. 2014 (J. Power Sources 262)
- Severson et al. 2019 (Nature Energy 4)
- Attia et al. 2020 (Nature 578)
- Sulzer et al. 2021, PyBaMM (JORS 9)
- Li et al. 2020, cloud BMS twin (J. Energy Storage 30)
- UL 9540A, 5th ed. 2025

The DOI for Manimaran et al. 2026 was also added. References are renumbered by first citation.

## Note for the editor

- **Li et al. 2020:** the volume and article number (vol. 30, 101557) are from my own knowledge and are consistent with the 2020 dataset record. Please confirm them on the publisher's page at copy-editing.
- **Rendering:** equations render in Word. The LibreOffice preview used for checking leaves them blank in both the original and the revised file.
