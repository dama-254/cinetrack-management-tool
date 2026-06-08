from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def print_success(msg: str):
    console.print(f"[bold green]✔ {msg}[/bold green]")

def print_error(msg: str):
    console.print(f"[bold red]✘ {msg}[/bold red]")

def print_info(msg: str):
    console.print(f"[bold cyan]ℹ {msg}[/bold cyan]")

def display_users(users: list):
    if not users:
        print_info("No crew members found.")
        return
    table = Table(title="🎬 CineTrack Crew Members", box=box.ROUNDED)
    table.add_column("Name", style="bold yellow")
    table.add_column("Role", style="cyan")
    table.add_column("Projects", style="green")
    for u in users:
        table.add_row(u.name, u.role, str(len(u.projects)))
    console.print(table)

def display_projects(projects: list, owner_filter: str = None):
    filtered = projects
    if owner_filter:
        filtered = [p for p in projects if p.owner.lower() == owner_filter.lower()]
    if not filtered:
        print_info("No productions found.")
        return
    table = Table(title="🎥 Film Productions", box=box.ROUNDED)
    table.add_column("Title", style="bold magenta")
    table.add_column("Owner", style="yellow")
    table.add_column("Genre", style="cyan")
    table.add_column("Budget ($)", style="green")
    table.add_column("Progress", style="white")
    table.add_column("Contributors", style="blue")
    for p in filtered:
        table.add_row(p.title, p.owner, p.genre, f"{p.budget:,.0f}",
                      p.get_progress(), ", ".join(p.contributors) if p.contributors else "None")
    console.print(table)

def display_tasks(project):
    if not project.tasks:
        print_info(f"No tasks for '{project.title}' yet.")
        return
    table = Table(title=f"📋 Tasks for: {project.title}", box=box.ROUNDED)
    table.add_column("Title", style="bold white")
    table.add_column("Category", style="cyan")
    table.add_column("Assignee", style="yellow")
    table.add_column("Due Date", style="blue")
    table.add_column("Status", style="green")
    for t in project.tasks:
        status = "[green]Done[/green]" if t.completed else "[red]Pending[/red]"
        table.add_row(t.title, t.category, t.assignee, t.due_date or "N/A", status)
    console.print(table)
