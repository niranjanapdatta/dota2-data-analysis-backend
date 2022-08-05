import requests
import json


account_id = 108755293

# Get current match data
match_data = requests.get(f'https://api.opendota.com/api/players/{account_id}/recentMatches')
match_id = json.loads(match_data.text)[0]['match_id']
match_data_detailed = requests.get(f'https://api.opendota.com/api/matches/{match_id}')
players = json.loads(match_data_detailed.text)['players']

is_player_team_radiant = False
radiant_players = []
dire_players = []

for player in players:
    if player['isRadiant']:
        radiant_players.append(player)
        if player['account_id'] == account_id:
            is_player_team_radiant = True
    else:
        dire_players.append(player['account_id'])

for player in radiant_players:
    query_params = {'hero_id': player['hero_id']}
    _account_id = player['account_id']
    if player['account_id']:
        hero_history = requests.get(f'https://api.opendota.com/api/players/{_account_id}/matches', params=query_params)
        hero_history_json = json.loads(hero_history.text)
        for match in hero_history:
            match_data_detailed = requests.get(f'https://api.opendota.com/api/matches/{match_id}')
            match_data_detailed_json = json.loads(match_data_detailed.text)
            print(json.dumps(match_data_detailed_json, indent=4))
            picks_bans = match_data_detailed_json['picks_bans']
            print(json.dumps(picks_bans, indent=4))
        