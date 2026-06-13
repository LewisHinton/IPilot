# IP Consistency System

IPilot treats IP consistency as visual grammar, not only as a list of fixed features.

The default assumption is:

- poses may change;
- expressions may change;
- scenes may change;
- props may change;
- campaign contexts may change;
- the IP's visual grammar must remain stable.

## 1. Consistency layers

### Layer A - Identity anchors

Identity anchors are the features that make the IP recognizable at a glance.

Examples:

- species / object type;
- signature silhouette;
- iconic accessory;
- facial landmark;
- mascot emblem;
- fixed costume element;
- repeated symbolic motif.

These should be preserved in every generated asset unless the user explicitly approves a temporary themed variation.

### Layer B - Line language

Line language defines how the IP is drawn.

Track:

- line thickness;
- line weight variation;
- rounded vs sharp line endings;
- clean vector vs sketchy hand-drawn lines;
- closed-line requirement;
- outline color;
- internal detail-line density.

Common failures:

- the line becomes too realistic;
- outlines become broken or noisy;
- line weight changes between assets;
- decorative details overwhelm the IP silhouette.

### Layer C - Drawing style

Drawing style defines the visual system of the IP.

Track:

- chibi / flat vector / 3D toy / pixel art / hand-drawn / anime-inspired / brand illustration;
- degree of realism;
- detail density;
- edge softness;
- shading method;
- texture style;
- background complexity.

The asset may use different scenes, but the IP character itself should retain its drawing style.

### Layer D - Color system

Color consistency is not only "use the same colors". It includes color proportion.

Track:

- primary color;
- secondary color;
- accent color;
- neutral color;
- approximate color ratio;
- saturation level;
- contrast level;
- gradient / flat-fill rules;
- forbidden color drift.

Recommended format:

```text
Primary color: warm orange, about 60%
Secondary color: soft cream, about 25%
Accent color: blue scarf, about 10%
Neutral / shadow: about 5%
```

Common failures:

- the accent color dominates;
- the IP becomes a different color family;
- shadows shift the character into a different mood;
- platform backgrounds reduce recognizability.

### Layer E - Shape language and construction

Shape language defines how the character is built.

Track:

- round / square / triangular design logic;
- head-to-body ratio;
- eye-to-face proportion;
- limb proportion;
- accessory scale;
- symmetry / asymmetry;
- negative space;
- silhouette clarity;
- structural balance.

The IP can act differently, but the body construction should remain coherent.

### Layer F - Rendering quality

Generated assets must be production-usable, not merely conceptually correct.

Check:

- complete character construction;
- closed outlines where needed;
- clean color fills;
- no broken limbs;
- no melted accessories;
- no duplicated faces;
- no accidental extra fingers / ears / tails / props;
- no cropped character unless composition requires it;
- no inconsistent lighting on the IP;
- no clutter that destroys readability;
- no low-resolution or muddy rendering.

### Layer G - Personality expression

Personality should remain stable even when the emotion changes.

Examples:

- a gentle IP can be surprised, but not cruel;
- a professional IP can be funny, but not vulgar;
- a rebellious IP can be energetic, but not hateful;
- a sleepy IP can be exaggerated, but not visually degraded.

## 2. Fixed vs flexible rules

### Usually fixed

- species / object identity;
- silhouette family;
- line language;
- drawing style;
- color palette and approximate ratio;
- iconic accessory;
- facial proportion;
- core personality;
- brand-safe tone.

### Usually flexible

- pose;
- gesture;
- facial expression;
- scene;
- background;
- props;
- seasonal costume details;
- platform layout;
- campaign message;
- sticker caption.

### Conditionally flexible

- costume color;
- accessory variation;
- facial simplification;
- lighting style;
- themed decorations;
- text plate shape;
- background style.

Conditionally flexible elements require user confirmation if they may weaken recognizability.

## 3. Deep IP Consistency Profile

Before image generation, build or infer this profile:

```markdown
# Deep IP Consistency Profile

## Identity Anchors
- Character type:
- Signature silhouette:
- Fixed visual anchors:
- Iconic accessory / motif:

## Line Language
- Outline style:
- Stroke thickness:
- Stroke ending:
- Internal line density:
- Closed-line requirement:

## Drawing Style
- Style category:
- Detail density:
- Shading method:
- Texture method:
- Realism level:

## Color System
- Primary color and ratio:
- Secondary color and ratio:
- Accent color and ratio:
- Neutral / shadow rule:
- Forbidden color drift:

## Shape and Construction
- Head-to-body ratio:
- Face proportion:
- Limb / body construction:
- Accessory scale:
- Silhouette rule:
- Structural balance rule:

## Flexible Motion Space
- Allowed poses:
- Allowed expressions:
- Allowed props:
- Allowed backgrounds:
- Allowed seasonal / trend variations:

## Quality Constraints
- Required completeness:
- Line closure:
- Color fill quality:
- Element construction:
- Cropping rule:
- Background complexity:
```

## 4. Consistency scoring

Use these dimensions before image generation and after generation:

| Dimension | Question | Pass condition |
|---|---|---|
| Identity Anchors | Can the IP be recognized immediately? | all key anchors preserved |
| Line Language | Does the line work match the IP? | stroke, closure, and detail density stable |
| Drawing Style | Does the drawing belong to the same visual system? | style category and rendering method stable |
| Color System | Are color ratios and accents stable? | no major palette drift |
| Shape Construction | Is the IP structurally coherent? | proportions and silhouette stable |
| Flexible Variation | Are pose/expression/scene changes controlled? | variation does not damage identity |
| Production Quality | Is the image usable? | complete, clean, non-broken visual output |

## 5. Prompt discipline

Every image prompt should separate:

- invariant visual grammar;
- allowed variation;
- production-quality constraints;
- negative constraints.

Recommended prompt pattern:

```text
Create [asset type] featuring [IP name], a [character type] with [identity anchors]. Preserve the IP's line language: [line language]. Preserve the drawing style: [drawing style]. Preserve the color system: [primary/secondary/accent ratio]. The character may change pose/expression to [allowed variation], but must keep [visual anchors]. Ensure complete character construction, closed clean outlines, stable color fills, coherent anatomy/object structure, and no broken or melted elements. Avoid [forbidden changes].
```

## Reference-image extension

When reference images are available, the IP consistency system should be grounded in the reference-derived visual system.

Add these fields to the consistency profile:

- Reference source of truth;
- Supporting reference roles;
- Reference fidelity level;
- Reference-derived visual anchors;
- Reference-derived line language;
- Reference-derived drawing style;
- Reference-derived color ratio;
- Reference-derived construction rules;
- Forbidden reference drift.

Reference images do not freeze every visible detail. They identify what must stay recognizable. Poses, expressions, camera angle, props, scene, seasonal elements, and trend elements may change unless the user labels them as identity anchors.

## Reference fidelity scoring

| Score | Meaning |
|---:|---|
| 9-10 | preserves source-of-truth identity, style, palette, construction, and anchors; only allowed variations changed |
| 7-8 | recognizable but minor drift in proportions, line detail, or color ratio |
| 5-6 | identity is partially preserved but style or construction drift is visible |
| 3-4 | character is difficult to recognize as the same IP |
| 1-2 | generated character is effectively a different IP |

A production candidate should normally score at least 8 for reference fidelity when reference images are used.



