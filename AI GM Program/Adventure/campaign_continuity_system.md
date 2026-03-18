# Cypher System Campaign Continuity System

**Version:** 3.0
**Updated:** 2026-02-12

---

## Overview

This system enables persistent Cypher System Fantasy campaigns across multiple conversations with perfect continuity. It solves the problem of maintaining character state, campaign progress, NPC relationships, and narrative history across conversation boundaries.

All campaign files are stored under:

    ~/Desktop/CypherSystem/Setting - Fantasy/Adventures/

---

## File Architecture

### Folder Structure

    ~/Desktop/CypherSystem/Setting - Fantasy/Adventures/
    ├── campaign_continuity_system.md      (this file)
    ├── adventure_prompt.md                (session loading instructions)
    ├── Template_Adventure/
    │   ├── character_sheet.md
    │   ├── session_state.md
    │   ├── campaign_log.md
    │   ├── dice_roller.py
    │   └── gm_prompt.md
    └── [Adventure_Name]/
        ├── character_sheet.md
        ├── session_state.md
        ├── campaign_log.md
        ├── dice_roller.py
        └── gm_prompt.md

### File Purposes

| File | Purpose | Update Frequency |
|---|---|---|
| character_sheet.md | Character stats, pools, equipment, spells | Real-time in memory, written at scene breaks |
| session_state.md | Campaign progress, NPCs, objectives, flags | After scenes and at session end |
| campaign_log.md | Narrative history of all sessions | End of session |
| dice_roller.py | Random dice rolls | Never changed, it is a utility |
| gm_prompt.md | Quick reference for campaign loading | Updated at end of session |

---

## File Templates

### 1. character_sheet.md

**Purpose:** Single source of truth for character mechanical state.

**Update Frequency:** Real-time during play.

    # Character Sheet

    **Last Updated:** [YYYY-MM-DD HH:MM]

    ## Identity

    - **Name:** [Character Name]
    - **Descriptor:** [Descriptor]
    - **Ancestry:** [Ancestry]
    - **Type:** [Type]
    - **Focus:** [Focus]
    - **Tier:** [Number]
    - **Effort:** [Number]
    - **XP:** [Current] / [Needed for next advancement]

    ## Stat Pools

    | Stat | Current | Maximum | Edge |
    |------|---------|---------|------|
    | Might | [X] | [X] | [X] |
    | Speed | [X] | [X] | [X] |
    | Intellect | [X] | [X] | [X] |

    ## Damage Track

    - **Status:** Hale / Impaired / Debilitated
    - **Notes:** [Any active conditions]

    ## Recovery Rolls

    - [ ] Action (1 action)
    - [ ] Ten Minutes
    - [ ] One Hour
    - [ ] Ten Hours

    Check boxes as used. Reset after ten-hour recovery.

    ## Armor

    - **Total Armor:** [X]
    - **Armor Source:** [Equipment or abilities providing armor]
    - **Speed Cost Reduction:** [From Experienced in Armor or similar]

    ## Weapons

    | Weapon | Type | Damage | Notes |
    |--------|------|--------|-------|
    | [Name] | Light/Medium/Heavy | [X] | [Special properties] |

    ## Abilities

    ### Type Abilities
    - **[Ability Name]:** [Brief description, cost]

    ### Focus Abilities
    - **[Ability Name]:** [Brief description, cost]

    ### Ancestry Abilities
    - **[Ability Name]:** [Brief description]

    ## Skills

    ### Trained
    - [Skill 1]
    - [Skill 2]

    ### Specialized
    - [Skill 1]

    ### Inabilities
    - [Skill 1]

    ## Spellcasting (if applicable)

    - **Spell Slots:** [Current] / [Maximum]
    - **Spellbook Contents:** [List of known spells]
    - **Prepared Spells:** [List of currently memorized spells]
    - **Spell Focus:** [School/type if applicable]

    ## Equipment

    - [Item 1]
    - [Item 2]
    - **Gold:** [Amount] gp

    ## Artifacts (Attuned)

    | Artifact | Level | Effect | Slot |
    |----------|-------|--------|------|
    | [Name] | [X] | [Effect] | [X of max] |

    Maximum Attuned: [X]

    ## Cyphers

    | Cypher | Level | Effect |
    |--------|-------|--------|
    | [Name] | [X] | [Effect] |

    ## Background Notes

    [Brief character backstory, motivations, personality notes]

**Update Triggers:** Pool points spent, damage taken, recovery roll used, XP earned, equipment gained or lost, cypher used, character advances, spell memorized or cast.

