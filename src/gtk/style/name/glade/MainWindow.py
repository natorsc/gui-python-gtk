# -*- coding: utf-8 -*-
"""Alterando o estilo do widget através da propriedade name.

- 2 labels com a propriedade `name=label-bg-red`.
- 2 sem a propriedade name.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gdk


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


class Handler:

    def __init__(self):
        # Carregando e aplicando o arquivo de css personalizado.
        load_custom_css(file='../../../../data/css/name-label-bg-red.css')


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
