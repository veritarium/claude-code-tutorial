# Tutorial Narration Scripts
## From Non-Coder to Builder: Coding with AI for Engineers

---

# PART 1: FOUNDATIONS

---

## Chapter 1: The Core Partnership

### Diagram 01-1: THE CORE

**[SLIDE APPEARS]**

Let's start with the most important concept in this entire tutorial.

You don't need to become a programmer. You need to become a *builder*.

Look at this diagram. There are four elements here, and they form a partnership.

**YOU** — that's you, the engineer. You bring domain knowledge, judgment, and the ability to know what you actually need. You understand bolt stress calculations. You know what a valid engineering result looks like. You know what problem needs solving.

**AI** — this is your coding partner. It knows syntax, patterns, and can generate code quickly. It doesn't get tired. It doesn't judge your questions. But it doesn't know *your* problem unless you tell it.

**PROMPT** — this is the bridge. The prompt is how you communicate with AI. The quality of your prompt determines the quality of what you get back. We'll spend a lot of time on this.

**SOFTWARE** — this is the output. Working code that solves your problem. This is what we're building toward.

Here's the key insight: **You provide direction. AI provides code. Together, you build.**

You're not replacing yourself with AI. You're amplifying yourself. Think of it like power tools — a nail gun doesn't replace the carpenter, it makes the carpenter faster.

By the end of this tutorial, you'll be able to describe what you need and get working code. Not perfect code. Not beautiful code. *Working* code that solves real problems.

---

## Chapter 2: The Loop

### Diagram 02-1: THE LOOP

**[SLIDE APPEARS]**

This is how every coding session with AI actually works. Memorize this loop.

**DESCRIBE** — You tell AI what you want. "Create a function that calculates bolt stress from force and area."

**GET** — AI gives you code. It might be perfect. It probably won't be.

**RUN** — You actually run the code. Not just look at it. Run it. See what happens.

**EVALUATE** — Does it work? Does it do what you wanted? This is where your engineering judgment matters. AI doesn't know if the output makes sense for your application — you do.

Then you make a decision: **Done or Refine?**

If it works, you're done. Move on.

If it doesn't work, you go back to DESCRIBE with more information. "The function works but it's returning negative values when force is negative. Add validation to reject negative inputs."

This loop might run once. It might run ten times. That's normal. Every professional developer works this way — the only difference is they've done more loops.

The key insight: **Every problem is solvable through iteration.** You don't need to get it right the first time. You need to keep going until it's right.

---

### Diagram 02-2: THE DRAFT

**[SLIDE APPEARS]**

Here's what most beginners get wrong: they expect perfection on the first try.

Look at this progression. Version 1 is maybe 10% of what you want. It's rough. It might not even run.

That's fine. That's the *draft*.

Version 2 gets you to 40%. Now the basic structure works. Maybe the output format is wrong.

Version 3 is at 75%. It's doing the right calculation but doesn't handle edge cases.

Version 4 is at 100%. It works. Ship it.

The point is this: **Treat AI output like a first draft, not a final answer.**

When you write an engineering report, do you expect the first draft to be perfect? No. You write, review, revise, repeat.

Code works the same way. The first output from AI is a starting point. Your job is to test it, identify what's wrong, and guide the refinement.

This mindset shift is crucial. Stop asking "why didn't AI give me perfect code?" and start asking "what do I need to tell AI to make this better?"

---

## Chapter 3: Six Operations

### Diagram 03-1: SIX OPERATIONS

**[SLIDE APPEARS]**

Everything you'll ever do with AI coding falls into six categories. Just six.

**CREATE** — Making something new. "Create a function that..." or "Build a script that..."

**READ** — Understanding existing code. "Explain what this function does" or "What does line 15 mean?"

**EDIT** — Changing existing code. "Modify this to also handle..." or "Change the output format to..."

**RUN** — Executing code and seeing results. You do this part — AI can't run code for you.

**FIX** — Debugging errors. "I'm getting this error: [error message]. Here's the code. Fix it."

**EXTEND** — Adding to existing code. "Add a feature that..." or "Now make it also..."

That's it. Every prompt you write will be one of these operations.

When you're stuck, ask yourself: "Which operation am I trying to do?" Then structure your prompt around that operation.

For example:
- CREATE: "Create a function that calculates shear stress"
- READ: "Explain what this pandas code does"
- EDIT: "Change this to use metric units"
- FIX: "Debug this TypeError on line 23"
- EXTEND: "Add a feature to export results to CSV"

Knowing these six operations gives you a vocabulary for working with AI. You're not just "asking AI to help" — you're performing specific operations that have specific patterns.

---

# PART 2: SKILLS

---

## Chapter 4: Decomposition

### Diagram 04-1: DECOMPOSITION

