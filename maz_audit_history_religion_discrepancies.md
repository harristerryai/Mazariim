# Mazariim — History & Religion Audit: Discrepancies, Contradictions, and Inconsistencies

**Scope:** All files in `/history/` and `/religion/`, cross-checked against `/lore/maz_society_1overview.md` (calendar section).
**Audit Date:** 2026-03-04
**Canonical Hierarchy Used:** When sources conflict, the following priority was applied:
1. `maz_history_timeline.md` (chronological anchor) — except where specifically overridden below
2. `maz_religion_1overview_origins.md` (entity awakening/arrival records)
3. Individual deity files (deep canon for each entity)
4. Overview/narrative files (secondary)

---

## SECTION 1 — CRITICAL CONTRADICTIONS

These are direct factual conflicts between two or more sources on the same specific claim.

---

### 1.1 Minerva's War Sacrifice — Seven vs. Twelve+
| Source | Claim |
|--------|-------|
| `maz_history_1overview.md` | Minerva divided her essence among **the Seven Artharans** (seven leaders of the elven nations) |
| `maz_religion_minerva.md` | "It sent a portion of its avatar to each of the **seven leaders** of the elven nations" |
| `maz_history_timeline.md` | Confirms Seven Artharans |
| `maz_history_thewar.md` | "Minerva would sacrifice its avatar to divide its power among **more than a dozen** elven archmages, hierophants, and archdruids" |

**Verdict:** `maz_history_thewar.md` is the outlier. Three sources confirm seven. Fix: change "more than a dozen" in `maz_history_thewar.md` to "seven."

---

### 1.2 Asti's Awakening Date — ~12,000 BW vs. ~20,000 BW
| Source | Claim |
|--------|-------|
| `maz_history_timeline.md` | "~12,000 BW — Asti Awakens" (also in Old Gods table) |
| `maz_history_narrative.md` | "Around 12,000 BW, a seventh Old God awakened" (Asti) |
| `maz_religion_asti.md` | "approximately **20,000 years** before the War" |
| `maz_religion_1overview_origins.md` | "~**20,000 BW**" |
| `maz_history_humans.md` | "~**20,000 BW** — The Awakening of Asti" |
| `maz_history_nations.md` | "~**20,000 BW**: Asti awakens" |
| `maz_religion_entities.md` | "born of pure energy around a white hole approximately **20,000 years** before the Great War. She **settled on Mazariim** around 12,000 years ago" |

**Verdict:** The entities.md file clarifies the distinction: Asti was *born/awakened* ~20,000 BW but *settled on Mazariim* ~12,000 BW. The timeline and narrative confuse these two events — they both say "Asti awakens" at ~12,000 BW when they should say "Asti settles on Mazariim." Fix: correct `maz_history_timeline.md` (~12,000 BW entry label and Old Gods table) and `maz_history_narrative.md` to say "Asti settles on Mazariim" and add a ~20,000 BW entry for her awakening.

---

### 1.3 Guzon — Native Awakening vs. Immigrant from Another Plane
| Source | Claim |
|--------|-------|
| `maz_history_timeline.md` Appendix A | Lists Guzon under "Era of Awakening Entities" as "**arrived from another plane**" |
| `maz_religion_1overview_origins.md` | Guzon listed as **native awakening** in summary table |
| `maz_religion_guzon.md` | "emerged approximately **5,000 BW**" from gnomish philosophical consciousness (native) |

**Verdict:** Two sources say native; the timeline Appendix A says immigrant. Fix: correct the Appendix A entry for Guzon to "native awakening." The date discrepancy (~5,000 BW in the Guzon file vs. ~3,200 BW everywhere else) is addressed in Section 2.

---

