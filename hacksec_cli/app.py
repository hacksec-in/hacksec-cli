from interface.cli import cli as interface_cli
from config import app_config
from interface.banner.banner import ShowBanner
from mechanism.authentication.login import Login

config, user = app_config()
cli = interface_cli(
    prefix=user.username+"#", history_file="history.txt")
ShowBanner(version=config.version, host=config.website)

if user.isLogin == False:
    print("Your not logged in")
    Login.login_request(interface=cli)


def main():
    """entry point"""
    while True:
        cli.get_prompt()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
