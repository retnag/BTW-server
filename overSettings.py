worlds["survival"] = "/home/ganter/.minecraft/saves/BTW-Server"

def playerIcons(poi):
   if poi['id'] == 'Player':
      poi['icon'] = "https://mc-heads.net/avatar/%s/16.png" % poi['EntityId']
      return "Last known location for %s" % poi['EntityId']
def signFilter(poi):
    if poi['id'] == 'Sign':
        return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])


renders["survivalday"] = {
    "world": "survival",
    "title": "Day",
    "markers": [dict(name="Players", filterFunction=playerIcons),
                dict(name="Signs", filterFunction=signFilter)],
    "rendermode": smooth_lighting,
    "dimension": "overworld",
}


outputdir = "/opt/mscs/maps/BTW"
