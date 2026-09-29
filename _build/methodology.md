# BESS Benchmark – Methodology

## About this methodology

This is version 1.2 of 29 September 2026. The Independent Capacity Market B.V. ("the ICM") publishes it to explain how we calculate the BESS Benchmark and the Project Score, and how we show them to Members.

- The Methodology is part of the Terms & Conditions of the BESS Benchmark. If the two conflict, the Terms prevail.
- Capitalised terms, such as Member, Project, Project Results and Gross Revenue, have the meaning given in the Terms.
- All results are preliminary until final (see "Preliminary and final results").
- We publish every change with a new version number (see "Changes to this methodology").

## Principles

The BESS Benchmark shows what comparable batteries actually earned per MW, so a Member can see whether its own batteries earn more or less.

- **Real outcomes.** We use the revenues optimizers report for closed calendar months, plus capacity and availability. We never ask for bids, prices, trading strategies or inside information.
- **Independent.** The ICM owns no batteries and is not an optimizer. The same rules apply to every Member, whatever its optimizer.
- **Give-to-get.** A Member sees the BESS Benchmark only for the months to which it contributed data.
- **Anonymous.** We show peer data only in groups large enough that no asset, Member or optimizer can be identified. We never name optimizers or rank them.

## Real revenues, not a simulated index

| A simulated revenue index | The BESS Benchmark |
| --- | --- |
| Models a theoretical battery with fixed assumptions | Is based on realised revenues, as members received them from their optimizers |
| Assumes a full grid connection and no downtime | Anticipates restrictions such as CSC terms, TDTR limits and downtime |
| Cannot tell you how your optimizer performs comparatively | Compares your battery with batteries set up like yours |

## Scope

The BESS Benchmark covers battery energy storage (BESS) assets in the Netherlands that an optimizer trades under a merchant contract. We focus on assets of 3 to 30 MW and decide on each Project in the intake.

- **Asset.** One battery system with its own meter. The asset is the unit of calculation.
- **Project.** One or more assets at one site, as recorded in the project form. A Member can have several Projects.
- **Merchant contracts only.** Tolling and index contracts are out of scope, because their revenues do not reflect the optimizer's trading.
- **Batteries only.** We count only the revenues of the BESS assets, also at sites with solar, wind, CHP or an e-boiler.

## Data we collect

We use two sources: the project form, completed once per Project, and the monthly Project Results.

**Project form.** Per Project: context and objectives, a project diagram, project type and number of BESS assets. Per asset: name, EAN, brand, power (MW), energy (MWh), depth of discharge, estimated round-trip efficiency and state of health, connection capacity, maximum feed-in and off-take, power ceiling, transport right, congestion contract and rate, other constraints, markets, optimizer, contract type, optimizer fee, what the optimizer reports each month, system operator, energy supplier, EMS provider and metering service provider. The Member confirms that the form is complete and correct.

**Project Results, per asset and per month.**

| Item | Unit | Used for |
| --- | --- | --- |
| Gross Revenue | EUR | BESS Benchmark, Project Score, Membership Fee |
| Optimizer fee | EUR | Net view |
| Inactive hours | hours | Availability correction |

**How the data reaches us.** The Member uploads its optimizer's statements to its own Box folder, or asks its optimizer to copy bessbenchmark@icm.energy. If the optimizer contract restricts sharing, the Member and the optimizer first sign the Mandate. At the start, the Member shares at least the 6 most recent months. Amounts are in euros, excluding VAT.

## Quality control

Only figures that an ICM analyst has approved enter the BESS Benchmark. Until then, the month stays closed to the Member.

1. **Intake.** We check the project form with the Member: capacity, duration, contract type, own meter, markets and congestion contract.
2. **Every month.** We extract the amounts from each statement and check them against the document: the right month, Project and assets, and gross, fee and net adding up. We also check that the reported inactive hours are plausible.
3. **Corrections.** The Member sees the extracted amounts and can correct them. We check every correction against the statement. A corrected statement from the optimizer replaces the old one.
4. **Calculation.** Software calculates the BESS Benchmark and Project Scores with the rules below. It can flag unusual figures, but a person always decides.

