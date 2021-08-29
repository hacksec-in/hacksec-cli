from rich.console import Console
from rich.table import Table
import random

console = Console()


class Report():
    """Report class"""

    def get_data(self, request):
        """extract data from report"""
        data = request.get(endpoint="/writeups/latest")
        return data[0], data[1]

    def generate_report_table(self, data):
        """Generate report table"""
        table = Table(show_header=True, header_style="bold green")
        table.add_column("machine_name", style="green")
        table.add_column("location", style="green")
        table.add_column("author_name", style="green")
        table.add_column("point", style="green")
        table.add_column("youtube", style="green")
        table.add_column("articals", style="green")
        table.add_column("pdf", style="green")
        for i in data:
            youtube_len = len(i["writeup"]["youtube"])
            youtube_uri = ""
            artical_len = len(i["writeup"]["articals"])
            artical_uri = ""
            pdf_len = len(i["writeup"]["pdf"])
            pdf_uri = ""
            if youtube_len != 0:
                random_youtube_index = random.randrange(
                    len(i["writeup"]["youtube"]))
                youtube_uri = str(i["writeup"]["youtube"]
                                  [random_youtube_index])
            if artical_len != 0:
                random_artical_index = random.randrange(
                    len(i["writeup"]["articals"]))
                artical_uri = str(i["writeup"]["articals"]
                                  [random_artical_index])
            if pdf_len != 0:
                random_pdf_index = random.randrange(
                    len(i["writeup"]["pdf"]))
                pdf_uri = str(i["writeup"]["pdf"][random_pdf_index])
            table.add_row(str(i["machine_name"]), str(i["location"]), str(i["author_name"]),
                          str(i["point"]), youtube_uri, artical_uri, pdf_uri)
        console.print(table)
        console.print(
            "You can add your own report here using this command below 👇 \nexample : send_report machine_name report_url", style="bold green")

    def send_report(self, command, request):
        """Send report"""
        data = command.split()
        try:
            payload = {
                "url": data[2],
                "title": data[1]
            }
        except IndexError:
            console.print("Error: invalid command", style="bold red")
        with console.status("[bold green]please wait...\n") as status:
            data, status_code = request.post(
                endpoint="/writeups/add", payload=payload)
            if status_code == 200:
                console.print(
                    "Your report has been send successfully and it's under review 🔥", style="bold green")
            else:
                console.print("Error: {}".format(data), style="bold red")

    def generate_report(self, request):
        """Generate report"""
        with console.status("[bold green]please wait...\n") as status:
            data, status_code = self.get_data(request)
            if status_code == 200:
                # print(data)
                self.generate_report_table(data["data"])
            else:
                console.print("Error: {}".format(data), style="bold red")
