class User:
    ROLES = ["Director", "Producer", "Writer", "Editor", "Cinematographer", "Crew"]

    def __init__(self, name: str, role: str = "Crew"):
        if not name or not name.strip():
            raise ValueError("User name cannot be empty.")
        self.name = name.strip()
        self.role = role if role in self.ROLES else "Crew"
        self.projects = []

    def add_project(self, project_title: str):
        if project_title not in self.projects:
            self.projects.append(project_title)

    def to_dict(self) -> dict:
        return {"name": self.name, "role": self.role, "projects": self.projects}

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        user = cls(data["name"], data.get("role", "Crew"))
        user.projects = data.get("projects", [])
        return user

    def __repr__(self):
        return f"User(name={self.name}, role={self.role}, projects={len(self.projects)})"
