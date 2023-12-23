"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""

import dbus
from dbus.mainloop.glib import DBusGMainLoop

import pympris

dbus_loop = DBusGMainLoop()
bus = dbus.SessionBus(mainloop=dbus_loop)
PLAYLIST_NAME = 'Helloworld'
AUDIO_PLAYER = 'Rhythmbox'

class MprisClient():
    def __init__(self) -> None:
        # get unique ids for all available players
        players_ids = list(pympris.available_players())
        self.mp = pympris.MediaPlayer(players_ids[0], bus)

        # Get Rhythmbox
        for player_id in players_ids:
            player = pympris.MediaPlayer(players_ids[0], bus)
            print(self.mp.root.Identity)
            if player.root.Identity == AUDIO_PLAYER:
                self.mp = player
    
    def set_playlist(self) -> None:
        playlists = self.mp.playlists.GetPlaylists(0, 10, 'Alphabetical', False)
        for playlist in playlists:
            if PLAYLIST_NAME in playlist:
                self.mp.playlists.ActivatePlaylist(playlist[0])
                self.pause()
    
    def play(self) -> None:
        self.mp.player.Play()
    
    def pause(self) -> None:
        self.mp.player.Pause()

    
    @property
    def state(self) -> str:
        return self.mp.player.PlaybackStatus
    
    @property
    def metadata(self) -> str:
        title:str = self.mp.player.Metadata['xesam:title']
        state:str = self.state
        output:str = f'{title} '
        return output
    
    @property
    def meta_length(self) -> int:
        return len(self.metadata)