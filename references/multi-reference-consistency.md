# Multi-Reference Consistency

IPilot often receives several IP images: a main character image, old sticker samples, event posters, rough sketches, or user-preferred style references. Multi-reference handling is necessary because not all references have the same authority.

## Core Rule

Do not treat every reference image as equally authoritative.

Each reference must be labeled by role, reliability, and scope.

## Reference Authority Matrix

| Authority | Description | Use |
|---|---|---|
| Source of Truth | Official current character sheet or primary image | Highest priority for identity |
| Official Variant | Official artwork in a different pose or scene | Useful for variation range |
| Historical Variant | Old official art | Use only if compatible or confirmed |
| Fan / Draft / Experimental | Non-final or user-generated art | Inspiration only |
| Negative Example | What to avoid | Convert to negative constraints |

## Scope Tags

Assign scope tags to each reference:

- identity: defines the character itself;
- style: defines drawing/rendering style;
- color: defines palette or color ratio;
- pose: defines action range;
- expression: defines emotional range;
- material: defines format-specific layout;
- trend: defines meme or seasonal adaptation;
- negative: defines what not to do.

## Consistency Extraction Method

1. Identify the primary source of truth.
2. Extract stable identity anchors from the primary source.
3. Compare other references against the primary source.
4. Mark repeated features as high-confidence invariants.
5. Mark conflicting features as unresolved.
6. Ask the user to resolve unresolved conflicts if they affect generation.
7. Convert style/material-only references into scoped constraints, not global character identity.

## Conflict Types

| Conflict | Example | Action |
|---|---|---|
| Color conflict | scarf is blue in one image, green in another | ask which is official |
| Proportion conflict | chibi in one image, tall in another | ask if both are allowed styles |
| Style conflict | flat vector vs watercolor | ask output style or use material-specific style |
| Accessory conflict | glasses present in some images only | ask if accessory is required anchor |
| Mood conflict | soft cute vs aggressive | follow brand safety and user intent |

## Multi-Reference Output

```markdown
# Multi-Reference Consistency Map

## Primary Source of Truth
- Image:
- Reason:

## Supporting References
| Ref | Scope | Use | Reliability |
|---|---|---|---|

## High-Confidence Invariants
- 

## Flexible Variants
- 

## Unresolved Conflicts
| Conflict | Options | Needed User Decision |
|---|---|---|

## Final Consistency Rule
- Preserve:
- May vary:
- Must avoid:
```

## Generation Policy

When the user provides multiple references, image-generation prompts must identify which reference controls identity, which controls style, and which controls pose or material layout.

Never merge incompatible references without stating the compromise.

