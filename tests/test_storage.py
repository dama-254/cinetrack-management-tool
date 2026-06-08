import pytest
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import (save_users, load_users, save_projects, load_projects,
                            find_user, find_project, USERS_FILE, PROJECTS_FILE)

@pytest.fixture(autouse=True)
def clean_files():
    for f in [USERS_FILE, PROJECTS_FILE]:
        if os.path.exists(f):
            os.remove(f)
    yield
    for f in [USERS_FILE, PROJECTS_FILE]:
        if os.path.exists(f):
            os.remove(f)

class TestStorage:
    def test_save_load_users(self):
        users = [User("Alex", "Director"), User("Sam", "Producer")]
        save_users(users)
        loaded = load_users()
        assert len(loaded) == 2
        assert loaded[0].name == "Alex"

    def test_save_load_projects(self):
        projects = [Project("Dark Horizon", "Alex", "Sci-Fi", 500000)]
        projects[0].add_task(Task("Write Script"))
        save_projects(projects)
        loaded = load_projects()
        assert len(loaded) == 1
        assert len(loaded[0].tasks) == 1

    def test_find_user(self):
        users = [User("Alex", "Director")]
        assert find_user("alex", users) is not None

    def test_find_user_not_found(self):
        assert find_user("Bob", [User("Alex")]) is None

    def test_find_project(self):
        projects = [Project("Dark Horizon", "Alex")]
        assert find_project("dark horizon", projects) is not None

    def test_load_empty_returns_list(self):
        assert load_users() == []
