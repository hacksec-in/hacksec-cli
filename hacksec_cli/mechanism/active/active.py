from rich.console import Console
from rich.table import Table
import json

console = Console()


class Active_machine():
    """active machines class"""

    def get_data(self, request):
        """fetch data for active machines"""
        data = request.get(endpoint="/machines/active")
        return data[0], data[1]

    def show_active_machines(self, data):
        """formate data for active machines and insert the data into table"""
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

    def generate_table(self, request):
        """generate table from active machines data"""
        console.print("Active Machine", style="bold blue")
        with console.status("[bold green]please wait...\n") as status:
            data, status = self.get_data(request)
            if status == 200:
                self.show_active_machines(data["data"])
            else:
                pass