### 1.4 Ry'le — Awakened in 811–815 AW vs. ~2,800 BW
| Source | Claim |
|--------|-------|
| `maz_religion_ryle.md` header | "Power Level: Greater Entity (**Recently Born**)" |
| `maz_religion_ryle.md` opening | "awakened from eons of slumber…drawn to consciousness by planar disturbances in **811–815 AW**" |
| `maz_history_timeline.md` | "~**2,800 BW** — Ry'le Awakens in the Far Realm" |
| `maz_religion_1overview_origins.md` | "awakened ~**2,800 BW**"; first contact with Mazariim "820–824 AW" |
| `maz_history_nations.md` | "~**2,800 BW**: Ry'le awakens (Far Realm)" and "820 AW: Ry'le makes first contact" |
| `maz_society_1overview.md` holiday section | "Ry'le is a recently born entity (**awakened circa 102 AW**)" |

**Verdict:** The Ry'le deity file and the society overview holiday section both incorrectly describe Ry'le as recently born and awakened in the AW era. All primary chronological sources agree: Ry'le awakened ~2,800 BW but made *first contact with Mazariim* in 820 AW. Fix: correct `maz_religion_ryle.md` to remove "Recently Born" and fix the opening paragraph to say he awakened ~2,800 BW and made first contact in 820 AW. Also fix the "circa 102 AW" note in `maz_society_1overview.md`.

---

### 1.5 Ashura & Khan Awakening Date — ~2,900 BW vs. ~3,100 BW
| Source | Claim |
|--------|-------|
| `maz_history_timeline.md` | "~**2,900 BW** — Ashura and Khan Awaken" |
| `maz_religion_ashura.md` | "~**3,100 BW**" |
| `maz_religion_khan.md` | "~**3,100 BW**" |
| `maz_religion_1overview_origins.md` | "~**3,100 BW**" |

**Verdict:** Timeline is the outlier. Three sources confirm ~3,100 BW. Fix: correct the timeline entry from ~2,900 BW to ~3,100 BW.

---

### 1.6 Alagalothor's Plane — Astral Plane vs. Far Realm
| Source | Claim |
|--------|-------|
| `maz_history_timeline.md` 1,492 BW narrative entry | Alagalothor "settles in **Far Realm**" |
| `maz_history_timeline.md` Appendix A (Immigrant Entities table) | "**Astral Plane**" for Alagalothor |
| `maz_religion_1overview.md` (Entities by Plane table) | Alagalothor in "**Astral Plane**" |
| `maz_religion_1overview_origins.md` | "Merged with **Astral Plane**" |
| `maz_religion_alagalothor.md` | "Dominion: Astral Plane" |
| `maz_religion_entities.md` | "Dominion: Astral Plane" |

**Verdict:** The timeline's narrative entry at 1,492 BW says "Far Realm" — this contradicts every other source. Fix: change "settles in Far Realm" to "settles in Astral Plane" in the 1,492 BW narrative entry.

---

### 1.7 Zuel's Plane — Abaddon vs. Abyss
| Source | Claim |
|--------|-------|
| `maz_religion_1overview.md` (Entities by Plane table) | Zuel in "**Abaddon**" (NE alignment) |
| `maz_religion_1overview_origins.md` | "Zuel merged with the **Abyss**" |
| `maz_religion_zuel.md` | "Dominion: Abaddon (Plane of Endless War)" |

**Verdict:** Origins doc says Abyss; all other sources (overview table, individual file) say Abaddon. Fix: correct `maz_religion_1overview_origins.md` from "Abyss" to "Abaddon."

---

### 1.8 Asti's Plane — Not Listed vs. Positive Energy Plane
| Source | Claim |
|--------|-------|
| `maz_history_timeline.md` Appendix A (Old Gods table) | Asti: "**—**" (no plane created) |
| `maz_religion_1overview.md` (Entities by Plane table) | Asti at "**Positive Energy Plane**" |
| `maz_religion_asti.md` | "Dominion: Positive Energy Plane" |
| `maz_religion_1overview_origins.md` | "Plane Created: **Positive Energy Plane**" |
| `maz_religion_entities.md` | "Dominion: Positive Energy Plane" |

