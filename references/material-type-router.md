# Material Type Router

IPilot must route the workflow by material category before detailed concept generation. This prevents the Skill from using one generic asset process for every output.

The router has two jobs:

1. classify the requested material type;
2. decide what information must be confirmed before production.

## Routing rule

After the initial user request and before detailed concept generation, classify the requested output into one of these channels:

1. **IP identity assets**: IP introduction cards, mascot profile cards, avatar images, reference sheets, expression sheets, pose sheets, brand banners, profile headers.
2. **Community interaction assets**: stickers, emojis, chat reaction images, comment reply cards, welcome cards, fan badges, contributor badges.
3. **Meme and humor assets**: meme concept packs, reaction meme templates, four-panel comics, relatable pain-point memes, seasonal meme packs, trend-adapted cards.
4. **Digital promotional assets**: posters, social covers, campaign cards, announcement images, short-video covers, carousel cards, launch graphics, event visuals.
5. **Occasion-based assets**: IP birthday visuals, holiday greetings, festival posters, anniversary visuals, seasonal cards, countdown series, milestone celebration cards.
6. **Educational / explanatory assets**: explainer cards, glossary cards, tutorial thumbnails, workshop cards, science / technical visual cards.
7. **Lifecycle / retention assets**: weekly mood stickers, check-in cards, achievement badges, milestone cards, monthly calendar cards.
8. **Physical / tangible materials**: sticker sheets, badges, acrylic stands, keychains, tote bags, T-shirts, postcards, packaging, booth materials, flyers, standees, printed coupons.
9. **Hybrid asset systems**: online preview plus offline production, such as birthday key visual + sticker pack + physical postcard.

## Mandatory question rules

### If the material type is unclear

Ask for material type confirmation before detailed concepts.

Minimum question:

> Which material type should we produce first? Options could include sticker pack, meme pack, IP birthday visual, holiday greeting card, campaign poster, platform social post, physical sticker sheet, badge, acrylic stand, or a multi-asset campaign pack.

Do not generate detailed captions, prompts, or images until the user confirms, unless the user explicitly authorizes IPilot to choose.

### If the output is a digital promotional asset

Ask for the target publishing platform before detailed concept generation if the platform is missing.

Minimum question:

> Which platform will this be published on? Xiaohongshu, WeChat, Bilibili, Douyin, X, Instagram, or another platform?

Then apply platform adaptation rules.

### If the output is an occasion-based asset

Ask for the occasion context before detailed concept generation if it is missing.

Minimum question:

> What occasion is this for, when will it be published, and should it be a single visual or a series? Examples: IP birthday, holiday greeting, festival poster, anniversary card, seasonal campaign, countdown series.

If the output is digital, also ask for platform. If the output is physical, also ask for audience and production context.

### If the output is a physical / tangible material

Ask for the audience orientation before detailed concept generation if it is missing.

Minimum question:

> Who is this physical material for, and what audience style should it lean toward? Examples: children, students, fans, customers, employees, premium buyers, conference visitors, community contributors.

Then apply physical material audience rules.

### If the output is hybrid

Ask for every required branch:

1. target publishing platform;
2. physical material audience orientation and production context;
3. occasion context, if tied to birthday, holiday, festival, anniversary, seasonal campaign, or milestone.

## Decision table

| User request | Route | Must ask before generation |
|---|---|---|
| "Make a campaign poster" | Digital promotional asset | Target platform and placement |
| "Make a Xiaohongshu cover" | Digital promotional asset | None if platform and format are clear |
| "Make a sticker pack for WeChat" | Community interaction asset | Sticker usage context and humor boundary if missing |
| "Make some memes" | Meme and humor asset | Humor boundary, audience, and platform if missing |
| "Make an IP birthday visual" | Occasion-based asset | Date/window, platform, tone, output format |
| "Make a holiday greeting card" | Occasion-based asset | Holiday, cultural constraints, platform, tone |
| "Make badges for fans" | Physical material | Audience orientation and production use |
| "Make an acrylic standee" | Physical material | Audience, size/shape/material constraints if known |
| "Make a booth poster and social post" | Hybrid | Platform and offline scene |
| "I do not know what to make" | Material type confirmation / asset opportunity mapping | Goal and preferred channel |

## Output implication

The route must affect:

- questions asked;
- asset opportunity recommendations;
- platform, occasion, or physical constraints;
- image prompt structure;
- caption/text density;
- review rubric;
- final delivery format.

Do not proceed as if all materials are ordinary social-media images.

