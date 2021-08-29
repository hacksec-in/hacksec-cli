from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from tempfile import gettempdir
from os import path, system, name
from rich.console import Console
from interface.menu.menu import main_menu
from mechanism.overview.overview import Overview
from mechanism.active.active import Active_machine
from mechanism.retired.retired import retired_machine
from mechanism.upcoming.upcoming import upcoming_machine
from mechanism.profile.profile import profile_info
from mechanism.teams.teams import teams_info
from mechanism.announcement.announcement import announcement
from mechanism.activity.activity import activity
from mechanism.ranking.ranking import ranking
from mechanism.contact_us.contact_us import contact_us
from mechanism.help.help import Help
from mechanism.settings.settings import Settings
from mechanism.hash.hash import Hash
from mechanism.report.report import Report
import sys

console = Console()
overview = Overview()
active_machine = Active_machine()
retired_machine = retired_machine()
upcoming_machine = upcoming_machine()
profile_info = profile_info()
team_info = teams_info()
announcement = announcement()
activity = activity()
ranking = ranking()
contact_us = contact_us()
help = Help()
settings = Settings()
hash = Hash()
report = Report()


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

    def handle_menu(self, command, Logout):
        if command == "exit" or command == "quit" or command == "q":
            self.request.close_session()
            console.print("\nExiting...", style="bold yellow")
            sys.exit()
        elif command == "menu" or command == "mn":
            anwser = main_menu()
            self.handle_menu(anwser, Logout)
        elif command == None or command == "":
            pass
        elif command == "clear" or command == "cl":
            self.clear()
        elif command.startswith("!"):
            system(command[1:])
        elif command == "overview" or command == "ov":
            overview.generate_dashboard(self.request)
        elif command == "active weblab" or command == "aw":
            active_machine.generate_table(self.request)
        elif command == "retired weblab" or command == "rw":
            retired_machine.generate_table(self.request)
        elif command == "upcoming weblab" or command == "uw":
            upcoming_machine.generate_table(self.request)
        elif command == "profile" or command == "p":
            profile_info.generate_profile(self.request)
        elif command == "team" or command == "t":
            team_info.generate_team(self.request, self.prefix)
        elif command == "announcement" or command == "an":
            announcement.generate_dashboard(self.request)
        elif command == "activity" or command == "av":
            activity.generate_activity(self.request)
        elif command == "report" or command == "rp":
            report.generate_report(self.request)
        elif command.startswith("send_report") or command.startswith("sr"):
            report.send_report(command, self.request)
        elif command == "ranking" or command == "rn":
            ranking.which_ranking(self.request)
        elif command == "user ranking" or command == "ur":
            ranking.generate_rank(self.request, True)
        elif command == "team ranking" or command == "tr":
            ranking.generate_rank(self.request, False)
        elif command == "upload_lab" or command == "ul":
            upcoming_machine.upload_machine(self, self.request)
        elif command == "settings" or command == "st":
            settings.generate_setting_menu(self, self.request)
        elif command == "help" or command == "h":
            help.generate_help()
        elif command.startswith("hash") or command.startswith("hs"):
            hash.submit_hash(command, self.request)
        elif command == "logout" or command == "lg":
            Logout()
        elif command == "contact us" or command == "cn":
            contact_us.generate_contact()
        elif command == "about" or command == "ab":
            console.print("We develop tools and software for making pentesting easy. Founded in 2021 by script1337, We hope you enjoy our products as much as we enjoy offering them to you. If you have any questions or comments, please don’t hesitate to contact us.", style="bold blue")
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