**Verdict:** Timeline Appendix A is wrong — it has no plane for Asti. Four sources confirm Positive Energy Plane. Fix: update the Old Gods table in the timeline to show "Positive Energy Plane" for Asti.

---

### 1.9 Tiovin — Symbol, Favored Weapon, and Alignment Conflict Between Files
| Source | Symbol | Favored Weapon | Alignment |
|--------|--------|----------------|-----------|
| `maz_religion_tiovin.md` | Two hands held in supplication | Scimitar | LG |
| `maz_religion_entities.md` | White crown with golden rays | Longsword | G |

**Verdict:** Three separate contradictions in a single comparison. The individual deity file (`maz_religion_tiovin.md`) is the detailed canonical source. Fix: update `maz_religion_entities.md` to match: symbol = "two hands held in supplication," favored weapon = scimitar, alignment = LG.

---

### 1.10 Sheeva — Alignment NE vs. CE
| Source | Claim |
|--------|-------|
| `maz_religion_entities.md` | Sheeva alignment: "**CE**" |
| `maz_religion_1overview.md` (entity table) | Sheeva alignment: "**NE**" |
| `maz_religion_sheeva.md` | Alignment: "**NE**" |

**Verdict:** Two sources say NE; `maz_religion_entities.md` says CE. Fix: correct `maz_religion_entities.md` to NE.

---

### 1.11 Polyvin — Alignment N vs. NG
| Source | Claim |
|--------|-------|
| `maz_religion_entities.md` | Polyvin alignment: "**N**" (True Neutral) |
| `maz_religion_polyvin.md` | Alignment: "**NG**" (Neutral Good) |
| `maz_religion_1overview.md` (entity table) | Should be verified |

**Verdict:** Individual deity file says NG. Fix: correct `maz_religion_entities.md` to NG.

---

### 1.12 Asti's Origin — White Hole vs. Cosmic Merger
| Source | Claim |
|--------|-------|
| `maz_religion_asti.md` | "born of pure energy around a **white hole** approximately 20,000 years before the War" |
| `maz_religion_entities.md` | "born of pure energy around a **white hole** approximately 20,000 years before the Great War" |
| `maz_history_narrative.md` | Asti "emerged from the **cosmic merger that had created this universe** billions of years earlier" — then says she awakened ~12,000 BW |

**Verdict:** The narrative file gives a completely different origin (cosmic merger, billions of years ago) compared to the established white hole origin (~20,000 BW). The narrative file also contradicts the established awakening date. Fix: revise the Asti section in `maz_history_narrative.md` to align with the white hole origin at ~20,000 BW with settlement on Mazariim ~12,000 BW.

---

## SECTION 2 — SIGNIFICANT DATE INCONSISTENCIES

---

### 2.1 Gruhathyrir Awakening Date — ~25,000 BW vs. ~20,000 BW
| Source | Claim |
|--------|-------|
| `maz_history_timeline.md` | ~25,000 BW (Old Gods awakening) |
| `maz_religion_gruhathyrir.md` Mythology | "Gruhathyrir emerged around **25,000 BW**" — awakening; "As Gruhathyrir grew in power **around 20,000 BW**, its consciousness began to warp reality" (Feywild creation) |
| `maz_religion_1overview_origins.md` summary table | "~**20,000 BW**" (lists as awakening date) |

**Verdict:** Origins summary table uses 20,000 BW but that is actually the date of Feywild creation, not the awakening. Both the timeline and the deity's own mythology say ~25,000 BW for awakening. Fix: correct the `maz_religion_1overview_origins.md` summary table for Gruhathyrir from ~20,000 BW to ~25,000 BW.

---

### 2.2 Mordrion's Return After Banishment — 101 AW vs. 102 AW
| Source | Claim |
|--------|-------|
| `maz_history_timeline.md` | "**101 AW** — The Banishment Ends. Mordrion manifests immediately." |
| `maz_religion_mordrion.md` | "When Mordrion's avatar finally returned in **102 AW**" |