**[SLIDE APPEARS]**

This is the single most important skill for coding with AI: breaking big things into small things.

Look at this tree. At the top, you have a big task: "Build a bolt calculator app."

If you give that to AI, you'll get something. But it probably won't be what you want. The task is too big, too vague, too open to interpretation.

Now look what happens when we decompose it.

That big task breaks into medium tasks:
- Input section
- Calculation engine
- Results display
- File handling

Each of those breaks into small tasks:
- Input section → Get force value, Get area value, Validate inputs
- Calculation engine → Calculate stress, Check against limits, Determine pass/fail

These small tasks are *perfect* for AI. They're specific. They're contained. They have clear inputs and outputs.

**Big tasks confuse AI. Small tasks get perfect results.**

Think of it like engineering drawings. You don't hand someone a napkin sketch and say "build this building." You provide detailed drawings of each component. AI needs the same thing.

---

### Diagram 04-2: THE RULE

**[SLIDE APPEARS]**

Here's a simple test to know if your task is the right size.

Ask yourself: **"Can I explain this task in ONE sentence?"**

If NO — the task is too big. Break it down further.

If YES — the task is just right. Give it to AI.

Look at the examples:

TOO BIG: "Build me an app that handles all our bolt calculations with a UI and database and reports"

That's not one sentence describing one task. That's a paragraph describing a project.

JUST RIGHT: "Create a function that calculates tensile stress from force and area"

One sentence. One task. One clear outcome.

More examples of right-sized tasks:
- "Write a function that reads a CSV file and returns a list of values"
- "Add error handling to reject negative numbers"
- "Create a loop that processes each row in the data"

Each of these can be explained in one sentence. Each will get you good results from AI.

When you find yourself writing a paragraph to describe what you want, stop. That's a sign you need to decompose first.

---

## Chapter 5: Precision

### Diagram 05-1: THE SPECTRUM

**[SLIDE APPEARS]**

Not all prompts are equal. There's a spectrum from vague to precise, and where you land on that spectrum determines your success rate.

Look at this gradient bar. On the left, in red: VAGUE. On the right, in blue: PRECISE.

**VAGUE: "Help me with calculations"**
Success rate: maybe 20%. AI has no idea what calculations. What inputs? What outputs? What domain? It will guess, and it will probably guess wrong.

**MEDIUM: "Write a stress calculation function"**
Success rate: around 50%. Better. AI knows the domain now. But what kind of stress? What inputs does the function take? What should it return?

**PRECISE: "Write a Python function called calculate_tensile_stress that takes force in Newtons and area in square millimeters, returns stress in MPa, and raises an error if either input is negative"**
Success rate: 90%+. AI knows exactly what to build. The function name, the inputs, the output, the units, the error handling — it's all specified.

The pattern is clear: **More specific prompts = Fewer iterations = Better results.**

Yes, writing precise prompts takes more time upfront. But it saves enormous time in the loop. Would you rather spend 2 minutes writing a good prompt and get working code, or spend 30 seconds on a vague prompt and then 20 minutes trying to fix what AI gives you?

---

### Diagram 05-2: FIVE COMPONENTS

**[SLIDE APPEARS]**

Here's a framework for building precise prompts. Five components.

**WHAT** — The action you want. "Create a function" or "Fix this error" or "Explain this code"

**WHERE** — The location or context. "In the utils.py file" or "In the calculate function" or "For this data structure"

**HOW** — The method or approach. "Using a for loop" or "With error handling" or "Using the pandas library"

**WHY** — The purpose. "To improve performance" or "For user validation" or "To match the existing code style"

**EXAMPLE** — Show what you expect. "Input: [1,2,3], Output: 6" or "Like this existing function but for temperature"

You don't always need all five. But the more you include, the better your results.

Let's build a complete prompt:

**WHAT:** "Create a function"
**WHERE:** "in utils.py"
**HOW:** "using recursion"
**WHY:** "to calculate factorials for the stats module"
**EXAMPLE:** "factorial(5) should return 120"

Put it together: "Create a function in utils.py using recursion to calculate factorials for the stats module. Example: factorial(5) should return 120."

That's a precise prompt. AI will nail it on the first try.

---

## Chapter 6: Feedback

### Diagram 06-1: GOOD VS BAD FEEDBACK

**[SLIDE APPEARS]**

AI gave you something. It's not quite right. What do you say next?

This is where most beginners fail. They give bad feedback, and then wonder why AI keeps giving them wrong answers.

**BAD FEEDBACK:**

"It doesn't work" — AI has no idea what's wrong. Doesn't work how? What happened? What did you expect?

"This is wrong" — Wrong how? What's the correct behavior?

"Fix it" — Fix what? AI will guess, and it will guess wrong.

