#! /usr/bin/python

import sys
import gi
import threading
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk
gi.require_version('GdkX11', '3.0')
from gi.repository import GdkX11
import ConfigParser
import os.path
import os
import subprocess
import re
import pyautogui

import perpetualTimer

class MonitorWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Monitor")
        config = ConfigParser.ConfigParser()
        cfg = Parameter()
        cfg.config_file_name = 'monitor.config'
        if os.path.isfile(cfg.config_file_name):
            config.read(cfg.config_file_name)
            print '{} present'.format(cfg.config_file_name)
            try:
                cfg.x = int(config.get('GEOMETRY', 'x', cfg.x))
                cfg.y = int(config.get('GEOMETRY', 'y', cfg.y))
                cfg.power_off = True if config.get('PARAMETER', 'power_off_on_close', cfg.power_off) == 'True' else False
            except:
                pass
            cfg.always_on_top = True
            #cfg.always_on_top = True if config.get('PARAMETER', 'always_on_top', cfg.always_on_top) == 'True' else False
        print ('x={}, y ={} aot={}'.format(cfg.x, cfg.y, cfg.always_on_top))
        self.set_size_request(250, 300)
        self.move(cfg.x, cfg.y)
        self.set_keep_above(cfg.always_on_top)
        self.connect("delete_event",self.save_n_exit)
        self.connect("destroy",Gtk.main_quit)
        self.timex = perpetualTimer.perpetualTimer(2, self.status_check)
        self.config = config
        self.cfg = cfg
        self.jiggle_toggle = True
        self.jiggle_timeout = 100

    def setup_objects(self):
        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)

        self.label = Gtk.Label()
        self.label.set_justify(Gtk.Justification.LEFT)
        markup = 'PC is set to POWER OFF on CLOSE'
        self.label.set_markup(markup if self.cfg.power_off == True else "Starting")
        self.grid.attach(self.label, 0, 2, 2, 5)

        self.close_button = Gtk.Button()
        self.close_image = Gtk.Image.new_from_icon_name(
                "window-close", Gtk.IconSize.DIALOG)
        self.close_button.set_image(self.close_image)
        self.grid.attach(self.close_button, 0, 0, 1, 2)
        self.close_button.connect("clicked", self.enable_close_confm_button)

        self.close_confm_button = Gtk.Button()
        self.close_confm_image = Gtk.Image.new_from_icon_name(
                "stop" if self.cfg.power_off == True else "window-close", Gtk.IconSize.DIALOG)
        self.close_confm_button.set_image(self.close_confm_image)
        self.grid.attach(self.close_confm_button, 1, 0, 1, 2)
        self.close_confm_button.connect("clicked", self.save_n_exit)
        self.timex.start()

    def show(self):
        self.show_all()
        self.close_confm_button.set_sensitive(False)

    def enable_close_confm_button(self, widget=None, data=None):
        self.close_confm_button.set_sensitive(True)

    def save_n_exit(self, widget=None, data=None):
        self.timex.cancel()
        loc = self.get_position()
        config = self.config
        cfg = self.cfg
        try:
            config.add_section('GEOMETRY')
        except:
            pass
        config.set('GEOMETRY', 'x', loc[0])
        config.set('GEOMETRY', 'y', loc[1])
        try:
            config.add_section('PARAMETER')
        except:
            pass
        config.set('PARAMETER', 'power_off_on_close', cfg.power_off)
        with open(cfg.config_file_name, 'w') as configfile:
            config.write(configfile)
        Gtk.main_quit()
        if cfg.power_off == True:
            cmd = "sudo shutdown -h now"
            os.system(cmd)

    def jiggle_mouse(self):
        self.jiggle_timeout = self.jiggle_timeout+1
        if self.jiggle_timeout > 100:
            self.jiggle_timeout = 0
            pyautogui.moveTo(100, 100) if self.jiggle_toggle == True else pyautogui.moveTo(50,50)
            self.jiggle_toggle = not self.jiggle_toggle

    def status_check(self):
        h = subprocess.check_output(["sensors"])
        sensors = 0
        sensor = []
        for line in h.split("\n"):
            if "Core" in line:
                msplit = re.split('\:|\+|\(', line)
                s = Sensor(msplit[0], msplit[2])
                sensor.append(s)
                #print sensor[sensors].device+' '+sensor[sensors].output
                sensors = sensors+1
            if "fan2" in line:
                msplit = re.split('\:|\(', line)
                s = Sensor(msplit[0], msplit[1])
                sensor.append(s)
                #print sensor[sensors].device+' '+sensor[sensors].output
                sensors = sensors+1
        markup = ''
        for this_sensor in sensor:
            markup = markup+this_sensor.device+'   '+this_sensor.output+'\n'

        h = subprocess.check_output(["ps", "aux"])
        nodes = 0
        actor = []
        for line in h.split("\n"):
            if "atp-actors" in line and not "daemon" in line:
                #print line
                msplit = line.split()
                node_name = msplit[14].split('/')
                n = Actor(node_name[3], msplit[2], msplit[3])
                actor.append(n)
                print node_name[3]+' Cpu:'+msplit[2]+'% Mem:'+msplit[3]+'%'
        for this_actor in actor:
            markup = markup+'  '+this_actor.role+' '+this_actor.cpu+' '+this_actor.mem+'  \n'

        GLib.idle_add(self.label.set_markup, markup)
        self.jiggle_mouse()
        #print markup

class Actor():
    def __init__(self, role, cpu, mem):
        self.role = "<span font_desc='14' color='black'><b>"+role+"</b></span>"
        self.cpu = "<span font_desc='20' color= 'black'><b>Cpu:"+cpu+"%</b></span>"
        self.mem = "<span font_desc='16' color= 'black'><b>Mem:"+mem+"%</b></span>"

class Sensor():
    def __init__(self, dev, out):
        #color = 'red' if int(msplit[0]) >= 60 else 'black'
        self.device = "<span font_desc='14' color='black'><b>"+dev.strip()+"</b></span>"
        self.output = "<span font_desc='20' color= 'black'><b>"+out.strip()+"</b></span>"

class Parameter():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 200
        self.height = 200
        self.always_on_top = False
        self.power_off = False
        self.config_file_name = 'monitor.config'

if __name__ == '__main__':
    monitor = MonitorWindow()
    monitor.setup_objects()
    monitor.show()

    Gtk.main()


