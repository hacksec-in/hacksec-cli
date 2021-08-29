import sys
from rich.console import Console
from os import path
import json

console = Console()


class Authenticator():
    """ Login Class """

    def __init__(self, request, interface):
        """ Login Class Initialization """
        self.request = request
        self.interface = interface

    def save_new_user(self, response):
        """ Save new user information """
        DATA_FOLDER = path.join(path.expanduser(
            '~'), ".config", "hacksec")
        DATA_FILE = path.join(DATA_FOLDER, "user.json")
        with open(DATA_FILE, "w") as write_file:
            json.dump(response, write_file, indent=4)

    def login_user(self, response):
        """save user login information"""
        self.interface.prefix = response["username"] + self.interface.prefix
        self.request.authenticate(response["access_token"])
        self.save_new_user(response)

    def login_server(self, username, password):
        """ Login into Server """
        payload = {
            "username": username,
            "password": password
        }
        response, status = self.request.post(
            endpoint="/authorization/login", payload=payload)
        if status == 200:
            return response, True, None
        return None, False, "Your username and password is wrong"

    def login_request(self):
        """ Ask the user for login """
        try:
            while True:
                username = self.interface.get_prompt("Enter your username#")
                if username == "":
                    self.interface.print_error("Username cannot be empty")
                    continue
                password = self.interface.get_prompt(
                    "Enter your password#", is_password=True)
                if password == "":
                    self.interface.print_error("Password cannot be empty")
                    continue
                with console.status("[bold green]Please wait..."):
                    res, status, err = self.login_server(username, password)
                if status:
                    res["username"] = username
                    self.interface.print_success(
                        "You are successfully logged in")
                    self.login_user(res)
                    self.interface.handle_menu(
                        self.interface.show_main_menu(self.interface))
                    break
                else:
                    self.interface.print_error(err)
                    continue
        except KeyboardInterrupt:
            self.request.close_session()
            self.interface.print_warning("User interrupted\n\nExiting...")
            sys.exit()
