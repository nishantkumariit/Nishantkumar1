# Chapter 5 – Final review notes

**Chapter:** State Estimation, Parameter Identification and Twin Synchronization
**Revised file:** `Chapter-5_State-Estimation-Parameter-Identification-and-Twin-Synchronization_revised.docx` (42 pages, validated)

## What was checked

**The running data set (cell C-1) was reconstructed exactly.** Recovered generation details:
- OCV = 3.0 + 2.871z − 3.711z² + 2.040z³.
- Current levels uniform in [−40, 60] A with durations int(U(20, 180)) s.
- Voltage noise is drawn before current noise.
- SOC is integrated through the present sample.
- Seed: default_rng(2026).

With these settings the first sample is 4.0037 V at −21.97 A, matching Example 5.9's hand calculation.

**Results that reproduce exactly from the reconstructed data:**
- Example 5.5: ARX 0.9027 / 9.8 s / cond 4019; output error 1.5008, 1.0003, 20.07 s, 2.01 mV, six evaluations.
- Example 5.8: Monte Carlo over seeds 100 to 129; NEES 8.90 / 2.24 / 0.95, with 88 % in band.
- Example 5.9: 0.8306 after the first update, 0.87-point standard deviation, 0.015 pp RMS.
- Example 5.10: UKF RMS 0.015.
- Example 5.14 and Tables 5.3 and 5.4: 1.23 / 1.92 / 70.5; joint 0.10 / 0.23 / 1.60 / 2.239 ± 0.004 mΩ; RLS 1.749 / 2.160 / 2.188; the q_R study.
- Example 5.18: one and 66 false alarms; first alarm at 3733 s.
- Example 5.19: −2.88 pp error, 0.011 reported standard deviation, NIS 1.44.
- Table 5.7: all four rows, including 93 % coverage and the 0.0499 A offset estimate.

**Particle filter (Example 5.11):** reproduces to 0.011 pp with 855 resamplings, against the stated 0.012 pp and 848. The gap is explained by random-number details the text does not state, so the original values are kept.

**Hand examples recomputed and correct:**
- Examples 5.2, 5.3, 5.4, 5.6, 5.7, 5.12, 5.13, 5.15, 5.16, 5.17, 5.20 and 5.21.
- The holdover formula and its numbers.

**Answer key:** all 27 original answers recomputed and correct.

## Corrections

1. **Example 5.10 (unscented transform):** the exact variance 1.125 is obtained only with β = 0. With the β = 2 stated in the text as optimal for Gaussian priors, the transform reports 1.25. The interpretation now states β = 0 and explains the difference, and the related exercise specifies β = 0.
2. **Example 5.13:** the Huber estimate is within 0.14 % of the clean value, not "0.1 %".
3. **Example 5.15:** the age of sensor B's reading costs it about a quarter of its weight (0.28 against 0.36), not "a fifth".
4. **Table 5.4:** the column "90 % lag after ramp end" actually measures the lag behind the time the truth reaches 90 % of the step (590 s and 106 s reproduce only with that definition). The heading is corrected.
5. **Figure 5.30:** the case-study twin estimates the current-sensor offset b as a fourth state; the architecture diagram now shows it.

## Additions

- **Introduction** (about 920 words) replaces the numbered Learning outcomes list. It covers:
  - the history of estimation, from Gauss and Legendre through Wiener, Kalman and Schweppe to particle filters and moving horizon estimation;
  - the running data set;
  - the chapter's arc from filters to the synchronization contract.

  Its last paragraph states the learning outcomes in sentence form. The "How to read this chapter" box is kept.
- **New Advanced box (Section 5.5.4): estimating R and Q from the innovations.**
  - It gives Mehra's innovation-based noise estimate.
  - It includes a numerical example on C-1.
  - It covers the sampling uncertainty of the windowed variance (√(2/W)), positive definiteness, and why Q cannot be separated from R this way.
- **Section 5.15, new verified literature:**
  - the IEEE task force on power-system dynamic state estimation (IEEE Trans. Power Syst., 2019);
  - the cloud BMS battery digital twin of Li et al. (J. Energy Storage, 2020).
- **Further citations added:**
  - Plett's joint state-parameter EKF (2004), at the joint-estimation section;
  - Julier and Uhlmann's covariance intersection (1997), at the distributed-estimation paragraph.
- **Exercises:** 27 exercises and 10 review questions were merged into 15 exercises with linked conceptual, derivation and numerical parts. Complete solutions to all 15 are in the Answer key. New parts include:
  - the errors-in-variables limit for an AR(1) model;
  - parameter-variance growth during a rest;
  - an adaptive-R calculation;
  - a consistency check of two meters.
- **Figures:** all 30 redrawn at 600 dpi, regenerated from the reconstructed data set and the same filter code that verifies the tables.
- **References:** 19, renumbered in order of first citation; a DOI was added for Manimaran et al.

## Items for the author to confirm

1. The reconstructed OCV coefficients (2.871, −3.711, 2.040) reproduce every number. Consider stating them in Table 5.1 so that readers can regenerate the data.
2. The particle-filter values in Example 5.11 (0.012 pp, 848 resamplings) depend on the order of random draws, which the text does not specify.
3. The status labels in Section 5.15 reflect my reading of 2026 practice; adjust them if your experience differs.
4. As in the earlier chapters, the Review questions section was folded into the 15 exercises.
5. Equations do not render in LibreOffice (the same is true of the original file). They were verified by converting the document back to LaTeX; please glance at them once in Word.
