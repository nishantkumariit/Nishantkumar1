# Chapter 8: Technical Review and Correction Log

This log covers the review of *Chapter_8_Combined_and_Special_FACTS_Controllers_Publication_Ready.docx*. I read the chapter line by line, recomputed every numerical example, and checked the historical facts and references against the literature.

## 1. Errors corrected

| Location (original) | Problem | Correction |
|---|---|---|
| Sec. 8.2.2, "Illustrative IPFC case" paragraph | Equation symbols were missing, so the text read "At , pu and pu, holding while raising to 1.42 pu" | Restored: δ = 30°, X = 0.5 pu, V_pq,max = 0.25 pu, Q_1r = 0, P_1r = 1.42 pu (checked numerically) |
| Sec. 8.4.3, after Eqs. (8.13) and (8.14) | "where and are the required branch susceptances" (symbols missing) | Restored B_1 and B_2. Also checked both formulas by back-substitution: they return B_1 = -1, B_2 = +1 for Example 8.40 |
| Sec. 8.5.1, after Eq. (8.15) | "where is the reactance…, the phase voltage and the source reactance" (symbols missing) | Restored X_lim, V_ph, I_f,lim and X_s |
| Example 8.22 statement | "(a) for maximum power; (b) and ;" (symbols missing) | "(a) ρ for maximum power; (b) P_r and Q_r" |
| Example 8.23 statement | "pu and the target is pu… both values of ;" (data missing) | Rebuilt from the solution: V_pq = 0.45 pu, target P_r = 1.4 pu, both values of ρ (checked: ρ = -3.61° and 123.61°) |
| Fig. 8.4B (Pr, Qr versus ρ) | **Q_r was plotted with the wrong sign.** It showed Q_r = -0.165 pu at ρ = 0 and a maximum at ρ = 150°. Eq. (8.2) gives +0.165 pu at ρ = 0 and a minimum of -0.768 pu at ρ = 150° | Figure regenerated from Eq. (8.2) (new Fig. 8.5) |
| Fig. 8.9A (IPFC loci) | The Q axis had the opposite sign convention to Fig. 8.2: circles centred at +0.27, +1, +2 pu instead of -0.27, -1, -2 pu | Replaced by a new computed figure showing how the supporting-converter real-power limit clips the prime-line region (Fig. 8.14) |
| Fig. 8.13B (IPC branch decomposition) | The branch curves did not match the IPC120 equations. Example: the inductive branch was plotted as -0.1 at δ = -50° when the correct value is +0.1 | Regenerated exactly from sin(δ+60°) and sin(60°-δ) (Fig. 8.22) |
| Example 8.38 statement | It said "assuming the bus angle is unchanged", but the main answer (19.8°) assumes the **total transfer** is held and the angle falls | Restated as two cases: (a) total transfer held gives 19.8°; (b) angle held gives 13.2° |
| Example 8.34 | Asked for "the reactive power absorbed by the line" but gave per-end values | Clarified: the values are supplied per end, and the line absorbs twice that |
| Literature note | Gave 1999 for the first IPC installation, while Sec. 8.4.3 said June 1998 | Corrected to June 1998 (Plattsburgh APST, NYPA). Sources agree on 1998 |
| Sec. 8.1.8, Inez | The "three-level, 48-pulse-equivalent modules" detail could not be confirmed from primary sources | Changed to the verifiable wording: two ±160 MVA GTO voltage-sourced converters with multi-pulse harmonic neutralization. Test operation date (May 1998) added, with reference Renz et al. 1999 |
| Sec. 8.2.4, Marcy CSC | "commissioned in stages 2001 to 2004" was imprecise | STATCOM stage in commercial operation April 2001; full CSC completed July 2004 |
| Sec. 8.5.4 | "survives only 10 to 15 full-fault interruptions" is not a general rating | Reworded to "a limited number of full-rated fault interruptions before contact maintenance" |
| Sec. 8.5.5 | "SCFCL recovers within seconds" was overstated | Changed to "about a second to tens of seconds, depending on design and dissipated energy" |
| Sec. 8.1.3, phasor-mode figure | Series-reactance mode drew the injection at 90° to V_s instead of to the line current | Regenerated with the line current shown (Fig. 8.7) |
| Fig. 8.8 (PAR phasors) | Labels overlapped in panel (c) | Regenerated (Fig. 8.16) |

All 60 numerical results (Examples 8.1 to 8.40 and the 14 answer-key items) were recomputed with independent scripts. Apart from the items above, every answer was correct to the stated precision.

## 2. Structural and editorial problems fixed