**Verdict:** One-year discrepancy. The timeline says 101 AW; the Mordrion deity file says 102 AW. (Note: the 102 AW reference in the origins file is specifically for Zuel, not Mordrion.) Fix: reconcile — either update the Mordrion file to 101 AW or update the timeline to 102 AW. Timeline + origins doc jointly confirm 101 AW for the banishment end, so update `maz_religion_mordrion.md` to "101 AW."

---

### 2.3 Gyru's Ascension Date in Guzon's Mythology — ~3,000 BW vs. 1,111 BW
| Source | Claim |
|--------|-------|
| `maz_religion_guzon.md` Mythology | "When the dwarf Gyru attempted to achieve godhood…around **3,000 BW**" |
| `maz_history_timeline.md` | **1,111 BW** for Gyru's ascension |
| `maz_religion_gyru.md` | "**1111 BW**" |
| `maz_religion_entities.md` | Gyru "became a lesser entity in **1111 BW**" |

**Verdict:** The Guzon file has the wrong date. Fix: change "around 3,000 BW" in `maz_religion_guzon.md` to "1,111 BW."

---

### 2.4 Guzon's Awakening Date — ~5,000 BW vs. ~3,200 BW
| Source | Claim |
|--------|-------|
| `maz_religion_guzon.md` Mythology | "emerged approximately **5,000 BW**" |
| `maz_religion_1overview_origins.md` | "~**3,200 BW**" |
| `maz_history_timeline.md` | "~**3,200 BW**" |

**Verdict:** Two primary chronological sources say ~3,200 BW; the Guzon deity file says ~5,000 BW. Fix: update `maz_religion_guzon.md` to say ~3,200 BW.

---

### 2.5 Tiovin/Taovan Awakening Date — ~3,000 BW vs. ~3,100 BW
| Source | Claim |
|--------|-------|
| `maz_religion_tiovin.md` | "around **3000 BW**" |
| `maz_religion_taovan.md` | "In the beginning around **3000 BW**" |
| `maz_religion_1overview_origins.md` | "~**3,100 BW**" |

**Verdict:** Both individual files say ~3,000 BW; the origins overview says ~3,100 BW. Minor rounding difference, but should be standardized. Fix: update both individual deity files to "~3,100 BW" to match the origins document.

---

### 2.6 Garnak's Era Label — "Age of Awakening" vs. "Era of Arrival"
| Source | Claim |
|--------|-------|
| `maz_religion_garnak.md` | "He awakened in 1666 BW during the **Age of Awakening**" |
| `maz_history_timeline.md` | 1,666 BW falls in the **Era of Arrival** |
| All timeline/overview documents | Era of Awakening ends well before 1,666 BW |

**Verdict:** Garnak's file uses the wrong era name. Fix: change "Age of Awakening" to "Era of Arrival" in `maz_religion_garnak.md`.

---

## SECTION 3 — CALENDAR INCONSISTENCIES

The official Common Calendar (established in `maz_society_1overview.md`) defines 12 months. Multiple files use incorrect or non-existent month names.

**Official Month Names:**
| Month # | Name | Real-World Equiv. |
|---------|------|-------------------|
| 1 | Quarz | January |
| 2 | Xan | February |
| 3 | Minerva | March |
| 4 | Garn | April |
| 5 | Hinter | May |
| 6 | Mord | June |
| 7 | Pyran | July |
| 8 | Rivol | August |
| 9 | Iquin | September |
| 10 | Mauian | October |
| 11 | Tiovary | November |
| 12 | Zebul | December |

---

### 3.1 Tiovin's File Uses "Mor" for January
- `maz_religion_tiovin.md`: "New Year on the first of **Mor** (January 1)"
- Correct name: **Quarz** (January)
- **Fix:** Change "Mor" to "Quarz" in `maz_religion_tiovin.md`.

