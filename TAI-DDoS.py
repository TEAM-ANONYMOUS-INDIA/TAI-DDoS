import time
import sys
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()

def animate_text(text, color1, color2, delay=0.1):
    """Animate text with two alternating colors."""
    for i in range(3):  # Repeat animation 3 times
        console.print(Text(text, style=f"bold {color1}"), justify="center")
        time.sleep(delay)
        console.print(Text(text, style=f"bold {color2}"), justify="center")
        time.sleep(delay)
        console.clear()

def show_stylish_message():
    console.clear()
    
    # Stylish 'COMING SOON...'
    console.print(Panel.fit(
        "[bold magenta]COMING SOON...[/bold magenta]", 
        title="[bold cyan]Stay Tuned![/bold cyan]",
        border_style="bright_blue"
    ), justify="center")

    time.sleep(2)
    
    # Animate 'HydraKraken is Sleeping'
    animate_text("HydraKraken is Sleeping", "red", "blue", delay=0.3)

    # Final Sleepy Panel
    console.print(Panel.fit(
        "[bold yellow]💤 HydraKraken is Sleeping...[/bold yellow]",
        border_style="cyan",
        title="[bold green]Shh![/bold green]"
    ), justify="center")

if __name__ == "__main__":
    show_stylish_message()
