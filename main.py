'''
+==Spelunker==================================================================+
‖                                                                             ‖
‖ Author(s): Melesio Albavera                                                 ‖
‖ Created: 28 June 2023                                                       ‖
‖ Description: TO-DO                                                          ‖
‖                                                                             ‖
+=============================================================================+
'''

from pyfiglet import figlet_format
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.prompt import Prompt
from time import sleep
import os

class ConsoleWrapper(Console):
    def __init__(self, *args, **kwargs):
        console_file = open(os.devnull, 'w')
        super().__init__(record = True, file = console_file, *args, **kwargs)

    def __rich_console__(self, console, options):
        texts = self.export_text(clear=False).split('\n')
        for line in texts[-options.height:]:
            yield line

def main():
    version = "0.0.1"
    prompt = "[>>]"
    title_art = f"\n{figlet_format('Spelunker', font = 'kban')}"
    help_text = "\nType \"help\" or \"h\" for more information."
    splash_title = f"{title_art}\n[Version {version}]{help_text}"

    layout = Layout(name = "root")
    wrapper_console = ConsoleWrapper()

    layout.split(
        Layout(
            Panel(splash_title, title = "Welcome to", title_align = "left"),
            name = "header", size = 13),
        Layout(Panel(wrapper_console), name = "main"),
    )

    with Live(layout):
        name = Prompt.ask(prompt, console = wrapper_console)
        wrapper_console.print(name)

if __name__ == "__main__":
    main()