**Validation Checks:** Current pools never exceed maximum. Current pools never go below 0. Recovery rolls cannot be used twice before ten-hour rest. Artifacts do not exceed attunement limit. Timestamp updates with every change.

---

### 2. session_state.md

**Purpose:** Track campaign progress, decisions, and continuity.

**Update Frequency:** After significant events and at end of session.

    # Session State

    **Campaign Name:** [Name]
    **Current Session:** [Number]
    **Last Played:** [YYYY-MM-DD]

    ## Current Location

    - **Scene:** [Scene ID / Name]
    - **Location:** [Where the party is]
    - **Immediate Situation:** [What is happening right now]

    ## Active Objectives

    ### [Objective Title]
    - **Status:** Not Started / In Progress / Completed / Failed
    - **Details:** [Description]
    - **Next Steps:** [What needs to happen]

    ## Completed Objectives

    ### [Objective Title] — Session [X]
    - **Outcome:** [How it resolved]
    - **Key Events:** [What happened]

    ## Scenes Completed

    | Scene | Session | Outcome | Key Events |
    |-------|---------|---------|------------|
    | [Name] | [X] | [Brief outcome] | [Brief events] |

    ## Key Decisions

    | Session | Decision | Consequence |
    |---------|----------|-------------|
    | [X] | [What the player chose] | [What resulted] |

    ## NPCs Encountered

    ### Allies
    - **[NPC Name]:** [Role, relationship, trust level, last interaction]

    ### Enemies
    - **[NPC Name]:** [Role, threat level, last interaction]

    ### Neutral
    - **[NPC Name]:** [Role, disposition, last interaction]

    ## Reputation

    | Faction | Score | Descriptor |
    |---------|-------|------------|
    | [Faction Name] | [X] | Hostile/Unfriendly/Neutral/Friendly/Allied |

    ## Continuity Flags

    These are true/false switches tracking binary story states.

    - **[flag_name]:** true/false — [Brief explanation]

    ## GM Notes

    ### Player Preferences
    - [Notes about play style, content preferences, pacing]

    ### Next Session Prep
    - [Plot threads to follow up on]
    - [NPCs to reintroduce]
    - [Encounters to prepare]

**Update Triggers:** Scene completed, objective progress, player makes a choice, NPC encountered, faction interaction, important event setting continuity flags.

---

### 3. campaign_log.md

**Purpose:** Human-readable narrative history.

**Update Frequency:** End of each session.

    # Campaign Log: [Campaign Name]

    ---

    ## Session [N] — [YYYY-MM-DD]

    ### Scene: [Scene Name]

    **Location:** [Description]

    ### What Happened

    [Narrative summary of events in prose form]

    ### Dice Rolls

    - [Task description]: Rolled [X] — [Outcome]

    ### Combat / Challenges

    - **Encounter:** [Description]
    - **Rolls:** [Key rolls and outcomes]
    - **Pool Expenditures:** [Points spent and on what]
    - **Result:** [How the encounter resolved]

    ### Key Decisions

    - [Decision made and reasoning]
    - [Consequences that followed]

    ### Loot / Rewards

    - [Items gained]
    - [Gold earned]
    - [XP awarded and reason]

    ### End of Session Stats

    - **Pools:** M: [X]/[X], S: [X]/[X], I: [X]/[X]
    - **Damage Track:** [Status]
    - **XP Earned This Session:** [Amount]
    - **Total XP:** [Amount]
    - **Reputation Changes:** [Any changes]
    - **Recovery Rolls Remaining:** [List]

    ### Session Notes

    [Player feedback, preferences, what worked well, what to adjust]

---

### 4. dice_roller.py

**Purpose:** Generate random dice rolls with proper formatting.

    import random
    import sys

    def roll_dice(notation):
        notation = notation.lower().strip()
        modifier = 0

        if '+' in notation:
            parts = notation.split('+')
            notation = parts[0]
            modifier = int(parts[1])
        elif '-' in notation:
            parts = notation.split('-')
            notation = parts[0]
            modifier = -int(parts[1])

        if 'd' in notation:
            parts = notation.split('d')
            num_dice = int(parts[0]) if parts[0] else 1
            die_size = int(parts[1])
        else:
            print(f"Invalid notation: {notation}")
            return

        rolls = [random.randint(1, die_size) for _ in range(num_dice)]
        total = sum(rolls) + modifier

        mod_str = ""
        if modifier > 0:
            mod_str = f" + {modifier}"
        elif modifier < 0:
            mod_str = f" - {abs(modifier)}"

        print(f"Rolling {num_dice}d{die_size}{mod_str}")
        print(f"  Rolls: {rolls}")

        if num_dice == 1 and die_size == 20:
            if rolls[0] == 20:
                print(f"  *** NATURAL 20! ***")
            elif rolls[0] == 1:
                print(f"  *** NATURAL 1 — GM Intrusion! ***")

        print(f"  Total: {total}")

    if __name__ == "__main__":
        if len(sys.argv) > 1:
            roll_dice(sys.argv[1])
        else:
            roll_dice("d20")