## Definitions

**Revenue.**

- **Gross Revenue** is the total trading revenue in a calendar month, before the optimizer's fee. We include negative months as reported.
- **Net revenue** is Gross Revenue minus the optimizer's fee. It is a view option only.
- The 80% contact rule always uses Gross Revenue.

**Capacity.** Power in MW and energy in MWh, as in the project form.

**Duration.** Energy divided by power (MWh ÷ MW). Every asset falls in exactly one class:

| Duration class | MWh ÷ MW |
| --- | --- |
| 1-hour | up to 1.50 |
| 2-hour | above 1.50, up to 2.50 |
| 4-hour | above 2.50 |

The 1-hour and 2-hour classes follow the duration clusters in enspired's [portfolio performance reporting](https://www.enspired-trading.com/portfolio-performance). Like enspired, we keep assets above 2.50 hours out of the 2-hour class. We place them in the 4-hour class, so every battery is included.

**Project type.** Stand-alone: a site with only BESS. Co-located: BESS at a site with solar, wind, CHP or an e-boiler.

**Markets.** We group the markets an asset is active in. An asset counts in a group if it is active in at least one of its products.

| Market group | Products |
| --- | --- |
| Wholesale markets | Day-ahead, intraday, imbalance |
| Ancillary services | FCR, aFRR, mFRR |
| Congestion markets | Redispatch |

**Congestion contract.** None, CSC or CBC/CLC, as in the project form.

**Grid restrictions.** Restrictions from the transport right or a congestion contract (such as TDTR, TBTR, CSC or CBC) are part of the asset's set-up. They do not count as inactive hours.

## Availability

We correct for downtime per hour, so maintenance or a malfunction does not lower an asset's revenue per MW.

- An **inactive hour** is a clock hour in which the optimizer could not trade the asset, because of maintenance, a malfunction or a grid outage.
- **Active hours** are the hours in the month minus the inactive hours. Revenue from the active hours of a partly inactive day counts in full.
- We divide revenue by MW × active hours, never by MW × all hours.
- Reduced power (derating) and grid restrictions count as active hours.
- The Member reports inactive hours with the Project Results, backed by the optimizer's or EMS provider's records where available. If none are reported, all hours count as active.
- A month with zero active hours is left out for that asset.

## Missing data

We use incomplete data as far as it goes and never guess.

| Situation | In the BESS Benchmark | In the Member's own figures |
| --- | --- | --- |
| Results only for the Project as a whole | The Project counts as one unit. It enters a filtered view only if all its assets meet the filter; otherwise only views where the filter is "All". | Project Score shown; asset scores show "No asset data". |
| A characteristic is unknown | Included only where that filter is "All". | Not affected. |
| Optimizer fee unknown | Left out of the Net view. | Net figures not shown. |
| Inactive hours not reported | All hours count as active. | Same. |
| No results for a month | Not included that month. | No access to that month ("No invoice"). |

A Project reported as a whole counts as one asset towards the minimum group size. We do not split its revenue across assets.

## Calculating the BESS Benchmark

The BESS Benchmark for a month is the total Gross Revenue of all peer assets divided by their total capacity-hours, in EUR per MW per year. Larger assets weigh more, in proportion to their MW.

```latex
B_m = \frac{\sum_{i \in P} R_{i,m}}{\sum_{i \in P} MW_i \cdot H_{i,m}} \cdot 8760
```

- B = BESS Benchmark for month m, in EUR per MW per year.
- P = the peer set: all assets that match the selected filters and have results for month m.
- R = Gross Revenue of asset i in month m (net revenue in the Net view).
- MW = power of asset i; H = its active hours in month m; 8,760 = hours in a year.

**Periods.** Members can view months, calendar quarters or calendar years, over the last 6 months, the last 12 months (default) or the full timeline. The current year shows as year to date. For any period longer than a month, we add up revenue and capacity-hours first and divide once. We never average monthly figures.

