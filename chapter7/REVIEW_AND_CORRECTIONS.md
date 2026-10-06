# Chapter 7: Technical Review and Correction Log

This log covers the review of *Chapter_7_Series_FACTS_Controllers_Final.docx* (GCSC, TSSC, TCSC and SSSC). I read the chapter sentence by sentence and recomputed every worked example, practice problem and answer-key item with independent scripts (`source/chk7.py`, `source/chk7b.py`, `source/tcsc.py`). I also checked the installation data and the references against published sources. All edits were made inside the original Word file (`source/edit7.py`), so its styles, equations, header and footer are preserved.

## 1. Numerical verification

- **TCSC reactance law (7.16):** compared with an analytic periodic steady-state solution of the line-current-driven LC circuit (conduction centred on the capacitor-voltage zero). They agree to numerical precision for XL/XC from 0.1 to 0.25 over the whole range of β. The same solution was used to recompute the thyristor and capacitor currents of the worked examples.
- **GCSC fundamental, RMS and harmonic formulas (7.7) to (7.10):** compared with Fourier analysis of the waveform of (7.6) at 0° to 80°; they agree. The third harmonic peaks at 13.78% of IXC at γ = 30°, as stated.
- **Wide-area damping model (7.31):** delay roots solved numerically. The 0.7 Hz mode gives 12.7% at 150 ms and 9.8% at 200 ms, as stated.
- **All 43 worked examples and all 16 answer-key items:** every final number reproduces to the precision given. This includes the critical clearing angles, the SSR screening, the GCSC delays, the TCSC conduction angles and thyristor currents (1707 A RMS, 4.24 kA peak), the admittance-matrix example, the SSSC power ranges and the resistance-compensating SSSC.

## 2. Errors corrected

| Location (new numbering) | Problem | Correction |
|---|---|---|
| Section 7.2.3 and Example 7.21(f) | Said the sin²2γ form of the RMS formula gives a value below the fundamental at 60°. At 60° both forms are identical (sin 120° = sin 60°). | Correct statement: the wrong form gives 0.648 instead of 0.294 IXC at 30° (41.2 V instead of 22.45 V at 25°), and its radicand turns negative beyond about 60.2°. |
| Section 7.4.4 | "For 2 < ϖ < 3.3 there is exactly one resonance." For ϖ > 3 a second resonance appears at β = 3π/(2ϖ) < 90°. | Now reads 1 < ϖ < 3 (1/9 < XL/XC < 1), with practical ϖ of 2 to 3. The second resonance is explained. |
| Section 7.4.6 | Practical XL/XC "between 0.1 and 0.3". | About 0.11 to 0.25, with the second-resonance caveat below 1/9. |
| Example 7.33(e) | Uses XL/XC = 0.1 (ϖ = 3.16) without noting the second resonance at β = 85.4°. | Note added. |
| Section 7.4.5 | "Reactor current pulse reaches more than twice the peak line current". The exact waveform gives 1.71 times; it is the capacitor current that reaches 2.71 times. | Corrected. |
| Section 7.7.4 | 1.0 Hz mode falls below 5% damping "at about 180 ms". | The computed crossing is 188 ms, so the text now says "about 190 ms". |
| Example 7.30 | Rotor frequency 14.65 Hz. | 14.64 Hz. |
| Common Misconceptions | "Multiplying by 1000 ... overstates tenfold" is internally inconsistent. | Reworded: an extra factor overstates the term tenfold (1108.7 MW instead of 110.9 MW, Example 7.40). |
| Answer P7.16 | Said a TCSC "only raises flow". Its inductive vernier can reduce flow, as Table 7.3 states. | Corrected. |
| Example 7.25(d) | The sentence on the "upper bound m = 4" was confused. | Rewritten: the five-fold reduction exceeds m = 4 because the controlled module sits near full insertion. The duplicate note was replaced with a useful one. |
| Section 7.1.7 | Dated the TCSC proposal to 1986 but cited a 1988 paper. | Now reads: conceived in the mid-1980s (the rapid adjustment of network impedance scheme), with case studies at CIGRE in 1988 [1]. The SSSC sentence now separates Gyugyi's 1989 proposal from the 1997 analysis [4]. |
| Table 7.2 | Kanpur-Ballabhgarh was implied to be the first Indian TCSC. | Rourkela-Raipur (2004) is marked as India's first TCSC. Kanpur-Ballabhgarh is the first indigenous TCSC (BHEL with POWERGRID), in which a thyristor-controlled section varies an 8% fixed segment up to 20%. |