**Usage:**

    python3 dice_roller.py d20
    python3 dice_roller.py 3d6
    python3 dice_roller.py 1d6+2

---

### 5. gm_prompt.md

**Purpose:** Quick-start instructions for new conversations.

    # GM Quick-Start Prompt

    ## Loading Instructions

    When starting a new conversation, the player will say something like:
    "Load campaign from Adventures/[Adventure_Name]"

    Follow these steps:

    1. Read character_sheet.md to get current character state
    2. Read session_state.md to get campaign progress and continuity flags
    3. Read campaign_log.md to understand narrative history
    4. Confirm status with the player before beginning play

    ## Current Campaign Status

    - **Campaign:** [Name]
    - **Session:** [Number]
    - **Character:** [Name] — [Descriptor] [Ancestry] [Type] who [Focus]
    - **Tier:** [X]
    - **Location:** [Current location]
    - **Immediate Situation:** [What is happening]

    ## Active Plot Threads

    - [Thread 1]
    - [Thread 2]
    - [Thread 3]

    ## Player Preferences

    - [Preference 1]
    - [Preference 2]

    ## Quick Command Reference

    | Player Input | Claude Action |
    |---|---|
    | "d20" or "roll d20" | Execute dice_roller.py d20 |
    | "Check status" | Display pools, location, objectives |
    | "Recovery roll" | Execute dice_roller.py 1d6+[tier], update pools |
    | "What are my abilities?" | Read from character_sheet.md |
    | "Who have I met?" | Summarize NPCs from session_state.md |
    | "Save progress" | Update and confirm all files saved |

    ## Important Continuity Flags

    - [flag]: [value] — [meaning]

---

## Session Workflow

### Phase 1: Starting a New Conversation

**Step 1: Load Campaign Files.** The player says "Load campaign from Adventures/[Adventure_Name]" and Claude reads character_sheet.md, session_state.md, campaign_log.md, and gm_prompt.md.

**Step 2: Confirm Status.** Claude displays:

    Campaign Loaded: [Campaign Name]
    Character: [Name] ([Descriptor] [Ancestry] [Type] who [Focus], Tier [X])
    Location: [Current scene/location]
    Pools: M: [X]/[X], S: [X]/[X], I: [X]/[X]
    Armor: [X]
    Active Objectives:
      - [Objective 1]
      - [Objective 2]
    Condition: [Hale/Impaired/Debilitated]
    Ready to continue!

---

### Phase 2: Active Play

#### Task Resolution

When the player declares an action, Claude determines difficulty based on creature level or situation, checks for relevant skills or abilities where trained reduces by 3 and specialized reduces by 6, asks if the player wants to use Effort or spend points, requests a dice roll, executes dice_roller.py, compares the result to the target number, applies Edge if Effort was used, narrates the outcome, and updates pools if points were spent.

#### Combat Encounters

First, determine initiative using Speed-based tasks or narrative order. Each round, the player declares an action, Claude determines the task difficulty which is usually the enemy level multiplied by 3, the player rolls d20 and applies modifiers, damage is rolled if the attack hits, damage is tracked for both enemies and the PC, and pools are updated in real-time. After combat, all files are updated.

#### Recovery Rolls

When the player requests recovery, Claude checks which recovery rolls are still available, the player chooses which to use, Claude rolls 1d6 plus the character's Tier, adds the result to the chosen pool without exceeding maximum, checks the used box in character_sheet.md, and announces the result.

#### Key Decisions

When the player makes an important choice, Claude narrates the immediate consequence, records the decision in session_state.md, sets relevant continuity flags, and notes potential future consequences in GM Notes.

#### Scene Completion

When a scene ends, Claude adds it to Scenes Completed in session_state.md, updates Active Objectives progress, updates NPC relationships and reputation, sets continuity flags, notes equipment and gold changes, and awards XP if appropriate.

---

### Phase 3: End of Session

**Step 1: Final State Update.** Update character_sheet.md with final pool values, XP earned, equipment changes, cyphers used or gained, spells expended, and updated timestamp.

