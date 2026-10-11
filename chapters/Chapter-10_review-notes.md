# Chapter 10 – Final review notes

**Chapter:** Digital Twins for Electric Vehicles and Charging Infrastructure
**Revised file:** `Chapter-10_Digital-Twins-for-Electric-Vehicles-and-Charging-Infrastructure_revised.docx` (45 pages, validated)

## What was checked

Every worked example and answer that can be recomputed was recomputed independently. These were correct:

- **Example 10.1 (cable loss):** 395 A / 0.78 kW, 921 A / 4.24 kW, 197 A / 0.19 kW, 461 A / 1.06 kW.
- **Safety and pilot:** ISO 6469-3 insulation limits; control-pilot duty cycles (26.7 %, 65 A).
- **Example 10.2 (coast-down):** rotational-inertia factor 1.051; the 160 s coast-down duration was re-simulated.
- **Example 10.4 (motor and gear):** base speed 4620 r/min at 68 km/h; 235 km/h; 7413 N; 21.6°; 0 to 100 km/h in 8.9 s (re-simulated); 21.8 kW at 120 km/h.
- **Example 10.6 (winter range):** 445, 405, 361, 267 and 305 km; the heat pump recovers 38 km.
- **Connector limits and fault example:** 516 A, 404 A, 0.49 mΩ.
- **Charger control and capability:** PI gains 15.1 Ω and 251 Ω/s; 356 V and 329 V; about 2 kvar at a 600 V DC link.
- **Erlang C (Example 10.16):** 76 / 42 / 22 / 10 % wait and 91.5 / 16.9 / 5.2 / 1.8 min; Allen-Cunneen 9.2 and 2.8 min.
- **Plating limits (Figure 10.16):** 680 / 280 A at 25 °C and 234 / 96 A at 10 °C.
- **Exercise answers:** all correct.

A new closed-form derivation of the 25 °C charge time reproduces the 26.5-minute entry of Table 10.5 exactly.

## Errors corrected

1. **Wheel-to-battery energy balance (Section 10.3.3, Figure 10.5).**
   - The original text gave 6.05 kWh of traction. But traction must equal rolling + drag + braking energy (1.95 + 3.07 + 1.15 = 6.17 kWh), because the cycle starts and ends at rest.
   - Corrected balance: 7.10 kWh gross = 6.17 traction + 0.73 motoring losses + 0.21 accessories.
   - Regeneration returns 1.03 kWh after 0.12 kWh of losses.
   - Net battery energy is 6.07 kWh, the 0.170 kWh/km of Example 10.5.
   - Figure 10.5 is redrawn as a correct energy-flow diagram.
2. **Gradeability, (10.6).** The approximation used tan θ, which gives 20.2°; the example's 21.6° follows from sin θ + C_rr cos θ = F/mg. The equation now uses the sine.
3. **Bidirectional charger sign convention, (10.15)–(10.17) and Example 10.11.**
   - The text, Figure 10.21 (right) and Figure 10.22 use "P > 0 when charging", but the dq equations were written for current flowing out to the grid.
   - All three equations are now in one consistent load convention: i_q* = +2Q*/3V_d (+12.3 A for 6 kvar), and the discharge bound is written as −P_dis.
   - The control-loop panel of Figure 10.21 is redrawn to match.
   - The rise time is restated as about 0.5 ms; the ideal first-order loop gives 0.46 ms, and the original 0.58 ms could not be reproduced.
4. **Example 10.12:** v = 0.30 − 0.118 − 0.054 = 0.128 USD/kWh (not 0.129), giving 2.66 USD for the evening. "By a factor of two" is replaced by the actual margin.
5. **Example 10.10:** the interpretation claimed a gain over a fixed 200 kW split, but at the start the two allocations are identical. The gain comes as the SUV tapers, and the text now says so.
6. **Preconditioning energy.** The pack model has 300 + 150 kJ/K, so warming it 25 K needs about 3.1 kWh, not 2 kWh. Figure 10.11, its caption and Example 10.9 are corrected.
7. **Example 10.18 (gate hub) rebuilt.** The original figure contradicted the text:
   - the "250 kW / 250 kWh" battery let grid import exceed the 300 kW threshold twice;
   - the plotted peak did not match the stated 592 kW.

   A new reproducible simulation (seed 2026, 30 sessions, 1.39 MWh) gives:
   - charging-demand peaks of 663 kW over one minute and 534 kW as a 15-minute mean;
   - a PV-net peak of 453 kW;
   - a requirement of 153 kW / 45 kWh usable to hold 300 kW, for which 200 kW / 100 kWh is chosen;
   - a saving of 3510 USD per month.

   Figure 10.29 is regenerated from this simulation.
8. **Megawatt charging.** It is now attributed to SAE J3271 (issued March 2025). The 3.75 MW, 1250 V, 3000 A figures are described as the development targets, which is how the available sources state them.

## Figures redrawn (600 dpi)

- **10.1:** the "cloud" label was misplaced and the HVAC loads were not on the bus.
- **10.4:** the free-body diagram had the car floating above the slope and arrows starting inside the body.
- **10.5:** wrong energy-flow logic and numbers.
- **10.7:** the "torque-limited" label sat on the power-limited curve.
- **10.11:** preconditioning energy.
- **10.18:** only one module was connected, from a 1.2 MVA supply for a 400 kW station.
- **10.21 (left panel):** sign convention.
- **10.29:** inconsistent with the text.
- **10.32:** text overflowed its box.

## Added

- **Introduction:** about 1160 words, ending with the learning outcomes in sentence form. Section 10.1 is renamed.
- **[Advanced] box:** consumption against cruising speed, with the closed-form optimum v* = (ηP_acc/ρC_dA_f)^(1/3). Results: 27 km/h without heating and 63 km/h with it; heating doubles town consumption but adds only 18 % on the motorway.
- **Verified research paragraph:** Muratori 2018; Tomaszewska 2019; Attia 2020; Kempton & Tomić 2005; Dubarry 2017; OCPP 2.1 / IEC 63584-210:2025; SAE J3271.
- **Exercises:** 15 merged exercises with complete solutions, replacing 32 plus the mini-project. New items include the closed-form charge time, the health-aware current limits with an uncertainty margin, the departure quantile at 5 % risk, and fault patterns from energy residuals.

## Note for the editor

- **Kempton & Tomić 2005:** the DOI is omitted because sources disagree on it; please add it from ScienceDirect.
- **Example 10.8 and 10.9 sessions, and Example 10.19:** these come from simulations whose full inputs are not all published, so I checked them for internal consistency rather than re-simulating them.
