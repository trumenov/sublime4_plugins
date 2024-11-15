import sublime
import sublime_plugin
import os

class CopyRelativePathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Получаем путь к активному файлу
        file_path = self.view.file_name()
        if not file_path:
            sublime.error_message("File not saved, path not accessible.")
            return

        # Находим корневую папку проекта
        window = self.view.window()
        project_folders = window.folders()
        if not project_folders:
            custom_root = self.get_custom_root(file_path)
            if custom_root:
                relative_path = os.path.relpath(file_path, custom_root)
                sublime.set_clipboard(relative_path)
                sublime.status_message("Relative custom_root path copied: " + relative_path)
                return

            sublime.status_message("Project root folder not found.")
            sublime.set_clipboard(file_path)
            return

        # Вычисляем относительный путь
        for folder in project_folders:
            if file_path.startswith(folder):
                relative_path = os.path.relpath(file_path, folder)
                sublime.set_clipboard(relative_path)
                sublime.status_message("Relative path copied: " + relative_path)
                return

        custom_root = self.get_custom_root(file_path)
        if custom_root:
            relative_path = os.path.relpath(file_path, custom_root)
            sublime.set_clipboard(relative_path)
            sublime.status_message("Relative custom_root path copied: " + relative_path)
            return
        else:
            sublime.status_message("The file is outside the project root folder and no suitable root was found.")
            sublime.set_clipboard(file_path)
        return

    def get_custom_root(self, file_path):
        """
        Calculates the "project folder" based on custom logic:
        Take the part of the path that is after *_reps/ and go up +1 level.
        All my projects always placed with rule:
        /d/my_reps/somerepo1
        /d/dev38_reps/somerepo1
        /d/dev39_reps/somerepo1
        So plugin search in path this _reps suffix.
        """
        parts = file_path.split(os.sep)
        try:
            # Find index *_reps
            reps_index = next(i for i, part in enumerate(parts) if part.endswith('_reps'))
            # Return path including next level
            return os.sep.join(parts[:reps_index + 2])
        except StopIteration:
            return None