"That's not what I wanted" — Then what DID you want? AI can't read your mind.

**GOOD FEEDBACK:**

"Getting error: TypeError on line 15" — AI knows exactly where to look.

"Output is 5, but should be 10" — AI knows the gap it needs to close.

"Change the loop to start at 1, not 0" — AI knows exactly what to change.

"Add validation: reject negative numbers" — AI knows the requirement.

See the pattern? Good feedback is specific. It tells AI exactly what's wrong and often suggests what needs to change.

**Specific feedback → Specific fixes → Done faster.**

---

### Diagram 06-2: THE FORMULA

**[SLIDE APPEARS]**

Here's a formula you can use every time AI gives you something that's not quite right:

**"Got [X]. Expected [Y]. Change [Z]."**

Three parts. Complete information. Immediate fix.

**GOT [X]** — What actually happened. The current output, the error message, the current behavior.

**EXPECTED [Y]** — What should happen. The correct output, the desired behavior, the expected result.

**CHANGE [Z]** — What to modify. The specific fix, which part to change. This part is optional but helpful.

Example:

**Got:** "Function returns 15 when given input [1, 2, 3, 4, 5]"

**Expected:** "Should return 120 (the product, not the sum)"

**Change:** "Use multiplication instead of addition in the loop"

Put it together: "The function returns 15 for input [1,2,3,4,5] but should return 120 — it's calculating the sum instead of the product. Change the addition to multiplication in the loop."

AI now has everything it needs. One response, done.

**Complete information = One-shot fix.**

---

## Chapter 7: Context

### Diagram 07-1: THE WINDOW

**[SLIDE APPEARS]**

This concept will change how you work with AI.

Look at this diagram. The large box is YOUR WORLD — everything you know about your project, your history, your requirements, your preferences.

The small box inside is AI'S WINDOW — what AI can actually see.

**AI only sees what's in the prompt.**

AI cannot see your screen. It cannot access your files. It doesn't remember your past conversations. It doesn't know your project. It cannot read your mind.

Unless you tell it.

All that stuff floating outside the window — your project history, other files, business requirements, team coding standards, past conversations, your preferences, why you're doing this — AI has no access to any of it.

This is why vague prompts fail. You're assuming AI has context it doesn't have.

**SO YOU MUST:**
- Paste relevant code
- Share error messages
- Explain constraints
- Give context
- State requirements

Make the window bigger. The more context you share, the better AI understands. It's that simple.

---

### Diagram 07-2: WHAT TO SHARE

**[SLIDE APPEARS]**

There are five types of context that dramatically improve AI results.

**1. CONSTRAINTS** — Limitations and requirements.
"Must work in Python 3.8"
"No external libraries"
"Max 100 lines of code"

**2. PREFERENCES** — Style and approach choices.
"Use descriptive variable names"
"Add comments for complex logic"
"Prefer simple over clever"

**3. HISTORY** — What led to this point.
"We tried X but it failed because..."
"This is part of a larger system"
"Previous version had this bug..."

**4. ERRORS** — Exact error messages and symptoms.
"TypeError: 'NoneType' has no len()"
"Happens when input is empty list"
"Line 42 in process_data function"

**5. FILES** — Relevant code and data.
"Here's the current function: [code]"
"Sample input data: [data]"
"Related config file: [config]"

Before sending a prompt, run through this checklist:
- Did I share relevant constraints?
- Did I mention my preferences?
- Did I explain the history/context?
- Did I include error messages?
- Did I paste the relevant code/files?

**More context = Fewer iterations = Better results.**

---

## Chapter 8: When to Restart

### Diagram 08-1: THE DECISION

**[SLIDE APPEARS]**

Sometimes you need to know when to stop refining and start fresh.

Here's a simple decision tree.

AI gave you output. It's not right. Ask yourself: **Is it close to what you want?**

**If YES → REFINE.** Give feedback, iterate, build on what you have.

Signs to refine:
- Structure is correct
- Small bugs or typos
- Missing one feature
- Style needs adjustment
- Logic is correct but incomplete

**If NO → RESTART.** New conversation, new prompt, fresh start.

Signs to restart:
- Wrong approach entirely
- Missing the point of the request
- Multiple fundamental problems
- Would need complete rewrite
- Going in circles (same errors repeating)

Here's the thing: starting fresh isn't failure. It's efficiency. Sometimes the fastest path to working code is to abandon the current attempt and try again with a better prompt.

**Know when to cut your losses and start fresh.**

---

### Diagram 08-2: THE 5-ATTEMPT RULE

**[SLIDE APPEARS]**

Here's a simple rule: **Five attempts maximum, then restart.**

Look at the progression:

**Attempt 1: TRY** — Your initial prompt. See what happens.

