# Chapter 1: review notes (final round)

Revised file: `Chapter-1_Fundamentals-and-Evolution-of-Digital-Twin-Technology_revised.docx`

## Structure changes requested by the author

- The chapter now opens with an **Introduction** of about 1,250 words (unnumbered, so section, equation and figure numbers are unchanged). Its last paragraph states the learning outcomes in sentence form. The numbered "Learning outcomes" list has been removed. The "How to read this chapter" box is kept, after the Introduction.
- The 10 review questions, 28 exercises and the mini-project have been merged into **15 exercises**: 3 conceptual (1.1 to 1.3), 4 derivations (1.4 to 1.7), 7 numerical design problems (1.8 to 1.14) and 1 research project (1.15, which absorbs the mini-project).
- The **answer key** now gives full worked solutions for all 15 exercises. The sentence "full solutions are reserved for the instructor's manual" has been removed.

## Verification performed

- Every worked example (1.1 to 1.24), Table 1.7, the case-study record (Table 1.17), every numerical answer in the old answer key and every new solution were recomputed in Python. All original results were correct to the printed precision.
- The case-study generator listed in Section 1.15 was run. It reproduces Table 1.17 exactly: flag at 08:11:30, advisory at 08:21, R_th = 0.249 ± 0.002 K/W, state error 0.14 K RMS.
- The references and standards were checked online. ISO/IEC 30186:2025, ISO/IEC 30188:2026 (July 2026), ITU-T Y.4517 (06/26), IEEE 3835-2025 (October 2025), NIST IR 8356, Abuabed and Kittur (2026), Satpathy and Ramachandaramurthy (Appl. Energy, vol. 420, 2026), Manimaran et al. (2026), Thwe et al. (2025), Zhou et al. (arXiv:2601.01321) and Grid-Mind (arXiv:2602.20683) were all confirmed.

## Technical corrections

1. Section 1.2, Apollo 13: ref. [3] (Zhou, Zhang and Gu) traces the concept to virtual manufacturing, model predictive control and BIM. It does not discuss Apollo, so the sentence has been rewritten to say what the paper actually argues. Ref. [2] (a 2024 Vickers slide deck, whose content could not be checked) has been replaced by the Siemens Simcenter article that popularised the "Apollo 13 as first digital twin" story.
2. Section 1.2: Abuabed and Kittur "screened 84 studies" changed to "analysed 84 studies"; 84 is the number of included studies, not the number screened.
3. Section 1.5.1: the 0.044 K/s heating rate is now stated as the full-load rate on a cold winding. The motor-starting transient is excluded.
4. Example 1.2(d): the 130 °C fallback and the 115 °C margin rule are now reconciled explicitly (a 10 K margin is accepted because the overload relay remains as a second layer).
5. Example 1.6: "ten times the RTD noise" changed to "more than ten times" (3.5/0.3 ≈ 11.7).
6. Example 1.11: "T_amb = 30 ± 0.5 K" changed to "30 °C ± 0.5 K".
7. Example 1.17: added a sentence stating that both sides of (1.62) must use the same decision unit (per sample).
8. Section 1.8.1, Eq. (1.48): the p/N variance argument is now stated for models that are linear in their parameters.
9. Section 1.9: ISO/IEC 30186 Annex A is an example assessment of a *power* digital twin (a Korean case), not a "power-plant twin".
10. Table 1.12: the empty Level 0 cells now read "Not assessed".
11. Figure 1.7: listed the motor's hidden state as "hot-spot T", which contradicted Table 1.5 (clause 4: hot spot not estimated). It now reads "lumped winding T (hot spot out of scope)".
12. Figure 1.12: the innovation was labelled r; it is now ν, consistent with Eq. (1.26).
13. Figure 1.17: the caption said the one-node model meets the overheating-advisory profile, but the plotted decision requirement (5) exceeded what the model achieves (4). The requirement has been corrected so that figure and caption agree.
14. Figure 1.26: "offline ML model" was plotted at medium coupling, although Table 1.14 says it has no live link. It has been moved to low coupling.
15. Figure 1.35: the corrected-twin curve is now labelled "innovation", as in the text.
16. Figure 1.37: "fields" changed to "clauses", matching the text.
17. References: Mchirgui et al. (old [40]) and Palensky et al. (old [53]) could not be found in any index. They are replaced by Jafari et al. (IEEE Access, 2023) and Song et al. (Sustainability, 2023), both verified. DOIs have been added where they were missing. All references are renumbered in order of first citation (IEEE style).

## Additions

- **Power-system lineage** (Section 1.2, Table 1.2 and Figure 1.3): static state estimation (Schweppe and Wildes, 1970), phasor measurement units (late 1980s, IEEE C37.118) and fully digital real-time simulation (RTDS, 1995). This answers the common objection from power engineers that grid "twins" have existed for decades, and it makes clear what this book adds: the written acceptance criterion and the explicit uncertainty contract.
- **[Advanced] box "Which parameters can the data reveal?"** (end of Section 1.6.3): sensitivity derivation for R_th and C_th showing why steady-state data identify R_th but not C_th. Numbers are checked (2.9 K and 2.1 K at t = τ; 8.0 K in steady state).
- Citations added for the Luenberger observer (1971), the Kalman filter (1960), IEC 60076-7 (transformer loading guide) and IEC 61215-2 (NMOT).
- A short sentence in the chapter summary on the power-system lineage.

## Figures

- All 37 figures have been redrawn at 600 dpi; the originals were about 190 dpi, below print requirements. The style is the same: black line art, DejaVu Sans text and STIX math.
- Overlaps fixed in Figures 1.2, 1.5, 1.6, 1.10, 1.12, 1.23, 1.24, 1.26, 1.33 and 1.36. Clipped borders fixed in Figures 1.6 and 1.7.
- Figure 1.3 now includes the power-system milestones and is marked "not to scale". Figure 1.14 is marked "schematic, not to scale".
- The data plots were regenerated from the chapter's own equations and the case-study generator, so every plotted number matches the text.

## Items for the author to confirm (could not be fully verified online)

1. Abuabed and Kittur (2026): the counts "43 power and energy studies" and "5 cybersecurity/lifecycle studies", and the statement that prescriptive twins are the main open barrier. Only the abstract (7 themes, 84 studies, 2015 to 2025) could be confirmed.
2. Pavleska, Adv. Eng. Inform., vol. 70: the DOI and date were confirmed, but not the volume number.
3. Zomerdijk et al., Digital Twins Appl.: the DOI 10.1049/dgt2.12020 was confirmed, but not the volume and page numbers.
4. RTDS paper (Kuffel et al., 1995): the IEEE Xplore record gives April 1995, Texas (ICDS '95). The page numbers were not found.
5. Kavousi-Fard et al., Sol. Energy, vol. 274: sources disagree on the article number (112561 vs 109645). 112561 is kept.
6. TwinEU partner count: sources give 75 or 77; "about 75" is kept.
7. If any later chapter refers to old exercise numbers (for example "Exercise 1.12"), those references need updating. Inside this chapter, the one such reference now points to Exercise 1.9.

## Note on rendering

The equations are native Word equations. They display correctly in Microsoft Word. LibreOffice does not draw them, and that was equally true of the original file.
