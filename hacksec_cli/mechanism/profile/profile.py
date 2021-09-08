from rich.console import Console
from rich.table import Table
import json

console = Console()


class profile_info():
    """profile class"""

    def get_data(self, request):
        """fetch profile data"""
        data = request.get(endpoint="/accounts/profile")
        return data[0], data[1]

    def show_profile_info(self, data):
        """Formate profile data to fit in tables and return table"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("account_id", style="green")
        table.add_column("username", style="green")
        table.add_column("rank", style="green")
        table.add_column("email", style="green")
        table.add_column("team", style="green")
        table.add_column("role", style="green")
        table.add_row(str(data["account_id"]), str(data["username"]), str(data["rank"]),
                      str(data["email"]), str(data["team"]), data["role"])
        console.print(table)

    def show_machine_ownedInfo(self, data):
        """Formate profile machines owned data to fit in tables and return table"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("tottal_own", style="green")
        table.add_column("first_own", style="green")
        table.add_column("tottal_submition", style="green")
        table.add_row(str(data["tottal_own"]), str(
            data["first_blood"]), str(data["tottal_submition"]))
        console.print(table)

    def show_user_point(self, data):
        """formate and insert point data from user profile"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("tottal_point", style="green")
        table.add_column("firstown_point", style="green")
        table.add_column("submition_point", style="green")
        table.add_row(str(data["tottal_point"]), str(
            data["firstblood_point"]), str(data["submition_point"]))
        console.print(table)

    def completed_machines(self, data):
        """formate and insert point data from user profile"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("machine_id", style="green")
        table.add_column("machine_name", style="green")
        table.add_column("point", style="green")
        for i in data:
            table.add_row(str(i["machine_id"]), str(
                i["machine_name"]), str(i["point"]))
        console.print(table)

    def generate_profile(self, request):
        """Generate profile"""
        console.print("Profile", style="bold blue")
        with console.status("[bold green]please wait...\n") as status:
            data, status = self.get_data(request)
            # print(data["data"])
            if status == 200:
                self.show_profile_info(data["data"])
                console.print("Account info", style="bold blue")
                self.show_machine_ownedInfo(data["data"]["machine_count"])
                console.print("Tottal point", style="bold blue")
                self.show_user_point(data["data"]["machine_point"])
                console.print("Machine info", style="bold blue")
                self.completed_machines(data["data"]["machines"])
            else:
                pass
