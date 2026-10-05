# Chapter 9: Technical Review and Correction Log

This log covers the review of *Chapter_9_Custom_Power_Devices_Final_Publication_Copy.docx*. I read the chapter line by line, recomputed every worked example and answer with independent scripts, and checked the facts, standards data and references against the literature.

## 1. Numerical verification

All 35 original worked examples and all 25 answer-key items were recomputed. These include the complex-phasor cases: the four-wire unbalanced load (Ex. 9.3), the ZVR quadratic (Ex. 9.4), the pq instantaneous calculation (Ex. 9.10), both zero-power DVR roots, UPQC-Q/P/S (Ex. 9.20 to 9.25), the left-shunt swell case and the source-impedance DVR case. Every final number in the original matched to the stated precision, except the items below.

## 2. Errors corrected

| Location (original) | Problem | Correction |
|---|---|---|
| Example 9.1(f) | The problem specified the overload factor *a* = 1.2, but the solution used *a* = 1 ("as in the original problem statement") and gave 4.98 mF | The solution now applies the stated *a* = 1.2 and gives **5.98 mF**. The *a* = 1 value is kept as a comparison |
| Eq. (9.23), split-capacitor ripple | C = I₀/(2ω·v_pp) is not dimensionally derived for a midpoint current that divides between two capacitors | Re-derived: with two capacitors C in series and neutral-current amplitude Î_n, the ripple on each is Î_n/(ωC), so **C ≥ Î_n/(ω·Δv_pp)**. Also noted that a four-leg converter does not pass neutral current through its capacitor |
| Example 9.32 (UPQC design) | Used the split-capacitor formula for a **four-leg** shunt converter, which is inconsistent with the Eq. (9.23) definition and with the stated topology | The DC-link capacitor is now sized from the energy equation (9.22): **25.1 mF** for 5 % droop over 10 ms |
| Example 9.4, wording | Said the source "delivers 588.4 var of capacitive reactive power that lifts the bus". With a leading source current, the reactive power flows from the load bus toward the source | Reworded to describe the correct direction of reactive flow |
| Example 9.26 | Converter-side current 95.3 A came from rounding n = 0.292 | 95.1 A (= 27.82 × 171/50); kVA 14.27 |
| Example 9.27 | Line voltage 293.7 V | 293.8 V |
| Fig. 9.7 (DSTATCOM vs SVC V-I) | The regulation slope was drawn **falling** from capacitive to inductive current, which reverses the droop | Regenerated: bus voltage now rises as current moves from capacitive to inductive, and the SVC limits are labelled correctly |
| Fig. 9.40 (J versus δ) | Annotation text overlapped the curve | Regenerated |
| Section 9.4 intro | "Since the first utility installation in the mid-1990s…" was vague | Specific and verified: 1996, Duke Power, Anderson SC, 12.47 kV |
| Table 9.7 (IEEE 519) | Even-harmonic note was incomplete | Added the 2022 rule: even harmonics h ≤ 6 are limited to 50 % of the odd limits, and higher even harmonics share the odd limits (this changed from the 2014 rule of 25 %) |

## 3. Structural and editorial problems fixed

- **Meta text removed:** "The lecture material classifies…" and "Control algorithms listed in the lecture material…".
- **Duplicates merged:**
  - 9.3.2.1 to 9.3.2.3 against 9.3.1 and 9.3.2;
  - 9.3.3.1 to 9.3.3.3;
  - 9.4.2.1 and 9.4.2.2;
  - 9.4.3.1 to 9.4.3.3;
  - 9.4.5.1 and 9.4.5.2;
  - 9.5.2.1 and 9.5.2.2, and 9.5.3.1 to 9.5.3.3;
  - two pairs of algorithm tables;
  - the UPQC strategy tables;
  - two "first-screen" passages;
  - the repeated wide-bandgap paragraph in 9.9.
- **Formatting fixed:**
  - The UPQC section's opening paragraphs sat *before* "9.5.1" without styles, and figures 9.34 to 9.36 were unnumbered relative to their neighbours. Both are corrected.
  - Five untitled tables now have numbered captions.
  - Plain-text equations are now numbered Word equations: the DSTATCOM current decomposition, E_DVR, the UPQC DC-link equations, and TDD/THD_V in 9.7.
- **Numbering rebuilt automatically:** figures, tables, equations (72), examples (43) and citations, which are now renumbered by first appearance.

## 4. Sections 9.6, 9.7 and 9.8: rewritten and expanded

### 9.6 Series and hybrid active power filters

- Peng's harmonic-source models (current-source and voltage-source type), with a new figure.
- Source-current equations for:
  - a passive filter;
  - a shunt APF;
  - a series APF with a passive filter (Peng, Akagi and Nabae 1990), which shows why that combination removes the dependence on source impedance and damps resonance.
- A computed frequency-response figure.
- Capacitor-bank resonance h_r ≈ √(S_sc/Q_c) and detuning.
- Ratings of the Fujita–Akagi hybrid.
- Two new worked examples and a comparison table.

### 9.7 IEEE Std 519-2022

- The relation between TDD and THD, with a figure.
- A derivation of why the current limits scale with I_sc/I_L (V_h/V₁ = h·I_h/I_sc).
- Statistical assessment using IEC 61000-4-30 aggregation, with a percentile figure.
- The IEC 61000-3-6 summation law for several harmonic sources.
- An APF sizing rule for compliance, with a spectrum-versus-limits figure.
- A workflow diagram.
- Four new worked examples.

### 9.8 Comparing and selecting devices

- Interruption ride-through treated as an energy problem.
- Closed-form normalized converter ratings for DSTATCOM, DVR and UPQC, with a comparison figure.
- A storage map in the sag depth-duration plane.
- Life-cycle cost formulas (expected trip cost, capital recovery factor, losses), with a break-even figure.
- Weighted multi-criteria scoring.
- A corrected selection map.
- Three new worked examples.

### Other additions

- Section 9.9 now has the equations for the minor-loop impedance criterion and the MPC cost function.
- Three new unsolved problems (9.26 to 9.28), with answers.
- Thirteen new or regenerated figures in total.

## 5. References

- **Added:**
  - Peng, Akagi and Nabae (1990);
  - Peng (2001);
  - Fujita and Akagi (1991);
  - Akagi (2005);
  - IEC TR 61000-3-6;
  - IEC 61000-4-30;
  - IEEE 1346.
- **Confirmed online:**
  - the 2026 references [24] to [26] (titles, venues and authors);
  - the Fujita and Akagi (1991) paper;
  - Peng (2001);
  - the 1996 Duke Power DVR;
  - the IEEE 519-2022 even-harmonic change.
- **Still to check:** please verify the page ranges of Peng, Akagi and Nabae (1990) and Akagi (2005) in IEEE Xplore. I could not open the publisher pages from here.

## 6. Build

`source/` contains the Markdown source, the figure script and the numbering and post-processing scripts. The output .docx keeps the original header and footer, passes OOXML schema validation, and the 71-page PDF rendering was inspected page by page.
