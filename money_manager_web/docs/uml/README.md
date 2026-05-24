# PlantUML Diagrams

These files document the current Django multi-user web application:

- `auth-sequence.puml`: account signup and username/email login flow.
- `use-case.puml`: visitor, member, administrator, and password-reset use cases.
- `system-diagram.puml`: browser, Django server, email provider, and PostgreSQL architecture.
- `database-schema.puml`: Django authentication and expense-table relationships.

Render all diagrams with a PlantUML installation:

```powershell
plantuml .\docs\uml\*.puml
```

The database schema diagram documents tables produced by Django migrations. Update the Django models and migrations first, then update the diagram when the application schema changes.
