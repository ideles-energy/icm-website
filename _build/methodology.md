# BESS Benchmark – Methodology

## Status of this document

This is Methodology version 1.1 of 29 September 2026, published by Independent Capacity Market B.V. ("the ICM"). It describes how the ICM calculates the BESS Benchmark and the Project Score, and how both are shown to Members.

- The Methodology forms part of the Terms & Conditions – BESS Benchmark (version 0.9, 27 September 2026). In case of conflict, the Terms prevail.
- Capitalised terms (Member, Project, Project Results, Gross Revenue, Benchmark, Project Score, Onboarding Month, Historical Month, New Month) have the meaning given in the Terms.
- All Benchmarks and Project Scores are preliminary until final under section "Preliminary results, corrections and final results".
- Changes are published with a new version number and date; see "Changes to this methodology".

## Purpose and principles

The BESS Benchmark shows how much comparable battery storage assets actually earned per MW, so a Member can see whether its own assets earn more or less. It compares real revenues of real assets, not a simulated battery with fixed assumptions.

- **Real outcome data.** We use realised revenues as reported by the Optimizer for closed calendar months, plus capacity and availability. We do not request, process or display bids, prices, trading or dispatch logic, or inside information.
- **Independent.** The ICM does not own BESS assets and is not an optimizer, nor does it intend to become either. The same rules apply to every Member, whatever its Optimizer.
- **Give-to-get.** A Member sees the Benchmark only for months for which it provided Project Results.
- **Anonymous.** Peer data is shown only in groups large enough that no single asset, Member or Optimizer can be identified. We never publish results per optimizer or rankings of optimizers.
- **Transparent.** This document sets out every rule that determines a Benchmark or a Project Score.

## Why real revenues, not a simulated index

The BESS Benchmark compares what batteries actually earned. A simulated index models what a theoretical battery could have earned.

| A simulated revenue index | The BESS Benchmark |
| --- | --- |
| Models a theoretical battery with fixed assumptions | Is based on realised revenues, as members received them from their optimizers |
| Assumes a full grid connection and no downtime | Anticipates restrictions such as CSC terms, TDTR limits and downtime |
| Cannot tell you how your optimizer performs comparatively | Compares your battery with batteries set up like yours |

## Scope

The Benchmark covers battery energy storage (BESS) assets in the Netherlands that an Optimizer trades under a merchant contract. Our focus is assets of 3 to 30 MW; the ICM decides on each Project in the intake meeting.

- **Asset.** One battery system with its own meter, not shared with another asset. The asset is the unit of calculation.
- **Project.** A stand-alone asset, or a co-located group of assets, as recorded in the project form. A Member can have several Projects.
- **Contract type.** Merchant contracts only. Tolling and index contracts are not part of the Benchmark, because their revenues do not reflect the Optimizer's trading result.
- **Other asset types.** PV, wind, CHP and e-boilers at the same site are not included. Only BESS assets can be added to a Project.

## Data we collect

We use two sources: the project form, completed once per Project, and the monthly Project Results from the Optimizer.

**Project form (per asset).** Asset name, EAN, capacity (MW), energy capacity (MWh), brand, transport right, Optimizer, markets the asset is active in (wholesale markets, ancillary services, congestion markets), system operator and congestion contract (none, CSC, CBC/CLC). Optional: optimizer fee, estimated state of health, round-trip efficiency, power ceiling, connection capacity, EMS provider, metering service provider and energy supplier. The Member confirms the form is complete and accurate.

**Project Results (per asset, per calendar month).**

| Item | Unit | Use |
| --- | --- | --- |
| Gross Revenue | EUR | Benchmark, Project Score, Membership Fee |
| Optimizer fee | EUR | Net view only |
| Inactive hours | hours | Availability correction |

**How Project Results reach us.** The Member uploads them to its dedicated Box folder, or asks its Optimizer to copy bessbenchmark@icm.energy. If the optimizer contract restricts sharing, the Member and the Optimizer first sign the Mandate. At registration, the Member provides at least the 6 most recent Historical Months.

**Extraction and checks.** Amounts are in euros, excluding VAT. The Member sees the extracted amounts in app.icm.energy and can correct them. How we check the data is set out under "Quality control".

## Quality control

No figure enters the Benchmark without approval by an ICM employee. Software may read documents and flag anomalies, but a person always decides.

