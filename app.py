from flask import Flask, jsonify, request
from typing import List
from reports import status_report,sort_by_apt,find_highest_apt
from classes import Player
from player_data import input_player_data
from selectTeam import select_team,random_select_players

app = Flask(__name__)
@app.route('/status_report', methods=['POST'])
def api_status_report():
    players_data = request.json['players']
    players = input_player_data(players_data)
    result = status_report(players)
    return jsonify(result)
@app.route('/sort_by_apt', methods=['POST'])
def api_sort_by_apt():
    players_data = request.json['players']
    players = input_player_data(players_data)
    sorted_players = sort_by_apt(players)
    result = [player.to_dict() for player in sorted_players]
    return jsonify(result)
@app.route('/find_highest_apt', methods=['POST'])
def api_find_highest_apt():
    players_data = request.json['players']
    players = input_player_data(players_data)
    highest_apt_player = find_highest_apt(players)
    return jsonify(highest_apt_player.to_dict())
@app.route('/select_team', methods=['POST'])
def api_select_team():
    data = request.json
    players_data = data['players']
    num_defenders = data.get('num_defenders', 0)
    num_midfielders = data.get('num_midfielders', 0)
    num_attackers = data.get('num_attackers', 0)
    players = input_player_data(players_data)
    team = select_team(players, num_defenders, num_midfielders, num_attackers)
    result = [player.to_dict() for player in team]
    return jsonify(result)
@app.route('/random_select_players', methods=['POST'])
def api_random_select_players():
    data = request.json
    players_data = data['players']
    num_players = data.get('num_players', 0)
    players = input_player_data(players_data)
    selected_players = random_select_players(players, num_players)
    result = [player.to_dict() for player in selected_players]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

