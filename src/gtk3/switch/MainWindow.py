# -*- coding: utf-8 -*-
"""Gtk.Switch()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.Switch')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        grid = Gtk.Grid.new()
        grid.set_border_width(border_width=12)
        self.add(widget=grid)

        switch = Gtk.Switch.new()
        switch.connect('notify::active', self.on_switch_button_clicked)
        grid.add(widget=switch)

        self.show_all()

    def on_switch_button_clicked(self, widget, g_param):
        if widget.get_active():
            print('Botão marcado')
        else:
            print('Botão desmarcado')


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)


if __name__ == '__main__':
    import sys

    app = Application()
    app.run(sys.argv)
