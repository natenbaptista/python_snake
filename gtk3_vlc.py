#! /usr/bin/python

import sys
import gi
import threading
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('GdkX11', '3.0')
from gi.repository import GdkX11
import ConfigParser
import os.path

import vlc
import perpetualTimer

MRL = ""

class ApplicationWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title=MRL)
        self.player_paused=False
        self.is_player_active = False
        self.is_window_on_top = False
        self.player_stream_restart = False
        self.connect("destroy",Gtk.main_quit)
        self.timex = perpetualTimer.perpetualTimer(2, self.play_check)

    def show(self):
        self.show_all()

    def delete_event(self, data=None):
        print window.get_size()
        return False

    def setup_objects_and_events(self, x, y, width, height, always_on_top):
        self.playback_button = Gtk.Button()
        self.stop_button = Gtk.Button()
        self.on_top_button = Gtk.Button()
        self.close_button = Gtk.Button()

        self.play_image = Gtk.Image.new_from_icon_name(
                "media-playback-start",
                Gtk.IconSize.BUTTON
            )
        self.pause_image = Gtk.Image.new_from_icon_name(
                "media-playback-pause",
                Gtk.IconSize.BUTTON
            )
        self.stop_image = Gtk.Image.new_from_icon_name(
                "media-playback-stop",
                Gtk.IconSize.BUTTON
            )
        self.close_image = Gtk.Image.new_from_icon_name(
                "window-close",
                Gtk.IconSize.BUTTON
            )

        self.playback_button.set_image(self.play_image)
        self.stop_button.set_image(self.stop_image)
        self.on_top_button.set_label('ON TOP')
        self.close_button.set_image(self.close_image)

        self.playback_button.connect("clicked", self.toggle_player_playback)
        self.stop_button.connect("clicked", self.stop_player)
        self.on_top_button.connect("clicked", self.on_top_window)
        self.close_button.connect("clicked", Gtk.main_quit)

        self.draw_area = Gtk.DrawingArea()
        #self.draw_area.set_size_request(1366,768)
        self.set_size_request(400, 200)
        self.resize(width, height)
        self.move(x, y)
        self.is_window_on_top = always_on_top
        self.apply_window_ontop()
        #self.set_keep_above(self.is_window_on_top)
        #self.set_keep_below(not self.is_window_on_top)
        #print self.get_position()

        self.draw_area.connect("realize",self._realized)

        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.grid.attach(self.draw_area, 0, 0, 4, 6)
        self.grid.attach(self.playback_button, 0, 6, 1, 1)
        self.grid.attach(self.stop_button, 1, 6, 1, 1)
        self.grid.attach(self.on_top_button, 2, 6, 1, 1)
        self.grid.attach(self.close_button, 3, 6, 1, 1)

    def stop_player(self, widget=None, data=None):
        self.player.stop()
        self.is_player_active = False
        self.playback_button.set_image(self.play_image)

    def apply_window_ontop(self):
        self.set_keep_above(self.is_window_on_top)
        self.set_keep_below(not self.is_window_on_top)
        self.on_top_button.set_label('ON TOP' if self.is_window_on_top == True else 'ON BOTTOM')

    def on_top_window(self, widget=None, data=None):
        self.is_window_on_top = not self.is_window_on_top
        print self.is_window_on_top
        self.apply_window_ontop()


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
        #return
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

    def get_pos(self):
        print self.get_position()


class Parameter():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 1300
        self.height = 700
        self.always_on_top = False
        self.config_file_name = 'gtk3_vlc.config'

if __name__ == '__main__':
    if not sys.argv[1:]:
       print "Exiting \nMust provide the MRL."
       sys.exit(1)
    if len(sys.argv[1:]) >= 1:
        MRL = sys.argv[1]

        config = ConfigParser.ConfigParser()
        cfg = Parameter()
        if sys.argv[2:]:
            cfg.config_file_name = sys.argv[2]
            print 'Using config {}'.format(cfg.config_file_name)
            if os.path.isfile(cfg.config_file_name):
                config.read(cfg.config_file_name)
                print '{} present'.format(cfg.config_file_name)
                cfg.x = int(config.get('GEOMETRY', 'x', cfg.x))
                cfg.y = int(config.get('GEOMETRY', 'y', cfg.y))
                cfg.width = int(config.get('GEOMETRY', 'width', cfg.width))
                cfg.height = int(config.get('GEOMETRY', 'height', cfg.height))
                cfg.always_on_top = True if config.get('PARAMETER', 'always_on_top', cfg.always_on_top) == 'True' else False
        print ('x={}, y ={}, w={}, h={} aot={}'.format(cfg.x, cfg.y, cfg.width, cfg.height, cfg.always_on_top))

        window = ApplicationWindow()
        window.setup_objects_and_events(cfg.x, cfg.y, cfg.width, cfg.height, cfg.always_on_top)
        window.show()
        Gtk.main()

        loc = window.get_position()
        sze = window.get_size()
        try:
            config.add_section('GEOMETRY')
        except:
            pass
        config.set('GEOMETRY', 'x', loc[0])
        config.set('GEOMETRY', 'y', loc[1])
        config.set('GEOMETRY', 'width', sze[0])
        config.set('GEOMETRY', 'height', sze[1])
        try:
            config.add_section('PARAMETER')
        except:
            pass
        config.set('PARAMETER', 'always_on_top', window.is_window_on_top)

        with open(cfg.config_file_name, 'w') as configfile:
            config.write(configfile)

        window.timex.cancel()
        window.player.stop()
        window.vlcInstance.release()
        print 'Player Shutdown.'


