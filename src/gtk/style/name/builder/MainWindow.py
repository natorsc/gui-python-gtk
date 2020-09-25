# -*- coding: utf-8 -*-
"""Alterando o estilo do widget através da propriedade name.

- 2 labels com a propriedade `name=label-bg-red`.
- 2 sem a propriedade name.
"""

import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk, Gdk


def load_custom_css(file):
    css_provider = Gtk.CssProvider.new()
    css_provider.load_from_path(path=file)

    screen = Gdk.Screen()

    style_context = Gtk.StyleContext.new()
    style_context.add_provider_for_screen(
        screen=screen.get_default(),
        provider=css_provider,
        priority=Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
    )


@Gtk.Template(filename='MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # Carregando e aplicando o arquivo de css personalizado.
        load_custom_css(file='../../../../data/css/name-label-bg-red.css')

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)


if __name__ == '__main__':
    app = Application()
    app.run(sys.argv)
