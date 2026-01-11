# Step 1: LIST - All Concepts

Dump everything. No organization yet. One concept per line.

---

## Mental Models

- You and AI are partners - neither works alone
- AI writes code, you provide direction
- The prompt is the bridge between you and AI
- First result is always a draft, not final
- Iteration is normal, not failure
- Expect 3-5 cycles for simple tasks
- Expect 5-15 cycles for complex tasks
- You don't need to know how to code
- You need to know what you want
- AI sees only what you show it
- AI cannot read your mind
- AI cannot see your screen
- AI cannot see files you haven't shared
- Vague input produces vague output
- Specific input produces specific output
- Big problems must be broken into small pieces
- Each small piece = one prompt
- If you can't describe it in one sentence, it's too big
- Working software emerges through refinement
- The skill is decomposition, not coding

## What You Bring

- The problem to solve
- Context (background, constraints, history)
- Intent (what outcome you want)
- Judgment (is the result correct?)
- Domain knowledge (engineering, business, etc.)

## What AI Brings

- Code in any language
- Syntax knowledge
- Standard patterns
- Libraries and tools
- Speed

## Operations (Things You Can Do)

- CREATE: make something new
- READ: view or understand something
- EDIT: change something existing
- RUN: execute code
- FIX: repair broken code
- EXTEND: add to existing code

## Prompting Skills

- Describe what, not how
- Be specific about inputs and outputs
- Include examples when helpful
- State constraints explicitly
- Mention what you've already tried
- Provide context AI can't see
- Use the feedback formula: "Got X, expected Y, change Z"

## Giving Feedback

- Good feedback is specific
- Bad feedback is vague
- "Wrong" is bad feedback
- "Output is 42, should be 84" is good feedback
- "Fix it" is bad feedback
- "Handle empty input" is good feedback
- Include error messages when available
- Describe expected vs actual behavior

## When to Refine vs Restart

- Refine when structure is right but details wrong
- Refine when missing edge cases
- Refine when small behavior change needed
- Restart when fundamentally wrong approach
- Restart after 5+ failed refinements
- Restart when easier to describe fresh

## Error Types

- Syntax error: code isn't valid
- Runtime error: code fails when running
- Logic error: no error but wrong output
- Import error: missing dependency
- Data error: problem with the data itself

## Debugging

- The error message is your friend
- Paste the full error, not a summary
- Describe what you tried
- Describe what you expected
- Let AI figure out the fix
- Isolate problems by testing parts separately

## Testing

- Input → Code → Output → Compare to expected
- Arrange: set up the test
- Act: run the code
- Assert: check the result
- Test normal cases
- Test edge cases (empty, zero, boundary)
- Test error cases (invalid input)

## Building Incrementally

- Small working steps, not giant leaps
- Build one piece, test it
- Add next piece, test combined
- Never add to broken code
- Fix first, then extend
- If it breaks, bug is in last change

## Data Pipeline Pattern

- Input → Clean → Process → Output
- Validate data before processing
- Handle missing or bad data
- Transform to useful format
- Export results

## Web App Pattern

- Frontend: what user sees
- Backend: logic and data
- Build bottom-up: data → logic → API → UI
- Single HTML file works for simple tools
- Add backend only when needed

## Automation Pattern

- Trigger → Action → Output
- Triggers: time, file change, event, manual
- Build action first, test manually
- Add trigger after action works
- Add logging for visibility
- Add error handling for robustness

## API Pattern

- Request → Process → Response
- CRUD: Create, Read, Update, Delete
- POST = create
- GET = read
- PUT = update
- DELETE = delete
- Start with one endpoint, test, add more

## Engineering Calculations

- Input → Validate → Calculate → Check → Output
- Always include units
- Always check against limits
- Factor of safety
- Deflection limits
- Allowable stress
- Material properties database
- Formatted output report

## Project Flow

- Define what you need
- Break into pieces
- Build smallest piece first
- Test each piece
- Combine pieces
- Refine until done
- Know when to stop

## Context Management

- AI context is limited to conversation
- Share relevant files
- Paste error messages
- Explain constraints
- Mention preferences
- State what you've tried

## Quality

- Don't expect perfection first try
- Verify outputs make sense
- Test with known values
- Check edge cases
- Review generated code
- Understand before using

---

**Count:** ~100 concepts listed

**Next:** Step 2 - ARRANGE (find dependencies, group into chapters)
