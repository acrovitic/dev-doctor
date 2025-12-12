from rich.console import Console

console = Console()


def print_report(results):
    passed = 0
    failed = 0

    for r in results:
        if r.passed:
            console.print(f"[green]✓[/green] {r.name} — {r.details}")
            passed += 1
        else:
            console.print(f"[red]✗[/red] {r.name} — {r.details}")
            failed += 1

    console.print()
    console.print(f"Summary: {passed} passed, {failed} failed")
