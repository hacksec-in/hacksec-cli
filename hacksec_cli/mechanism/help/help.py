from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax

console = Console()

JSON_FORMATED_CODE = """
{
    "shortcuts":[
        {   
            "shortcut": "hello_about",
            "command": "about"
        }
    ]
}
"""
HACKSEC_JSON = "Anwser: Create a hacksec.json file inside your home directory and inside the shortcuts list enter your shortcut and command in dictionary"


class Help():
    """Help class"""

    def generate_table(self, options):
        """Generate help table"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("shortcut", style="green")
        table.add_column("command", style="green")
        table.add_column("description", style="green")
        for i in options:
            table.add_row(i["short"], i["command"], i["desc"])
        console.print(table)
        console.print("1.How i can create my own shortcut commands?",
                      style="bold green")
        console.print(HACKSEC_JSON, style="bold green")
        console.print("Example : ", style="bold green")
        syntax = Syntax(JSON_FORMATED_CODE, "python",
                        theme="monokai", line_numbers=True)
        console.print(syntax)

    def generate_help(self):
        """Generate help table from list and dict"""
        options = [{"short": "mn", "command": "menu", "desc": "open menu"},
                   {"short": "ov", "command": "overview", "desc": "show overview"},
                   {"short": "aw", "command": "active weblab",
                       "desc": "show active weblab"},
                   {"short": "hs", "command": "hash",
                       "desc": "submit weblab hash example : hash weblab_name hash_goes_here"},
                   {"short": "rp", "command": "report",
                    "desc": "show all report"},
                   {"short": "sr", "command": "send_report",
                    "desc": "send your report to us using this command and we will review it and add it to our website"},
                   {"short": "rw", "command": "retired weblab",
                       "desc": "show retired weblab"},
                   {"short": "uw", "command": "upcoming weblab",
                       "desc": "show upcoming weblab"},
                   {"short": "p", "command": "profile",
                       "desc": "show user profile"},
                   {"short": "t", "command": "team",
                       "desc": "show user's team profile"},
                   {"short": "an", "command": "announcement",
                       "desc": "show hacksec's important announcements"},
                   {"short": "av", "command": "activity",
                       "desc": "show user activity"},
                   {"short": "rn", "command": "ranking",
                       "desc": "show popup a menu where you can choose which type of ranking you want see"},
                   {"short": "ur", "command": "show user ranking",
                       "desc": "show overview"},
                   {"short": "tr", "command": "show team ranking",
                       "desc": "show overview"},
                   {"short": "cn", "command": "contact us",
                       "desc": "show how you can contact us"},
                   {"short": "st", "command": "settings",
                       "desc": "this will open settings menu where you can change your username ,email or password"},
                   {"short": "ab", "command": "about", "desc": "show what we are"},
                   {"short": "h", "command": "help", "desc": "show help"},
                   {"short": "!", "command": "!",
                       "desc": "use ! to run os command example : !ls -la"},
                   {"short": "ul", "command": "upload_lab",
                       "desc": "you can upload your own weblab using um or upload_lab command"},
                   {"short": "q", "command": "quit", "desc": "quit program"},
                   {"short": "cl", "command": "clear", "desc": "clear screen"},
                   {"short": "lg", "command": "logout", "desc": "logout user from hacksec-cli"}]
        self.generate_table(options)
