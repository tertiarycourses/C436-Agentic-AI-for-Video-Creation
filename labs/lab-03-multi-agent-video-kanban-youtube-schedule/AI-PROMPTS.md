# Video Prompts for Lab 03

## Main Hermes prompt

```text
Create a five-agent team for this video: Researcher, Scriptwriter, Video Creator, Auditor and YouTube Publisher. Put their work on a Kanban board in dependency order. Ask Researcher to improve the factual angle, Scriptwriter to rewrite the 15-second story, Video Creator to create version three using our saved video skill, and Auditor to return time-coded feedback. Keep the YouTube task blocked until I approve the final draft. Then upload it as Private and create a paused weekly schedule for the same pipeline.
```

## Profile prompts

- Researcher: `Find three reliable facts for the topic. Return only the fact, source, why it matters and any uncertainty.`
- Scriptwriter: `Turn the approved facts into a 15-second script with Hook, Value, Proof and Action.`
- Video Creator: `Create the video from the approved script and saved brand skill. Return a draft for review.`
- Auditor: `Watch as a new viewer. Give time-coded feedback on clarity, pacing, captions, consistency and call to action.`
- YouTube Publisher: `Prepare a Private upload with the approved title and description. Stop before public publishing.`

## Schedule prompt

`Create a paused weekly schedule for Tuesday at 9:00 AM Singapore time. Start the research card, move work through Script, Video and Audit, then wait for human approval before a Private YouTube upload.`


## Review prompt

```text
Review the result as a first-time viewer. Tell me what is clear, what is confusing, where attention drops, whether the visual style stays consistent, and the three changes with the greatest impact. Refer to exact times or shot numbers.
```

## Revision prompt

```text
Create a new version that changes only the approved review points. Keep the story message, approved references and successful shots unchanged. Show me what changed before replacing the current draft.
```
