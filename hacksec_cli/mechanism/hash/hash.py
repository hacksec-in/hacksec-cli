from interface.menu.menu import main_menu
from rich.console import Console

console = Console()


class Hash():
    """hash class"""

    def send_hash(self, machine_name, hash, request):
        """send hash to server"""
        payload = {
            "machine_name": machine_name,
            "hash": hash
        }
        data = request.post(endpoint="/machines/hash", payload=payload)
        return data[0], data[1]

    def submit_hash(self, command, request):
        """send hash for check to hacksec server"""
        cmd = command.split()
        try:
            machine_name = cmd[1]
            hash = cmd[2]
        except IndexError:
            console.print(
                "Error: Please provide machine name and hash", style="bold red")
        with console.status("[bold green]please wait...\n") as status:
            response, status_code = self.send_hash(machine_name, hash, request)
            if status_code == 200:
                console.print(response["data"],
                              style="bold green")
            else:
                console.print(response["detail"],
                              style="bold red")
