# Adventure Continuity Prompt

**Version:** 3.0
**Updated:** 2026-02-12

---

## How to Continue Any Adventure

At the start of a new conversation, say:

    Load campaign from Adventures/[ADVENTURE_NAME]

Example:

    Load campaign from Adventures/Thornkeep

---

## What Happens When You Load

**Step 1:** Claude loads all core Cypher System Fantasy rules from:

    ~/Desktop/CypherSystem/Setting - Fantasy/

This includes character types, ancestries, spells, foci, house rules, conditions, flavors, and the ability index.

**Step 2:** Claude loads all campaign-specific files from:

    ~/Desktop/CypherSystem/Setting - Fantasy/Adventures/[ADVENTURE_NAME]/

Files loaded: character_sheet.md, session_state.md, campaign_log.md, and gm_prompt.md.

**Step 3:** Claude confirms character status, current location, active objectives, and pools. Then asks: "Ready to continue? What do you do?"

---

## Common Commands During Play

| Say This | What Happens |
|---|---|
| d20 or roll d20 | Rolls 1d20 for task resolution |
| 3d6 | Rolls 3d6 |
| recovery roll | Rolls 1d6 plus your Tier |
| check status | Shows pools, location, and objectives |
| who have I met | Lists NPCs encountered |
| what are my abilities | Reads abilities from character sheet |
| what do I know | Lists discoveries and clues |
| save progress | Updates all files and confirms |
| recap | Summarizes recent events |

---

## Creating a New Adventure

1. Copy Template_Adventure to a new folder under Adventures with your chosen name
2. Fill in character_sheet.md with your character (use character_creation.md for guidance)
3. Set up session_state.md with starting location and objectives
4. Customize gm_prompt.md with campaign quick reference
5. Leave campaign_log.md blank — it fills in as you play
6. Say: Load campaign from Adventures/[YourAdventureName]

---

## Available Adventures

- **Template_Adventure** — Blank template, copy and customize

*Add adventures here as they are created.*

---

## Version History

- **v1.0** (2025-12-30): Initial creation
- **v2.0** (2026-02-12): Revised for Fantasy setting
- **v3.0** (2026-02-12): Streamlined, removed duplication and AI Drive references