from interface.menu.menu import main_menu
from rich.console import Console
import os
import sys
import subprocess

console = Console()


class Settings():
    """A class to change settings in user profile"""

    def open_uri(self, url):
        if sys.platform == 'win32':
            os.startfile(url)
        elif sys.platform == 'darwin':
            subprocess.Popen(['open', url])
        else:
            try:
                subprocess.Popen(['xdg-open', url])
            except OSError:
                print('Please open a browser on: '+url)

    def get_data(self, request, url, data):
        """extract data from activity"""
        data = request.post(endpoint=url, payload=data)
        return data[0], data[1]

    def change_password(self, cli, request):
        """Change password"""
        old_password = cli.get_prompt(
            label="Please enter your old password: ", is_password=True)
        new_password = cli.get_prompt(
            label="Please enter your new password: ", is_password=True)
        payload = {
            "old_password": old_password,
            "password": new_password
        }
        with console.status("[bold green]please wait...\n") as status:
            response, status = self.get_data(
                request, "/authorization/change/password", payload)
            if status == 200:
                console.print(response["data"], style="bold green")
            else:
                console.print("Error: {}".format(
                    response["data"]), style="bold red")

    def change_account_information(self, cli, request):
        """Change account information"""
        options = ["change username", "change email"]
        # anwser = main_menu("Settings", options,
        #                    "i want to ")
        self.open_uri("https://www.app.hacksec.in/settings")

    def generate_setting_menu(self, interface, request):
        """Generate menu for settings"""
        options = ["change password", "change account information"]
        anwser = main_menu("Settings", options,
                           "i want to ")
        if anwser == options[0]:
            self.change_password(interface, request)
        else:
            self.change_account_information(interface, request)
