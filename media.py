from keyboard import *
from secret import *

KEYWORDS = {'stop': "stop_media",
            'arrête': "stop_media",
            'play': "play/pause_media",
            'pause': "play/pause_media",
            'pose': "play/pause_media",
            'lance': "play/pause_media",
            'augmente': "volume_up",
            'haut': "volume_up",
            'plus': "volume_up",
            'rédui': "volume_down",
            'baisse': "volume_down",
            'moins': "volume_down",
            'suivant': "next_track",
            'passe': "next_track",
            'précédent': "previous_track",
            'revien': "previous_track",
            'mute': "volume_mute",
            'coupe': "volume_mute",
            'met': "volume_mute"
            }


def controlMedia(secret, action):

    if secret != getSecret("Media"):
        return

    print(action)
    for key, value in KEYWORDS.items():
        if key in action:
            print(key, value)
            press(value)
            break