**Attempt 2: REFINE** — Add more specifics. Clarify what's wrong.

**Attempt 3: ADJUST** — Fix errors. Try different wording.

**Attempt 4: REPHRASE** — Different approach. New angle on the problem.

**Attempt 5: LAST TRY** — Final attempt with everything you've learned.

If you're still not there after five attempts, **RESTART.** New conversation, better prompt, fresh context.

Why five?

**Too Few (1-2):** You're giving up too early. Missing easy fixes. Sometimes the solution is one more piece of information away.

**Just Right (3-5):** Enough attempts to find solutions. Not so many that you're wasting time spinning your wheels.

**Too Many (6+):** Diminishing returns. Context is getting cluttered. You're probably going in circles.

**5 attempts max, then start fresh with what you learned.**

The beautiful thing about restarting is you're not starting from zero. You now know what doesn't work. Your second attempt will be better because of your first failure.

---

# PART 3: PROBLEMS

---

## Chapter 9: Common Pitfalls

### Diagram 09-1: COMMON TRAPS

**[SLIDE APPEARS]**

Let's talk about mistakes. Every beginner makes these. Now you won't.

**TRAP 1: BLIND TRUST**
Running code without reading it. AI-generated code can have bugs, security issues, or just not do what you think.
*Fix: Always review before running. Ask AI to explain what the code does.*

**TRAP 2: VAGUE PROMPTS**
"Make it better" or "Fix this" — AI will guess what you mean, usually wrong.
*Fix: Be specific about what's wrong. State expected vs actual behavior.*

**TRAP 3: TOO BIG TASKS**
"Build me a whole app" — Too much at once. AI loses focus, you lose control.
*Fix: Break into small tasks. One feature at a time.*

**TRAP 4: NO CONTEXT**
Not sharing error messages or relevant code. AI is working blind.
*Fix: Paste errors, include code, share the context.*

**TRAP 5: GIVING UP TOO FAST**
First attempt didn't work, quit. But you were maybe one iteration away.
*Fix: Give 3-5 attempts. Iterate and refine.*

**TRAP 6: NOT LEARNING**
Copy-paste without understanding. You never build skills this way.
*Fix: Ask AI to explain. Learn from each solution.*

The pattern: Most traps come from treating AI like magic instead of a tool.

**Stay engaged, stay specific, stay curious.**

---

### Diagram 09-2: TRUST LEVELS

**[SLIDE APPEARS]**

How much should you trust AI's output? It depends on the consequences of failure.

**LOW TRUST — Verify Everything**

When: Security-related code, financial calculations, safety-critical systems, data deletion operations.

Action: Read every line. Test thoroughly. Get a second opinion. Understand fully.

**MEDIUM TRUST — Review and Test**

When: Standard features, business logic, API integrations, database operations.

Action: Skim the code. Run basic tests. Check edge cases. Verify behavior.

**HIGH TRUST — Quick Check**

When: Simple utilities, formatting code, text manipulation, documentation.

Action: Glance at output. Run once. Check it works. Move on.

Key insight: **Trust level depends on consequences of failure, not AI confidence.**

AI might be very confident about code that deletes your database. That doesn't mean you should trust it blindly.

For a bolt stress calculator in a real engineering application? Low trust. Verify everything.

For a script that renames files in a folder? Higher trust. Quick check.

**Higher stakes = More verification needed.**

---

## Chapter 10: Debugging

### Diagram 10-1: THE DEBUGGING FLOW

**[SLIDE APPEARS]**

Your code doesn't work. Here's the systematic approach to fixing it.

**Step 1: CAPTURE** — Copy the exact error message. All of it. Not a summary, the actual text.

**Step 2: LOCATE** — Find the problem line. Error messages usually tell you where.

**Step 3: CONTEXT** — Include the surrounding code. AI needs to see what's happening around the error.

**Step 4: ASK** — Send to AI with all this context.

**Step 5: APPLY** — Make the fix.

**Step 6: TEST** — Run it again. Verify it's actually fixed.

Let me show you the difference between bad and good debug requests.

**BAD:** "My code doesn't work, fix it"
- Missing: error message
- Missing: which line fails
- Missing: relevant code
- Missing: what it should do
- Result: AI will guess wrong

**GOOD:** "Error: TypeError on line 15. Here's lines 10-20: [code]. Input was: [1, 2, None]. Expected: sum of numbers. Should skip None values."
- Has: exact error
- Has: location
- Has: code context
- Has: input data
- Has: expected behavior
- Result: Precise fix provided

**Better information in = Better fix out.**

---

### Diagram 10-2: ERROR TYPES

**[SLIDE APPEARS]**

Understanding error types helps you describe them better to AI.

