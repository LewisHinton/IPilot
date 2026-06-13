# Visual Quality Control

IPilot should not accept a generated asset only because the idea is correct. The image must also be visually usable.

## Pre-generation quality constraints

Before invoking image generation, prompts should specify:

- complete character or intentional crop;
- clean closed lines when the style uses outlines;
- coherent body / object construction;
- stable color fills;
- no melted accessories;
- no duplicate faces or limbs;
- no accidental extra objects;
- readable silhouette;
- low background clutter;
- transparent background if needed for stickers;
- text-free image when the user plans to add typography later.

## Post-generation review

After generation, evaluate:

| Dimension | Pass | Revise | Reject |
|---|---|---|---|
| Completeness | full intended asset visible | minor crop | key element missing |
| Line quality | clean and closed | small breaks | broken / noisy lines |
| Color quality | stable fills and palette | slight drift | muddy / wrong palette |
| Construction | coherent structure | minor awkwardness | broken body / object |
| Visual anchors | all anchors present | one weak anchor | anchor missing |
| Background | supports asset | mild clutter | distracts from IP |
| Text handling | no unwanted text | minor artifact | unreadable or wrong text |

## Regeneration triggers

Regenerate or revise the prompt if:

- the IP species or object type changes;
- the signature accessory disappears;
- the color ratio changes substantially;
- the line style changes substantially;
- the asset has broken limbs, melted accessories, duplicated faces, or incomplete construction;
- the image includes unwanted random text;
- the background dominates the character;
- the result cannot be used as a sticker, poster, or social asset without major repair.

## Revision prompt pattern

```text
Regenerate with stricter IP consistency. Preserve [identity anchors], [line language], [drawing style], and [color ratio]. Keep the new pose/expression, but fix: [issue list]. Ensure clean closed outlines, coherent construction, complete elements, stable color fills, and no random text.
```

## Reference-driven quality checks

When a reference image is used, visual quality is not only general polish. It also includes reference fidelity.

Reject or revise if the generated image has:

- changed signature accessories or marks;
- changed the primary color ratio without user approval;
- changed the drawing style or line language;
- changed the head/body or object construction beyond the allowed range;
- hidden an identity anchor behind props or text;
- merged separate accessories into the body;
- added random features not present in the IP system;
- made the character less recognizable than the reference.

A generated asset may change pose, expression, background, props, and seasonal/trend decoration, but these changes should not block or overwrite the IP's core anchors.

