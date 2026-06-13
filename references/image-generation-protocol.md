# Image Generation Protocol

IPilot can prepare image-generation prompts or invoke an available image-generation tool. Image generation must be gated by IP consistency, reference-image fidelity, brand safety, and user confirmation unless the user explicitly authorizes automatic generation.

## Trigger conditions

Invoke image generation only when all conditions are satisfied:

1. The user wants visual creation, not only strategy or copywriting.
2. The IP profile has enough fixed visual features and, when consistency matters, a Deep IP Visual Consistency Profile with line language, drawing style, color ratio, shape construction, and visual anchors.
3. The desired asset type is clear.
4. The material route is clear. For digital promotional assets, the target platform and placement are clear. For physical materials, the audience orientation and usage context are clear.
5. The visual style is specified or safely inferable.
6. The concept has passed the safety and consistency review.
7. Safety risk is Low or Medium-Low.
8. The final prompt includes all invariant features, deep visual consistency constraints, production-quality constraints, and forbidden changes.
9. Reference images, if required, are uploaded or accessible in the current environment.
10. Reference image roles, source of truth, and fidelity level are clear when references are used.
11. The user has approved the selected concept or explicitly authorized automatic generation.

## Do not invoke image generation when

- The IP identity is under-specified.
- Fixed visual features are missing.
- The user only asks for brainstorming.
- Safety risk is Medium-High or High.
- The request relies on copyrighted characters or famous mascots without user ownership.
- The requested output would distort the IP beyond recognition.
- The prompt asks for hateful, sexualized, discriminatory, political-persuasion, harassing, or brand-damaging content.

## Pre-generation checklist

- IP Consistency Profile exists.
- Fixed visual features and deep visual grammar are included in the prompt.
- Forbidden visual changes are included in negative constraints.
- Material route and asset type are specified.
- Platform and placement are specified for digital promotional assets.
- Physical audience orientation and usage context are specified for tangible materials.
- Caption is short enough or handled outside the image as a separate text layer.
- Safety review has passed.
- Reference image status, source of truth, and fidelity level are clear.
- Confirmation Gate 2 has been satisfied, unless automatic generation was explicitly authorized.

## Prompt structure

```text
Create a [asset_type] for [platform_or_physical_context].
Existing IP character: [ip_name].
Reference source of truth, if any: [primary_reference_and_scope].
Reference fidelity level: [strict / balanced / loose].
Fixed visual features that must be preserved: [fixed_features].
Deep visual consistency constraints: [line_language], [drawing_style], [color_ratio], [shape_construction], [visual_anchors].
Production-quality constraints: complete construction, clean closed lines when applicable, stable color fills, coherent elements, no melted accessories, no random text unless requested.
Personality to express: [personality_invariants].
Scene: [scene].
Action: [ip_action].
Facial expression: [expression].
Visual style: [visual_style].
Composition: [composition].
Platform adaptation or physical production constraints: [constraints].
Caption text, if any: [caption].
Avoid: [forbidden_visual_changes], [forbidden_topics], [brand_safety_constraints], [forbidden_reference_drift].
The character must remain visually consistent with the provided IP profile and any uploaded reference image. Poses, expressions, scenes, props, and occasion/trend elements may change, but the IP's line language, drawing style, color ratio, visual anchors, silhouette, construction, and production quality must remain stable.
```

## Text handling and font direction

IPilot can design text layout, but should usually keep final typography as a separate design layer. Provide font direction and text hierarchy, then recommend that the user finish layout in a design tool when exact Chinese text matters.

Prefer separating image text from the visual prompt when:

- the caption is longer than 8-10 Chinese characters or 3-5 English words;
- the platform allows adding text after generation;
- text accuracy is important;
- the image model is likely to render text incorrectly.

If text must be inside the image, keep it short, high-contrast, and explicitly state that the text should be rendered as a caption layer or signboard.

## Post-generation review

Evaluate the generated image using:

- Reference Fidelity;
- Identity Anchors;
- Line Language;
- Drawing Style;
- Color System;
- Shape Construction;
- Production Quality;
- Visual Consistency;
- Personality Consistency;
- Brand Fit;
- Text Accuracy;
- Safety Risk;
- Platform Fit, for digital assets;
- Physical Material Fit, for tangible assets.

Then output one of:

- **Accept**: usable as-is.
- **Minor revision**: small prompt, layout, or caption changes needed.
- **Regenerate**: major consistency, safety, or usability issue.

## Revision prompt pattern

```text
Regenerate the same asset while preserving [fixed_features], [primary_reference_identity], [line_language], [drawing_style], [color_ratio], [shape_construction], and [visual_anchors]. Correct these issues: [issues]. Keep the same scene, action, expression, and platform format unless the issue requires a composition change. Ensure complete construction, clean closed lines, stable color fills, coherent elements, and no random text unless requested. Avoid [negative_constraints] and [forbidden_reference_drift].
```

