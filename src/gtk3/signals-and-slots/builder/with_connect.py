# -*- coding: utf-8 -*-
"""Signal e Slots."""


import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gio, Gtk


@Gtk.Template(filename='window-without-signal.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    # Acessando widgets do arquivo de interface.
    entry = Gtk.Template.Child(name='entry')
    label = Gtk.Template.Child(name='label')
    button = Gtk.Template.Child(name='button')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.button.connect('clicked', self._on_button_clicked)

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
