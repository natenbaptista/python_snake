#! /usr/bin/env python
import sys
import gi
import threading
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, Pango
import ConfigParser
import os
import requests
import collections
import xmltodict, json

import perpetualTimer
class CurrencyManager():
    def __init__(self):
        self.currencies_str_list = ['INR', 'PHP', 'SGD', 'HKD', 'USD', 'JPY']
        self.xCurrencies = collections.OrderedDict()
        for cur in self.currencies_str_list:
            self.xCurrencies[cur] = [1.0, 1.0]
        print self.xCurrencies

        self.url = 'http://spreadsheets.google.com/feeds/list/0Av2v4lMxiJ1AdE9laEZJdzhmMzdmcW90VWNfUTYtM2c/2/public/basic'
        self.rates = ConfigParser.ConfigParser()
        self.rates_file = 'rates.txt'
        if os.path.isfile(self.rates_file):
            self.rates.read(self.rates_file)
            print '{} present'.format(self.rates_file)
            for currency in self.xCurrencies:
                data = self.rates.get('CURRENCY', currency, '1,1')
                data = data.split(',')
                self.xCurrencies[currency][0] = float(data[0])
                self.xCurrencies[currency][1] = float(data[1])
        else:
            self.update_rates()
        print self.xCurrencies

    def update_rates(self):
        r = requests.get(self.url)
        o = xmltodict.parse(r.text)
        for entry in o['feed']['entry']:
            currency = ''
            xRate = 1.0
            for key, value in entry.iteritems():
                try:
                    if key == 'title':
                        currency = value['#text']
                    if key == 'content':
                        xRate = float(value['#text'][8:])
                except:
                    pass
            #print '{}={}'.format(currency, xRate)
            if currency in self.xCurrencies:
                self.xCurrencies[currency][0] = xRate
                self.xCurrencies[currency][1] = float('{0:.6f}'.format(1/xRate))
        try:
            self.rates.add_section('CURRENCY')
        except:
            pass
        for currency in self.xCurrencies:
            data = '{},{}'.format(self.xCurrencies[currency][0], self.xCurrencies[currency][1])
            self.rates.set('CURRENCY', currency, data)

        with open(self.rates_file, 'w') as rates_file:
            self.rates.write(rates_file)

class CurrencyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="XCE")
        config = ConfigParser.ConfigParser()
        cfg = Parameter()
        cfg.config_file_name = 'currencyApp.config'
        if os.path.isfile(cfg.config_file_name):
            config.read(cfg.config_file_name)
            print '{} present'.format(cfg.config_file_name)
            try:
                cfg.x = int(config.get('GEOMETRY', 'x', cfg.x))
                cfg.y = int(config.get('GEOMETRY', 'y', cfg.y))
                #cfg.power_off = True if config.get('PARAMETER', 'power_off_on_close', cfg.power_off) == 'True' else False
            except:
                pass
        print ('x={}, y ={} '.format(cfg.x, cfg.y))
        self.set_size_request(250, 300)
        self.set_keep_above(True)
        self.move(cfg.x, cfg.y)
        self.connect("delete_event",self.save_n_exit)
        self.connect("destroy",Gtk.main_quit)
        #self.timex = perpetualTimer.perpetualTimer(2, self.status_check)
        self.config = config
        self.cfg = cfg
        self.currency_manager = CurrencyManager()

    def setup_objects(self):
        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)

        cur_list = self.currency_manager.currencies_str_list
        rate_dict = self.currency_manager.xCurrencies
        self.cur_objs = []
        grid_y = 0
        for currency_str in cur_list:
            new_cur_obj = CurrencyObj(currency_str, rate_dict[currency_str][0], rate_dict[currency_str][1], self.update)
            self.grid.attach(new_cur_obj, 0, grid_y, 6, 1)
            self.cur_objs.append(new_cur_obj)
            grid_y = grid_y+1

        self.cur_hide = Gtk.Button()
        self.grid.attach(self.cur_hide, 6, 0, 1, 6)
        self.cur_hide.connect("clicked", self.c_hide)

    def c_hide(self, widget=None, data=None):
        self.hide()

    def show(self):
        self.show_all()

    def save_n_exit(self, widget=None, data=None):
        #self.timex.cancel()
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
            config.add_section('CURRENCY')
        except:
            pass
        #config.set('PARAMETER', 'power_off_on_close', cfg.power_off)
        with open(cfg.config_file_name, 'w') as configfile:
            config.write(configfile)
        Gtk.main_quit()

    def update(self, id, usd):
        #print 'updating all except {} with {}'.format(id, usd)
        for cur_obj in self.cur_objs:
            if cur_obj.id == id:
                continue
            cur_obj.update_currency_entry(usd)


class CurrencyObj(Gtk.Grid):
    def __init__(self, text, usd_to_cur, cur_to_usd, update_func):
        Gtk.Grid.__init__(self)
        self.set_column_homogeneous(True)
        self.set_row_homogeneous(True)
        self.id = text
        self.usd_to_cur = usd_to_cur
        self.cur_to_usd = cur_to_usd
        self.image =  Gtk.Image.new_from_file('images/'+text.lower()+'.png')
        self.attach(self.image, 0, 0, 1, 1)
        self.label = Gtk.Label()
        self.label.set_markup("<span font_desc='20' color= 'black'><b>"+text+"</b></span>")
        self.attach(self.label, 1, 0, 1, 1)
        self.entry = Gtk.Entry()
        self.entry.set_alignment(xalign=0.5)
        self.entry.modify_font(Pango.FontDescription('Dejavu Sans Mono 20'))
        self.entry.set_text("0")
        self.entry.connect('changed', self.on_changed, update_func)
        self.attach(self.entry, 2, 0, 3, 1)

    def on_changed(self, argh, update_func):
        if self.entry.is_focus() == False:
            return
        text = self.entry.get_text().strip()
        self.entry.set_text(''.join([i for i in text if i in '0123456789,.']))
        num = self.entry.get_text().replace(',','')
        usd = 0
        if len(num) != 0:
            usd = float(num)*self.cur_to_usd
        update_func(self.id, usd)

    def update_currency_entry(self, usd):
        #float('{0:.6f}'.format(1/xRate))
        self.entry.set_text('{:20,.2f}'.format(usd*self.usd_to_cur).strip())

class Parameter():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 200
        self.height = 200

class TrayIcon(Gtk.StatusIcon):
    def __init__(self, app):
        Gtk.StatusIcon.__init__(self)
        self.set_from_icon_name('help-about')
        self.set_has_tooltip(True)
        self.set_visible(True)
        self.connect("popup_menu", self.right_click)
        self.connect("activate", self.left_click)
        self.app = app

    def left_click(self, widget):
        print 'left_click'
        self.app.show()

    def right_click(self, widget, button, time):
        print 'right_click'
        self.app.hide()
        #menu = Gtk.Menu()

        #menu_item1 = Gtk.MenuItem("First Entry")
        #menu.append(menu_item1)

        #menu_item2 = Gtk.MenuItem("Quit")
        #menu.append(menu_item2)
        #menu_item2.connect("activate", Gtk.main_quit)

        #menu.show_all()
        #menu.popup(None, None, None, self, 3, time)


if __name__ == "__main__":
    app = CurrencyWindow()
    app.setup_objects()
    app.show()
    tray = TrayIcon(app)
    Gtk.main()