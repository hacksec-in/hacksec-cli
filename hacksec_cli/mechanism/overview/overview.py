from rich.console import Console
from rich.table import Table

console = Console()


class Overview():
    """overview class"""

    def get_data(self, request):
        """extract data from overview"""
        data = request.get(endpoint="/home/")
        return data[0], data[1]

    def top_member(self, members):
        """print top memeber and team information"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("Top members", style="green")
        table.add_column("Top team", style="green")
        for i in members:
            table.add_row(i["username"], i["teams"])
        console.print(table)

    def show_stacks(self, rank_info):
        """print rank inforamtion"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("RANK", style="green")
        table.add_column("SCORE", style="green")
        table.add_column("TEAM RANK", style="green")
        table.add_column("TEAM SCORE", style="green")
        table.add_row(str(rank_info["rank"]), str(rank_info["point"]),
                      str(rank_info["teamrank"]), str(rank_info["teampoint"]))
        console.print(table)

    def generate_dashboard(self, request):
        """generate overview table
        data["topplayer"]["members"] extract the memeber list
        data["topplayer"]["teams"] extract the teams list
        {"username": data["topplayer"]["members"] , "team" : data["topplayer"]["members"]} insert the list into dictionary
        table.add_column(data["topplayer"]["members"],data["topplayer"]["members"]) loop over list and extract username and team and insert them into add_column
        """
        console.print("Overview", style="bold blue")
        with console.status("[bold green]please wait...\n") as status:
            data, status = self.get_data(request)
            if status == 200:
                top_userinfo = []
                self.show_stacks(data["rankinfo"])
                for i in data["topplayer"]["members"]:
                    top_userinfo.append({"username": i["username"]})
                for idx, val in enumerate(data["topplayer"]["teams"]):
                    top_userinfo[idx]["teams"] = val["team_name"]
                self.top_member(top_userinfo)
            else:
                pass
