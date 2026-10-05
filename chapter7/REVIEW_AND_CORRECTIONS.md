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
