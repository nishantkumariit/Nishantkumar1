# Chapter 6 – Final review notes

**Chapter:** Data-Driven, AI and Physics-Informed Digital Twins
**Revised file:** `Chapter-6_Data-Driven-AI-and-Physics-Informed-Digital-Twins_revised.docx` (44 pages, validated)

## What was checked

**Hybrid battery twin (Sections 6.7.3, 6.8.2, 6.10, 6.12): reproduced exactly.**
- Method: the cell C-1 generator of Chapter 5 was extended with the second RC branch (R2 = 0.8 mΩ, τ2 = 400 s), seeds 2031 to 2035.
- Physics-baseline residual: 9.2, 10.3 and 13.9 mV.
- Filter-bank ridge model: 1.99 / 2.10 / 2.12 mV.
- Conformal interval: order statistic 6481; q̂ = 3.45 mV; coverage 89.8 %.
- Ageing record: 25 % coverage and 15.7 mV in the second hour.
- CUSUM alarm: 3840 s, with R0 up 6.7 %.
- Physics update: ΔR̂0 = 0.747 mΩ.
- Hold-out errors: deployed 15.5 mV, candidate A 2.09 mV, candidate B 2.06 mV.

**M-07 benchmark (Table 6.3).** The text does not give enough generator detail to rebuild it bit for bit. An independent rebuild from the stated description (two-node model of Chapter 4, temperature-dependent copper loss, stated loads, ambients and split) still confirms it:
- Grey-box fit: R̂ = 0.203 K/W, Ĉ = 4618 J/K and β̂ = 0.0018 K⁻¹, against the stated 0.203, 4645 and 0.0019.
- Every ranking and conclusion holds. Test and OOD errors:
  - grey box: 0.70 and 2.17 K;
  - ridge: 1.9 and 5.9 K;
  - network: 1.9 and 39 K;
  - Gaussian process: 1.3 and 35 K.
- The original values are kept.

**Hand calculations recomputed and correct:**
- Examples 6.3, 6.4, 6.5 to 6.10, 6.12, 6.13 coefficient, 6.14, 6.16 and 6.17.
- The MLP parameter count (1281) and the attention costs.
- The autoencoder threshold.
- The ensemble decomposition, PICP standard deviation, PSI 0.228 and Mahalanobis distance.
- All 28 original answers.

## Corrections

1. **Example 6.11:** x* = 1 with ℓ = 2 is *half* a length scale, not "one length scale"; x* = 4 is two length scales.
2. **Example 6.2:** "flatters the model by 60 %" is now stated precisely: the random split reports an error 38 % lower than the blocked estimate (1.07 against 1.73 K).
3. **Example 6.19 and Table 6.7:** the 1.99 mV results on the second aged record (seed 2035) hold only on its aged part (5400 to 7200 s). The text now says so; over the whole record the error is about 14 mV, because the first hour is unaged.
4. **Gaussian-process cost (Section 6.5.5):** the predictive mean costs N per prediction and the variance N².
5. **Section 6.11.1:** added that Regulation (EU) 2026/1744 (Digital Omnibus on AI, OJ 24 July 2026) deferred the stand-alone high-risk obligations, which cover critical-infrastructure safety components, to 2 December 2027.

## Additions

- **Introduction** (about 1140 words) replaces the numbered Learning outcomes list. It covers:
  - the history of learning in power engineering;
  - the extrapolation problem;
  - the two running examples;
  - the chapter's conclusions on physics-guided learning.

  Its last paragraph states the learning outcomes in sentence form.
- **New Advanced box (Section 6.8.2): adaptive conformal inference under drift.**
  - It gives the Gibbs–Candès update with a two-line proof of the long-run bound.
  - It includes a worked example on the ageing record. A fixed calibration set restores 89.6 % coverage, but with 61 % infinite intervals. A rolling 600 s window gives 90.2 % coverage with intervals about 7× wider.
  - It closes with the lesson that width is itself a drift signal.
- **Figure 6.25** gains a third panel showing the adaptive interval.
- **Section 6.13, verified research paragraph.** It cites:
  - adaptive conformal inference (NeurIPS 2021);
  - EnbPI (ICML 2021);
  - TimesFM (ICML 2024);
  - universal differential equations (2020);
  - PINNs for power systems (IEEE PES GM 2020);
  - Aykol et al. on physics plus machine learning for battery lifetime (J. Electrochem. Soc. 2021);
  - the Digital Omnibus on AI.
- **Exercises:** 28 exercises and 10 review questions were merged into 15 linked exercises with complete solutions in the Answer key. New parts include:
  - a backpropagation calculation;
  - attention without scaling;
  - GP prediction at two length scales;
  - physics-guided filter features;
  - PINN identifiability;
  - the ACI bound;
  - CUSUM alarm timing;
  - the update gate applied to Example 6.19;
  - int8 rounding error.
- **Figures:** 25 of 28 were redrawn at 600 dpi. Figure 6.25 was regenerated from the reproduced battery data, and the right panel of Figure 6.27 from Table 6.3. Specific fixes:
  - Figure 6.5 now shows the residuals its caption mentions.
  - Figure 6.15 has six points, as its caption states.
  - Label overlaps in Figures 6.6, 6.13, 6.14 and 6.17 were removed.
- **Figures kept as in the original:** 6.18, 6.21 and 6.26. They plot model outputs from the original M-07 and PINN runs, which cannot be regenerated exactly.
- **References:** 39, renumbered in order of first citation; a DOI was added for Manimaran et al.

## Items for the author to confirm

1. To make Table 6.3 reproducible, consider stating the M-07 generator details: ambient profile, block-duration distribution, initial state and the order of random draws.
2. The page range of Gibbs and Candès (NeurIPS 34) could not be confirmed from an accessible source, so it was left out.
3. As in the earlier chapters, the Review questions section was folded into the 15 exercises.
4. Equations do not render in LibreOffice (the same is true of the original file). They were verified by converting the document back to LaTeX; please glance at them once in Word.