## 3. Structure, formatting and flow

- **Example numbering:**
  - In-text examples were labelled 7.A to 7.L while the practice examples were 7.1 to 7.31.
  - All 43 are now numbered 7.1 to 7.43 in order of appearance, and every cross-reference is updated.
  - The Section 7.7 examples (7.8 to 7.12) now have separate title lines like the other in-text examples.
- **Later-added subsections in "Normal" style:** 7.2.6, 7.3.5, 7.3.6, 7.4.12, 7.4.13 and 7.5.9 to 7.5.12 were in a different style, with plain-text maths (X_GCSC(gamma), di/dt, S_SSSC = sqrt(3) Vq,LL I, |Vq|).
  - All are restyled, and their maths is now proper Word equations.
  - The TCSC and SSSC additions repeated earlier subsections and broke the reading order. Their unique content is merged where it belongs:
    - control chain and damping channel into 7.4.8;
    - model hierarchy into 7.4.10;
    - fault behaviour into 7.4.11;
    - SSSC rating into 7.5.3;
    - topologies and fault bypass into 7.5.5;
    - the SSCI caveat into 7.5.6;
    - direct and indirect control and the control functions into 7.5.7.
  - Section 7.4 now ends at 7.4.11, and Section 7.5 at 7.5.8.
- **Duplicates removed:**
  - Old Figure 7.27 duplicated Figure 7.25 and Example 7.6; it was also in a different graphic style.
  - Old Figure 7.28 was a generic "conceptual" impedance plot; Section 7.7.3 covers that analysis properly.
  - A paragraph in 7.5.7 repeated 7.5.2.
  - Figures are renumbered 7.1 to 7.33, with all references updated.
- **Tables:**
  - Table 7.1 had no visible caption and was never cited. Both are added.
  - Table 7.4 had its caption below the table and no borders, and was never cited. All three are fixed.
  - Equation (7.16) was clipped in Table 7.8; the column is widened.
- **Schema repairs:** the source file had pre-existing Word-schema errors (element order, numbering IDs, math properties, duplicate bookmark IDs). These are repaired, and the final file passes full validation.
- **Writing:** the prose had no em dashes and no template phrasing. Edits were limited to clarity: two repeated sentences were removed and one awkward phrase was rewritten.

## 4. Literature verification

- **Confirmed:**
  - Vithayathil's rapid adjustment of network impedance (RANI) scheme from the mid-1980s (US patent 5,032,738; EP 0258314);
  - IEC 60143-4:2023, Edition 2.0, in which subclause 7.5.4 introduces the hardware-in-the-loop test that replaces the network-simulator test;
  - CIGRE 2024 papers B4-11213 (Colombian SSSC operation) and B4-11214 (M-SSSC EMT modelling);
  - CIGRE 2026 paper B5-12216 (SSSC and protection);
  - Krommydas et al., IEEE OAJPE (2025), on the Greek M-SSSC;
  - Pattabiraman, EPSR vol. 241, 111394 (2025);
  - the Colombian deployments on 220 kV circuits (ISA TRANSELCA, Grupo Energía Bogotá);
  - Rourkela-Raipur TCSC, 2004, the first in India;
  - Gyugyi, Schauder and Sen, IEEE TPWRD 12(1), 1997;
  - Kayenta (1992), Slatt (1993), Stöde (1998), the Brazilian North-South link (1999) and Mohave (1970, 1971), all consistent with standard references.
- **Please check before print:**
  - the commissioning year of the Kanpur-Ballabhgarh TCSC, left as "2000s, in two phases" because I found no primary source for the year;
  - the page ranges of Karady et al. (1993), which I could not open from here.

## 5. Build

- `source/build7.sh` reproduces the final file from the original. It:
  1. converts `blocks.md` (rewritten paragraphs) with pandoc;
  2. merges runs;
  3. runs `edit7.py` (all corrections, moves and renumbering);
  4. runs `post7.py` (Table 7.8 widths);
  5. runs `schemafix.py`.
- The output passes OOXML validation and renders to 46 pages. Every changed page was inspected.

---

# Second review: *Chapter_7_Series_FACTS_Controllers_Publication_Revised.docx*

The revised chapter keeps most corrections of the first review and adds new material:
- rewritten paragraphs (about 170 changed lines);
- an angle-reference table;
- a closed-form TCSC waveform section;
- worked-example extensions;
- four new references;
- 25 redrawn figures.

