import random
def select_team(players, num_defenders, num_midfielders, num_attackers):
    sorted_players = sorted(players, key=lambda p: p.set, reverse=True)
    defenders, midfielders, attackers = [], [], []
    for player in sorted_players:
        if player.position == 'defender' and len(defenders) < num_defenders:
            defenders.append(player)
        elif player.position == 'midfielder' and len(midfielders) < num_midfielders:
            midfielders.append(player)
        elif player.position == 'attacker' and len(attackers) < num_attackers:
            attackers.append(player)
        if len(defenders) + len(midfielders) + len(attackers) == 10:
            break
    return defenders + midfielders + attackers