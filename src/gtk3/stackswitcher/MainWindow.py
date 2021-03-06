# -*- coding: utf-8 -*-
"""Gtk.StackSwitcher()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Stack Layout com StackSwitcher')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        header_bar = Gtk.HeaderBar.new()
        header_bar.set_title(title='Stack Layout')
        header_bar.set_subtitle(subtitle='com StackSwitcher')
        header_bar.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=header_bar)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        stack = Gtk.Stack.new()
        # Definindo o efeito de transição.
        stack.set_transition_type(
            transition=Gtk.StackTransitionType.SLIDE_LEFT_RIGHT
        )
        # Definindo o tempo da transição (1000 = 1 segundo).
        stack.set_transition_duration(duration=1000)

        page1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        # Adicionando o Box Layout 1 no Stack Layout.
        stack.add_titled(child=page1, name='pagina1', title='Página 1')
        vbox.pack_end(child=stack, expand=True, fill=True, padding=0)

        # Utilizando um laço de repetição para criar alguns botões.
        for n in range(5):
            botao = Gtk.Button.new_with_label(label=f'Botão {n}')
            page1.add(botao)

        page2 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        stack.add_titled(child=page2, name='pagina2', title='Página 2')

        for n in range(5):
            label = Gtk.Label.new(str=f'Linha {n}')
            page2.add(widget=label)

        stack_switcher = Gtk.StackSwitcher.new()
        stack_switcher.set_stack(stack=stack)
        header_bar.set_custom_title(title_widget=stack_switcher)

        self.show_all()


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
