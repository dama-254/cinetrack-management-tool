from datetime import datetime

class Task:
    CATEGORIES = ["Pre-Production", "Production", "Post-Production", "Marketing", "Other"]

    def __init__(self, title: str, assignee: str = "Unassigned", due_date: str = "", category: str = "Other"):
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")
        self.title = title.strip()
        self.assignee = assignee
        self.due_date = due_date
        self.category = category if category in self.CATEGORIES else "Other"
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def mark_complete(self):
        self.completed = True

    def to_dict(self) -> dict:
        return {
            "title": self.title, "assignee": self.assignee,
            "due_date": self.due_date, "category": self.category,
            "completed": self.completed, "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        task = cls(data["title"], data.get("assignee", "Unassigned"),
                   data.get("due_date", ""), data.get("category", "Other"))
        task.completed = data.get("completed", False)
        task.created_at = data.get("created_at", "")
        return task

    def __repr__(self):
        status = "Done" if self.completed else "Pending"
        return f"Task({self.title}, {status}, assignee={self.assignee})"
