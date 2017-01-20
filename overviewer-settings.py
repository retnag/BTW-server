worlds['BTW'] = "/home/ganter/.minecraft/saves/BTW-Server"
world = 'BTW'

def playerIcons(poi):
    # displays icons for each player
    if poi['id'] == 'Player':
        poi['icon'] = "https://www.minecraftskinstealer.com/face.php?u=%s" % poi['EntityId']
        return "Last known location for %s: <br><b>X<b/>:%5d<br><b>Y<b/>:%5d<br><b>Z<b/>:%5d" % (poi['EntityId'],poi['x'],poi['y'],poi['z'])

def wpFilter(poi):
    # display special signs: all signs where the first row equals "[Waypoint]" (ignorecase)
    # second row of the sign is the waypoints HEX color code ("#123adf")
    if poi['id'] == "Sign":
        if poi['Text1'].upper() == "[Waypoint]".upper():
            poi['icon'] = "http://www.googlemapsmarkers.com/v1/%s/" % poi['Text2']
            return ("Waypoint", "\n".join(["---------------", poi['Text3'], poi['Text4']]), "<br>Coordinates: <br><b>X<b/>:%5d<br><b>Y<b/>:%5d<br><b>Z<b/>:%5d" % (poi['x'],poi['y'],poi['z']))


def wpPlaceFilter(poi):
    # display special signs: all signs where the
    # first row MUST EQUAL "[Waypoint]" (ignorecase)
    # second  row of the sign is the waypoints type
    # third row of the sign is the waypoints HEX color code ("#123adf")
    # fourth row is user specific comment on the WP
    if poi['id'] == "Sign":
        if poi['Text1'].upper() == "[Waypoint]".upper():
            if poi['Text2'].upper() == "Place".upper():
                poi['icon'] = "http://www.googlemapsmarkers.com/v1/%s/" % poi['Text3']
                return ("Place", "\n".join(["---------------", poi['Text4'], ("Coordinates: <br><b>X<b/>:%5d<br><b>Y<b/>:%5d<br><b>Z<b/>:%5d" % (poi['x'],poi['y'],poi['z']))]))

def wpSpawnerFilter(poi):
    # display special signs: all signs where the first row equals "[Waypoint]" (ignorecase)
    # second row of the sign is the waypoints HEX color code ("#123adf")
    if poi['id'] == "Sign":
        if poi['Text1'].upper() == "[Waypoint]".upper():
            if poi['Text2'].upper() == "Spawner".upper():
                poi['icon'] = "http://www.googlemapsmarkers.com/v1/%s/" % poi['Text3']
                return ("Spawner", "\n".join(["---------------", poi['Text4']]), "<br>Coordinates: <br><b>X<b/>:%5d<br><b>Y<b/>:%5d<br><b>Z<b/>:%5d" % (poi['x'],poi['y'],poi['z']))

def imgurFilter(poi):
    # This looks for signs that have their first line in the 'Image:<id>' format, where <id> is an
    # id from an Imgur.com image.
    if poi['id'] == 'Sign':
        if poi['Text1'].startswith('Image:'):
            poi['icon'] = "painting_icon.png"
            image_html = "<style>.infoWindow img[src='{icon}'] {{display: none}}</style><a href='http://imgur.com/{id}'><img src='http://imgur.com/{id}s.jpg' /></a>".format(icon=poi['icon'], id=poi['Text1'][6:])
            return "\n".join([image_html, poi['Text2'], poi['Text3'], poi['Text4']])

renders['overworld-render'] = {
  'title': 'Nappal',
  'dimension': 'overworld',
  'rendermode': "smooth_lighting",
  'imgformat': 'jpg',
  'markers': [dict(name="Waypoints", filterFunction=wpFilter, checked=True),
              dict(name="Places", filterFunction=wpPlaceFilter, checked=True),
              dict(name="Spawners", filterFunction=wpSpawnerFilter, checked=True),
              dict(name="Images", filterFunction=imgurFilter, checked=True),
              dict(name="Players", filterFunction=playerIcons, checked=True)]
}
'''
renders['overworld-render-at-night'] = {
  'title': 'Ejjel',
  'dimension': 'overworld',
  'rendermode': "smooth_night",
  'imgformat': 'jpg',
  'markers': [dict(name="Waypoints", filterFunction=wpFilter, checked=True),
              #dict(name="Places", filterFunction=wpPlaceFilter, checked=True),
              #dict(name="Spawners", filterFunction=wpSpawnerFilter, checked=True),
              dict(name="Images", filterFunction=imgurFilter, checked=True),
              dict(name="Players", filterFunction=playerIcons, checked=True)]
}
'''
renders['nether-render'] = {
  'title': 'Nether',
  'dimension': 'nether',
  'rendermode': "nether",
  'imgformat': 'jpg',
  'markers': [dict(name="Waypoints", filterFunction=wpFilter, checked=True),
              dict(name="Places", filterFunction=wpPlaceFilter, checked=False),
              dict(name="Spawners", filterFunction=wpSpawnerFilter, checked=True),
              dict(name="Images", filterFunction=imgurFilter, checked=True),
              dict(name="Players", filterFunction=playerIcons, checked=True)]
}

renders['nether-cave'] = {
  'title': 'Nether-cave',
  'dimension': 'nether',
  'rendermode': "cave",
  'imgformat': 'jpg',
  'markers': [dict(name="Waypoints", filterFunction=wpFilter, checked=True),
              dict(name="Places", filterFunction=wpPlaceFilter, checked=False),
              dict(name="Spawners", filterFunction=wpSpawnerFilter, checked=True),
              dict(name="Images", filterFunction=imgurFilter, checked=True),
              dict(name="Players", filterFunction=playerIcons, checked=True)]
}

renders['end-render'] = {
  'title': 'End',
  'dimension': 'end',
  'rendermode': 'normal',
  'imgformat': 'jpg',
  'markers': [dict(name="Waypoints", filterFunction=wpFilter, checked=True),
              #dict(name="Places", filterFunction=wpPlaceFilter, checked=True),
              #dict(name="Spawners", filterFunction=wpSpawnerFilter, checked=True),
              dict(name="Images", filterFunction=imgurFilter, checked=True),
              dict(name="Players", filterFunction=playerIcons, checked=True)]
}

processes = 2
outputdir = '/opt/mscs/maps/BTW'
