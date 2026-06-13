# Asset Output Template

## Asset [Number]: [Title]

- Asset Type:
- Material Route: identity / community / meme / digital promotional / occasion / educational / lifecycle / physical / hybrid
- Use Case:
- Platform / Occasion / Physical Distribution Context:
- Platform Placement / Occasion Timing / Physical Audience:
- Platform / Occasion / Production Constraints:
- Scene:
- IP Action:
- Facial Expression:
- Caption / Text:
- Text Layout Plan:
- Font Direction:
- Visual Composition:
- Image Generation Prompt:
- Negative Prompt / Avoid:
- Reference Fidelity Notes:
- Deep IP Consistency Notes:
- Visual Quality Notes:
- Brand Safety Notes:
- Revision Priority:


## Reference image requirements

Use this section when reference images are provided.

- Primary Reference / Source of Truth:
- Supporting Reference Roles:
- Reference Fidelity Level: strict / balanced / loose
- Reference-Derived Visual Anchors:
- Reference-Derived Style Rules:
- Allowed Reference-Based Variations:
- Forbidden Reference Drift:

## Deep IP consistency requirements

Use this section when visual stability matters.

- Identity Anchors:
- Line Language:
- Drawing Style:
- Color System / Ratio:
- Shape and Construction Rules:
- Flexible Elements Allowed:
- Production Quality Constraints:
- Text Rendering Rule:

## Digital platform adaptation

Use this section for digital promotional assets.

- Target Platform:
- Placement:
- Aspect / Layout Logic:
- Text Density:
- Safe Area / Overlay Notes:
- CTA Placement:
- Caption Strategy:

## Occasion-based notes

Use this section for IP birthday, holiday, festival, anniversary, seasonal, or milestone assets.

- Occasion Type:
- Date or Publishing Window:
- Cultural Context:
- Desired Tone:
- Single Asset or Series:
- Mandatory Text / Hashtag / CTA:
- Cultural or Brand Sensitivity Notes:

## Physical material production notes

Use this section for tangible materials.

- Material Type:
- Audience Orientation:
- Distribution Context:
- Usage Scenario:
- Suggested Size / Shape:
- Material / Finish Suggestion:
- Front-side Design:
- Back-side Design:
- Production Cautions:

## Prompt handoff

Use this section when the asset is ready for image generation.

```text
Create a [asset_type] for [platform_or_physical_context]. Existing IP character: [ip_name]. Reference source of truth, if any: [primary_reference_and_scope]. Reference fidelity level: [strict / balanced / loose]. Fixed visual features that must be preserved: [fixed_features]. Deep visual consistency constraints: [line_language], [drawing_style], [color_ratio], [shape_construction], [visual_anchors]. Production-quality constraints: complete construction, clean closed lines when applicable, stable color fills, coherent elements, no melted accessories, no random text unless requested. Personality to express: [personality_invariants]. Scene: [scene]. Action: [action]. Facial expression: [expression]. Visual style: [style]. Composition: [composition]. Platform or production constraints: [constraints]. Caption text, if any: [caption]. Avoid: [negative_constraints]. Preserve the IP identity and do not add unrelated characters.
```

## Safety & Consistency Review

| Dimension | Score / Level | Notes |
|---|---:|---|
| Reference Fidelity | /10 | if reference images are used |
| Identity Anchors | /10 | |
| Line Language | /10 | |
| Drawing Style | /10 | |
| Color System | /10 | |
| Shape Construction | /10 | |
| Production Quality | /10 | |
| Visual Consistency | /10 | |
| Personality Consistency | /10 | |
| Brand Fit | /10 | |
| Creative Strength | /10 | |
| Platform Suitability | /10 | for digital assets |
| Occasion Suitability | /10 | for occasion-based assets |
| Physical Material Suitability | /10 | for tangible materials |
| Misinterpretation Risk | Low / Medium / High | |
| Copyright Risk | Low / Medium / High | |
| Offensive Content Risk | Low / Medium / High | |
| Final Recommendation | Generate / Revise / Reject | |

## Confirmation before generation

Use this section before invoking image generation.

```markdown
## Confirmation Gate 2 - Approve Image Generation

Selected concept: [title]
Asset type: [asset type]
Material route: [identity / community / meme / digital / occasion / physical / hybrid]
Platform, occasion, or physical context: [context]
Safety result: [Low / Medium-Low]
Reference fidelity score, if applicable: [score]
IP consistency score: [score]

Image prompt:
[final prompt]

Avoid:
[negative constraints]

Please confirm one option:
- Generate this image
- Revise the concept
- Choose another concept
```


