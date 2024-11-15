import sublime
import sublime_plugin
import re

class SnakeToCamelCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Получаем выделенный текст
        for region in self.view.sel():
            if not region.empty():
                # Получаем текст выделенной области
                s = self.view.substr(region)
                # Преобразуем snake_case в CamelCase
                camel_case = re.sub(r'(?:^|_)(.)', lambda m: m.group(1).upper(), s)
                # Заменяем выделенный текст на преобразованный
                self.view.replace(edit, region, camel_case)