I compared it paragraph by paragraph with the previously verified version, recomputed every new number, checked all 25 new figures against the governing equations, verified the new references online where possible, and read the whole chapter once more at the end. The final file is built from the revised document by `source/revised_review/build7b.sh`.

## 1. Verification of the new material

- **Waveform formulas:** the closed-form TCSC conduction-interval expressions (y, t and the Fourier integral) agree with my independent analytic solution, and with Equation (7.16).
- **Example 7.33 at boost 2:**
  - branch RMS currents 1852, 1707 and 1614 A;
  - capacitor-voltage THD 16.20%, 14.77% and 13.63%;
  - individual-thyristor RMS 1206.7 A.
- **Example 7.36:** device RMS 511.55 A and branch loss 26.17 kW.
- **Example 7.24, Case B:** currents 1494.29, 1660.32 and 2490.49 A; 79.70 kV; 595.44 Mvar; third harmonic 49.7% of the fundamental.
- **Example 7.25:** a lone module at 45° gives 0.1363 Ω.
- **Example 7.37:** reactive injections −20.26 Mvar at each bus.
- **Example 7.42:** saturated current 978.09 A.
- **Delay roots:** 12.66% and 9.83%; the 1 Hz mode falls below 5% at 188 ms.
- **P-V noses (Fig. 7.4):** 0.82, 1.17 and 1.64 pu at 0.647 pu voltage.
- **Figures:** all 25 redrawn figures agree with the equations and the example values (phasor geometry, equal-area angles, GCSC and TCSC waveforms, harmonic curves, routing and headroom, relay geometry, resistance screen, delay damping).

## 2. Corrections made

| Location | Problem | Correction |
|---|---|---|
| Example 7.11 note | Says the converter term moves the boundary to "about 59%". With the converter term now specified for Fig. 7.31, R_c(f) = −0.004(f/50)⁴, the boundary is k = 61.9%, and the redrawn figure crosses zero there | "about 62%" |
| Section 7.4.6 | Third harmonic at β = 25° given as 17.2% of I_mX_C and 10.7% of the fundamental | 17.3% and 10.8% |
| Table 7.3, Rourkela-Raipur | Date removed, with a note that the supplier page does not date commissioning | 2004, India's first TCSC (Hitachi Energy reference page); reference [26] updated |
| New angle-reference table | Unnumbered, unstyled, without borders, and placed under the 7.2 GCSC heading although it covers all devices | Now Table 7.2, styled like the other tables, moved to the end of 7.1.7 and cited; later tables renumbered 7.3 to 7.9 |
| Section 7.7 intro | The research-gap table was no longer cited | Citation restored (Table 7.6) |
| Table 7.7 | One cell in a larger font | Normalized |
| Several paragraphs | Notation and wording slips: "provides numerical values beside this derivation through the cross-reference", "genuinely excluded", "12.6635% … printed as 12.7%", a repeated statement of 15.15 Ω and 0.88 Ω, "XC" as plain text, a duplicated "Figure 7.21 shows" pointer | Rewritten |
| Conventions and the 7.7 intro | "UG path … PG study" | Plain wording |

## 3. Writing and flow

The revision had added one or more disclaimers to most paragraphs: "universal" 13 times, "guarantee" 4 times, and repeated "not proof", "illustrative" and "must not" phrasing. Each qualification was correct, but the stacking made the text defensive and machine-like. I rewrote 21 paragraphs and one caption so that each qualification is stated once, in plain technical language, and no technical content was removed. The final text has no "universal" or "guarantee", and no em dashes.

## 4. References

- **Confirmed:**
  - Rourkela-Raipur (Hitachi Energy, installed 2004, first TCSC in India);
  - Imperatriz (Hitachi Energy, TCSC commissioning 1999);
  - Krommydas et al. (2025), Pattabiraman (2025), and the CIGRE 2024/2026 papers, from the first review.
- **Please check before print:**
  - Reference [23], Ministry annual report 2005-06, pp. 49-50 (Kanpur-Ballabhgarh test commissioning);
  - Reference [24], Svenska Kraftnät report 2005 (Stöde).

  I could not open either document from here; the URLs look plausible.
- **Numbering order:** references [23] to [26] are numbered out of first-citation order in Table 7.3 (24, 25, 23, 26). Renumber them if the publisher requires citation order.

## 5. Build

The final file passes full OOXML validation and renders to 58 pages. Every changed page was inspected.