**SYNTAX ERROR** — Code can't even run.
Examples: Missing brackets, typos, wrong indentation.
Tell AI: "Syntax error on line X: [error message]"
Difficulty: Easiest. Usually one character or line to fix.

**RUNTIME ERROR** — Code runs but crashes midway.
Examples: Division by zero, null access, file not found.
Tell AI: "Crashes at line X with [error]. Input was [data]."
Difficulty: Medium. Need to understand what triggered it.

**LOGIC ERROR** — Code runs but gives wrong result.
Examples: Wrong calculation, off-by-one, wrong condition.
Tell AI: "Got [X], expected [Y]. Here's the code."
Difficulty: Hardest. No error message to guide you.

When sharing errors with AI, include:

| Error Type | Must Include | Also Helpful |
|------------|--------------|--------------|
| Syntax | Error message, line number | Few lines around error |
| Runtime | Error message, traceback, input | Full function, what triggers it |
| Logic | Actual output, expected output, code | Test cases, what it should do |

**Name the error type = Faster fix.**

---

## Chapter 11: Getting Unstuck

### Diagram 11-1: GETTING STUCK

**[SLIDE APPEARS]**

Getting stuck is normal. Recognizing it early saves time.

**Warning signs you might be stuck:**
- Same error keeps coming back
- Fixing one thing breaks another
- AI gives same answer repeatedly
- More than 5 attempts without progress
- Getting frustrated or confused

**What's actually happening:**
- Wrong mental model of the problem
- Missing crucial information
- Task is actually too complex
- Solving wrong problem entirely
- Context window exhausted

Here's what the stuck loop looks like:

TRY → FAIL → TRY AGAIN → SAME FAIL → (back to TRY)

You're going in circles. Each attempt looks slightly different but you're not actually making progress.

Here's the key insight: **Being stuck is information.** It's telling you that your approach needs to change. Not your code — your approach.

**Recognize stuck early = Save time and frustration.**

---

### Diagram 11-2: ESCAPE ROUTES

**[SLIDE APPEARS]**

Six ways to get unstuck. Pick one based on your situation.

**1. START FRESH**
New conversation, new prompt. Clears context clutter. Fresh perspective.
*Use when: Same error keeps repeating.*

**2. BREAK SMALLER**
Task too big? Split it. Solve one piece at a time. Combine when working.
*Use when: Task seems impossible.*

**3. ADD CONTEXT**
Share more information. Full error messages. Related files, examples.
*Use when: AI seems confused about your situation.*

**4. REPHRASE**
Explain differently. Use different words. Focus on different aspect.
*Use when: AI misunderstands you.*

**5. ASK WHY**
Get AI to explain the error. "Why is this happening?" "What causes this?"
*Use when: You don't understand the error.*

**6. SIMPLIFY**
Make a minimal example. Strip to core problem. Add complexity later.
*Use when: Too many things could be wrong.*

Quick decision guide:
- Same error over and over? → Start Fresh
- Task seems impossible? → Break Smaller
- AI misunderstanding you? → Rephrase
- Don't understand error? → Ask Why

**Every problem has an escape route.**

---

# PART 4: BUILDING

---

## Chapter 12: Reading Code

### Diagram 12-1: LEARNING TO READ CODE

**[SLIDE APPEARS]**

Here's a secret: You don't need to write code to understand it.

Reading code is like reading a recipe. You can follow along without being a chef. You can understand what's happening without knowing how to create it from scratch.

**LOOK FOR these patterns:**

*Names* — Variables describe what they hold. `bolt_diameter`, `max_stress`, `is_valid` — the names tell you what's inside.

*Structure* — Indentation shows grouping. Things indented under an `if` only happen when that condition is true.

*Keywords* — `if`, `for`, `while`, `return` — these control the flow. They're the same in almost every language.

*Comments* — Lines starting with `#` are human explanations. They're notes for you.

*Flow* — Code runs top to bottom, unless something branches it.

**ASK AI these questions:**
- "What does this code do?"
- "Explain line by line"
- "What is [variable] for?"
- "Why is this needed?"
- "What would break this?"
- "Simplify this for me"

AI is your code interpreter. Use it.

**SKIP FOR NOW:**
- Memorizing syntax
- Understanding every detail
- Advanced patterns
- Optimization tricks

Focus on the big picture first.

**Goal: Understand what code does, not memorize how to write it.**

---

### Diagram 12-2: CODE ANATOMY

**[SLIDE APPEARS]**

Let me show you the universal parts of every program. Once you know these, you can read any code.

Here's a simple example:

```python
# Calculate bolt stress
def calculate_stress(force, area):
    stress = force / area
    if stress > 250:
        print("Warning: High stress!")
    return stress

result = calculate_stress(1000, 4)
print(result)
```