| Step | Who | What is checked |
| --- | --- | --- |
| Project form | ICM employee, in the intake meeting | Capacity (MW, MWh), duration class, contract type, own meter, markets, congestion contract |
| Project Results | ICM employee, every month | Amounts match the document; month, Project and assets are right; gross, fee and net add up |
| Inactive hours | ICM employee, every month | The reported hours are plausible and consistent with the Project Results |
| Corrections by the Member | ICM employee | The correction matches the Raw Data |
| Corrections by the Optimizer | ICM employee | The new document replaces the old one; affected months are recalculated |
| Calculation and publication | Automated | Benchmark, Project Scores, thresholds and hidden selections follow the rules in this document |

**Anomaly flags.** Before approval, a result is flagged for a second look if it differs strongly from the asset's own history or from its peers, if revenue is negative, or if more than 10% of the month's hours are inactive. A flagged result is only approved once explained.

**Pending results.** Until approved, Project Results are not part of any Benchmark, and the month is not yet open to the Member.

## Definitions and classification

We classify assets on measured characteristics, not on labels, so that like is compared with like.

**Revenue.**

- **Gross Revenue**: total trading revenue in a calendar month as stated in the Project Results, before the Optimizer's fee. Negative months are included in the Benchmark as reported.
- **Net revenue**: Gross Revenue minus the Optimizer's fee for that month.
- The 80% contact rule always uses Gross Revenue. Net revenue is a view option only.

**Capacity.** Power in MW and energy in MWh as recorded in the project form.

**Duration.** Energy capacity divided by power (MWh ÷ MW), classified into bands:

| Duration class | MWh ÷ MW |
| --- | --- |
| 1-hour | 0.90 – 1.50 |
| 2-hour | 1.51 – 2.50 |
| 4-hour | 3.50 – 4.50 |
| Other | all other values |

Assets classified as "Other" are not included in any Benchmark.

**Project type.** Stand-alone (one asset) or co-located (several assets in one Project).

**Markets.** The market groups an asset is active in, as recorded in the project form. An asset counts as active in a group if it is active in at least one product of that group.

| Market group | Products |
| --- | --- |
| Wholesale markets | Day-ahead, intraday, imbalance |
| Ancillary services | FCR, aFRR, mFRR |
| Congestion markets | Redispatch |

**Congestion contract.** None, CSC or CBC/CLC, as recorded in the project form. Grid restrictions that follow from the connection or transport right (such as TDTR, TBTR, CSC or CBC) are characteristics of the asset. They do not count as inactive hours.

## Availability: active hours

We correct for downtime per hour, so an asset is not penalised for maintenance or a malfunction and its revenue per MW stays comparable.

- **Inactive hour**: a clock hour in which the asset was not available to the Optimizer for trading, due to maintenance, a malfunction or a grid outage.
- **Active hours** = hours in the calendar month − inactive hours. Revenue earned in the active hours of a partly inactive day counts in full.
- Numerator and denominator use the same active hours: revenue is divided by MW × active hours, never by MW × all hours in the month.
- Reduced power (derating) and contractual grid restrictions count as active hours.
- The Member reports inactive hours with the Project Results, backed by the Optimizer's or EMS provider's records where available. Without a report, all hours count as active.
- A month with zero active hours is left out of the calculation for that asset.

## Missing and incomplete data

Incomplete data is used as far as it goes and is never guessed. A Project or asset counts only in selections where its known characteristics are certain to meet the filter.

| Situation | In the Benchmark | Member's own figures |
| --- | --- | --- |
| Project Results only for the Project as a whole, not per asset | The Project counts as one unit. It is included in a filtered selection only if all its assets meet that filter (for example, all 2-hour, or all with a CSC). Otherwise it counts only where that filter is set to "All". | Project Score shown; asset scores show "No asset data". |
| A characteristic is unknown (for example the congestion contract) | Included only where that filter is set to "All". | Not affected. |
| Optimizer fee unknown | Excluded from the Net Benchmark only. | Net figures not shown. |
| Inactive hours not reported | All hours count as active. | Same rule. |
| No Project Results for a month | Not included for that month. | No access to that month; "No invoice". |

**Counting towards thresholds.** A Project reported as a whole counts as one asset for the minimum of 5 assets, whatever the number of assets inside it. We do not split its revenue across assets.

## Calculating the Benchmark

The Benchmark for a month is the total Gross Revenue of all peer assets divided by their total capacity-hours, expressed in EUR per MW per year. Larger assets therefore weigh more, in proportion to their MW.

```latex
B_m = \frac{\sum_{i \in P} R_{i,m}}{\sum_{i \in P} MW_i \cdot H_{i,m}} \cdot 8760
```