- **Publication-unsafe meta text removed.** The original referred to "the PPT", "the lecture material", "TNA results in the PPT", and contained internal audit notes ("Numerical audit convention…", "Several lecture-deck numerical examples contain sign… ambiguities…", "The 40 solved examples… were rechecked individually").
- **Duplicate content merged.** About 20 paragraphs were repeated (for example 8.1.5 and 8.1.5D, 8.1.7A and 8.1.7B, 8.2.1B and 8.2.2B, and most of 8.8.1 to 8.8.6). Examples 8.8 and 8.9 were the same problem with different numbers. The two "Common Misconceptions" lists and the two selection tables (8.4A and 8.4) are now one each.
- **Numbering rebuilt.** Figures (8.1A, 8.2A, 8.4A to C before 8.4, 8.6B before 8.6, a missing 8.22), tables (no Table 8.1, a "Table 8.4A"), equations and examples are now numbered sequentially and generated automatically. Every cross-reference is resolved from the same source. Citations are renumbered in order of first appearance.
- **Formatting fixed.** About 15 inserted sub-headings were plain paragraphs and are now real headings. Plain-text equations (for example "d(½CdcVdc²)/dt = …") are now numbered Word equations. Empty spacer paragraphs before each figure are removed, and page numbers are added.
- **Redundant figures removed:** image2, image4, image5, image7, image8, image10, image14, image19 and image20 duplicated other figures.

## 3. Section 8.8 (Recent Advances): rewritten and expanded

The original 8.8 was a short list of keywords followed by duplicated paragraphs. The new section has 11 subsections. Each one covers the state of the art, the governing equations, the limitations of current approaches and the open problems:

1. State of the art: timeline figure and an installations table (Inez, Plattsburgh, Marcy, Nanjing 220 kV MMC-UPFC, Suzhou 500 kV MMC-UPFC, transformerless UPFC, modular SSSC fleets)
2. Modular and solid-state UPFC: N-1 cell sizing, a **derived cell-capacitor ripple formula** C ≥ S/(ω·Vdc·ΔVpp), and a redundancy availability model (Eqs. 8.27 to 8.30; Fig. 8.37; Examples 8.16 and 8.17)
3. Distributed series control: module-count sizing (Eq. 8.31; Example 8.18)
4. Coordinated dispatch: an AC-OPF formulation with IPFC and UPFC coupling constraints and its convexity issues (Eqs. 8.32 and 8.33)
5. Impedance-based stability: minor-loop gain, the generalized Nyquist criterion, and a delay-induced negative-resistance model with a computed Bode plot and phase-margin example (Eqs. 8.34 to 8.36; Fig. 8.38; Example 8.19)
6. Wide-area damping delay (Eq. 8.37; Fig. 8.39; Example 8.20)
7. Grid-forming and current-limited operation: capability circle, priority rules and the virtual-impedance bound (Eq. 8.38; Fig. 8.40; Example 8.21)
8. Protection-aware design: relay apparent impedance with series injection and an overreach example; solid-state breaker MOV energy E = ½LI₀²·k/(k−1) (Eqs. 8.39 and 8.40; Fig. 8.41; Examples 8.22 and 8.23)
9. Data-driven methods: a physics-informed loss function (Eq. 8.41)
10. Validation hierarchy for publishable evidence
11. A research map table: problem, governing equation, limitation, potential contribution and minimum evidence

The chapter also gains a new IEC 60909 peak-current factor (Eq. 8.22, with an extended Example 8.12) and three new unsolved problems (8.15 to 8.17) with answers.

## 4. References

Fifteen references were added and checked: Renz 1999; Yang et al. 2016; Wang et al. 2019 (Suzhou); Divan and Johal 2007; Sun 2011; Wang and Blaabjerg 2019; Fan et al. 2022; Molzahn and Hiskens 2019; Sen and Sen 2003; Keshavarzi et al. 2025; IEC 60099-4; IEC 60909-0; CIGRE 38-101 (1998); Häfner and Jacobson 2011; Kreikebaum et al. 2010. The three DOIs already in the chapter ([13] to [15] in the original) were confirmed to exist with matching titles and venues through web searches (direct DOI lookup was blocked in this environment).

**Please check before submission:** I recalled page ranges for Divan and Johal 2007, Sun 2011, Wang and Blaabjerg 2019, Molzahn and Hiskens 2019, Sen and Sen 2003, Häfner and Jacobson 2011 and Kreikebaum et al. 2010 from memory and could not confirm them online in this session. Please check them in IEEE Xplore or Scopus.

## 5. Build

`source/` contains the Markdown source, the figure script (`figs.py`) and the numbering and post-processing scripts. The output .docx passes OOXML schema validation, and the PDF rendering (50 pages) was inspected page by page.

---

# Second review: *Chapter_8_Final_Publication_Copy.docx*

I read the revised chapter sentence by sentence against the previous final version and recomputed every number, including all new simulation results. The source scripts for this round are in `source/publication_copy_review/` (`chk1.py` to `chk4.py` reproduce every check below).

## A. Numerical verification

All examples (8.1 to 8.43), all answer-key items (8.1 to 8.17) and every quoted model output were recomputed independently. Everything agrees to the stated precision except two values, both corrected:

