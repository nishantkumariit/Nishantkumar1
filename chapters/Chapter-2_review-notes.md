# Chapter 2: review notes (final round)

Revised file: `Chapter-2_Digital-Twin-Architecture-Frameworks-Lifecycle-and-Standards_revised.docx`

## Structure changes requested by the author

- The chapter now opens with an **Introduction** of about 1,300 words (unnumbered, so all numbering is unchanged). Its last paragraph states the learning outcomes in sentence form. The numbered list has been removed, and the "How to read this chapter" box is kept after the Introduction.
- The 10 review questions, 31 exercises and the mini-project have been merged into **15 exercises**: 3 conceptual, 4 derivations, 7 numerical (including one new problem on the new repairable-pair material) and 1 research project that absorbs the mini-project and the open design questions.
- The **answer key** gives full worked solutions for all 15. The sentence about an instructor's manual has been removed.

## Verification performed

- Every worked example (2.1 to 2.23), every equation-based figure and every old answer-key value were recomputed in Python. All were correct.
- The synthetic timing campaign (Section 2.3.5) was regenerated from the stated distributions with `default_rng(2026)`. It reproduces Table 2.7 exactly: mean 47.22 ms, 99.9th percentile 122.95 ms, 270 misses, longest run of 2; after the fix, 71.48 ms and no misses.
- Standards and sources were checked online. Confirmed: Margo Preview Release 1 (13 Jan 2026), ISO 23247-5 (June 2026), ISO 23247-6 (July 2026, with integrated, unified and federated composition), ISO/IEC 30188:2026, IEEE 3835-2025 (10 Oct 2025), ITU-T Y.4517 (06/2026, in force), Fett et al. (Electronics, 2024), Schmidt et al. (Sensors, 2023), and the IDTA AAS metamodel versions 3.1.1 (Jul 2025) and 3.2 (Jul 2026).

## Corrections

1. **Figure 2.12 (error):** the plotted "added age" reached about 16 s at the 1 s batch because the x-axis counted individual values, while (2.21) counts sampling instants. Equation (2.21) now states "n_b successive sampling instants of P_1 bytes", and the figure is redrawn with 16 values per instant: 29.9 kbit/s and 0.98 s added age at n_b = 50, consistent with Example 2.11.
2. **Figure 2.3 (inconsistency):** the historian was drawn in series on the real-time path, contradicting the lesson of Example 2.1. It is redrawn with the historian on a parallel branch, and the caption is updated.
3. **Figure 2.5 caption:** the campaign is in Section 2.3.5, not 2.3.4.
4. **ISO/IEC 30188 viewpoints:** the text named specific viewpoints ("digital target entity", "architecture-pattern viewpoint") that could not be verified from any public source. The sentence now states only the published scope. Figure 2.4 replaces the unverifiable 30188 column with the functional domains of the Industrial Internet Reference Architecture.
5. **AAS version:** "now at version 3.1.1 with 3.2 published in 2026" changed to "at version 3.2 since July 2026", with the reference updated.
6. **AAS → IEC 61850 claim:** previously uncited. It is now stated precisely (IID files generated from AAS records for a low-voltage benchmark grid) and cited to the TU Dortmund dataset on IEEE DataPort.
7. **Table 2.5:** "edition details to verify" for ITU-T Y.4517 replaced; the Recommendation is confirmed in force (06/2026).
8. **TwinArch:** the reference is updated to its journal version (J. Syst. Softw., vol. 231, 2026).
9. **Performability paragraph:** now says explicitly that the same weighting gives the expected value of any per-state metric, since the example averages an RMSE rather than Ψ.
10. **Figure 2.7:** packet age is now labelled Δ(t), consistent with the text, and the delays span exactly the stated 8 to 67 ms.
11. Typo "Exercise Exercise 2.5" removed (the exercises were rewritten).

## Additions

- **ISO/IEC/IEEE 42010:2022** (architecture description: stakeholders, concerns, viewpoints, views) introduced in Section 2.1.1.
- **[Advanced] box "Redundancy with repair"** (Section 2.9.2): Markov derivation of the mean time to failure of a repaired 1oo2 pair, (3λ+μ)/(2λ²), and of the unavailability with one or two repair crews. Worked numbers: a repaired pair lasts 457 years against 6000 h unrepaired, and a single crew doubles the unavailability. It explains why maintenance organization is itself an architecture parameter. Exercise 2.14 practises it.
- Zomerdijk et al. (2024) added as a power-system-specific reference-architecture proposal.

## Figures

- All 30 figures have been redrawn at 600 dpi (the originals were about 190 dpi), in the same style as Chapter 1.
- Overlaps fixed in Figures 2.14, 2.15, 2.18, 2.19, 2.22, 2.23, 2.24 and 2.29.
- In Figure 2.29 the PQ meter is moved to the device tier and the PV inverter now connects to a PV data logger.
- The data figures are regenerated from the chapter's own equations and the reproduced campaign.

## Items for the author to confirm

1. The same Abuabed and Kittur statements as in Chapter 1 (Section 2.14): only the abstract could be checked.
2. The Schwierz IEEE DataPort dataset: the year and DOI were not retrievable online; please add them from the dataset page.
3. TwinArch, J. Syst. Softw. vol. 231: the article number was not found.
4. The IIRA functional-domain mapping in Figure 2.4 follows IIRA v1.9/1.10 (control, operations, information, application, business). Please check it against the edition you cite.

## Note on rendering

The equations are native Word equations and display correctly in Microsoft Word. LibreOffice does not draw them, and the same was true of the original file.
