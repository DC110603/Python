"""4. You are tasked with designing a logging system for an enterprise application.
The system must support writing logs to:
• Files
• Databases
• External monitoring systems
Instead of creating a deep inheritance hierarchy, design the system such that:
• A Logger object does not directly know how logs are written.
• The responsibility of writing logs is delegated to another object.
Create separate writer classes, each responsible for a specific destination.
Your design must allow:
• Switching the logging destination at runtime.
• Adding new log destinations without modifying existing code.
Explain:
• Why inheriting one logger from another would tightly couple the system.
• Why delegating responsibilities produces a more flexible design.
• Why this approach is easier to test and maintain. """