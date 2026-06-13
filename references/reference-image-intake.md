# Reference Image Intake

Reference images are the strongest practical source for IP consistency. IPilot should treat uploaded or provided IP images as evidence, not decoration.

## Purpose

Use reference image intake when the user provides, mentions, or plans to provide existing IP artwork, mascot sheets, logo characters, sticker samples, posters, or historical campaign visuals.

The goal is to extract a stable visual system that can survive new poses, expressions, scenes, trends, and material formats.

## When to Trigger

Trigger this workflow when:

- the user uploads one or more IP images;
- the user says the IP already has an official look;
- the user asks for strong character consistency;
- the user wants multiple asset types based on the same IP;
- the user complains that generated images change the character style;
- the user wants a production-ready image workflow.

## Reference Image Types

Classify each reference image before using it.

| Type | Meaning | How to Use |
|---|---|---|
| Primary reference | The most authoritative IP image | Treat as source of truth |
| Style reference | Shows rendering or visual style | Use for line/style/color guidance |
| Pose reference | Shows allowed action or angle | Use for variation only |
| Expression reference | Shows emotion set | Use for face/expression range |
| Material reference | Shows previous poster/sticker/merch | Use for production format guidance |
| Outdated reference | Historical but no longer official | Use cautiously; ask user if uncertain |
| Negative reference | What the user dislikes | Convert into avoid rules |

## Intake Questions

Ask concise questions when the reference role is unclear:

1. Which image is the official source of truth?
2. Are any images outdated, rejected, or only inspirational?
3. Which elements must remain unchanged across all generated assets?
4. Which elements may change by scene, action, or campaign?
5. Should the output strictly match the reference, or only preserve the character identity?
6. Is the reference used for character identity, drawing style, color palette, pose, or mood?
7. Are there existing brand colors, logo rules, or forbidden modifications?

## Reference Fidelity Levels

Ask or infer a fidelity level before generation.

| Level | Use Case | Rule |
|---|---|---|
| Strict | official stickers, merch, paid campaign visuals | preserve anchors, proportions, line style, palette, and rendering closely |
| Balanced | social posts, seasonal visuals, memes | preserve identity anchors and style while allowing pose/scene creativity |
| Loose | early ideation, brainstorming, trend exploration | preserve recognizable identity but allow broader visual experimentation |

Default: **Balanced** unless the user asks for merch, official visuals, or strict consistency.

## Extraction Checklist

From reference images, extract:

- silhouette and overall contour;
- head/body proportion;
- face construction and eye/mouth logic;
- signature accessories or marks;
- line thickness and line closure style;
- corner softness and curve language;
- color palette and color ratio;
- shading/rendering method;
- texture or grain;
- costume and prop rules;
- emotional range;
- allowed exaggeration level;
- background relationship;
- text placement conventions, if any;
- visual defects to avoid.

## Output Format

After reference intake, produce:

```markdown
# Reference Image Intake Report

## Reference Inventory
| Ref | Role | Reliability | Notes |
|---|---|---|---|
| Ref A | Primary / Style / Pose / Expression / Material / Negative | High / Medium / Low | |

## Extracted IP Invariants
- Silhouette:
- Proportions:
- Line Language:
- Drawing Style:
- Color System:
- Visual Anchors:
- Face Construction:
- Rendering Rules:

## Allowed Variations
- Poses:
- Expressions:
- Props:
- Scenes:
- Seasonal / trend elements:

## Forbidden Drift
- Style drift:
- Color drift:
- Proportion drift:
- Structural drift:
- Accessory drift:
- Mood drift:

## Recommended Fidelity Level
- Strict / Balanced / Loose:
- Reason:

## Missing Information
- Questions to ask before generation:
```

## Conflict Resolution

If multiple references disagree, do not average them blindly. Use this priority order:

1. user-designated primary reference;
2. most recent official artwork;
3. official brand guideline or character sheet;
4. repeated features across multiple references;
5. material-specific references only for that material type;
6. older or stylistic references only when confirmed.

If conflicts remain, ask the user to choose.

## Image Generation Rule

For direct image generation, include the reference-derived invariants in the prompt. The prompt should explicitly state that poses, expressions, scenes, and props may change, but line language, drawing style, color ratio, construction, and visual anchors must remain stable.

