from rich.console import Console
from rich.table import Table
import json

console = Console()


class teams_info():
    """Teams class"""

    def findadmin(self, member_list):
        for i in member_list:
            if i["role"] == "admin":
                return i["user"]

    def get_data(self, request):
        """fetch teams data"""
        data = request.get(endpoint="/teams/profile")
        return data[0], data[1]

    def show_teams_info(self, data, isadmin):
        """Formate teams data to fit in tables and return table"""
        if isadmin:
            role = "admin"
        else:
            role = "member"
        table = Table(show_header=True, header_style="bold green")
        table.add_column("team_id", style="green")
        table.add_column("team_name", style="green")
        table.add_column("slogan", style="green")
        table.add_column("is_private", style="green")
        table.add_column("team_admin", style="green")
        table.add_column("role", style="green")
        table.add_row(str(data["team_id"]), str(data["team_name"]), str(data["slogan"]),
                      str(data["is_private"]), str(data["team_admin"]), role)
        console.print(table)

    def show_machine_ownedInfo(self, data):
        """Formate teams machines owned data to fit in tables and return table"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("tottal_machine", style="green")
        table.add_column("first_own", style="green")
        table.add_column("tottal_submition", style="green")
        table.add_row(str(data["tottal_machine"]), str(
            data["firstblood"]), str(data["tottalsubmit"]))
        console.print(table)

    def show_teams_point(self, data):
        """formate and insert point data from teams profile"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("tottal_point", style="green")
        table.add_column("firstown_point", style="green")
        table.add_column("submit_point", style="green")
        table.add_row(str(data["tottal_point"]), str(
            data["firstblood_point"]), str(data["submit_point"]))
        console.print(table)

    def members(self, data):
        """formate and insert point data from teams profile"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("username", style="green")
        table.add_column("joined", style="green")
        table.add_column("role", style="green")
        for i in data:
            table.add_row(str(i["user"]), str(
                i["joined"]), str(i["role"]))
        console.print(table)

    def generate_team(self, request, username):
        """Generate Team profile"""
        console.print("Team profile", style="bold blue")
        with console.status("[bold green]please wait...\n") as status:
            data, status = self.get_data(request)
            # print(data)
            if status == 200:
                isadmin = False
                data["data"]["team_admin"] = self.findadmin(
                    data["data"]["members"])
                if data["data"]["team_admin"] == username:
                    isadmin = True
                self.show_teams_info(data["data"], isadmin)
                console.print("Team info", style="bold blue")
                self.show_machine_ownedInfo(data["data"]["team_info"])
                console.print("Tottal point", style="bold blue")
                self.show_teams_point(data["data"]["point_info"])
                console.print("Member information", style="bold blue")
                self.members(data["data"]["members"])
            else:
                pass
