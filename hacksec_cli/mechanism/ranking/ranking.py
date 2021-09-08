from rich.console import Console
from rich.table import Table
from interface.menu.menu import main_menu

console = Console()


class ranking():
    """activity class"""

    def get_data(self, request, url):
        """extract data from activity"""
        data = request.get(endpoint=url)
        return data[0], data[1]

    def generate_ranking_table(self, data, isUser):
        """activity table generator"""
        table = Table(show_header=True, header_style="bold green")
        if isUser:
            table.add_column("account_id", style="green")
            table.add_column("username", style="green")
            table.add_column("team", style="green")
            table.add_column("tottal_point", style="green")
            for i in data:
                table.add_row(str(i["account_id"]),
                              i["username"], i["team"],  str(i["tottal_point"]))
        else:
            table.add_column("team_id", style="green")
            table.add_column("team_name", style="green")
            table.add_column("point", style="green")
            table.add_column("tottal member", style="green")
            for i in data:
                table.add_row(str(i["team_id"]),
                              i["team_name"],  str(i["point"]), str(len(i["members"])))
        console.print(table)

    def which_ranking(self, request):
        """which ranking team or user"""
        options = ["user ranking", "team ranking"]
        anwser = main_menu("Ranking", options,
                           "Which ranking you want to see")
        if anwser == options[0]:
            self.generate_rank(request, True)
        else:
            self.generate_rank(request, False)

    def generate_rank(self, request, isUser=True):
        """activity"""
        if isUser:
            console.print("User Ranking", style="bold blue")
        else:
            console.print("Team Ranking", style="bold blue")
        with console.status("[bold green]please wait...\n") as status:
            if isUser:
                data, status = self.get_data(request, "/members/100")
            else:
                data, status = self.get_data(request, "/teams/top/100")
            # print(data)
            if status == 200:
                self.generate_ranking_table(data["data"], isUser)
            else:
                pass