| Location | Problem | Correction |
|---|---|---|
| Example 8.36(c) | P0 = 3(127.0)² sin 25°/50 = 408.98 MW, printed 409.1 MW | 409.0 MW |
| Example 8.40(d) | Total ideal THD = √(2V²rms/A1² − 1) = 5.4532 %, printed 5.4512 % | 5.4532 % |

New model results confirmed by direct simulation or exact solution:
- **Series-resonant SSFCL (Fig. 8.26):** I integrated the stated circuit equations. The limited peak is 2.440 kA and the prospective peak is 14.964 kA, both matching the text.
- **Biased bridge (Fig. 8.28):** prefault 1.000 kA peak, lagging by 4.0115°. Halving the 2 μs step changes the maximum current by 0.008 %, which supports the "less than 0.01 %" claim.
- **TCVL energization (Fig. 8.34):**
  - The no-clamp response (64/63)cos θ − (127/63)cos 8θ is exact.
  - The clamp energies 4.097 (h = 1.7) and 6.807 (h = 1.3) are reproduced.
- **Delayed impedance (Fig. 8.38, Example 8.19):**
  - Crossings 903.93, 1598.19 and 2165.92 Hz.
  - Angular separations 60.66°, 11.68° and 91.59°.
  - Delay thresholds 157.41 and 314.83 μs.
  - Lambert-W dominant roots −228.22 ± j10346.42 and −3454.90 ± j7658.96 s⁻¹.
  - All of these are reproduced, but only with L_f = 1 mH and K_p = 15 Ω. Those two values were not stated anywhere, so they are now given in the text, the caption and the figure.
- **Other results:**
  - IPFC Example 8.32: ρ1 = 27.60°, P1pq = 0.19053 pu, and the two ρ2 roots with their line-2 powers.
  - Lossy-line Example 8.27.
  - IPC inverse Eqs. (8.19) and (8.20), which back-substitute to B1 = −1, B2 = +1.
  - Fourier coefficients of Example 8.40.
  - AC versus DC comparison in Example 8.41.

Earlier correction revisited honestly: my first review gave 13.2° for Example 8.41(b). The revised chapter's 0.46 rad (26.356°) is the correct value for equal path powers at a fixed corridor angle, and it is retained.

## B. Literature check

These items were confirmed from the named sources:
- **IEC 60909-0:2026:** edition 3.0, 23 July 2026, superseding the 2016 edition.
- **Plattsburgh APST:** end of June 1998; 75 Ω inductors raised summer transfer from 105 to 140 MW (Lemay et al., IEEE Canadian Review no. 34).
- **Nanjing West Ring:** three 60 MVA MMCs; the shunt converter is on the 35 kV bus; in service December 2015.
- **Suzhou 500 kV:** end of 2017.
- **EirGrid SmartValve pilot:** 2016, Cashla–Ennis 110 kV.
- **IPTO FARCROSS:** October 2021, Nea Santa–Iasmos 150 kV.
- **Marcy CSC:** STATCOM April 2001; complete July 2004; two 100 MVA converters, a 200 MVA shunt transformer and two 100 MVA series transformers.
- **Bibliographic details:** the DOIs and details of Sun et al. (PSCE 2004), Radmanesh et al. (2016), Yuan et al. (DPFC, 2010), Monteiro et al. (2011), Mandal et al. (2025), Keshavarzi et al. (arXiv:2511.14209), Yang et al. (4.16 kV test setup), Alajrash et al. (2024), CIGRE Electra 213 / TB 242 and US 8519682 B2.

One correction:
- **Inez UPFC:** no source supports "test operation in May 1998". The shunt STATCOM stage entered service in 1997 and the UPFC was commissioned in mid-1998 (dedicated June 1998). The text now says this.

## C. Figures

All 42 figures were checked against their equations. Five were redrawn:
- **Fig. 8.7(b):** the capacitive injection was drawn about 71° ahead of the current instead of 90°. It is now drawn to scale, with equal axes.
- **Fig. 8.29 and Fig. 8.42:** box text overflowed the box borders.
- **Fig. 8.35:** the y-axis label was cut off at both ends.
- **Fig. 8.38:** crossing labels overlapped the curves, and the model parameters were missing. Both are now fixed.

## D. Writing, structure and references

- Removed the "UG path / PG study" labels.
- Turned stacked disclaimers ("universal", "guarantee", "not proof", "honestly") into single, specific statements.
- Rewrote the Example 8.15 solution so that it answers the question asked.
- Smoothed the transition into Eq. (8.2) and the sentence after Eq. (8.9).
- Made the run-in heading "Important topology distinctions." bold, consistent with the other run-in headings.
- Six references ([9], [10], [14], [17], [25], [28] in the revised numbering) were listed but never cited. Each is now cited where it fits.
- The eleven new references had been appended out of order. All 41 references are now renumbered in order of first citation, including the cross-reference inside the IEC 2026 entry.
- Removed the em dash from the IPC reference title.
- Fixed one OMML matrix element order so the file passes schema validation.

The output .docx passes OOXML validation. The 61-page PDF rendering was inspected, including every page with a changed figure.