**Step 2: Update Session State.** Update session_state.md by incrementing the session number, updating Current Location, marking completed objectives, adding new NPCs, updating reputation, setting continuity flags, and adding GM Notes for next session.

**Step 3: Write Campaign Log.** Append a new session entry to campaign_log.md covering the session number and date, scenes completed, narrative summary, key dice rolls, important decisions and consequences, end of session stats, and player feedback.

**Step 4: Confirm Save.** Claude displays a summary confirming the session is complete with XP earned, scenes completed, key decisions, final pool values, condition, and a preview of what comes next.

---

## File Management Protocols

### When to Update Files

| Event | File | Update Type |
|---|---|---|
| Pool points spent | character_sheet.md | Immediate in memory, write at scene break |
| Damage taken | character_sheet.md | Immediate in memory, write at scene break |
| Recovery roll used | character_sheet.md | Immediate in memory, write at scene break |
| Equipment gained or lost | character_sheet.md | At scene break |
| XP awarded | character_sheet.md | At scene break |
| Spell cast or memorized | character_sheet.md | At scene break |
| Major decision made | session_state.md | After resolution |
| Scene completed | session_state.md | Immediately |
| NPC encountered | session_state.md | After scene |
| Reputation change | session_state.md | After scene |
| Session ends | All files | End of session |

### Update Procedure

Track changes in conversation memory and announce changes to the player immediately. Write accumulated changes at natural break points: after combat ends, after a major scene completes, after a significant decision and its consequences, and at end of session which is mandatory for all files.

### Timestamp Protocol

Include the timestamp in character_sheet.md as Last Updated with date and time. This identifies the most recent version if multiple copies exist.

---

## Dice Rolling System

### Command Recognition

Claude recognizes these player inputs as dice roll requests: "d20", "roll d20", "3d6", "roll 3d6", "roll damage", "recovery roll", "1d6+2", and "make a roll".

### Result Interpretation

**Task Resolution (d20):** Compare the total to the target number which is the difficulty level multiplied by 3. A natural 20 is an automatic success with a possible bonus effect. A natural 1 is a GM Intrusion opportunity and Edge does not reduce Intellect costs on spell rolls of 1.

**Damage:** Weapon damage is fixed by weapon type where Light equals 2, Medium equals 4, and Heavy equals 6. Effort on damage adds 3 per level for single targets or 2 per level for area spells. Subtract the target's Armor from damage dealt.

**Recovery (1d6 plus Tier):** Roll 1d6, add the character's Tier, add the result to the chosen pool. The result cannot exceed the pool maximum.

### Special Cases

**Natural 20 on Spell:** The spell costs no pool points or has an additional beneficial effect at the GM's choice.

**Natural 1 on Spell:** Edge does not apply to the Intellect cost. The cost cannot drop a pool below 1.

---

## Damage Track Reference

| Condition | Trigger | Effect |
|---|---|---|
| Hale | All pools greater than 0 | Normal |
| Impaired | One pool equals 0 | Effort costs 1 extra point per level, ignore minor and major effect results |
| Debilitated | Two pools equal 0 | Cannot take most actions, can only move immediate distance, if Speed is 0 cannot move |
| Dead | Three pools equal 0 | Character dies |

Claude must check the damage track after every damage instance, announce status changes immediately, apply penalties to subsequent rolls, and remind the player of their status if Impaired or Debilitated.

---

## Cypher and Artifact Management

**Cyphers** such as potions and scrolls are single-use. When used, immediately remove from character_sheet.md. Cyphers have no carry limit in this system. Retrieving and using a potion or scroll is an action that provokes an Attack of Opportunity.

**Artifacts** have attunement limits that vary by type and tier. Track attuned artifacts in character_sheet.md. Do not exceed the maximum.

---

## XP Awards

**When to Award XP:** Major discovery awards 1 XP, completing an objective awards 1 XP, exceptional roleplaying awards 1 XP, and a GM Intrusion accepted awards 2 XP where 1 is kept and 1 is given to another player or saved.

**Process:** Announce the XP award and reason, update character_sheet.md XP field, check if the player has 4 XP which is enough to purchase one advancement, and if yes remind them of advancement options.

---

## Session Transitions

### Ending a Session

Claude suggests a natural stopping point, completes all file updates, provides a session summary, and previews the next session's opening. Claude reminds the player to say "Load campaign from Adventures/[Adventure_Name]" when they return.

### Starting a New Session

The player says "Load campaign from Adventures/[Adventure_Name]" and Claude reads all campaign files, synthesizes the information, confirms status with the player, and asks "Ready to continue? What do you do?"