**COMMENT** — `# Calculate bolt stress`
Notes for humans. Ignored by computer. Like sticky notes on code.

**FUNCTION** — `def calculate_stress(force, area):`
Reusable blocks of code. Take inputs, give outputs. Named for what they do. Like machines in a factory.

**VARIABLE** — `stress = force / area`
Named containers for data. `stress` holds the result of the calculation.

**CONDITION** — `if stress > 250:`
Makes decisions. True/false. Branches the flow. Like a fork in the road.

**OUTPUT** — `print("Warning: High stress!")`
Shows results to the user. Makes the invisible visible.

**FUNCTION CALL** — `calculate_stress(1000, 4)`
Using a function you defined. Put in values, get back a result.

Every program you'll ever see is made of these same building blocks, just arranged differently.

**Learn the parts = Read any program.**

---

## Chapter 13: Core Concepts

### Diagram 13-1: VARIABLES

**[SLIDE APPEARS]**

Variables are named containers for data. That's it.

Think of them like labeled boxes. The name tells you what's inside.

```python
bolt_diameter = 12.5
```

This creates a box labeled `bolt_diameter` and puts the value `12.5` inside it.

**Types of data you can store:**

*NUMBERS*
```python
count = 42
price = 19.99
stress = 250.5
```

*TEXT* (called "strings")
```python
name = "M12"
grade = "8.8"
status = "OK"
```

*TRUE/FALSE* (called "booleans")
```python
is_valid = True
has_error = False
passed = True
```

*LISTS* (multiple items)
```python
sizes = [8, 10, 12]
```

**Naming rules:**
- No spaces (use underscores: `bolt_count`, not `bolt count`)
- Start with a letter
- Be descriptive

Good names: `bolt_count`, `max_stress`, `is_valid`
Bad names: `x`, `bc`, `thing1`

**Good variable names make code self-documenting.** When you read `if stress > max_allowable_stress`, you know exactly what's being checked.

---

### Diagram 13-2: CONTROL FLOW

**[SLIDE APPEARS]**

How programs make decisions and repeat actions. Three patterns handle most logic.

**IF/ELSE — Decisions**

```python
if stress > 250:
    print("Fail")
else:
    print("Pass")
```

Check a condition. If true, do one thing. If false, do another. Like a fork in the road.

**FOR LOOP — Repeat N times**

```python
for size in [8, 10, 12]:
    print(size)
```

Do something for each item in a list. Process each one, then move to the next.

**WHILE LOOP — Repeat until**

```python
while error > 0.01:
    refine()
```

Keep going until a condition is met. Don't know how many times in advance.

**Summary:**
- `if/else` — Choose between options
- `for` — Do something N times
- `while` — Keep going until done

That's it. These three patterns handle most logic you'll ever need.

**Programs = Data + Decisions + Repetition**

---

## Chapter 14: Functions and Libraries

### Diagram 14-1: FUNCTIONS

**[SLIDE APPEARS]**

A function is like a machine: put something in, get something out.

```python
def calculate_stress(force, area):
    return force / area

result = calculate_stress(1000, 4)
# result is now 250
```

**Parts of a function:**
- *Name* — what it does (`calculate_stress`)
- *Parameters* — inputs (`force`, `area`)
- *Body* — the work (`return force / area`)
- *Return* — output (the calculated stress)

**Why use functions?**
- Reuse code (write once, use many times)
- Organize logic (clear names for clear operations)
- Test easily (isolated units you can verify)
- Fix in one place (change the function, all uses updated)

**Ask AI to:**
- "Create a function that..."
- "Explain this function"
- "What does it return?"
- "Add error handling to this function"

**Functions = Reusable building blocks of code.**

---

### Diagram 14-2: LIBRARIES

**[SLIDE APPEARS]**

Libraries are pre-built code you can use. Don't reinvent the wheel.

**Without libraries:**
```python
# Calculate average manually
total = 0
for num in numbers:
    total = total + num
average = total / len(numbers)
```
5 lines, reinventing the wheel.

**With libraries:**
```python
import statistics
average = statistics.mean(numbers)
```
1 line, tested, reliable.

**Libraries for engineers:**

*Math/Science*
- `numpy` — Arrays, matrices
- `scipy` — Engineering calculations
- `pandas` — Data tables
- `math` — Basic math operations

*Visualization*
- `matplotlib` — Charts, plots
- `plotly` — Interactive plots
- `seaborn` — Statistical visualization

*Files/Automation*
- `os` — File operations
- `json` — Read/write JSON
- `csv` — Spreadsheets
- `datetime` — Dates and times

**Ask AI:** "What library should I use to [task]?" or "Show me how to use [library] for [goal]"

**Stand on shoulders of giants — use libraries!**

---

## Chapter 15: Data and Files