- B = Benchmark for month m, in EUR/MW/year.
- P = the peer set: all assets that meet the selected filters and have Project Results for month m.
- R = Gross Revenue of asset i in month m (or net revenue in the Net view).
- MW = power of asset i; H = its active hours in month m; 8,760 = hours in a year.

**Quarters and years.** Members can view months, calendar quarters (for example "Q3 2026") or calendar years; the current year is shown as year-to-date (for example "2026 YTD (Jan–Sep)"). For a quarter, a year or any other period of several months, we add up revenue and capacity-hours over all months first and divide once. We do not average monthly Benchmarks.

**Peer set.** By default the peer set excludes the Project being viewed; the Member can choose to include it. The Member's other Projects are part of the peer set, but they never count towards the minimum group size, which counts only assets of other organisations.

**Group size shown.** Every Benchmark states its number of assets and organisations for the most recent period shown.

**Net view.** A peer whose optimizer fee is unknown is left out of the Net Benchmark. The Net view shows its own asset and organisation counts.

## Calculating the Project Score

The Project Score is the Project's own revenue per MW per year divided by the Benchmark over exactly the same months. A score above 100% means the Project earned more per MW than its peers; below 100%, less.

```latex
\text{Score}_T = \frac{\sum_{m \in T} \sum_{i \in A} R_{i,m} \;/\; \sum_{m \in T} \sum_{i \in A} MW_i \cdot H_{i,m}}{\sum_{m \in T} \sum_{j \in P_m} R_{j,m} \;/\; \sum_{m \in T} \sum_{j \in P_m} MW_j \cdot H_{j,m}} \times 100\%
```

- A = the assets of the Project (or a single asset, for an asset score).
- T = the months in the period for which the Project has Project Results and a Benchmark is published. Months without Project Results are left out of both numerator and denominator.
- The Project figure is MW-weighted across its assets. Project revenue in EUR always equals the sum of its assets' revenue.

**Difference with the Benchmark.** For each period we also show the Project's revenue per MW per year minus the Benchmark, in EUR per MW per year.

**Rounding.** We divide by the unrounded Benchmark and show the score with one decimal. The score band follows the displayed value: 99.98% displays as 100.0% and falls in "Above benchmark".

**Score bands.**

| Band | Project Score |
| --- | --- |
| Below benchmark | below 80% |
| Near benchmark | 80% to below 100% |
| Above benchmark | 100% to below 115% |
| Well above benchmark | 115% and above |

**Summary figures.** Above the chart, the Member sees the Project's revenue per MW per year, its difference with the Benchmark (per MW and for the whole Project per year) and its Project Score. These figures follow the selected filters and period (last 6 months, last 12 months, the full timeline, or a period the Member selects), so the Member chooses which comparison to judge. The default period is the last 12 months. The difference per year equals the rounded difference per MW × the Project's MW.

**Worked example (fictional).** A 10 MW asset earns EUR 150,000 gross in a 31-day month (744 hours) with 20 inactive hours. It earns 150,000 ÷ (10 × 724) × 8,760 = EUR 181,492 per MW per year. With a Benchmark of EUR 200,000 per MW per year, its score is 90.7%: Near benchmark.

**Contact under article 7.3 of the Terms.** The ICM may contact a Member if a Project's score was below 80% in at least 6 of the last 12 calendar months. For this rule the ICM always uses the same fixed Benchmark, independent of any filter a Member selects: all durations, Gross Revenue, all peers, excluding the Project itself.

## Filters

Filters narrow the peer set so a Member can compare its Project with assets of a similar set-up. Each filter applies to the peer assets, not to the Member's own figures.

| Filter | Options | Rule |
| --- | --- | --- |
| Duration | All assets, plus the duration classes of the Member's own assets | "All assets" includes all 1-, 2- and 4-hour assets. Only the Member's own duration classes are offered (give-to-get). Default: All assets. |
| Revenue | Gross · Net | Net = after the Optimizer's fee. Default: Gross. |
| Project type | All assets · Stand-alone · Co-located | Default: All assets. |
| Markets | Wholesale markets · Ancillary services · Congestion markets | None selected = all markets. Several selected = peers active in all selected groups. |
| Congestion contract | All · CSC or CBC/CLC · None | Default: All. |
| Benchmark | Excluding Project [name] · Including Project [name] | Default: excluding. |

There is no filter by optimizer. If a filter combination does not meet the thresholds in the next section, no Benchmark is shown for that selection.

## Anonymity and publication thresholds

A Benchmark is shown only if it includes at least 5 assets from at least 3 organisations other than the viewing Member. Below that, the page shows "No benchmark for this selection".