---

### 3.2 Quarzel's Holidays Use "Quarz" for March
Both `maz_religion_quarzel.md` and the Quarzel holiday section of `maz_society_1overview.md` treat "Quarz" as equivalent to March (e.g., "first day of **Quarz** (March 1)", "fifteenth of **Quarz** (March 15)").
- Correct: Quarz = **January**; March = **Minerva**
- **Fix:** Replace "Quarz (March)" with "Minerva (March)" in Quarzel holiday references. OR if the holidays are intended for January, update the parenthetical to "(January)."

---

### 3.3 Xannith's Holidays Use "Xan" for October
Both `maz_religion_xannith.md` and the Xannith holiday section of `maz_society_1overview.md` treat "Xan" as October (e.g., "**1 Xan** (October 1)", "**15 Xan** (October 15)").
- Correct: Xan = **February**; October = **Mauian**
- **Fix:** Either change the month name to "Mauian" (if October is the intended date) or change the parenthetical to "(February)" (if February is intended).

---

### 3.4 Polyvin's Holidays Use "Polyvin" as a Month Name
Both `maz_religion_polyvin.md` and the Polyvin holiday section of `maz_society_1overview.md` use "Polyvin" as a month name (e.g., "**1 Polyvin** (March 1)"). No month named "Polyvin" exists in the official calendar; March = **Minerva**.
- **Fix:** Replace "Polyvin" with "Minerva" in Polyvin holiday references throughout.

---

### 3.5 Paladine Holidays Use "Tio" and "Paladine" as Month Names
The Paladine holiday section of `maz_society_1overview.md` uses "**Tio**" for April and "**Paladine**" for May. Neither exists in the official calendar; April = **Garn**, May = **Hinter**.
- **Fix:** Replace "Tio" with "Garn" and "Paladine" with "Hinter" in `maz_society_1overview.md` Paladine holiday section.

---

### 3.6 Eilistraee's "First Dance" Uses "Rivoleen" for June
`maz_society_1overview.md`: "The First Dance (**13 Rivoleen** / June 13)." No month named "Rivoleen" exists; June = **Mord**. (Rivoleen → Rivol = August.)
- **Fix:** Replace "13 Rivoleen" with "13 Mord" in the Eilistraee holiday section.

---

### 3.7 Sheeva's "Night of Knives" Uses "Taovan" for November
`maz_society_1overview.md`: "The Night of Knives (**13 Taovan** / November 13)." No month named "Taovan" exists; November = **Tiovary**.
- **Fix:** Replace "13 Taovan" with "13 Tiovary" in the Sheeva holiday section.

---

### 3.8 Gyru's "Day of Ascension" — "11 Minerva / May 11" Mismatch
Both `maz_religion_gyru.md` and `maz_society_1overview.md` Gyru section: "Day of Ascension (**11 Minerva** / May 11)." Minerva = March, not May; May = Hinter.
- If the event is in March: it should say "11 Minerva (March 11)."
- If the event is in May: it should say "11 Hinter (May 11)."
- **Fix:** Determine the intended month. Since Gyru ascended in 1,111 BW (the date likely determines the month), this should be verified and corrected consistently.

---

### 3.9 Months Have 28 Days But Many Holidays Listed on Day 30
The official calendar states months have 28 days (4 weeks × 7 days). Yet numerous holidays reference "**30 Zebul**," "**30 Mord**," "**30 Quarz**," "**30 Tio**," etc. — days that do not exist in a 28-day month.

Specific examples:
- Zebulba's Night of Unmaking: "30 Zebul" (appears in `maz_religion_zebulba.md` and `maz_society_1overview.md`)
- Dwarven Stoneshaper's Vigil: "30 Zebul" (`maz_society_1overview.md`)
- Halfling Festival of Lanterns: "30 Zebul" (`maz_society_1overview.md`)
- Quarzel's Final Stand: "30 Quarz" (`maz_religion_quarzel.md` and `maz_society_1overview.md`)
- Taovan's Shadow Feast: "30 Zebul" (`maz_religion_taovan.md`)
- Bleeding Feast (Zuel): "30 Mord" (`maz_religion_zuel.md` and `maz_society_1overview.md`)

