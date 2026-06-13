# Reference Image Workflow Demo

This demo shows how IPilot should handle an existing IP with reference images before generating assets.

## User Request

> I already have an IP character called Pixel Deer. I uploaded its official front-view image and two old sticker samples. Please help me create a festival greeting visual and a small reaction sticker pack while keeping the IP consistent.

## Step 1 - Reference Image Intake

IPilot classifies the references:

| Ref | Role | Reliability | Notes |
|---|---|---|---|
| A | Primary reference | High | Official current front-view image |
| B | Expression reference | Medium | Old sticker; useful for emotional range |
| C | Material reference | Medium | Old sticker; useful for sticker layout, not final color |

## Step 2 - Extracted IP Invariants

- Character: small deer mascot.
- Silhouette: round head, short antlers, compact chibi body.
- Visual anchors: star-shaped forehead mark, scarf, small square hooves.
- Line language: clean closed rounded outlines, medium-weight strokes.
- Drawing style: flat vector sticker style with soft highlights.
- Color system: warm beige body, cream face area, red scarf, small yellow star accent.
- Construction: large head, small body, antlers must remain symmetrical.

## Step 3 - Allowed Variations

- Expressions may change: happy, shy, surprised, proud, sleepy.
- Poses may change: waving, holding a lantern, carrying a gift, jumping.
- Scene may change: festival lights, greeting card background, transparent sticker background.
- Props may change if they do not cover the forehead star or scarf.

## Step 4 - Conflict Resolution

Old sticker sample C uses a blue scarf, but the official reference A uses a red scarf. IPilot asks:

> The official image uses a red scarf, while an old sticker uses a blue scarf. Should the red scarf be treated as the current fixed visual anchor?

User confirms red scarf.

## Step 5 - Confirmed Consistency Rule

Preserve: deer species, chibi proportions, short antlers, star mark, red scarf, rounded closed line style, warm beige/cream/yellow palette.

May vary: pose, expression, festival props, background, scene lighting.

Must avoid: changing scarf color, hiding the star mark, making the deer realistic, adding broken outlines, adding messy color fills.

## Step 6 - Asset Concepts

### Asset 1: Festival Greeting Key Visual

- Asset Type: occasion-based digital promotional asset
- Platform: Xiaohongshu and WeChat
- Scene: Pixel Deer holding a small lantern under soft festival lights
- IP Action: waving with one hoof while holding the lantern
- Caption: separate text layer, not rendered by image model
- Font Direction: rounded sans-serif, warm festive tone
- Image Prompt: Create a festival greeting key visual featuring Pixel Deer, a small chibi deer mascot with short antlers, star-shaped forehead mark, red scarf, small square hooves, warm beige body and cream face area. Preserve the clean closed rounded outlines, flat vector sticker style, and soft highlights. Pixel Deer is waving while holding a small lantern in a warm festival background. Pose and scene may change, but preserve the IP's silhouette, scarf, star mark, antlers, color ratio, and construction. Avoid changing the scarf color, hiding the forehead star, realistic animal anatomy, messy outlines, broken linework, incomplete limbs, incorrect color fills, and random text.

### Asset 2: Reaction Sticker Pack

- Sticker 1: "收到!" - happy salute
- Sticker 2: "我在努力" - sleepy but determined
- Sticker 3: "太会了" - proud sparkle
- Sticker 4: "先别急" - calming gesture

## Step 7 - Generation Gate

IPilot asks:

> The concept passed consistency and safety review. Generate the festival key visual first, or generate the reaction sticker pack first?



