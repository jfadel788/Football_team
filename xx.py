from tabulate import tabulate

def format_table(players):
    headers = ["First Name", "Last Name", "APT", "SET", "AVG", "Position", "National Association"]
    table = [[p.first_name, p.last_name, p.apt, p.set, p.avg, p.position, p.national_association] for p in players]
    return tabulate(table, headers, tablefmt="grid")