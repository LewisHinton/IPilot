# Confirmation Gates

IPilot uses confirmation gates to keep the user in the loop. The purpose is not to slow down the workflow, but to prevent wasted generation and preserve IP consistency.

Use `human-in-the-loop-dialogue.md` for the conversational cadence around these gates. Every gate should include a short recap, a recommended next step, clear choices, and a pause unless the user has explicitly authorized automatic continuation.

## Gate 0 - Material type confirmation

Use before detailed concepts when the user has not clearly selected the output type.

### Trigger

Use this gate when the user asks for "ideas", "assets", "something for my IP", "help me make materials", or any request where multiple material routes would fit.

### Assistant behavior

Present 5-8 suitable material types, recommend one starting point, and ask the user to choose, combine options, or authorize IPilot to auto-pick.

### Output format

```markdown
## Confirmation Gate 0 - Choose Material Type

Current understanding:
- IP: [name or description]
- Goal: [goal]

I recommend starting with [material type] because [reason].

Choose one:
- A: [material type]
- B: [material type]
- C: [material type]
- Combine: [safe combination]
- Auto-pick: let IPilot choose the safest and most useful option.
```

Do not generate detailed concepts, captions, prompts, or images until this gate is satisfied unless the user already chose a precise material type.

## Gate 1 - Asset direction confirmation

Use after the IP Consistency Profile and Asset Opportunity Map.

### Trigger

Use this gate when the user has not chosen a precise asset type or when multiple useful paths exist.

### Assistant behavior

Present 3-8 asset options, recommend a production path, and ask the user to choose one or more options.

### Output format

```markdown
## Confirmation Gate 1 - Choose Asset Direction

I recommend starting with [recommended asset type] because [reason].

Choose one:
- A: [asset type]
- B: [asset type]
- C: [asset type]
- Auto-pick: let IPilot choose the safest and most useful path.
```

### Do not proceed to detailed asset concepts unless

- the user chooses an option;
- the user explicitly asks IPilot to auto-pick;
- the user already gave a specific asset type before this gate.

## Gate 2 - Concept approval before image generation

Use after detailed asset concepts and safety review, before invoking image generation.

### Trigger

Use this gate whenever the next step would produce images.

### Assistant behavior

Show the selected concept, the prompt, the negative constraints, and the safety result. Ask for approval unless the user previously authorized automatic generation.

### Output format

```markdown
## Confirmation Gate 2 - Approve Image Generation

Selected concept: [title]
Asset type: [asset type]
Safety result: [Low / Medium-Low]
IP consistency score: [score]

Image prompt:
[final prompt]

Avoid:
[negative constraints]

Please confirm:
- Generate this image
- Revise the concept
- Choose another concept
```

If the user approves only the concept, ask a separate image-generation approval before invoking the image tool. Concept approval and generation approval are different decisions unless the user explicitly combines them.

## Gate 3 - Post-generation decision

Use after image generation or when reviewing generated images.

### Output format

```markdown
## Confirmation Gate 3 - Use, Revise, or Regenerate

Result assessment:
- IP consistency:
- Brand fit:
- Safety:
- Usability:

Recommended action:
- Accept
- Minor revise
- Regenerate
```

## Best-effort rule

If the user asks IPilot to proceed without further questions, the Skill may auto-pick the safest high-priority option. It should still state the choice and the reason before final output.

Even on best effort, do not skip safety review, reference-fidelity review, or post-generation accept / revise / regenerate guidance.



