from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from tempfile import gettempdir
from os import path
from termcolor import cprint


class cli():
    def __init__(self, prefix, history_file):
        self.prefix = prefix
        self.history_file = path.join(gettempdir(), history_file)

    def get_prompt(self, label=None):
        if not label:
            return prompt(self.prefix + " ",
                          history=FileHistory(self.history_file),
                          auto_suggest=AutoSuggestFromHistory(),
                          )
        return prompt(label + " ",
                      history=FileHistory(self.history_file),
                      auto_suggest=AutoSuggestFromHistory(),
                      )

    @staticmethod
    def print_error(msg):
        cprint(msg, 'red')

    @staticmethod
    def print_success(msg):
        cprint(msg, 'green')

    @staticmethod
    def print_warning(msg):
        cprint(msg, 'yellow')

    @staticmethod
    def print_info(msg):
        cprint(msg, 'blue')
