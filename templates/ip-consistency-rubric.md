# IP Consistency Rubric

Use this rubric before final delivery, before image generation, and after image generation.

IPilot treats IP consistency as visual grammar. Poses, expressions, scenes, props, and trend elements may change. The line language, drawing style, color system, visual anchors, shape construction, and production quality should remain stable.

## Deep visual consistency scoring table

| Dimension | 10 | 7 | 4 | 1 |
|---|---|---|---|---|
| Reference Fidelity | Source-of-truth identity and scoped reference constraints preserved | Minor drift from reference | Noticeable drift in style, color, or construction | No longer resembles reference IP |
| Identity Anchors | All visual anchors preserved and recognizable | One weak anchor | Multiple anchors weak or missing | IP becomes another character |
| Line Language | Stroke, outline, closure, and detail density match the IP | Minor line drift | Obvious line-style mismatch | Broken/noisy/incompatible line work |
| Drawing Style | Same visual system and rendering method | Slight style drift | Mixed or unstable style | Completely different style |
| Color System | Palette and approximate ratios preserved | Minor color drift | Accent or primary color ratio unstable | Wrong color family |
| Shape Construction | Proportions, silhouette, and structure coherent | Minor construction awkwardness | Proportions drift noticeably | Broken or incoherent construction |
| Visual Quality | Complete, clean, production-usable | Minor cleanup needed | Several visual defects | Unusable output |
| Flexible Variation Control | Pose/expression/scene changes strengthen the asset | Variation mostly controlled | Variation weakens recognizability | Variation destroys identity |
| Personality Consistency | Fully matches persona | Mostly matches | Tone drifts | Contradicts persona |
| Brand Fit | Strongly supports brand | Acceptable | Weak fit | Damages brand |
| Creative Strength | Fresh and usable | Solid but common | Generic | Confusing or stale |
| Platform / Physical Suitability | Native to target use | Minor adaptation needed | Weak fit | Unsuitable |
| Safety | Low risk | Medium-low risk | Medium-high risk | High risk / reject |

## Required review dimensions

| Dimension | Score / Level | Notes |
|---|---:|---|
| Reference Fidelity | /10 | if reference images are used |
| Identity Anchors | /10 | |
| Line Language | /10 | |
| Drawing Style | /10 | |
| Color System | /10 | |
| Shape Construction | /10 | |
| Visual Quality | /10 | |
| Flexible Variation Control | /10 | |
| Personality Consistency | /10 | |
| Brand Fit | /10 | |
| Creative Strength | /10 | |
| Platform Suitability | /10 | for digital assets |
| Occasion Suitability | /10 | for occasion assets |
| Physical Material Suitability | /10 | for tangible materials |
| Text Layout Suitability | /10 | for text-heavy assets |
| Misinterpretation Risk | Low / Medium / High | |
| Copyright Risk | Low / Medium / High | |
| Offensive Content Risk | Low / Medium / High | |
| Trend Adaptation Risk | Low / Medium / High | if trend-based |
| Final Recommendation | Generate / Revise / Reject | |

## Decision rule

- **Generate**: reference fidelity >= 8 when references are used, identity anchors >= 8, line language >= 8, drawing style >= 8, color system >= 8, shape construction >= 8, visual quality expectation >= 8, brand fit >= 8, and safety risk Low or Medium-Low.
- **Revise**: any key score between 5 and 7, or safety risk Medium.
- **Reject**: any key score <= 4, safety risk High, direct conflict with forbidden changes, or production quality too poor to use.

## Common failure patterns

- The IP keeps the name but changes species or object type.
- Reference source of truth is ignored.
- Signature accessory disappears.
- Color palette or color ratio drifts.
- The line style becomes sketchy, noisy, too realistic, or inconsistent.
- The drawing style changes from flat vector to realistic rendering without approval.
- The character construction becomes broken, incomplete, or visually melted.
- The image contains random or unreadable text.
- The pose is creative but weakens the silhouette.
- The humor attacks the target audience.
- The prompt relies on a copyrighted character for recognizability.
- The caption is funny but not brand-safe.
- The image contains too much text to render reliably.

