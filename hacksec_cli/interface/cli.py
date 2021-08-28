from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from tempfile import gettempdir
from os import path, system, name
from rich.console import Console
from interface.menu.menu import main_menu
import sys

console = Console()


class cli():
    def __init__(self, prefix, history_file, request):
        self.prefix = prefix
        self.history_file = path.join(gettempdir(), history_file)
        self.request = request

    def get_prompt(self, label=None, is_password=False):
        if not label:
            return prompt(self.prefix + " ",
                          history=FileHistory(self.history_file),
                          auto_suggest=AutoSuggestFromHistory(),
                          is_password=is_password
                          )
        return prompt(label + " ",
                      history=FileHistory(self.history_file),
                      auto_suggest=AutoSuggestFromHistory(),
                      is_password=is_password
                      )

    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def handle_menu(self, command):
        if command == "exit":
            self.request.close_session()
            console.print("\nExiting...", style="bold yellow")
            sys.exit()
        elif command == "menu":
            anwser = main_menu()
            self.handle_menu(anwser)
        elif command == None or command == "":
            pass
        elif command == "clear":
            self.clear()
        elif command.startswith("!"):
            system(command[1:])
        else:
            console.print("command not found", style="bold yellow")

    @staticmethod
    def print_error(msg):
        console.print(msg, style="bold red")

    @staticmethod
    def print_success(msg):
        console.print(msg, style="bold green")

    @staticmethod
    def print_warning(msg):
        console.print(msg, style="bold yellow")

    @staticmethod
    def print_info(msg):
        console.print(msg, style="bold blue")

    @staticmethod
    def show_main_menu(cls):
        try:
            anwser = main_menu()
            return anwser
        except KeyboardInterrupt:
            cls.request.close_session()
            console.print("\nExiting...", style="bold yellow")
