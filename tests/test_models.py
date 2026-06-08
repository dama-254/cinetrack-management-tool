import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from models.user import User
from models.project import Project
from models.task import Task

class TestUser:
    def test_create_user(self):
        user = User("Alex", "Director")
        assert user.name == "Alex"
        assert user.role == "Director"

    def test_invalid_role_defaults(self):
        user = User("Sam", "SuperStar")
        assert user.role == "Crew"

    def test_empty_name_raises(self):
        with pytest.raises(ValueError):
            User("")

    def test_add_project(self):
        user = User("Alex", "Director")
        user.add_project("Dark Horizon")
        assert "Dark Horizon" in user.projects

    def test_no_duplicate_projects(self):
        user = User("Alex")
        user.add_project("Dark Horizon")
        user.add_project("Dark Horizon")
        assert user.projects.count("Dark Horizon") == 1

    def test_to_dict_from_dict(self):
        user = User("Alex", "Director")
        user.add_project("Dark Horizon")
        restored = User.from_dict(user.to_dict())
        assert restored.name == "Alex"
        assert "Dark Horizon" in restored.projects

class TestTask:
    def test_create_task(self):
        task = Task("Write Script", "Alex", "2025-06-01", "Pre-Production")
        assert task.title == "Write Script"
        assert task.completed == False

    def test_empty_title_raises(self):
        with pytest.raises(ValueError):
            Task("")

    def test_mark_complete(self):
        task = Task("Write Script")
        task.mark_complete()
        assert task.completed == True

    def test_invalid_category_defaults(self):
        task = Task("Do something", category="InvalidCat")
        assert task.category == "Other"

    def test_to_dict_from_dict(self):
        task = Task("Write Script", "Alex", "2025-06-01", "Pre-Production")
        task.mark_complete()
        restored = Task.from_dict(task.to_dict())
        assert restored.completed == True

class TestProject:
    def test_create_project(self):
        proj = Project("Dark Horizon", "Alex", "Sci-Fi", 500000)
        assert proj.title == "Dark Horizon"
        assert proj.genre == "Sci-Fi"

    def test_empty_title_raises(self):
        with pytest.raises(ValueError):
            Project("", "Alex")

    def test_invalid_genre_defaults(self):
        proj = Project("Movie", "Alex", "UnknownGenre")
        assert proj.genre == "Other"

    def test_add_task(self):
        proj = Project("Dark Horizon", "Alex")
        proj.add_task(Task("Write Script"))
        assert len(proj.tasks) == 1

    def test_add_contributor(self):
        proj = Project("Dark Horizon", "Alex")
        proj.add_contributor("Sam")
        assert "Sam" in proj.contributors

    def test_no_duplicate_contributors(self):
        proj = Project("Dark Horizon", "Alex")
        proj.add_contributor("Sam")
        proj.add_contributor("Sam")
        assert proj.contributors.count("Sam") == 1

    def test_progress_no_tasks(self):
        proj = Project("Dark Horizon", "Alex")
        assert "0%" in proj.get_progress()

    def test_progress_with_tasks(self):
        proj = Project("Dark Horizon", "Alex")
        t1 = Task("Script")
        t2 = Task("Casting")
        t1.mark_complete()
        proj.add_task(t1)
        proj.add_task(t2)
        assert "50%" in proj.get_progress()

    def test_to_dict_from_dict(self):
        proj = Project("Dark Horizon", "Alex", "Sci-Fi", 500000)
        proj.add_task(Task("Write Script"))
        proj.add_contributor("Sam")
        restored = Project.from_dict(proj.to_dict())
        assert restored.title == "Dark Horizon"
        assert len(restored.tasks) == 1
