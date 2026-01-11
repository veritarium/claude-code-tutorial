# 12: Pattern — API

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                            PATTERN: API                                      ║
║                                                                              ║
║   Use this pattern when: Systems need to talk to each other                  ║
║                                                                              ║
║  ┌──────────────────────────────────────────────────────────────────────┐    ║
║  │                                                                      │    ║
║  │          REQUEST                              RESPONSE               │    ║
║  │                                                                      │    ║
║  │   ┌──────────┐      ┌──────────────────┐      ┌──────────┐          │    ║
║  │   │          │      │                  │      │          │          │    ║
║  │   │  CLIENT  │─────►│       API        │─────►│  CLIENT  │          │    ║
║  │   │          │      │                  │      │          │          │    ║
║  │   │ "I want  │      │  Receives,       │      │ "Here's  │          │    ║
║  │   │  data X" │      │  Processes,      │      │  data X" │          │    ║
║  │   │          │      │  Returns         │      │          │          │    ║
║  │   └──────────┘      └──────────────────┘      └──────────┘          │    ║
║  │                                                                      │    ║
║  └──────────────────────────────────────────────────────────────────────┘    ║
║                                                                              ║
║  ═══════════════════════════════════════════════════════════════════════     ║
║                                                                              ║
║   THE FOUR OPERATIONS (CRUD):                                                ║
║                                                                              ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │                                                                     │    ║
║   │   ┌────────────┬────────────┬────────────────────────────────────┐ │    ║
║   │   │  ACTION    │   METHOD   │   EXAMPLE                          │ │    ║
║   │   ├────────────┼────────────┼────────────────────────────────────┤ │    ║
║   │   │  Create    │   POST     │   POST /items      → Add new item  │ │    ║
║   │   │  Read      │   GET      │   GET /items       → List items    │ │    ║
║   │   │            │            │   GET /items/5     → Get item 5    │ │    ║
║   │   │  Update    │   PUT      │   PUT /items/5     → Replace item  │ │    ║
║   │   │  Delete    │   DELETE   │   DELETE /items/5  → Remove item   │ │    ║
║   │   └────────────┴────────────┴────────────────────────────────────┘ │    ║
║   │                                                                     │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║                                                                              ║
║  ═══════════════════════════════════════════════════════════════════════     ║
║                                                                              ║
║   API STRUCTURE:                                                             ║
║                                                                              ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │                                                                     │    ║
║   │                        ┌──────────────────┐                         │    ║
║   │                        │      ROUTER      │                         │    ║
║   │                        │                  │                         │    ║
║   │                        │  /items ──────┐  │                         │    ║
║   │                        │  /users ────┐ │  │                         │    ║
║   │                        │  /orders ─┐ │ │  │                         │    ║
║   │                        └───────────┼─┼─┼──┘                         │    ║
║   │                                    │ │ │                            │    ║
║   │                    ┌───────────────┘ │ └───────────────┐            │    ║
║   │                    │                 │                 │            │    ║
║   │                    ▼                 ▼                 ▼            │    ║
║   │             ┌──────────┐      ┌──────────┐      ┌──────────┐        │    ║
║   │             │  Order   │      │   User   │      │   Item   │        │    ║
║   │             │ Handler  │      │ Handler  │      │ Handler  │        │    ║
║   │             └────┬─────┘      └────┬─────┘      └────┬─────┘        │    ║
║   │                  │                 │                 │              │    ║
║   │                  └────────────┬────┴─────────────────┘              │    ║
║   │                               │                                     │    ║
║   │                               ▼                                     │    ║
║   │                        ┌──────────────┐                             │    ║
║   │                        │     DATA     │                             │    ║
║   │                        │   STORAGE    │                             │    ║
║   │                        └──────────────┘                             │    ║
║   │                                                                     │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║                                                                              ║
║  ═══════════════════════════════════════════════════════════════════════     ║
║                                                                              ║
║   BUILD SEQUENCE:                                                            ║
║                                                                              ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │                                                                     │    ║
║   │   1. DATA                                                           │    ║
║   │      "Create list to store items in memory"                         │    ║
║   │                                                                     │    ║
║   │   2. ONE ENDPOINT                                                   │    ║
║   │      "Create GET /items that returns all items as JSON"             │    ║
║   │                                                                     │    ║
║   │   3. TEST IT                                                        │    ║
║   │      "Start the server and test with curl"                          │    ║
║   │                                                                     │    ║
║   │   4. ADD ENDPOINTS                                                  │    ║
║   │      "Add POST /items to create new item"                           │    ║
║   │      "Add GET /items/{id} to get single item"                       │    ║
║   │      "Add DELETE /items/{id} to remove item"                        │    ║
║   │                                                                     │    ║
║   │   5. ADD VALIDATION                                                 │    ║
║   │      "Validate that item has name and price before creating"        │    ║
║   │                                                                     │    ║
║   │   6. ADD ERROR RESPONSES                                            │    ║
║   │      "Return 404 if item not found, 400 if invalid data"            │    ║
║   │                                                                     │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║                                                                              ║
║  ═══════════════════════════════════════════════════════════════════════     ║
║                                                                              ║
║   CONSUMING AN API (using someone else's):                                   ║
║                                                                              ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │                                                                     │    ║
║   │   1. "Fetch data from https://api.example.com/items"                │    ║
║   │   2. "Parse the JSON response and extract names"                    │    ║
║   │   3. "Handle errors if request fails"                               │    ║
║   │                                                                     │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## What This Shows

API = Request → Process → Response. Four operations cover everything: Create (POST), Read (GET), Update (PUT), Delete (DELETE). Router directs requests to handlers. Handlers access data.

## Key Insight

Every API is just CRUD operations on resources. Start with one GET endpoint, test it, then add the rest.

---

[← Automation Pattern](11-pattern-automation.md) | [Next: Debugging Pattern →](13-pattern-debugging.md)