- **Anonymisation.** Before data enters the benchmark dataset, we remove the Member's name, asset name, EAN, location and Optimizer.
- **Protection against subtraction.** Comparing two filter selections could reveal a small group of assets. We therefore also hide a selection whose peer set differs from another visible selection, for the same Member, month and duration, by 1 to 4 assets or 1 to 2 organisations. Which selection is hidden is fixed, so it does not change between visits.
- **Corrections.** When a single Project Result is corrected, we do not show the before-and-after change per selection.
- **No optimizer results.** We never show results per optimizer or rankings of optimizers.
- **Reports.** A Member can print its results as a report. The report contains its own figures, the Benchmark, the selected filters and period, and which months are preliminary. It never contains asset-level data of other organisations.

## Access: give-to-get

A Member sees the Benchmark for a calendar month only if it provided Project Results for at least one of its Projects for that month.

- Historical Months provided at registration count, so a new Member sees at least 6 months from the start.
- A Project Score or asset score for a month appears only for Projects and assets with Project Results for that month. Otherwise the month shows "No invoice".
- If Project Results arrive late, access to that month opens once they are received and checked.
- Access is per organisation: the Member's employees with an account on app.icm.energy see the same months.

## Preliminary results, corrections and final results

Every Benchmark and Project Score is preliminary. A month becomes final once no correction has been received for 3 months after the end of that month.

- **Late data.** Project Results received after a month is first published are added to that month's Benchmark. This can change the Benchmark and every Project Score for that month.
- **Corrections.** If an Optimizer corrects Project Results, we replace the old figures and recalculate the Benchmark and Project Scores for the months affected. The Membership Fee is adjusted to the corrected Gross Revenue.
- **Marking.** Preliminary months carry a "Preliminary" tag in the app and in reports.
- **After a month is final.** We only change a final month to correct a clear error, and we record the change in the changelog. Final results are not a warranty of accuracy.

## Changes to this methodology

We publish every change with a new version number and date on app.icm.energy and icm.energy, and inform Members by email. Article 1.6 of the Terms applies.

- **Recalculation.** After a change, we recalculate all past months under the new version, so every period shown uses the same rules.
- **Comparability.** If past months cannot be recalculated, we mark them as not comparable.
- **Effect.** For material changes we state the effect on the Benchmark, separating a change in method from a change in the peer group.

| Version | Date | Change |
| --- | --- | --- |
| 1.1 | 29 September 2026 | Markets in three groups; congestion contract as none, CSC or CBC/CLC; quarters and years; summary figures follow the filters; fixed Benchmark for the 80% contact rule; Member's other Projects in the peer set; section on real revenues versus a simulated index |
| 1.0 | 28 September 2026 | First published version |

## Limitations

The Benchmark shows what comparable assets earned; it does not explain why, and it is not advice.

- **Set-up versus optimizer.** A score reflects both the asset's set-up (brand, connection, grid restrictions, state of health) and the Optimizer's trading. Filters reduce but do not remove differences in set-up.
- **Group size.** In the first months the peer group is small. A Benchmark may then not be representative of the market.
- **Who joins first.** Early Members may well be owners who doubt their optimizer. The first Benchmarks can therefore be lower than the market as a whole.
- **Changing peer group.** Assets join and leave. A change in the Benchmark can come from a different peer group rather than from the market.
- **Reported data.** We rely on Project Results and inactive hours as reported. We check extraction, but cannot verify the Optimizer's settlement.
- **Outcome data only.** Figures describe closed months. They do not predict future revenue.

## Glossary

| Term | Meaning |
| --- | --- |
| aFRR / mFRR | Automatic / manual frequency restoration reserve, balancing services procured by TenneT |
| ATO | Aansluit- en transportovereenkomst: connection and transport agreement with the system operator, firm or non-firm |
| BESS | Battery energy storage system |
| CBC / CLC | Capaciteitsbeperkingscontract (capacity limiting contract): congestion contract under which the connected party limits its use of capacity |
| CSC | Capaciteitssturingscontract: congestion contract under which the system operator can ask to limit or increase use of capacity |
| EAN | Unique code identifying a grid connection |
| EMS | Energy management system that controls the asset on site |
| FCR | Frequency containment reserve |
| MW / MWh | Power / energy capacity of an asset |
| Redispatch | Congestion management through bids on GOPACS, at the request of a system operator |
| SoH | State of health: remaining capacity of a battery relative to new |
| TBTR | Tijdsblokgebonden transportrecht: transport right limited to fixed time blocks |
| TDTR | Tijdsduurgebonden transportrecht: transport right limited to a maximum duration |
| YTD | Year to date: from 1 January up to the latest month with data |
