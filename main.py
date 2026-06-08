import argparse
import sys
from cli.commands import (
    cmd_add_user, cmd_list_users, cmd_delete_user,
    cmd_add_project, cmd_list_projects, cmd_add_contributor, cmd_project_progress,
    cmd_add_task, cmd_list_tasks, cmd_complete_task, cmd_delete_task, cmd_search
)

def build_parser():
    parser = argparse.ArgumentParser(prog="cinetrack", description="🎬 CineTrack — Film Production Management CLI")
    sub = parser.add_subparsers(dest="command", help="Available commands")
    sub.required = True

    p = sub.add_parser("add-user", help="Add a crew member")
    p.add_argument("--name", required=True)
    p.add_argument("--role", default="Crew", choices=["Director","Producer","Writer","Editor","Cinematographer","Crew"])
    p.set_defaults(func=cmd_add_user)

    p = sub.add_parser("list-users", help="List all crew members")
    p.set_defaults(func=cmd_list_users)

    p = sub.add_parser("delete-user", help="Remove a crew member")
    p.add_argument("--name", required=True)
    p.set_defaults(func=cmd_delete_user)

    p = sub.add_parser("add-project", help="Create a film production")
    p.add_argument("--user", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--genre", default="Other", choices=["Action","Drama","Comedy","Horror","Sci-Fi","Documentary","Animation","Other"])
    p.add_argument("--budget", type=float, default=0.0)
    p.set_defaults(func=cmd_add_project)

    p = sub.add_parser("list-projects", help="List all productions")
    p.add_argument("--user", default=None)
    p.set_defaults(func=cmd_list_projects)

    p = sub.add_parser("add-contributor", help="Add contributor to production")
    p.add_argument("--project", required=True)
    p.add_argument("--contributor", required=True)
    p.set_defaults(func=cmd_add_contributor)

    p = sub.add_parser("progress", help="Show production progress")
    p.add_argument("--project", required=True)
    p.set_defaults(func=cmd_project_progress)

    p = sub.add_parser("add-task", help="Add a task to a production")
    p.add_argument("--project", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--assignee", default="Unassigned")
    p.add_argument("--due-date", dest="due_date", default="")
    p.add_argument("--category", default="Other", choices=["Pre-Production","Production","Post-Production","Marketing","Other"])
    p.set_defaults(func=cmd_add_task)

    p = sub.add_parser("list-tasks", help="List tasks for a production")
    p.add_argument("--project", required=True)
    p.set_defaults(func=cmd_list_tasks)

    p = sub.add_parser("complete-task", help="Mark a task complete")
    p.add_argument("--project", required=True)
    p.add_argument("--task", required=True)
    p.set_defaults(func=cmd_complete_task)

    p = sub.add_parser("delete-task", help="Delete a task")
    p.add_argument("--project", required=True)
    p.add_argument("--task", required=True)
    p.set_defaults(func=cmd_delete_task)

    p = sub.add_parser("search", help="Search productions")
    p.add_argument("--query", required=True)
    p.set_defaults(func=cmd_search)

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except ValueError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nExiting CineTrack.")
        sys.exit(0)

if __name__ == "__main__":
    main()
