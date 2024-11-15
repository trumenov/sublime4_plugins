import sublime
import sublime_plugin
import os

class CopyFilenameCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Получаем путь к активному файлу
        file_path = self.view.file_name()
        if not file_path:
            sublime.status_message("No file is currently active.")
            return

        file_name_without_extension = os.path.splitext(os.path.basename(file_path))[0]
        sublime.set_clipboard(file_name_without_extension)
        sublime.status_message(f"Filename copied: {file_name_without_extension}")
        return
