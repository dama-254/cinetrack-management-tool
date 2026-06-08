import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
USERS_FILE = os.path.join(DATA_DIR, "users.json")
PROJECTS_FILE = os.path.join(DATA_DIR, "projects.json")

def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def save_json(filepath: str, data: list):
    ensure_data_dir()
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print(f"[ERROR] Could not save data: {e}")

def load_json(filepath: str) -> list:
    ensure_data_dir()
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"[ERROR] Could not load data: {e}")
        return []

def save_users(users: list):
    save_json(USERS_FILE, [u.to_dict() for u in users])

def load_users() -> list:
    from models.user import User
    return [User.from_dict(d) for d in load_json(USERS_FILE)]

def save_projects(projects: list):
    save_json(PROJECTS_FILE, [p.to_dict() for p in projects])

def load_projects() -> list:
    from models.project import Project
    return [Project.from_dict(d) for d in load_json(PROJECTS_FILE)]

def find_user(name: str, users: list):
    for u in users:
        if u.name.lower() == name.lower():
            return u
    return None

def find_project(title: str, projects: list):
    for p in projects:
        if p.title.lower() == title.lower():
            return p
    return None