### Handling Gaps Between Sessions

If the player forgot what happened, Claude offers a brief recap from campaign_log.md, highlights key decisions, reminds the player of active objectives, and shows the current location and situation.

---

## Troubleshooting

**Files Out of Sync.** If character_sheet.md shows different values than expected, check campaign_log.md end-of-session stats as the authoritative source. Correct character_sheet.md accordingly.

**Player Disputes Outcome.** Review recent expenditures in campaign_log.md, reconstruct the math with the player, correct any errors found.

**Dice Roller Not Available.** Use Python's random module inline to generate results.

**Continuity Error.** Always consult session_state.md continuity flags before referencing past events. If an error is found, correct immediately and continue with accurate continuity.

---

## Best Practices

**Do:** Update files regularly at natural break points. Announce pool changes immediately. Check continuity flags before referencing past events. Offer recaps when resuming. Track player preferences. Use GM Intrusions to make sessions dynamic. Award XP for discoveries and roleplay. Give players meaningful choices with real consequences. Apply all house rules including defensive casting, attacks of opportunity, spell components, and armor restrictions.

**Do not:** Make up details that contradict session_state.md. Forget to apply Impaired or Debilitated penalties. Let the player exceed artifact attunement limits. Award advancement without the player spending 4 XP. Forget to mark recovery rolls as used. Let spells stack when they should not per the one instance per spell rule. Break character to discuss file management.

### Maintaining Immersion

Integrate mechanics into narrative seamlessly. Do not announce file operations to the player. Instead of saying "I need to update character_sheet.md," narrate the action and quietly track the mechanical change.

---

## Quick Reference Tables

### Difficulty

| Level | Target Number | Description |
|---|---|---|
| 0 | 0 | Routine, no roll needed |
| 1 | 3 | Simple |
| 2 | 6 | Standard |
| 3 | 9 | Demanding |
| 4 | 12 | Difficult |
| 5 | 15 | Challenging |
| 6 | 18 | Intimidating |
| 7 | 21 | Formidable |
| 8 | 24 | Heroic |
| 9 | 27 | Immortal |
| 10 | 30 | Impossible |

### Modifiers

- Trained: -1 level (-3 to target number)
- Specialized: -2 levels (-6 to target number)
- Expert: -3 levels (-9 to target number)
- Inability: +1 level (+3 to target number)
- Asset (maximum 2): -1 level each (-3 each)
- Effort per level: -1 level (-3 to target number)

### Damage

| Weapon Type | Base Damage |
|---|---|
| Light | 2 points |
| Medium | 4 points |
| Heavy | 6 points |

| Effort on Damage | Bonus |
|---|---|
| Per level, single target | +3 damage |
| Per level, area effect | +2 damage |

### Armor Speed Penalties

| Armor Type | Speed Effort Cost |
|---|---|
| Light | +1 |
| Medium | +2 |
| Heavy | +3 |

Experienced in Armor reduces penalty by 1. Mastery in Armor reduces penalty by 2.

### Common Commands

| Player Input | Claude Action |
|---|---|
| Load campaign | Read all session files and confirm status |
| d20 or roll d20 | Execute dice_roller.py d20 |
| Check status | Display pools, location, and objectives |
| Recovery roll | Execute dice_roller.py 1d6+[tier] and update pools |
| What are my abilities | Read from character_sheet.md |
| Who have I met | Summarize NPCs from session_state.md |
| What do I know | List discoveries and clues from session_state.md |
| Save progress | Update all files and confirm save |
| Recap | Summarize recent events from campaign_log.md |

---

## Creating New Adventures

### From Template

Copy the Template_Adventure folder to a new folder under Adventures with your chosen adventure name. The dice_roller.py file needs no changes. Fill in character_sheet.md with your character's stats. Set up session_state.md with starting location and objectives. Customize gm_prompt.md with campaign details. Start campaign_log.md blank.

### From Scratch

Create a new folder under Adventures. Copy dice_roller.py from Template_Adventure. Create character_sheet.md, session_state.md, campaign_log.md, and gm_prompt.md following the templates in this document.

### Launch

    Load campaign from Adventures/[YourAdventureName]

---

## Version History

- **v1.0** (2025-12-30): Initial system design for Comet Protocol superhero setting
- **v2.0** (2026-02-12): Revised for Fantasy setting, all files converted to markdown, paths updated to Desktop folder
- **v3.0** (2026-02-12): Consolidated with README, removed AI Drive references, streamlined

**System Status:** Fully Operational