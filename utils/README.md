# 🎬 CineTrack — Film Production Management CLI Tool

CineTrack is a command-line tool for managing film productions. Crew members can create productions, assign tasks, track progress, and collaborate as contributors.

## Project Structure

```
cinetrack/
├── main.py              # Entry point
├── requirements.txt     # Dependencies
├── pytest.ini           # Test config
├── data/
│   ├── users.json       # Persisted crew members
│   └── projects.json    # Persisted productions
├── models/
│   ├── user.py          # User class
│   ├── project.py       # Project class (inherits BaseEntity)
│   └── task.py          # Task class
├── cli/
│   └── commands.py      # All CLI command handlers
├── utils/
│   ├── storage.py       # JSON persistence
│   └── display.py       # Rich pretty-printing
└── tests/
    ├── test_models.py   # Unit tests for models
    └── test_storage.py  # Unit tests for storage
```

## Setup

```bash
pip install -r requirements.txt
```

## Commands

### Users (Crew Members)
```bash
python main.py add-user --name "Alex" --role Director
python main.py list-users
python main.py delete-user --name "Alex"
```

### Productions (Projects)
```bash
python main.py add-project --user "Alex" --title "Dark Horizon" --genre Sci-Fi --budget 500000
python main.py list-projects
python main.py list-projects --user "Alex"
python main.py add-contributor --project "Dark Horizon" --contributor "Sam"
python main.py progress --project "Dark Horizon"
```

### Tasks
```bash
python main.py add-task --project "Dark Horizon" --title "Write Script" --assignee "Alex" --category Pre-Production --due-date 2025-06-01
python main.py list-tasks --project "Dark Horizon"
python main.py complete-task --project "Dark Horizon" --task "Write Script"
python main.py delete-task --project "Dark Horizon" --task "Write Script"
```

### Search
```bash
python main.py search --query "Sci-Fi"
```

## Run Tests
```bash
pytest tests/ -v
```

## Data Model

- **User → Projects** (one-to-many): Each crew member owns multiple productions
- **Project → Tasks** (one-to-many): Each production has multiple tasks
- **Project ↔ Contributors** (many-to-many): Multiple crew members can contribute to one production