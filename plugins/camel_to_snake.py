import sublime
import sublime_plugin
import re

class CamelToSnakeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                text = self.view.substr(region)
                snake_case_text = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
                self.view.replace(edit, region, snake_case_text)