### Diagram 15-1: DATA STRUCTURES

**[SLIDE APPEARS]**

Ways to organize multiple pieces of data.

**LIST** — Ordered collection
```python
bolt_sizes = [8, 10, 12, 16]
```
Access by position: `bolt_sizes[0]` gives you `8`.
Can add/remove items. Like a shopping list.

**DICTIONARY** — Key-value pairs
```python
bolt = {"name": "M12", "grade": "8.8", "diameter": 12.0}
```
Access by name: `bolt["grade"]` gives you `"8.8"`.
Like a real dictionary: word → definition.

**TUPLE** — Fixed, unchangeable list
```python
coords = (100.0, 200.5, 50.2)
```
Can't change after creation. Good for coordinates, constants.
Like a sealed envelope.

**When to use what:**

| Structure | Use When |
|-----------|----------|
| LIST | Collection of similar items, need to add/remove |
| DICTIONARY | Named properties, need to look up by name |
| TUPLE | Fixed group of values, should never change |

**Ask AI:** "What data structure should I use for [description]?"

**Right structure = Cleaner, faster code.**

---

### Diagram 15-2: FILES AND I/O

**[SLIDE APPEARS]**

Files are permanent storage. Data survives when the program ends.

**READING FILES**

```python
with open("data.csv") as file:
    content = file.read()
```

File on disk → Your program → Data in memory

**WRITING FILES**

```python
with open("results.txt", "w") as file:
    file.write("Stress: 250 MPa")
```

Your program → File on disk → Permanent storage

**Common file types:**

*Text files* (human readable)
- `.txt` — Plain text
- `.csv` — Spreadsheet data
- `.json` — Structured data

*Data files* (use libraries to read)
- `.xlsx` — Excel files
- `.xml` — Structured format
- `.db` — Databases

**Ask AI:**
- "Read this CSV file into a list"
- "Write results to a new file"
- "Parse this JSON data"

AI handles the details. You describe what you need.

**Files = Permanent data that survives restarts.**

---

## Chapter 16: Quality

### Diagram 16-1: TESTING

**[SLIDE APPEARS]**

Testing is quality control for code. You verify it actually works.

**Types of testing:**

*Manual Testing*
- Run the code
- Check the output
- Try different inputs
Good for quick checks.

*Automated Testing*
- Write test code
- Runs automatically
- Catches regressions
Good for reliability.

*Edge Case Testing*
- Empty inputs
- Extreme values
- Invalid data
Good for robustness.

**Simple test example:**

```python
result = calculate_stress(1000, 4)
expected = 250
assert result == expected, "Test failed!"
```

If result doesn't match expected, you'll know immediately.

**Test results:**
- PASS — Code works!
- FAIL — Fix needed.

**Ask AI:** "Write tests for this function"

**Test before trusting.** Known input + expected output = verification.

**Tested code = Trusted code.**

---

### Diagram 16-2: PROJECT STRUCTURE

**[SLIDE APPEARS]**

Organizing files for bigger projects. Like a well-organized toolbox.

**Typical project structure:**

```
bolt_calculator/
    main.py              # Entry point
    calculations.py      # Core functions
    utils.py             # Helper functions
    data/                # Input files
        bolt_specs.csv
        materials.json
    output/              # Results
        results.txt
    tests/               # Test files
        test_calculations.py
    README.md            # Documentation
```

**Why organize?**
- Find files quickly
- Separate concerns (logic vs data vs tests)
- Easy to share and collaborate
- Professional standard

**File naming rules:**
- Lowercase: `calculations.py` not `Calculations.py`
- Underscores: `bolt_stress.py` not `bolt-stress.py`
- Descriptive: `test_calculations.py` not `test1.py`

Names should describe content.

**Ask AI:** "Create a project structure for [description]" — it will set everything up.

**Organized project = Maintainable project.**

---

# PART 5: APPLICATION

---

## Chapter 17: Your First Project

### Diagram 17-1: YOUR FIRST PROJECT

**[SLIDE APPEARS]**

Time to apply everything. Here's the approach.

**Start small, make it work, then expand.**

**Phase 1: PLAN**
Define your goal. What should it do? What inputs/outputs? What's the simplest version?
Write it in one sentence before coding.

**Phase 2: BUILD**
Work with AI. Start with core feature. Test as you go. Add features one by one.
Get it working before making it perfect.

**Phase 3: REFINE**
Polish it. Handle edge cases. Add error messages. Clean up code.
Ask AI to review and improve.

**Example: Bolt Stress Calculator**

*Plan:* "Calculate stress from force and area, warn if too high"

*Build:*
1. Create function
2. Add input
3. Add warning
4. Format output

*Refine:* Handle zero area, add units, save to file

Each step is small. Each step is testable. Each step gets you closer.

