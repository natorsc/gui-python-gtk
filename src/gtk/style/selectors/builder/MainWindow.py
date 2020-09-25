# -*- coding: utf-8 -*-
"""Principais seletores css do GTK."""

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

    entry = Gtk.Template.Child(name='entry')
    label = Gtk.Template.Child(name='label')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def _on_button_clicked(self, button):
        """Método é chamado quando o botão da interface é pressionado.

        Caso haja algum texto/caractere no campo de entrada de texto o
        texto será exibido no label da interface, caso não haja
        é exibida outra mensagem.

        :param button: Instância do objeto ``Gtk.Button()``. Basicamente
        informações do botão que foi pressionado.
        """
        if self.entry.get_text():
            self.label.set_label(str=self.entry.get_text())
        else:
            self.label.set_label(str='Digite algo no campo acima!')


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # Carregando e aplicando o arquivo de css personalizado.
        load_custom_css(file='../../../../data/css/custom.css')

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