**Peer set.** By default, the peer set leaves out the Project being viewed; the Member can choose to include it. The Member's other Projects are part of the peer set, but never count towards the minimum group size.

**Group size.** Every BESS Benchmark shows its number of assets and organisations for the latest period shown.

## Calculating the Project Score

The Project Score is the Project's revenue per MW per year divided by the BESS Benchmark over exactly the same months. Above 100% means the Project earned more per MW than its peers.

```latex
\text{Score}_T = \frac{\sum_{m \in T} \sum_{i \in A} R_{i,m} \;/\; \sum_{m \in T} \sum_{i \in A} MW_i \cdot H_{i,m}}{\sum_{m \in T} \sum_{j \in P_m} R_{j,m} \;/\; \sum_{m \in T} \sum_{j \in P_m} MW_j \cdot H_{j,m}} \times 100\%
```

- A = the assets of the Project (or one asset, for an asset score).
- T = the months in the period with both Project Results and a published BESS Benchmark.
- The Project figure is weighted by MW. Project revenue in euros always equals the sum of its assets.

**Rounding.** We divide by the unrounded BESS Benchmark and show one decimal. The band follows the shown value: 99.98% shows as 100.0% and falls in the band "100% to 115%".

| Band | Project Score |
| --- | --- |
| Below 80% of benchmark | below 80% |
| 80% to 100% of benchmark | 80% up to 100% |
| 100% to 115% of benchmark | 100% up to 115% |
| 115% and above of benchmark | 115% and above |

The chart marks every month (or quarter or year) in which the Project Score was below 80%.

**Summary figures.** Above the chart, the Member sees the Project's revenue per MW per year, its difference with the BESS Benchmark (per MW and per year for the whole Project) and its Project Score. These follow the selected filters and period; the default period is the last 12 months.

**Example (fictional).** A 10 MW asset earns EUR 150,000 in a 31-day month (744 hours) with 20 inactive hours: 150,000 ÷ (10 × 724) × 8,760 = EUR 181,492 per MW per year. Against a BESS Benchmark of EUR 200,000, its score is 90.7%, in the band "80% to 100%".

**When we reach out.** The ICM may contact a Member if a Project scored below 80% in at least 6 of the last 12 months (article 7.3 of the Terms). For this rule we always use the same view: all durations, Gross Revenue, all peers, without the Project itself.

## Filters

Filters narrow the peer set to assets with a similar set-up. They apply to the peers, not to the Member's own figures.

| Filter | Options | Rule |
| --- | --- | --- |
| Duration | All assets, plus the Member's own duration classes | "All assets" includes every duration class. Members see only their own classes (give-to-get). A Project with assets in several classes sees only "All assets". |
| Revenue | Gross, Net | Default: Gross. |
| Project type | All assets, Stand-alone, Co-located | Default: All assets. |
| Markets | Wholesale markets, Ancillary services, Congestion markets | Nothing selected means all. Several selected means peers active in all of them. |
| Congestion contract | All, CSC or CBC/CLC, None | Default: All. |
| Optimizer | All optimizers, Same optimizer as this Project, Other optimizers | Default: All optimizers. We take the optimizer from each month's statement, so a switch counts from the month it happens. |
| Benchmark | Excluding or including the Project itself | Default: excluding. |

If a selection does not meet the thresholds below, we show no BESS Benchmark for it.

## Anonymity

We show a BESS Benchmark only if it includes at least 5 assets from at least 3 organisations other than the viewing Member.

- **Anonymization.** Before data enters the BESS Benchmark, we remove the Member's name, asset name, EAN and location. We keep the optimizer only to apply the optimizer filter and never show it.
- **No subtraction.** Comparing two selections could reveal a small group of assets. We therefore also hide a selection whose peers differ from another visible selection by 1 to 4 assets or 1 to 2 organisations. The hidden selection stays the same between visits.
- **Corrections.** When one result is corrected, we do not show the change per selection.
- **No optimizer results.** We never show results per named optimizer or rank optimizers. The optimizer filter only compares the Member's own optimizer with all others, within the same group size rules.
- **Reports.** A Member can print its results as a report: its own figures, the BESS Benchmark, the filters and period, and which months are preliminary. It never contains asset data of other organisations.

