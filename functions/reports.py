def status_report(players):
    position_count = {'attacker': 0, 'midfielder': 0, 'defender': 0}
    for player in players:
        position_count[player.position] += 1
    return position_count

def sort_by_apt(players):
    return sorted(players, key=lambda p: p.apt, reverse=True)

def find_highest_apt(players):
    return max(players, key=lambda p: p.apt)

def find_lowest_avg(players):
    return min(players, key=lambda p: p.avg)
