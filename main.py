from ossapi import *
# setting up api stuff
limit = 30
count = 0
in_bm = input()
in_bm_author = api.beatmap(in_bm).user_id
for i in api.user_beatmaps(user_id=in_bm_author, type_="favourite", limit=30):
    print("https://osu.ppy.sh/beatmapsets/" + str(i.id))