**Verdict:** Either months actually have 30 days and the "28 days" statement in the calendar is wrong, OR all "30th day" dates should be "28th day." Given that day 30 is used deliberately and widely, it is likely that months are actually 30 days and the calendar spec is wrong. Fix: **Either** correct the calendar spec to "30 days per month" (producing 360 + 4 = 364 days/year) **or** change all 30th-day holidays to 28th-day. Consistency is needed.

---

### 3.10 "Zuel's Bleeding Feast" — "30 Mord (June 15)" Is Internally Inconsistent
In `maz_religion_zuel.md` and `maz_society_1overview.md`: "The Bleeding Feast occurs on **30 Mord (June 15)**." The 30th day of the 6th month would correspond to the end of June, not June 15. June 15 would be the 15th of June = "**15 Mord**."
- **Fix:** Either change "30 Mord" to "15 Mord" (if June 15 is correct) or update the parenthetical to "(June 30 / end of June)."

---

## SECTION 4 — NAME/SPELLING INCONSISTENCIES

---

### 4.1 Dukhan Empire Name Spelling
| Source | Spelling |
|--------|----------|
| `maz_history_lostempires.md` (throughout) | **Dukahn** |
| `maz_history_timeline.md`, `maz_history_nations.md`, and others | **Dukhan** |

**Fix:** Standardize to "Dukhan" throughout `maz_history_lostempires.md`.

---

### 4.2 Rivoleen's Description of Xannith's Portfolio
`maz_religion_rivoleen.md` states Rivoleen opposes "Xannith the entity of **madness and chaos**."
- Xannith's actual portfolio: **greed, wealth, corrupt nobility**
- "Madness and chaos" describes Og'thallith or Kazrokath, not Xannith
- **Fix:** Correct the Rivoleen file's description of Xannith to reflect her actual portfolio.

---

## SECTION 5 — INTERNAL FILE INCONSISTENCIES

---

### 5.1 Og'thallith Origin — "Always Existed" vs. ~18,000 BW Awakening
`maz_religion_ogthallith.md` Mythology section states: "Most scholars believe he **always existed**, lurking in the spaces between planes… Some theorize he is not an entity at all."

However, `maz_religion_1overview_origins.md` definitively states Og'thallith "**awakened in the later Timeless Era (~18,000 BW)**." The deity's own mythology file creates ambiguity that contradicts the established canon.

**Fix:** Revise the Og'thallith mythology section to acknowledge the ~18,000 BW awakening as established, while keeping the "mystery of origins" flavor if desired.

---

### 5.2 Og'thallith vs. Xorancon — Overlapping Madness Portfolios
`maz_religion_rivoleen.md` labels Xannith as the entity of madness (see 4.2 above). More broadly, both `maz_religion_ogthallith.md` and `maz_religion_xorancon.md` partially overlap on madness/aberrations, and the `maz_religion_entities.md` description of Xannith says "Portfolio: Greed, desire, wealth" (correct) rather than madness — but this caused the cross-file error in Rivoleen's file. **No fix needed in the entity files themselves**, only in the Rivoleen file.

---

### 5.3 Zebulba's Alignment Inconsistency in Description File
`maz_religion_entities.md` header for Zebulba says alignment "**CE**." This is actually consistent with `maz_religion_zebulba.md` which says CE. ✓ **No issue.**

---

### 5.4 Thalaman's Portfolio Description Difference
- `maz_religion_thalaman.md`: Portfolio = "Time, madness, chronomancy, fragmented consciousness"
- `maz_religion_entities.md`: Portfolio = "**Chaos, insanity, time travel**"

