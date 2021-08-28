from interface.cli import cli as interface_cli
from config import app_config
from interface.banner.banner import ShowBanner
from mechanism.authentication.login import Authenticator
from utils.request.req import MakeRequest

config, user = app_config()
request = MakeRequest(config)
cli = interface_cli(
    prefix=user.username+config.cmd_prefix, history_file="history.txt", request=request)
Login = Authenticator(request=request, interface=cli)
ShowBanner(version=config.version, host=config.website)


def Exit():
    request.close_session()
    cli.print_warning("\nExiting...")


if user.isLogin == False:
    cli.print_info("Your not logged in")
    Login.login_request()


def main():
    """entry point"""
    while True:
        anwser = cli.get_prompt()
        cli.handle_menu(anwser)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        Exit()
