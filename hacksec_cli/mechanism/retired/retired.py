from rich.console import Console
from rich.table import Table
import json

console = Console()


class retired_machine():
    """retired machines class"""

    def get_data(self, request):
        """fetch retired machines data"""
        data = request.get(endpoint="/machines/retired")
        return data[0], data[1]

    def show_retired_machines(self, data):
        """Formate retired machines data to fit in tables and return table"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("machine_id", style="green")
        table.add_column("machine_name", style="green")
        table.add_column("host", style="green")
        table.add_column("hint", style="green")
        table.add_column("point", style="green")
        table.add_column("tottal_own", style="green")
        for i in data:
            table.add_row(str(i["machine_id"]), str(i["machine_name"]), str(i["host"]),
                          str(i["hint"]), str(i["point"]), str(i["tottal_own"]))
        console.print(table)

    def generate_table(self, request):
        """Generate table for retired machines"""
        console.print("Retired Web-lab", style="bold blue")
        with console.status("[bold green]please wait...\n") as status:
            data, status = self.get_data(request)
            if status == 200:
                self.show_retired_machines(data["data"])
            else:
                pass
