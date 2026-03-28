class Note:
    def __init__(self, note_id: int, title: str, content: str = None, date=None, user_id: int = None, budget_id: int = None):
        self.note_id = note_id
        self.title = title
        self.content = content
        self.date = date
        self.user_id = user_id
        self.budget_id = budget_id