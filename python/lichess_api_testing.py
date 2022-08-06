import datetime as dt
import berserk as bk
import json as js

config = js.load(open("config/lichess.json"))

session = bk.TokenSession(config["token"])
client = bk.Client(session=session)

start_date = bk.utils.to_millis(dt.datetime(2022, 1, 1))
end_date = bk.utils.to_millis(dt.datetime(2022, 1, 31))
the_games = client.games.export_by_player('rvalla', rated=True, max=10)
games = list(the_games)

for g in games:
	if g["players"]["white"]["user"]["name"] == "rvalla":
		print(g["players"]["white"]["rating"])
	else:
		print(g["players"]["black"]["rating"])
