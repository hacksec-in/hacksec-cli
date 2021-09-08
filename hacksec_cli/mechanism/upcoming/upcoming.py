from rich.console import Console
from rich.table import Table
import os

console = Console()


class upcoming_machine():
    """upcoming machines class"""

    def get_data(self, request):
        """fetch upcoming machines data"""
        data = request.get(endpoint="/machines/upcoming")
        return data[0], data[1]

    def show_upcoming_machines(self, data):
        """Formate upcoming machines data to fit in tables and return table"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("machine_id", style="green")
        table.add_column("machine_name", style="green")
        table.add_column("host", style="green")
        table.add_column("hint", style="green")
        table.add_column("point", style="green")
        table.add_column("tottal_own", style="green")
        table.add_column("owned", style="green")
        for i in data:
            table.add_row(str(i["machine_id"]), str(i["machine_name"]), str(i["host"]),
                          str(i["hint"]), str(i["point"]), str(i["tottal_own"]), str(i["owned"]))
        console.print(table)
        console.print(
            "You can  upload your own weblab using this command below 👇\nExample : upload_lab or ul", style="bold green")

    def upload_machine(self, interface, request):
        """Upload machine to upcoming machines"""
        console.print("Upload Web-lab", style="bold blue")
        machine_name = interface.get_prompt(
            label="Enter your weblab name: ")
        point = interface.get_prompt(
            label="Enter your weblab point: ")
        file_location = interface.get_prompt(
            label="Enter your weblab file location: ")
        file_name = os.path.basename(file_location)
        with console.status("[bold green]Uploading machine please wait...\n") as status:
            data, status_code = request.post(endpoint="/machines/upload/machine", payload={
                                             "machine_name": machine_name, "point": point, "filename": file_name})
            if status_code == 200:
                try:
                    with open(file_location, 'rb') as f:
                        _, status_code = request.upload(
                            endpoint="/machines/upload/zip", file=f)
                    if status_code == 200:
                        console.print(data["data"], style="bold green")
                except FileNotFoundError:
                    console.print(
                        "Error : File not found please recheck you file location", style="bold red")
            else:
                console.print(
                    "Upload failed please contact with our support team", style="bold red")

    def generate_table(self, request):
        """Generate table for upcoming machines"""
        console.print("Upcoming weblab", style="bold blue")
        with console.status("[bold green]please wait...\n") as status:
            data, status = self.get_data(request)
            if status == 200:
                self.show_upcoming_machines(data["data"])
            else:
                pass
