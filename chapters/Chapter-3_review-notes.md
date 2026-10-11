# Chapter 3 – Final review notes

**Chapter:** Sensors, IoT, Data Acquisition, Communication and Connectivity
**Revised file:** `Chapter-3_Sensors-IoT-Data-Acquisition-Communication-and-Connectivity_revised.docx` (53 pages, validated)

## What was checked

- **Worked examples:** every numerical result in Examples 3.1 to 3.23 was recomputed in Python. This covers the CT, divider and RTD budgets, aliasing, Butterworth orders, quantization and jitter, PTP, holdover and TVE, Modbus and CAN timing, the LoRaWAN link, Kalman gains, gating, fusion, the two-node Riccati placement study, calibration intervals and the timing bounds.
  - All results are correct except for the wording issues listed below.
  - The two-node placement results in Example 3.21 were reproduced exactly: time constants 136 s and 1144 s; condition numbers 13.2, 35.9 and 1.1; P∞ traces 0.0264, 0.0245 and 0.0184 K².
- **Exercises:** all 37 original exercise answers were recomputed. They were correct.
- **Equations:** every OMML equation was inspected.
- **Standards and references:** checked online.
  - Confirmed: IEC 60751:2022, ISO 11898-1:2024 (CAN XL), Sparkplug as ISO/IEC 20237:2023, NIST IR 8356 (Feb 2025), IEEE 802.1Q-2022, and Manimaran et al. (2026, DOI added).
  - The IEC/IEEE 61850-9-3 second edition is still an active IEEE/IEC project (PAR approved 2021), not a published standard.
  - IEC 61869-2:2012 is still the current edition; a second edition was circulated as a draft in 2024.

## Corrections

1. **Equation (3.45):** the GOOSE repetition term was typeset as T with subscript "02" and superscript n. It now reads T₀·2ⁿ.
2. **Example 3.7 and Section 3.6:** the literal text "49.4 k\Omega" inside the equations now shows 49.4 kΩ.
3. **Example 3.4:** added the case of independent resistor tolerances (u(k)/k = 0.063 %), alongside the original fully correlated case (0.081 %).
4. **Example 3.5:** "eight times its Class A tolerance" changed to "about seven and a half times (2.64 K against ±0.35 K)".
5. **Section 3.11.2:** "about 120 m at 500 kbit/s" now states its assumptions: sample point 80 %, node delay 200 ns. With the sample point at 87.5 % the length is 135 m.
6. **Example 3.18:** "a few values per minute under a 1 % duty cycle" was wrong. At 1.3 s time on air the sensor may send one message about every 130 s.
7. **Section 3.12.2 and Table 3.5, 5G URLLC:** 3GPP TR 38.913 sets a 0.5 ms average user-plane latency target in each direction. The 1 ms figure belongs to the reliability requirement (1 − 10⁻⁵ for 32 bytes within 1 ms). The reference is now TR 38.913 V14.3.0 (Release 14).
8. **Section 3.16:** a CT calibration cuts the channel budget by a factor of about three, not four (0.358 % falls to about 0.12 %). The 2.5 W copper-loss figure is now labelled as an upper bound.
9. **Section 3.18:** the second edition of IEC/IEEE 61850-9-3 "will align" with IEEE 1588-2019 once published; the text no longer says it already aligns.
10. **Section 3.13.4, Table 3.7 and Figure 3.29 (data-quality demonstration):** the demonstration was re-implemented from the stated parameters (`demo.py`).
    - The new results are close to the original but not identical, so the table now carries the reproducible values:
      - whole-record RMS error 0.85 K naive and 0.21 K validated (was 0.83 and 0.18)
      - bias alarm after 10 min at a 0.6 K shift (was 8 min and 0.5 K)
    - The text now explains exactly what each test caught. Without the timestamp test, the gate needs nine samples to start rejecting the frozen value, and the bias alarm then shuts the stream down.
    - The Reproducibility paragraph now states the noise-draw order, the initial variance and the six false gate rejections.
    - The dropout variance growth (0.0127 to 0.0350 K²) was confirmed exactly.
11. **Figure 3.26:** the SF7 sensitivity was shown as about −123 dBm; it is −124.5 dBm.
12. **Figure 3.30:** the ambient temperature is now drawn as a source of temperature (voltage-source symbol), not a current source.
13. **Figure 3.23:** the CAN arbitration waveforms now show all 11 identifier bits for IDs 0x065, 0x063 and 0x06C. The withdrawal points at bits 9 and 8 are verified.

## Additions

- **Introduction** (about 1150 words) replaces the numbered Learning outcomes list. It covers the history of measurement for twins (SCADA, synchrophasors, IEC 61850, IIoT), the three organizing questions, the two recurring themes and the levels of treatment. Its last paragraph states the learning outcomes in sentence form. The "How to read this chapter" box is kept.
- **Box 3.2 [Advanced]:** CUSUM detection delay and false-alarm rate with Siegmund's approximation, and a numerical trade-off for choosing κ and h_c.
- **Section 3.10:** IEEE 1588g-2022 timeTransmitter/timeReceiver terminology (the PTP figure now uses both terms), and the P1588f amendment on asymmetry calibration (in preparation).
- **Section 3.18:**
  - multi-antenna GNSS spoofing detection for substations (Laverty et al., IEEE Trans. Smart Grid, 2022)
  - a new paragraph on field evidence of data quality (Huang et al., 2016; Mishra et al., IJEPES, 2024)
- **Exercises:** 37 exercises and 10 review questions were merged into 15 exercises with linked conceptual, derivation and numerical parts. Complete worked solutions to all 15 are in the Answer key, including new parts such as the 4th-order sampling rate, CT linear range, burst-length probability and CUSUM ARL.
- **Figures:** all 33 figures were redrawn at 600 dpi from the stated parameters, and overlapping labels were removed.
- **References:** renumbered in order of first citation (46 in total). New: Huang et al. 2016, Mishra et al. 2024, Laverty et al. 2022, Basseville and Nikiforov 1993, IEEE 1588g-2022.

## Items for the author to confirm

1. Laverty et al.: the volume (13, 2022) is from the DOI record. Confirm the issue and page numbers in IEEE Xplore.
2. Example 3.21 cites "the two-node M-07 model derived in Chapter 4". Make sure Chapter 4 uses the same parameters (Cw = 2.5 kJ/K, Cf = 6.5 kJ/K, Rwf = 0.08 K/W, Rfa = 0.12 K/W).
3. The calibration-chain uncertainties in Figure 3.31 (0.002, 0.01, 0.04 and 0.09 K) are indicative. Replace them with your laboratory's certificate values if you have them.
4. Table 3.10 is labelled as design values; keep that label until real certificate values exist.
5. The Review questions section was folded into the 15 exercises, as for Chapters 1 and 2.
6. Equations do not render in LibreOffice (the same is true of the original file). They were verified by converting the document back to LaTeX; please glance at them in Word.
