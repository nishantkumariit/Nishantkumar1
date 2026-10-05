# Chapter 6: Technical Review and Correction Log

This log covers the review of *Chapter6_Shunt_FACTS_Controllers.docx* (TCR, TSR, TSC, SVC and STATCOM). I read the chapter sentence by sentence, recomputed every worked example, practice problem and answer-key item with independent scripts (`source/chk.py`, `source/chk2.py`), and checked the installation data and references against published sources. Edits were made directly in the original OOXML (`source/edit6.py`), so the original layout, styles, equations, header and footer are preserved.

## 1. Numerical verification

- The TCR fundamental and harmonic expressions were checked against direct numerical integration of the conduction waveform over the full firing range, including the harmonic maxima of Table 6.3.
- All 35 worked examples and all answer items A6.1 to A6.17 were recomputed: TCR/TSC ratings, switching transients, binary banks, SVC droop and ESCR design, Steinmetz balancing, STATCOM dq control, DC-capacitor sizing, six-pulse and multipulse harmonics, and energy-storage STATCOM limits. Spot values: Ex. 6.30(f) peak 2.361 pu at 94.85 deg; the THD values of Ex. 6.26.
- **Result: no numerical error was found.** Every stated result matches to the precision given.

## 2. Errors corrected

| Location | Problem | Correction |
|---|---|---|
| Example numbering | Examples appeared out of order (6.1, 6.5, 6.9, ... in the text, with the lower numbers in the practice section) | All 35 examples renumbered 6.1 to 6.35 in order of appearance; all 48 occurrences, including in-text cross-references, updated |
| Fig. 6.39 and Fig. 6.51 | Labels embedded in the images cited the old example numbers (6.32, 6.35) | Image labels changed to Example 6.13 and Example 6.16 |
| Fig. 6.18 (TSR closing transient) | Curves labelled with the firing angle alpha, although the text defines the closing angle theta_c from the voltage zero | Regenerated with theta_c = 90 deg (transient-free) and theta_c = 180 deg (full DC offset) |
| Three solution lines (54.02, 652.4, 494.8) | Current values without units | " A" added |
| Table 6.5 (installations) | Radsted listed as 2006, "Transmission" level; Strathmore year "n.a." | Radsted 2007, 132 kV; Strathmore 2007 |
| Steinmetz example (now Ex. 6.31) | The role of the *ab* branch was stated unclearly | Reworded: the branch only cancels the load's own 300 kvar; without it the line currents would be neither balanced nor at unity power factor |

## 3. Writing and flow

The prose reads naturally and is technically precise. It contains no em dashes and no template phrasing. The two mentions of "lecture notes" refer to the general teaching literature and were kept. No restructuring was needed.

## 4. References and facts

- **Confirmed:**
  - Devers SVC (2006, 525 kV, +330/-110 Mvar plus a 110 Mvar MSC);
  - Radsted (in service 2007, 132 kV);
  - Wang, Xu and Li, IEEE TPWRD 39(6), 3450-3461 (2024);
  - Narula et al., EPSR 234, 110801 (2024);
  - CIGRE TB 935 (WG B4.84, 2024);
  - UNIFI Specifications v2, NREL/TP-5D00-89269 (2024).
- **Please check before print:** the Greenbank/South Pine, Bom Jesus da Lapa and Gerdau rows of Table 6.5. I could not find a primary source for their ratings and years.

## 5. Build

The final .docx passes OOXML schema validation and renders to 67 pages. Every edit was confirmed in the PDF text, and the pages that carry the changed figures were inspected visually.