**Done is better than perfect — ship V1, improve later.**

---

### Diagram 17-2: PROJECT CHECKLIST

**[SLIDE APPEARS]**

Before calling it done, verify everything.

**Before Starting:**
- [ ] Goal clearly defined?
- [ ] Inputs and outputs identified?
- [ ] Broken into small tasks?

**While Building:**
- [ ] Testing each piece?
- [ ] Understanding AI's code?
- [ ] Saving working versions?

**Before Finishing:**
- [ ] Works with normal input?
- [ ] Works with edge cases?
- [ ] Has clear error messages?

**Quality Check:**
- [ ] Code readable?
- [ ] Names descriptive?
- [ ] Comments where needed?

**Final Questions:**
- Can someone else use this without your help?
- Would you trust this code in production?

If yes to both, you're done.

**Checklist complete = Project ready to ship.**

---

## Chapter 18: Moving Forward

### Diagram 18-1: GROWING YOUR SKILLS

**[SLIDE APPEARS]**

Here's the progression from beginner to confident.

**Stage 1: COPY**
- Follow AI's code exactly
- Ask for explanations
- Learn patterns

Goal: Get code working. Understand what it does.

**Stage 2: MODIFY**
- Adjust AI's code yourself
- Combine pieces
- Fix small issues alone

Goal: Adapt solutions. Build on existing code.

**Stage 3: CREATE**
- Design solutions
- Use AI as assistant
- Guide the process

Goal: Build anything. AI accelerates, not replaces.

You'll move through these stages naturally as you build more projects. Each project teaches you something new.

**The Secret:** Every expert was once a beginner who kept building.

**Growth = Practice + Curiosity + Persistence**

---

### Diagram 18-2: RESOURCES

**[SLIDE APPEARS]**

Where to go when you need help.

**AI Tools:**
- Claude (Anthropic) — Great for explanations
- ChatGPT (OpenAI) — Good for code generation
- GitHub Copilot — In-editor assistance

Use what works for you.

**Learning More:**
- Python.org — Official documentation
- Stack Overflow — Q&A for specific errors
- YouTube tutorials — Visual learning

Search when stuck.

**Practice Ideas:**
- Automate calculations (turn Excel work into code)
- Data visualization (create charts from data)
- File processing (batch convert/rename)

Solve real problems.

**When You're Stuck — The Workflow:**
1. Ask AI
2. Search Web
3. Rephrase
4. Break Down

Most problems solved in 1-2 steps.

**Your best resource: curiosity and willingness to experiment.**

**Help is always one question away.**

---

### Diagram 18-3: THE JOURNEY

**[SLIDE APPEARS]**

Look how far you've come.

**You Started Here:**
"I can't code"

**What You Learned:**
- The Loop: Describe → Get → Run → Evaluate
- Decomposition: Big tasks → Small tasks
- Communication: Specific prompts → Better results

**You Are Here:**
"I build with AI"

**Skills You Now Have:**
- Read and understand code
- Communicate with AI effectively
- Debug and fix problems
- Build working solutions

**What's Next:**
- Pick a real problem you want to solve
- Build your first real project
- Share it with someone
- Then build another one!

**You don't need to know everything to build something useful.**

**The Truth About Coding:**
Everyone looks things up. Everyone gets stuck. Everyone asks for help.
The only difference is persistence.

**Now go build something!**

---

### Diagram 18-4: KEY TAKEAWAYS

**[SLIDE APPEARS]**

Everything in one page.

**YOU + AI = BUILDER**
You provide direction and judgment. AI provides code and speed.

**Six Principles:**

1. **THE LOOP** — Describe → Get → Run → Evaluate. Iterate until it works.

2. **DECOMPOSE** — Big task → Small tasks. One sentence = right size.

3. **BE SPECIFIC** — Precise prompts → Better results. What, where, how, why, example.

4. **GIVE FEEDBACK** — Got X, Expected Y, Change Z. Tell AI what's wrong specifically.

5. **SHARE CONTEXT** — AI only knows what you tell it. Code, errors, constraints.

6. **KNOW WHEN TO RESTART** — 5 attempts, then fresh start. Cut losses and try again.

**The Formula for Success:**
Clear Goal + Small Steps + Iteration + Persistence = Working Code

**You now have everything you need. Start building.**

---

# END OF NARRATION SCRIPTS

---

## Usage Notes

- Each section corresponds to one diagram
- Pause after showing each diagram to let the content sink in
- The `[SLIDE APPEARS]` marker indicates when to advance
- Code examples can be shown in a separate code view if presenting live
- For self-paced learning, readers should study the diagram while reading the narration
- Total estimated presentation time: 90-120 minutes
- Can be broken into 5 sessions (one per part) of ~20 minutes each
