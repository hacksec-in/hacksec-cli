from rich.console import Console
from rich.table import Table
import json

console = Console()


class announcement():
    """overview class"""

    def get_data(self, request):
        """extract data from overview"""
        data = request.get(endpoint="/announcement/")
        return data[0], data[1]

    def generate_announcement_table(self, data):
        """print top memeber and team information"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("title", style="green")
        table.add_column("content", style="green")
        table.add_column("author", style="green")
        table.add_column("date", style="green")
        for i in data:
            table.add_row(i["title"],
                          i["content"], i["author"], i["date"])
        console.print(table)

    def generate_dashboard(self, request):
        """announcement"""
        console.print("Announcement", style="bold blue")
        with console.status("[bold green]please wait...\n") as status:
            data, status = self.get_data(request)
            # print(data)
            if status == 200:
                self.generate_announcement_table(data["data"])
            else:
                pass