Minor wording discrepancy. The individual file is more precise. **Fix:** Update `maz_religion_entities.md` Thalaman portfolio to match the individual file.

---

## SECTION 6 — MINOR INCONSISTENCIES

---

### 6.1 Mordrion's Wound — "Eye" vs. "Left Eye"
Some sources specify "left eye" and others simply say "eye":
- Specific about left eye: `maz_history_timeline.md`, `maz_religion_1overview_origins.md`, `maz_religion_zuel.md`
- Unspecified: `maz_history_1overview.md`, `maz_religion_mordrion.md`

**Fix:** Add "left" to the unspecified references in `maz_history_1overview.md` and `maz_religion_mordrion.md` for consistency.

---

### 6.2 Zuel's Return After Banishment — 101 vs. 102 AW
`maz_history_timeline.md`: "101 AW — The Banishment Ends" (general statement).
`maz_religion_1overview_origins.md`: "Zuel's consciousness…couldn't manifest an avatar until **102 AW**."
`maz_religion_zuel.md`: "In **102 AW**, Zuel's avatar returned."

**Verdict:** The banishment ending at 101 AW and Zuel not manifesting until 102 AW is actually **consistent** (banishment ends at 101 AW = Mordrion manifests; Zuel manifests one year later at 102 AW). This distinction may need to be clarified in the timeline entry ("101 AW — The Banishment Ends; Mordrion manifests immediately; Zuel manifests in 102 AW"). **No fix required** beyond clarifying the timeline note.

---

### 6.3 Current Setting Year — 811 AW vs. Campaigns Set in 824–842 AW
- `maz_society_1overview.md`: "It is currently the year **811 AW**."
- Multiple deity campaign references: "Lords of Madness" = 824 AW; "Secrets of Shadows" = 832 AW
- `maz_history_elves.md` title references "100,000 BW – **842 AW**"

**Note:** The 811 AW figure appears to be the "default" campaign start year (for the Orcs Beyond campaign, Campaign 01). The higher years are campaign-specific. This is likely intentional rather than an error. **No fix required** but a clarifying note in the society overview about the multi-campaign timeline would be helpful.

---

### 6.4 Yrugas Founding Date — ~4,000 BW
- `maz_history_narrative.md` and `maz_history_lostempires.md`: both reference ~4,000 BW for Yrugas founding.
- `maz_religion_zebulba.md`: "flourishing from approximately **4000 to 2700 BW**."
- **Consistent across sources. ✓ No issue.**

---

### 6.5 Elven Reckoning Year 1 Conversion
`maz_society_1overview.md` conversion table: "Year 1 ER = 3,402 BW" and "Year 3,402 ER = Year 1 AW = End of War." This implies 3,402 years between Year 1 ER and Year 1 AW, which requires: BW = 3,402 − ER for the BW era. The elven history file confirms this with "Year 1 ER = 3,402 BW." **Consistent. ✓ No issue.**

---

## SUMMARY TABLE

