import sys


class Login():
    """ Login Class """

    @staticmethod
    def login_request(interface):
        """ Ask the user for login """
        try:
            while True:
                username = interface.get_prompt("Enter your username#")
                if username == "":
                    interface.print_error("Username cannot be empty")
                    continue
                password = interface.get_prompt("Enter your password#")
                if password == "":
                    interface.print_error("Password cannot be empty")
                    continue
                break
        except KeyboardInterrupt:
            interface.print_warning("User interrupted\n\nExiting...")
            sys.exit()
