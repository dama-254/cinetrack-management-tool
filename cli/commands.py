from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import (load_users, save_users, load_projects, save_projects, find_user, find_project)
from utils.display import (display_users, display_projects, display_tasks, print_success, print_error, print_info)

def cmd_add_user(args):
    users = load_users()
    if find_user(args.name, users):
        print_error(f"Crew member '{args.name}' already exists.")
        return
    user = User(args.name, args.role)
    users.append(user)
    save_users(users)
    print_success(f"Crew member '{args.name}' added with role '{user.role}'.")

def cmd_list_users(args):
    display_users(load_users())

def cmd_delete_user(args):
    users = load_users()
    user = find_user(args.name, users)
    if not user:
        print_error(f"Crew member '{args.name}' not found.")
        return
    users.remove(user)
    save_users(users)
    print_success(f"Crew member '{args.name}' removed.")

def cmd_add_project(args):
    users = load_users()
    projects = load_projects()
    user = find_user(args.user, users)
    if not user:
        print_error(f"Crew member '{args.user}' not found. Add them first.")
        return
    if find_project(args.title, projects):
        print_error(f"Production '{args.title}' already exists.")
        return
    project = Project(args.title, args.user, args.genre, args.budget)
    project.add_contributor(args.user)
    user.add_project(args.title)
    projects.append(project)
    save_projects(projects)
    save_users(users)
    print_success(f"Production '{args.title}' created for '{args.user}'.")

def cmd_list_projects(args):
    display_projects(load_projects(), getattr(args, "user", None))

def cmd_add_contributor(args):
    users = load_users()
    projects = load_projects()
    project = find_project(args.project, projects)
    if not project:
        print_error(f"Production '{args.project}' not found.")
        return
    contributor = find_user(args.contributor, users)
    if not contributor:
        print_error(f"Crew member '{args.contributor}' not found.")
        return
    project.add_contributor(args.contributor)
    contributor.add_project(args.project)
    save_projects(projects)
    save_users(users)
    print_success(f"'{args.contributor}' added as contributor to '{args.project}'.")

def cmd_project_progress(args):
    projects = load_projects()
    project = find_project(args.project, projects)
    if not project:
        print_error(f"Production '{args.project}' not found.")
        return
    print_info(f"Progress for '{project.title}': {project.get_progress()}")

def cmd_add_task(args):
    projects = load_projects()
    project = find_project(args.project, projects)
    if not project:
        print_error(f"Production '{args.project}' not found.")
        return
    task = Task(args.title, args.assignee, args.due_date, args.category)
    project.add_task(task)
    save_projects(projects)
    print_success(f"Task '{args.title}' added to '{args.project}'.")

def cmd_list_tasks(args):
    projects = load_projects()
    project = find_project(args.project, projects)
    if not project:
        print_error(f"Production '{args.project}' not found.")
        return
    display_tasks(project)

def cmd_complete_task(args):
    projects = load_projects()
    project = find_project(args.project, projects)
    if not project:
        print_error(f"Production '{args.project}' not found.")
        return
    for task in project.tasks:
        if task.title.lower() == args.task.lower():
            task.mark_complete()
            save_projects(projects)
            print_success(f"Task '{task.title}' marked as complete!")
            return
    print_error(f"Task '{args.task}' not found in '{args.project}'.")

def cmd_delete_task(args):
    projects = load_projects()
    project = find_project(args.project, projects)
    if not project:
        print_error(f"Production '{args.project}' not found.")
        return
    for task in project.tasks:
        if task.title.lower() == args.task.lower():
            project.tasks.remove(task)
            save_projects(projects)
            print_success(f"Task '{task.title}' deleted from '{args.project}'.")
            return
    print_error(f"Task '{args.task}' not found in '{args.project}'.")

def cmd_search(args):
    projects = load_projects()
    results = [p for p in projects if args.query.lower() in p.title.lower()
               or args.query.lower() in p.genre.lower()
               or args.query.lower() in p.owner.lower()]
    if not results:
        print_info(f"No productions found matching '{args.query}'.")
        return
    display_projects(results)