| # | Severity | File(s) to Fix | Issue |
|---|----------|----------------|-------|
| 1.1 | Critical | `maz_history_thewar.md` | "More than a dozen" should be "seven" (Minerva's sacrifice) |
| 1.2 | Critical | `maz_history_timeline.md`, `maz_history_narrative.md` | Asti "awakens" at ~12,000 BW should be "settles on Mazariim"; add ~20,000 BW awakening |
| 1.3 | Critical | `maz_history_timeline.md` Appendix A | Guzon listed as "arrived from another plane" — should be "native awakening" |
| 1.4 | Critical | `maz_religion_ryle.md`, `maz_society_1overview.md` | Ry'le awakened ~2,800 BW (not 811–815 AW / 102 AW); "recently born" label wrong |
| 1.5 | Critical | `maz_history_timeline.md` | Ashura/Khan awakening: ~2,900 BW should be ~3,100 BW |
| 1.6 | Critical | `maz_history_timeline.md` (1,492 BW entry) | Alagalothor "settles in Far Realm" should be "Astral Plane" |
| 1.7 | Critical | `maz_religion_1overview_origins.md` | Zuel's plane "Abyss" should be "Abaddon" |
| 1.8 | Critical | `maz_history_timeline.md` Appendix A | Asti has no plane listed; should be "Positive Energy Plane" |
| 1.9 | Critical | `maz_religion_entities.md` | Tiovin: wrong symbol, weapon, and alignment |
| 1.10 | Critical | `maz_religion_entities.md` | Sheeva alignment CE should be NE |
| 1.11 | Critical | `maz_religion_entities.md` | Polyvin alignment N should be NG |
| 1.12 | Critical | `maz_history_narrative.md` | Asti's origin contradicts established canon (white hole, ~20,000 BW) |
| 2.1 | Significant | `maz_religion_1overview_origins.md` | Gruhathyrir awakening: ~20,000 BW should be ~25,000 BW |
| 2.2 | Significant | `maz_religion_mordrion.md` | Mordrion returns "102 AW" should be "101 AW" |
| 2.3 | Significant | `maz_religion_guzon.md` | Gyru ascension date "~3,000 BW" should be "1,111 BW" |
| 2.4 | Significant | `maz_religion_guzon.md` | Guzon awakening "~5,000 BW" should be "~3,200 BW" |
| 2.5 | Significant | `maz_religion_tiovin.md`, `maz_religion_taovan.md` | Tiovin/Taovan awakening "~3,000 BW" should be "~3,100 BW" |
| 2.6 | Significant | `maz_religion_garnak.md` | Era label "Age of Awakening" should be "Era of Arrival" |
| 3.1 | Calendar | `maz_religion_tiovin.md` | Month "Mor" for January should be "Quarz" |
| 3.2 | Calendar | `maz_religion_quarzel.md`, `maz_society_1overview.md` | "Quarz" used for March should be "Minerva" (or date corrected to January) |
| 3.3 | Calendar | `maz_religion_xannith.md`, `maz_society_1overview.md` | "Xan" used for October should be "Mauian" (or date corrected to February) |
| 3.4 | Calendar | `maz_religion_polyvin.md`, `maz_society_1overview.md` | Month "Polyvin" doesn't exist; March = "Minerva" |
| 3.5 | Calendar | `maz_society_1overview.md` | Paladine holidays: "Tio" (April) = "Garn"; "Paladine" (May) = "Hinter" |
| 3.6 | Calendar | `maz_society_1overview.md` | "13 Rivoleen / June 13" should be "13 Mord / June 13" |
| 3.7 | Calendar | `maz_society_1overview.md` | "13 Taovan / November 13" should be "13 Tiovary / November 13" |
| 3.8 | Calendar | `maz_religion_gyru.md`, `maz_society_1overview.md` | "11 Minerva / May 11" — Minerva = March, not May; needs reconciliation |
| 3.9 | Calendar | Multiple files | Day "30" referenced in 28-day months — calendar spec may need to say 30 days |
| 3.10 | Calendar | `maz_religion_zuel.md`, `maz_society_1overview.md` | "30 Mord (June 15)" — 30th day ≠ June 15; likely should be "15 Mord (June 15)" |
| 4.1 | Spelling | `maz_history_lostempires.md` | "Dukahn" should be "Dukhan" throughout |
| 4.2 | Wording | `maz_religion_rivoleen.md` | Xannith described as "entity of madness and chaos" — should be greed/wealth |
| 5.1 | Internal | `maz_religion_ogthallith.md` | Mythology says Og'thallith "always existed"; contradicts ~18,000 BW awakening in origins doc |
| 5.4 | Minor | `maz_religion_entities.md` | Thalaman portfolio wording differs from individual file |
| 6.1 | Minor | `maz_history_1overview.md`, `maz_religion_mordrion.md` | "Eye" should be "left eye" for consistency |
