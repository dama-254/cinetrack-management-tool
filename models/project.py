from datetime import datetime
from models.task import Task

class BaseEntity:
    def __init__(self, title: str):
        if not title or not title.strip():
            raise ValueError("Title cannot be empty.")
        self.title = title.strip()
        self.created_at = datetime.now().strftime("%Y-%m-%d")

    def get_age_days(self) -> int:
        created = datetime.strptime(self.created_at, "%Y-%m-%d")
        return (datetime.now() - created).days

class Project(BaseEntity):
    GENRES = ["Action", "Drama", "Comedy", "Horror", "Sci-Fi", "Documentary", "Animation", "Other"]

    def __init__(self, title: str, owner: str, genre: str = "Other", budget: float = 0.0):
        super().__init__(title)
        self.owner = owner
        self.genre = genre if genre in self.GENRES else "Other"
        self.budget = float(budget)
        self.tasks = []
        self.contributors = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def add_contributor(self, name: str):
        if name not in self.contributors:
            self.contributors.append(name)

    def get_progress(self) -> str:
        total = len(self.tasks)
        if total == 0:
            return "0% (no tasks yet)"
        done = sum(1 for t in self.tasks if t.completed)
        pct = int((done / total) * 100)
        return f"{pct}% ({done}/{total} tasks complete)"

    def get_pending_tasks(self) -> list:
        return [t for t in self.tasks if not t.completed]

    def get_completed_tasks(self) -> list:
        return [t for t in self.tasks if t.completed]

    def to_dict(self) -> dict:
        return {
            "title": self.title, "owner": self.owner, "genre": self.genre,
            "budget": self.budget, "created_at": self.created_at,
            "contributors": self.contributors,
            "tasks": [t.to_dict() for t in self.tasks]
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Project":
        proj = cls(data["title"], data["owner"], data.get("genre", "Other"), data.get("budget", 0.0))
        proj.created_at = data.get("created_at", datetime.now().strftime("%Y-%m-%d"))
        proj.contributors = data.get("contributors", [])
        proj.tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
        return proj

    def __repr__(self):
        return f"Project(title={self.title}, owner={self.owner}, genre={self.genre})"
