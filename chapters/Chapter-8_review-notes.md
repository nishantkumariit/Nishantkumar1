# Chapter 8 – Final review notes

**Chapter:** Digital Twins for Solar PV and Wind Energy Systems
**Revised file:** `Chapter-8_Digital-Twins-for-Solar-PV-and-Wind-Energy-Systems_revised.docx` (42 pages, validated)

## What was checked

Every worked example and every answer was recomputed independently. Results:

**PV**
- **Example 8.2 (single-diode fit):** reproduced exactly for n = 1.0, 1.1 and 1.2.
  - Fitted parameters: 0.307 / 0.267 / 0.228 Ω and 322 / 496 / 1069 Ω.
  - Low-irradiance powers: 74.9 to 75.4 W, 34.3 to 35.8 W and 14.5 to 16.6 W.
  - Other values: 301.2 W, 351.7 W, β_Voc −0.25 %/K.
- **Examples 8.4 to 8.6 (shaded string, weak module, MPPT trap):** reproduced with a cell-group model with bypass clamping.
  - 7997 W unshaded; 5924 W global and 1779 W local peaks.
  - 7582 / 7281 W; mismatch 4.3 %; loss 5.2 %.
- **Examples 8.1 and 8.3 and Sections 8.4.2 to 8.4.6:** correct (POA 647 W/m², Faiman 63.3 °C, IAM, bifacial, uncertainty).

**Wind**
- **Power curve and energy:** reproduced from (8.18) with η = 0.95.
  - C_P,max 0.480 at λ 8.10; speed limit at 10.1 m/s.
  - 755 kW at 8 m/s and 709 kW at 7.83 m/s.
  - AEP 6300 MWh, CF 36.0 %, S_E 1.78.
- **Example 8.13 (drivetrain):** a re-simulation gives 2.0 Hz, shaft torque 0.49 to 1.57 MN·m, peak 1.50 × rated, one-mass speed rise 0.011 rad/s.
- **Example 8.16 (wake row):** reproduced exactly (8.00, 6.19, 6.41, 6.38, 6.38 m/s) once two unstated assumptions are made explicit:
  - deficits are evaluated on the hub centreline;
  - velocity deficits u_i·δ_i are superposed as a root sum of squares.

  The aligned-direction loss reproduces at 30 to 31 %, against the stated 29 %; the difference depends on the thrust curve above rated, which is unstated.
- **Example 8.17 (wake steering):** reproduced (671 + 445 kW at 20°) when the downstream deficit uses the yawed thrust coefficient C_T·cos²γ.
- **Examples 8.10, 8.11, 8.12, 8.15 and 8.18 and the DEL:** correct.

**Synthetic-year results (Examples 8.7 to 8.9 and 8.19 to 8.23)**
- These depend on unstated generator details, so they were checked for internal consistency rather than regenerated: yields, PR, utilization, curtailment shares and detection statistics.

**Answer key:** all 32 answers recomputed; one error, corrected below.

## Corrections

1. **Section 8.9.2:** with the stated model, rated power is reached at 11.2 m/s, not 11.3 m/s. Figure 8.15 already showed 11.2.
2. **Example 8.10:** IEC 61400-12-2 (nacelle anemometry) was cited as the 61400-12-1 reference. It now has its own entry (IEC 61400-12-2:2022, Ed. 2).
3. **Section 8.12.1 and Examples 8.16 and 8.17:** the superposition rule, the evaluation point and the yawed thrust coefficient used for the results are now stated.
4. **Figure 8.22:** the caption said the offset began "on day 14" while the text said day 15. Both now agree: 14 days on the time axis, the start of day 15.
5. **Answer 8.27:** the large cycles cause 51 % of the damage, not 49 %.
6. **Heading 8.9.1:** displayed raw LaTeX ("$C_P(\lambda,\beta)$") and now reads "power-coefficient surface".
7. **Figure 8.16:** rated rotor torque is now 1.05 MN·m, consistent with Example 8.13; it was 1.00.
8. **Figure 8.6:** the angles θ_z and θ_i are now drawn correctly, and ground reflection comes from in front of the module.
9. **Figure 8.21:** the confusing "sum − 500 kW" curve is replaced by the total on its own axis.

## Additions

- **Introduction** (about 1040 words) precedes Section 8.1, which is retitled "Two weather-driven plants inside one twin". It covers:
  - the history of PV and wind;
  - the chapter's three parts;
  - the running P-1 and T-1 example;
  - the synchronization theme.

  Its last paragraph states the learning outcomes in sentence form.
- **New Advanced box (Section 8.12.1): where the Gaussian wake formula comes from.**
  - It derives the formula from momentum conservation.
  - It gives the condition for a real root, x/D ≥ 1.8, which explains the near-wake limit.
  - It includes a numerical check against Example 8.16 and explains the superposition rule.
- **Verified literature added:**
  - Ilse et al., soiling (Joule 2019);
  - Sinha et al., UV-induced degradation (Prog. Photovolt. 2023);
  - pvlib python (JOSS 2018);
  - Howland et al., collective wind-farm operation (Nature Energy 2022);
  - Yang et al., solar forecasting review (RSER 2022);
  - IEC 61400-12-2:2022.
- **Exercises:** 32 exercises and 10 review questions were merged into 15 linked exercises with complete solutions. New parts include:
  - the region-II turbulence factor 1 + 3TI²;
  - detection days for failed strings;
  - the Gaussian wake derivation and its near-wake limit;
  - combined forecast intervals;
  - PV energy delivered per MWh at the shared connection.
- **Figures:** six were redrawn at 600 dpi (8.1, 8.3, 8.6, 8.12, 8.16, 8.21), regenerated from the chapter's models where they are plots. The others were checked and found correct.
- **References:** 18, renumbered in order of first citation; a DOI was added for Manimaran et al.

## Items for the author to confirm

1. To make Examples 8.16 and 8.17 reproducible, consider stating the thrust curve used above rated wind speed.
2. The synthetic-year generators (Examples 8.7, 8.19 to 8.23) are described only in outline. Consider publishing the code or the remaining details.
3. As in the earlier chapters, the Review questions section was folded into the 15 exercises.
4. Equations do not render in LibreOffice (the same is true of the original file). They were verified by converting the document back to LaTeX; please glance at them once in Word.
