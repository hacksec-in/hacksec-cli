from interface.menu.menu import main_menu
from interface.cli import cli
from rich.console import Console

cli = cli()
console = Console()


class Settings():
    """A class to change settings in user profile"""

    def get_data(self, request, url, data):
        """extract data from activity"""
        data = request.post(endpoint=url, data=data)
        return data[0], data[1]

    def change_password(self, request):
        """Change password"""
        old_password = cli.get_prompt(
            label="Please enter your old password", is_password=True)
        new_password = cli.get_prompt(
            label="Please enter your new password", is_password=True)
        payload = {
            "old_password": old_password,
            "password": new_password
        }
        with console.status("[bold green]please wait...\n") as status:
            response, status = self.get_data(
                request, "/authorization/change/password", payload)
            if status == 200:
                console.print(response, style="bold green")
            else:
                console.print(response, style="bold red")

    def change_account_information(self, request):
        """Change account information"""
        options = ["change username", "change email"]
        anwser = main_menu("Settings", options,
                           "i want to ")
        if anwser == options[0]:
            self.change_username(request)
        else:
            self.change_email(request)

    def generate_setting_menu(self, request):
        """Generate menu for settings"""
        options = ["change password", "change account information"]
        anwser = main_menu("Settings", options,
                           "i want to ")
        if anwser == options[0]:
            self.change_password(request)
        else:
            self.change_account_information(request)
