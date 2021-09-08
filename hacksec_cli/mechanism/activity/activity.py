from rich.console import Console
from rich.table import Table
import json

console = Console()


class activity():
    """activity class"""

    def get_data(self, request):
        """extract data from activity"""
        data = request.get(endpoint="/activity/")
        return data[0], data[1]

    def generate_activity_table(self, data):
        """activity table generator"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("title", style="green")
        table.add_column("content", style="green")
        table.add_column("date", style="green")
        for i in data:
            table.add_row(i["title"],
                          i["content"],  i["date"])
        console.print(table)
        console.print("Activity", style="bold blue")

    def generate_activity(self, request):
        """activity"""
        console.print("Activity", style="bold blue")
        with console.status("[bold green]please wait...\n") as status:
            data, status = self.get_data(request)
            # print(data)
            if status == 200:
                self.generate_activity_table(data["data"])
            else:
                pass
