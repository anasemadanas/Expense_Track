import os

# Define project structure
project_structure = {
    "money_manager": {
        "docs": ["project_document.md"],
        "src": {
            "presentation": {
                "views": [
                    "dashboard_view.py",
                    "add_transaction_view.py",
                    "budget_view.py"
                ],
                "controllers": [
                    "transaction_controller.py"
                ],
                "main.py": None
            },
            "business": {
                "services": [
                    "transaction_service.py",
                    "budget_service.py"
                ],
                "models": [
                    "transaction.py",
                    "budget.py"
                ]
            },
            "data": {
                "repositories": [
                    "transaction_repo.py",
                    "budget_repo.py"
                ],
                "interfaces": [
                    "ITransactionRepo.py",
                    "IBudgetRepo.py"
                ],
                "database.py": None
            },
            "shared": [
                "util.py",
                "constants.py"
            ]
        },
        "tests": [
            "test_transaction_service.py",
            "test_budget_service.py",
            "test_repo.py"
        ],
        "requirements.txt": None,
        ".gitignore": None,
        "README.md": None
    }
}

# Function to create files and folders recursively
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for item in content:
                if isinstance(item, str):
                    open(os.path.join(path, item), 'w').close()
                elif isinstance(item, dict):
                    create_structure(path, item)
        elif content is None:
            open(path, 'w').close()

# Run the script
create_structure(".", project_structure)
print("Project structure created successfully!")