## Access

A Member sees the BESS Benchmark for a month only if it shared results for at least one of its Projects for that month.

- The months shared at the start count, so a new Member sees at least 6 months.
- A Project or asset score appears only for months with results for that Project or asset. Otherwise the month shows "No invoice".
- Late results open the month once we have received and checked them.
- Access is per organisation: all the Member's users see the same months.

## Preliminary and final results

Every result is preliminary. A month becomes final once no correction has come in for 3 months after its end.

- **Late data.** Results that arrive after a month is first shown are added to that month. This can change the BESS Benchmark and every Project Score for that month.
- **Corrections.** When an optimizer corrects a statement, we replace the figures and recalculate the months affected. The Membership Fee follows the corrected Gross Revenue.
- **Marking.** Preliminary months carry a "Preliminary" tag on screen and in reports.
- **Final months.** We change a final month only to correct a clear error, and log the change.

## Changes to this methodology

We publish every change on icm.energy with a new version number and date, and inform Members by email. Article 1.6 of the Terms applies.

- After a change, we recalculate past months under the new rules where the data allows. Months we cannot recalculate are marked as not comparable.
- For material changes, we show the effect on the BESS Benchmark, separating a change in method from a change in the peer group.

| Version | Date | Change |
| --- | --- | --- |
| 1.2 | 29 September 2026 | Duration classes cover every battery (above 2.50 hours counts as 4-hour); optimizer filter; bands and periods as in the app; co-located defined by other asset types at the site; shorter, plainer text |
| 1.1 | 29 September 2026 | Markets in three groups; congestion contract as none, CSC or CBC/CLC; quarters and years; summary figures follow the filters; fixed view for the 80% contact rule |
| 1.0 | 28 September 2026 | First published version |

## Limitations

The BESS Benchmark shows what comparable assets earned. It does not explain why, and it is not advice.

- **Set-up or optimizer.** A score reflects both the asset's set-up (brand, connection, grid restrictions, state of health) and the optimizer's trading. Filters reduce set-up differences but do not remove them.
- **Small groups.** In the first months, peer groups are small and may not represent the market.
- **Who joins first.** Early Members may be owners who doubt their optimizer, so early BESS Benchmarks may be lower than the market.
- **Changing peers.** Assets join and leave. A change in the BESS Benchmark can come from the peer group rather than the market.
- **Reported data.** We check every statement, but we cannot verify the optimizer's settlement.
- **Past only.** Results describe closed months. They do not predict future revenue.

## Glossary

| Term | Meaning |
| --- | --- |
| aFRR / mFRR | Automatic / manual frequency restoration reserve: balancing services TenneT buys |
| ATO | Aansluit- en transportovereenkomst: connection and transport agreement with the system operator, firm or non-firm |
| BESS | Battery energy storage system |
| CBC / CLC | Capaciteitsbeperkingscontract (capacity limiting contract): the connected party limits its use of capacity |
| CSC | Capaciteitssturingscontract: the system operator can ask the connected party to limit or increase its use of capacity |
| DoD | Depth of discharge: the share of energy capacity that is used |
| EAN | Code that identifies a grid connection |
| EMS | Energy management system that controls the asset on site |
| FCR | Frequency containment reserve |
| MW / MWh | Power / energy capacity of an asset |
| Redispatch | Congestion management through bids on GOPACS, at a system operator's request |
| RTE | Round-trip efficiency: energy out as a share of energy in |
| SoH | State of health: remaining capacity of a battery compared with new |
| TBTR | Tijdsblokgebonden transportrecht: transport right limited to fixed time blocks |
| TDTR | Tijdsduurgebonden transportrecht: transport right limited to a maximum duration |
| YTD | Year to date: from 1 January to the latest month with data |
