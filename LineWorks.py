import sublime, sublime_plugin, subprocess, re

# singlify shamelessly ripped from singleline package

class LineworksDeleteCommand(sublime_plugin.WindowCommand):
    def run(self, **args):
        self.window.show_input_panel("Which lines to delete?", "", Lineworks.delete, None, None)


class LineworksMultiToSingleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in reversed(self.view.sel()):

            text = self.view.substr(region)

            text = Lineworks.singlify(text)
            self.view.replace(edit, region, text)

class Lineworks(sublime_plugin.TextCommand):
    def delete(str):
        awindow = sublime.active_window()
        aview = awindow.active_view()

        print(str)
        line_from = int(str[:str.find(":")])
        line_to = int(str[str.find(":")+1:])
        for i in range(line_from - 1, line_to):
            #sublime.active_window().active_view().erase(edit, self.view.line(self.view.text_point(i,0)))
            line = aview.line(aview.text_point(i,0))
            print(line)
            sublime.active_window().active_view().run_command("lineworks_delete_line", {"line_n": i})

    def singlify(text):
        m = re.search('^(?P<leading>\s*).*$', text.split('\n')[0])  # grab leading spacing
        single = m.group('leading') + ' '.join([x.strip() for x in text.split('\n')])
        return single


class LineworksDeleteLineCommand(sublime_plugin.TextCommand):
    def run(self, edit, line_n):
        aview = sublime.active_window().active_view()
        line_region = aview.line(aview.text_point(line_n,0))
        aview.erase(edit, line_region)

