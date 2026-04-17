# UML (PlantUML)

Copy/paste any `.puml` file content into a PlantUML renderer (for example the PlantUML web server or a VS Code PlantUML plugin).

- `docs/uml/class_diagram.puml`: high-level architecture (UI → services → repositories → DB + models)
- `docs/uml/sequence_add_transaction.puml`: flow for saving a transaction
- `docs/uml/sequence_login.puml`: flow for login
- `docs/uml/sequence_add_budget.puml`: flow for adding/updating a budget
- `docs/uml/sequence_edit_transaction.puml`: flow for editing a transaction
- `docs/uml/sequence_dashboard.puml`: dashboard load/refresh/save/export flow
- `docs/uml/usecase.puml`: main actors + use cases
- `docs/uml/activity_add_transaction.puml`: activity flow for adding a transaction
- `docs/uml/object_add_transaction_snapshot.puml`: example runtime object snapshot
- `docs/uml/erd.puml`: ERD from `database/schema.sql`
- `docs/uml/eer.puml`: EER (enhanced/logical) diagram (includes inheritance + derived attributes)
- `docs/uml/erd_dashboard.puml`: dashboard ERD (logical views used by `DashBoardService`)
