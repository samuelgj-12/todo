class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id = code_id
        self.title = title
        self.description = description
        self.completed = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed: bool = True

    def add_tag(self,tags: list[str]):
        self.tags = tags

    def __str__(self):
        return f"{self.code_id}-{self.title}"
