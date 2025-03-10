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
        return f"{self.code_id} - {self.title}"

class TodoBook:
    def __init__(self):
        self.todos = {}
        self.next_id = 1

    def add_todo(self, title: str, description: str   ) -> int:
        code_id = len(self.todos)+1
        new_todo = Todo(code_id, title, description)
        self.todos[code_id] = new_todo
        return code_id

    def pending_todo(self):
        return [todo for todo in self.todos.values() if not todo.completed]