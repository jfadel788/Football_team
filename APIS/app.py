from flask import Flask, jsonify, request
from typing import List
import sys
sys.path.append('/Users/User/Desktop/football/')

from functions.reports import status_report,sort_by_apt,find_highest_apt,find_lowest_avg
from classes.classes import Player
from functions.player_data import input_player_data
from functions.selectTeam import select_team,random_select_players

app = Flask(__name__)
@app.route("/input_data", methods=["POST"])
def api_input_data():
   
        data = request.get_json()  
        players_data = data.get("players", [])  
        players = input_player_data(players_data)  
        players_dict = [player.to_dict() for player in players]
        return jsonify(players_dict)
  

    
##Create API for status Report
@app.route('/status_report', methods=['POST'])
def api_status_report():
    players_data = request.json['players']
    players = input_player_data(players_data)
    result = status_report(players)
    return jsonify(result)
@app.route('/find_lowest_avg',methods=['POST'])
def api_lowest_avg():
    data=request.json["players"]
    players=input_player_data(data)
    result=find_lowest_avg(players)
    return jsonify(result.to_dict())

##Create API for sort by APT
@app.route('/sort_by_apt', methods=['POST'])
def api_sort_by_apt():
    players_data = request.json['players']
    players = input_player_data(players_data)
    sorted_players = sort_by_apt(players)
    result = [player.to_dict() for player in sorted_players]
    return jsonify(result)
##API for find highest apt
@app.route('/find_highest_apt', methods=['POST'])
def api_find_highest_apt():
    players_data = request.json['players']
    players = input_player_data(players_data)
    highest_apt_player = find_highest_apt(players)
    return jsonify(highest_apt_player.to_dict())
##API for select team
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
##API for random select players
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

