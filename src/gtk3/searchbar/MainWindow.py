# -*- coding: utf-8 -*-
"""Gtk.SearchBar()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk, Gio


class MainWindow(Gtk.ApplicationWindow):
    _current_button_state = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.SearchBar')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')
        # Conectando o evento de tecla pressionada à janela principal.
        self.connect('key-press-event', self.key_press_event)

        header_bar = Gtk.HeaderBar.new()
        header_bar.set_title(title='Gtk.SearchBar')
        header_bar.set_subtitle(subtitle='Gtk.SearchBar')
        header_bar.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=header_bar)

        btn_icon_search = Gtk.Image.new_from_icon_name(
            icon_name='system-search-symbolic',
            size=Gtk.IconSize.BUTTON,
        )

        self.btn_search = Gtk.ToggleButton.new()
        self.btn_search.set_image(image=btn_icon_search)
        self.btn_search.connect('clicked', self.on_btn_search_clicled)
        header_bar.pack_start(child=self.btn_search)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.add(widget=vbox)

        search_entry = Gtk.SearchEntry.new()

        self.search_bar = Gtk.SearchBar.new()
        self.search_bar.connect_entry(entry=search_entry)
        self.search_bar.add(widget=search_entry)
        vbox.pack_start(child=self.search_bar, expand=False, fill=True, padding=0)

        label = Gtk.Label.new(
            str='Pressione <b><tt>Ctrl+f</tt></b> para abrir a pesquisa ou '
                'clique no ícone de pesquisa na barra de título.',
        )
        label.set_use_markup(setting=True)
        vbox.pack_start(child=label, expand=True, fill=True, padding=0)

        self.show_all()

    def _show_hidden_search_bar(self):
        if self.search_bar.get_search_mode():
            self.search_bar.set_search_mode(search_mode=False)
        else:
            self.search_bar.set_search_mode(search_mode=True)

    def _change_button_state(self):
        if self._current_button_state:
            self.btn_search.set_state_flags(flags=Gtk.StateFlags.NORMAL, clear=True)
            self._current_button_state = False
        else:
            self.btn_search.set_state_flags(flags=Gtk.StateFlags.ACTIVE, clear=True)
            self._current_button_state = True

    def on_btn_search_clicled(self, widget):
        self._current_button_state = widget.get_active()
        self._show_hidden_search_bar()

    def key_press_event(self, widget, event):
        shortcut = Gtk.accelerator_get_label(event.keyval, event.state)
        if shortcut in ('Ctrl+F', 'Ctrl+Mod2+F'):
            self._show_hidden_search_bar()
            self._change_button_state()
        if shortcut == 'Mod2+Esc' and self.search_bar.get_search_mode():
            self._show_hidden_search_bar()
            self._change_button_state()
        return True


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
