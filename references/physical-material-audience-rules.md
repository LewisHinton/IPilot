# Physical Material Audience Rules

IPilot should handle tangible materials differently from digital promotional images. Physical materials have audience, production, cost, durability, and usage constraints.

## Mandatory audience question

If the user asks for physical materials but does not specify audience orientation, ask:

> Who is this physical material for, and what audience style should it lean toward? Examples: children, students, fans, customers, employees, premium buyers, conference visitors, community contributors.

Do not generate final physical material concepts before this is answered unless the user authorizes IPilot to infer the safest default.

## Required physical material brief

Ask or infer these fields:

- Material Type: sticker, badge, acrylic standee, keychain, tote bag, T-shirt, postcard, package, flyer, booth poster, standee, coupon, card.
- Audience Orientation: children, students, fans, customers, employees, contributors, collectors, premium users, event visitors.
- Distribution Context: paid product, free giveaway, event booth, purchase bonus, internal culture, onboarding, fan merch, packaging insert.
- Usage Scenario: daily use, display, collection, wearing, sharing, scanning QR code, event check-in, decoration.
- Design Tone: cute, premium, playful, professional, energetic, collectible, minimal, ceremonial.
- Production Constraints: size, material, color limit, print method, transparent/white background, one-sided/two-sided, budget tier.
- Safety Constraints: age suitability, choking risk for small items, sharp edges, washable/wearable concerns, brand reputational risk.

## Audience orientation matrix

| Audience | Design Bias | Copy Bias | Material Bias | Risk Notes |
|---|---|---|---|---|
| Children | simple, soft, high-recognition | gentle, no sarcasm | safe shapes, durable, non-sharp | avoid small detachable parts and mature humor |
| Students | energetic, meme-aware, affordable | relatable, light humor | stickers, badges, cards, tote bags | avoid insulting academic pressure |
| Fans / community members | collectible, expressive, insider references | identity-building | badge sets, acrylic stands, sticker sheets | avoid excluding newcomers too strongly |
| Customers | clear brand value, practical | benefit-led, friendly | package inserts, coupons, product cards | avoid overcomplicated lore |
| Employees | professional, culture-building | internal pride, appreciation | onboarding cards, desk stickers, badges | avoid cringe or forced humor |
| Premium buyers | refined, minimal, high-quality | restrained, ceremonial | acrylic, metal badge, fabric, thick card | avoid cheap-looking layouts |
| Event visitors | high-recognition, fast comprehension | CTA-oriented | flyers, booth posters, handouts | ensure event info and QR space are readable |
| Open-source contributors | community-native, technical, badge-like | appreciative, witty | stickers, badges, README graphics | avoid corporate over-polish |

## Physical material concept output

For physical materials, each concept should include:

```markdown
## Physical Concept [Number]: [Title]

- Material Type:
- Audience Orientation:
- Distribution Context:
- Usage Scenario:
- IP Pose / Expression:
- Front-side Design:
- Back-side Design, if any:
- Copy / Text:
- Suggested Size / Shape:
- Material / Finish Suggestion:
- Production Notes:
- Safety Notes:
- IP Consistency Notes:
- Revision Priority:
```

## Physical production caution

IPilot can provide design concepts and prompts, but it should not claim manufacturing feasibility without user-provided vendor, material, budget, and production details.

For final production, tell the user to verify:

- exact size;
- bleed and safe margin;
- color mode and print profile;
- material availability;
- minimum order quantity;
- production cost;
- shipping and event deadlines;
- age-safety requirements when relevant.

