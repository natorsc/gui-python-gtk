# -*- coding: utf-8 -*-
"""Utilizando name para aplicar um estilo personalizado (CSS)."""

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


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Utilizando name para aplicar um estilo personalizado (CSS)')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        for i in range(1, 3):
            label = Gtk.Label.new(str=f'Label {i} COM propriedade name')
            label.set_name(name='label-bg-red')
            vbox.pack_start(child=label, expand=True, fill=True, padding=0)

        for i in range(1, 3):
            label = Gtk.Label.new(str=f'Label {i} SEM propriedade name')
            vbox.pack_start(child=label, expand=True, fill=True, padding=0)

        self.show_all()


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # Carregando e aplicando o arquivo de css personalizado.
        load_custom_css(file='../../data/css/name-label-bg-red.css')

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
