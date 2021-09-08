#!/usr/bin/python3
from interface.cli import cli as interface_cli
from config import app_config
from interface.banner.banner import ShowBanner
from mechanism.authentication.login import Authenticator
from utils.request.req import MakeRequest
import json
import os
import sys
from update import version_verify

config, user = app_config()
version_verify(config.version)
request = MakeRequest(config)
cli = interface_cli(
    prefix=user.username+config.cmd_prefix, history_file="history.txt", request=request)
Login = Authenticator(request=request, interface=cli)
ShowBanner(version=config.version, host=config.website)


def Exit():
    request.close_session()
    cli.print_warning("\nExiting...")


def LoadExternalConfig():
    """load external config"""
    config_file = os.path.join(os.path.expanduser('~'), "hacksec.json")
    if os.path.isfile(config_file):
        with open(config_file, "r") as external_config:
            return json.load(external_config)
    return None


def Logout():
    """logout"""
    try:
        user.logout()
        os.remove(os.path.expanduser('~'))
    except:
        pass
    cli.print_info("Logged out")
    Exit()
    sys.exit(0)


if user.isLogin == False:
    cli.print_info("Your not logged in")
    Login.login_request(Logout)
else:
    request.authenticate(user.access_token)


def main():
    """entry point"""
    external_config = LoadExternalConfig()
    if external_config != None:
        while True:
            anwser = cli.get_prompt()
            for i in external_config["shortcuts"]:
                if anwser == i["shortcut"]:
                    anwser = anwser.replace(i["shortcut"], i["command"])
            cli.handle_menu(anwser, Logout)
    else:
        while True:
            anwser = cli.get_prompt()
            cli.handle_menu(anwser, Logout)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        Exit()
