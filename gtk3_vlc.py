#! /usr/bin/python

import sys
import gi
import threading
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('GdkX11', '3.0')
from gi.repository import GdkX11

import vlc
import perpetualTimer

MRL = ""

class ApplicationWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Python-Vlc Media Player")
        self.player_paused=False
        self.is_player_active = False
        self.player_stream_restart = False
        self.connect("destroy",Gtk.main_quit)
        self.timex = perpetualTimer.perpetualTimer(2, self.play_check)

    def show(self):
        self.show_all()

    def setup_objects_and_events(self):
        self.playback_button = Gtk.Button()
        self.stop_button = Gtk.Button()
        self.close_button = Gtk.Button()

        self.play_image = Gtk.Image.new_from_icon_name(
                "media-playback-start",
                Gtk.IconSize.DIALOG
            )
        self.pause_image = Gtk.Image.new_from_icon_name(
                "media-playback-pause",
                Gtk.IconSize.DIALOG
            )
        self.stop_image = Gtk.Image.new_from_icon_name(
                "media-playback-stop",
                Gtk.IconSize.DIALOG
            )
        self.close_image = Gtk.Image.new_from_icon_name(
                "window-close",
                Gtk.IconSize.DIALOG
            )

        self.playback_button.set_image(self.play_image)
        self.stop_button.set_image(self.stop_image)
        self.close_button.set_image(self.close_image)

        self.playback_button.connect("clicked", self.toggle_player_playback)
        self.stop_button.connect("clicked", self.stop_player)
        self.close_button.connect("clicked", Gtk.main_quit)

        self.draw_area = Gtk.DrawingArea()
        #self.draw_area.set_size_request(1366,768)
        self.set_size_request(1300, 738)

        self.draw_area.connect("realize",self._realized)

        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.grid.attach(self.draw_area, 0, 0, 3, 6)
        self.grid.attach(self.playback_button, 0, 6, 1, 1)
        self.grid.attach(self.stop_button, 1, 6, 1, 1)
        self.grid.attach(self.close_button, 2, 6, 1, 1)

    def stop_player(self, widget=None, data=None):
        self.player.stop()
        self.is_player_active = False
        self.playback_button.set_image(self.play_image)

    def toggle_player_playback(self, widget=None, data=None):
        """
        Handler for Player's Playback Button (Play/Pause).
        """

        if self.is_player_active == False and self.player_paused == False:
            self.player.play()
            self.playback_button.set_image(self.pause_image)
            self.is_player_active = True

        elif self.is_player_active == True and self.player_paused == True:
            self.player.play()
            self.playback_button.set_image(self.pause_image)
            self.player_paused = False

        elif self.is_player_active == True and self.player_paused == False:
            self.player.pause()
            self.playback_button.set_image(self.play_image)
            self.player_paused = True
        else:
            pass


    def _realized(self, widget, data=None):
        self.vlcInstance = vlc.Instance("--no-xlib")
        self.player = self.vlcInstance.media_player_new()
        win_id = widget.get_window().get_xid()
        self.player.set_xwindow(win_id)
        self.player.set_mrl(MRL)
        self.player.play()
        self.playback_button.set_image(self.pause_image)
        self.is_player_active = True
        print "Staring timex"
        self.timex.start()

    def play_check(self):
        state = str(self.player.get_state())
        if state == 'State.Ended' and self.is_player_active == True:
            print 'Stream is playing but ENDED'
            self.stop_player()
            self.player_stream_restart = True
        elif state == 'State.Stopped' and self.player_stream_restart == True:
            print 'Stream is Stopped but forced to Restart'
            self.player_stream_restart = False
            self.toggle_player_playback()
        elif state == 'State.Error' and self.is_player_active == True:
            print 'Stream is playing but ERROR with exit'
            Gtk.main_quit()
            self.player_stream_restart = False

        print "Check "+state

if __name__ == '__main__':
    if not sys.argv[1:]:
       print "Exiting \nMust provide the MRL."
       sys.exit(1)
    if len(sys.argv[1:]) == 1:
        MRL = sys.argv[1]
        window = ApplicationWindow()
        window.setup_objects_and_events()
        window.show()
        Gtk.main()
        window.timex.cancel()
        window.player.stop()
        window.vlcInstance.release()
        print 'Player Shutdown.'


