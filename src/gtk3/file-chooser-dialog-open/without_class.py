# -*- coding: utf-8 -*-
"""Gtk.FileChooserDialog() open."""

from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):
    # Definindo o diretório padrão.
    home = Path.home()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.FileChooserDialog open')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(vbox)

        button_save_file = Gtk.Button.new_with_label('Selecionar arquivo')
        button_save_file.connect('clicked', self.open_dialog)
        vbox.add(button_save_file)

        self.check_button = Gtk.CheckButton.new_with_label(label='\tSelecionar vários arquivos?')
        vbox.add(self.check_button)

        self.show_all()

    def open_dialog(self, widget):
        select_multiple = self.check_button.get_active()
        dialog = Gtk.FileChooserDialog()
        dialog.set_transient_for(parent=self)
        dialog.set_title(title='Selecionar Arquivo')
        dialog.set_modal(modal=True)
        # Tipo de ação que o dialogo irá executar.
        dialog.set_action(action=Gtk.FileChooserAction.OPEN)
        # Defininido se a seleção será multipla ou não
        dialog.set_select_multiple(select_multiple=select_multiple)
        # Pasta onde o diálogo será aberto.
        dialog.set_current_folder(filename=str(self.home))

        # Botões que serão exibidos.
        dialog.add_buttons(
            '_Cancelar', Gtk.ResponseType.CANCEL,
            '_OK', Gtk.ResponseType.OK
        )

        # Adicionando class action nos botões.
        btn_cancel = dialog.get_widget_for_response(
            response_id=Gtk.ResponseType.CANCEL,
        )
        btn_cancel.get_style_context().add_class(class_name='destructive-action')

        btn_save = dialog.get_widget_for_response(
            response_id=Gtk.ResponseType.OK,
        )
        btn_save.get_style_context().add_class(class_name='suggested-action')

        # Criando e adicionando filtros.
        txt_filter = Gtk.FileFilter()
        txt_filter.set_name(name='txt')
        txt_filter.add_pattern(pattern='.txt')
        txt_filter.add_mime_type(mime_type='text/plain')
        dialog.add_filter(filter=txt_filter)

        py_filter = Gtk.FileFilter()
        py_filter.set_name(name='python')
        py_filter.add_pattern(pattern='.py')
        py_filter.add_mime_type(mime_type='text/x-python')
        dialog.add_filter(filter=py_filter)

        all_filter = Gtk.FileFilter()
        all_filter.set_name(name='todos')
        all_filter.add_pattern(pattern='*')
        dialog.add_filter(filter=all_filter)

        # É obrigatório utilizar ``show_all()``.
        dialog.show_all()

        # Executando o dialogo e recebendo a resposta.
        response = dialog.run()

        # Verificando a resposta recebida.
        if response == Gtk.ResponseType.OK:
            if select_multiple:
                print('Botão SALVAR pressionado')
                print('CheckBox ESTÁ marcado')
                print(f'Caminho até os arquivos: {dialog.get_filenames()}')
                print(f'URI dos arquivos: {dialog.get_uris()}')
            else:
                print('Botão SALVAR pressionado')
                print('CheckBox NÃO está marcado')
                print(f'Caminho até o arquivo: {dialog.get_filename()}')
                print(f'URI do arquivo: {dialog.get_uri()}')

        dialog.destroy()


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
