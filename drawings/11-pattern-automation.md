# 11: Pattern — Automation

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                         PATTERN: AUTOMATION                                  ║
║                                                                              ║
║   Use this pattern when: Eliminating repetitive manual tasks                 ║
║                                                                              ║
║  ┌──────────────────────────────────────────────────────────────────────┐    ║
║  │                                                                      │    ║
║  │   ┌─────────────┐         ┌─────────────┐         ┌─────────────┐    │    ║
║  │   │             │         │             │         │             │    │    ║
║  │   │   TRIGGER   │────────►│   ACTION    │────────►│   OUTPUT    │    │    ║
║  │   │             │         │             │         │             │    │    ║
║  │   └─────────────┘         └─────────────┘         └─────────────┘    │    ║
║  │                                                                      │    ║
║  │   When X happens          Do Y                    Produce Z          │    ║
║  │                                                                      │    ║
║  └──────────────────────────────────────────────────────────────────────┘    ║
║                                                                              ║
║  ═══════════════════════════════════════════════════════════════════════     ║
║                                                                              ║
║   TRIGGER TYPES:                                                             ║
║                                                                              ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │                                                                     │    ║
║   │   ┌───────────┐    ┌───────────┐    ┌───────────┐    ┌───────────┐ │    ║
║   │   │   TIME    │    │   FILE    │    │   EVENT   │    │  MANUAL   │ │    ║
║   │   │           │    │           │    │           │    │           │ │    ║
║   │   │ "Every    │    │ "When new │    │ "When     │    │ "When I   │ │    ║
║   │   │  hour"    │    │  file     │    │  email    │    │  run the  │ │    ║
║   │   │ "Daily    │    │  appears" │    │  arrives" │    │  script"  │ │    ║
║   │   │  at 9am"  │    │ "When     │    │ "When API │    │           │ │    ║
║   │   │ "Every    │    │  modified"│    │  called"  │    │           │ │    ║
║   │   │  Monday"  │    │           │    │           │    │           │ │    ║
║   │   └───────────┘    └───────────┘    └───────────┘    └───────────┘ │    ║
║   │                                                                     │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║                                                                              ║
║  ═══════════════════════════════════════════════════════════════════════     ║
║                                                                              ║
║   COMMON AUTOMATION SHAPES:                                                  ║
║                                                                              ║
║   ┌─────────────┐    ┌─────────────────────────────────────────────────┐     ║
║   │ File Watch  │    │                                                 │     ║
║   │             │    │  ┌───────┐    ┌─────────┐    ┌────────┐         │     ║
║   │             │    │  │ Watch │───►│ Process │───►│ Move/  │         │     ║
║   │             │    │  │Folder │    │  File   │    │ Archive│         │     ║
║   │             │    │  └───────┘    └─────────┘    └────────┘         │     ║
║   └─────────────┘    └─────────────────────────────────────────────────┘     ║
║                                                                              ║
║   ┌─────────────┐    ┌─────────────────────────────────────────────────┐     ║
║   │ Scheduled   │    │                                                 │     ║
║   │ Report      │    │  ┌───────┐    ┌─────────┐    ┌────────┐         │     ║
║   │             │    │  │ Timer │───►│ Gather  │───►│ Email  │         │     ║
║   │             │    │  │ Daily │    │  Data   │    │ Report │         │     ║
║   │             │    │  └───────┘    └─────────┘    └────────┘         │     ║
║   └─────────────┘    └─────────────────────────────────────────────────┘     ║
║                                                                              ║
║   ┌─────────────┐    ┌─────────────────────────────────────────────────┐     ║
║   │ Data Sync   │    │                                                 │     ║
║   │             │    │  ┌───────┐    ┌─────────┐    ┌────────┐         │     ║
║   │             │    │  │ Timer │───►│ Fetch   │───►│ Update │         │     ║
║   │             │    │  │Hourly │    │ Source  │    │ Local  │         │     ║
║   │             │    │  └───────┘    └─────────┘    └────────┘         │     ║
║   └─────────────┘    └─────────────────────────────────────────────────┘     ║
║                                                                              ║
║  ═══════════════════════════════════════════════════════════════════════     ║
║                                                                              ║
║   BUILD SEQUENCE:                                                            ║
║                                                                              ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │                                                                     │    ║
║   │   1. ACTION FIRST (without trigger)                                 │    ║
║   │      "Create script that processes all CSVs in /input folder"       │    ║
║   │                                          ↓                          │    ║
║   │   2. TEST MANUALLY                     Run it, verify it works      │    ║
║   │                                          ↓                          │    ║
║   │   3. ADD TRIGGER                                                    │    ║
║   │      "Make it watch for new files" or "Run every hour"              │    ║
║   │                                          ↓                          │    ║
║   │   4. ADD LOGGING                                                    │    ║
║   │      "Log each run to automation.log with timestamp"                │    ║
║   │                                          ↓                          │    ║
║   │   5. ADD ERROR HANDLING                                             │    ║
║   │      "If processing fails, move file to /failed and notify me"      │    ║
║   │                                                                     │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║                                                                              ║
║   ┌─────────────────────────────────────────────────────────────────────┐    ║
║   │  KEY RULE: Always build and test the action before adding trigger.  │    ║
║   └─────────────────────────────────────────────────────────────────────┘    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## What This Shows

Automation = Trigger + Action + Output. Triggers start the work (time, file change, event). Actions do the work. Build the action first and test it manually, then add the trigger.

## Key Insight

If you do something more than twice, automate it. Build the action, verify it works, then set it to run automatically.

---

[← Build Incrementally](10-build-incrementally.md) | [Next: API Pattern →](12-pattern-api.md)
