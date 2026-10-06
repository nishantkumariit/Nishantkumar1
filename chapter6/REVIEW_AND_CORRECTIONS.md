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

---

# Second review: updated version *Chapter6_v1.docx*

The updated chapter keeps all corrections of the first review (sequential examples, Fig. 6.18, units, Steinmetz wording). It also rewrites about 120 paragraphs, adds derivation notes and three references, and redraws 22 figures. I compared it paragraph by paragraph with the previously verified version, checked every changed statement and number, inspected all 22 new figures, and read the complete chapter once more at the end. The final file is built from *Chapter6_v1.docx* by `source/v1_review/build6b.sh`.

## 1. Verification of the new material

- **New numbers:** all correct.
  - Gain-variation ratios 3.97 and 14.8 (95° to 150° and 95° to 165°).
  - α = 113.82677° for half rating.
  - Pulse-number voltage THDs 31.08%, 15.22%, 7.57% and 3.78%; two-pair truncation underestimates them by 12.1% to 12.8%.
  - DC-link figures: 1.125 mF hypothetical rule, 0.50 mF transient deficit, 318 V ripple.
  - Chain-link energy bound 15.9 kJ/MVA at 10% ripple.
  - Star envelope 0.231 to 0.429 (r = 0.3) and 0.444 to 4.0 (r = 0.8).
  - Example 6.16: 20 MW, 16 MJ, 0.980 pu, 21.3 MJ.
  - Fig. 6.53 threshold gain K = 0.790.
  - Negative input conductance from 0.84 kHz in Fig. 6.54, recomputed from Equation (6.77).
  - Example 6.22 reactor loss 26.97 W; Example 6.24 valve stress 664.1 V; Example 6.33 angle −1.65°.
- **New derivations:** correct. These are the TSC minimum-oscillation proof (x_opt = ρ, A_min = √(1 − ρ²/k)), the SVC sensitivity K_N = E_th·X_th/(1 − X_th·B₀)², and the triangle-inequality envelope of Equation (6.70).
- **Redrawn figures:** all 22 were checked against the governing equations.
  - Fig. 6.3: P = 4·V_m·sin(δ/2) with the current- and susceptance-limited midpoint laws.
  - Fig. 6.29: primary susceptance 0.682/−0.370 pu.
  - Fig. 6.39: P = 0.30, Q = 0.742 pu.
  - Figs. 6.37 and 6.46: phasor and control-loop signs.
  - Figs. 6.44, 6.47, 6.50, 6.51 and 6.53: these reproduce the example values.

## 2. Corrections made

| Location | Problem | Correction |
|---|---|---|
| Table 6.5, Radsted | Changed back to 2006, the supplier-list year | 2007: the SVC entered service in summer 2007 (Siemens/T&D World) |
| Table 6.5, Islington | 2009 | 2010: Transpower records SVC9 (+150/−75 Mvar) as installed in 2010 |
| Table 6.5 text | Year basis not stated; Devers source [40] listed but never cited | States that years are in-service years; [40] now cited |
| Fig. 6.3 | "STATCOM 1 pu" and "SVC 1 pu" both dotted; legend covered the curves | Redrawn with distinct markers and a two-column legend; curves recomputed |
| Fig. 6.20 caption | Same line style for both firing schemes at each n | Caption states which curves are voltage matching and which are crest firing |
| Section 6.2.4 | Derivation note placed between "dividing by 2π:" and Equation (6.16) | Moved after the equation as a short "to evaluate it" note |
| Section 6.2.5 | Note interrupted the sentence leading into Equation (6.19); long inline integral | Rewritten in order: integral, identity, then Equation (6.19) |
| Section 6.5.7 | Sensitivity derivation inserted between Equation (6.44) and its "where K_N…" definition | Definitions and derivation merged into one paragraph after the equation |
| Section 6.1.2 | "I_sh without an underline", but the notation is an overbar | "without an overbar" |
| Example 6.31 | "The unequal b-c and c-a reactive currents" (they are equal and opposite) | Corrected |
| Section 6.4.5 | Fig. 6.21 called "simulated"; it is computed from Equation (6.27) | "computed" |
| Section 6.7.3 | Text referred to an "earlier one-sided discharge integral" that no longer exists | Paragraph tightened; reference removed |
| Section 6.7 intro | "UG readers … PG readers" | Plain wording |

## 3. Writing and flow

The revision added a qualification to almost every paragraph. "Universal" appeared 11 times, "guarantee" 4 and "certified/illustrative/heuristic" repeatedly, often three disclaimers in one paragraph. That made the text defensive and machine-like. I rewrote 20 paragraphs and 3 captions so that each necessary qualification is stated once, in plain technical prose, and no technical content was removed:

- Sections 6.1.3 and 6.4.3;
- the TSC strategy paragraphs;
- the TSC configurations and FC-TCR losses;
- SVC tuning and STATCOM overload;
- DC-link sizing;
- system strength, chain-link energy and the sequence envelope;
- virtual-impedance limiting and the impedance criterion;
- the model-class discussion.

The final text has no "universal" or "guarantee", and no em dashes.

## 4. References

- **Confirmed:**
  - UNIFI Specifications Version 3, NLR/TP-5D00-98381 (2026);
  - Marzo et al., IJEPES vol. 142, 108267 (2022), all six authors;
  - Hitachi Energy Gerdau case (SVC Light, 13.2 kV, 0 to 64 Mvar, three-level VSC, commissioned end of 2006).
- **Please check before print:**
  - The 32 MVA converter rating of Gerdau, which I could not confirm in a public source.
  - Reference [41] is a supplier brochure archived on StudyLib. I suggest replacing it with a primary source, or a citable Siemens Energy reference page, where one is available.
  - The rows still flagged from the first review: Greenbank/South Pine and Bom Jesus da Lapa II.

## 5. Build

The final file passes full OOXML validation, including pre-existing schema-order issues that were repaired. It renders to 82 pages. Every changed page was inspected.
