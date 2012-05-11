import sublime
import sublime_plugin
import subprocess
import commandline


class CompileLessOnSave(sublime_plugin.EventListener):

    def on_post_save(self, view):
        try:
            less = commandline.find_binary('less')
        except commandline.BinaryNotFoundError:
            sublime.error_message("I couldn't find \"less\" binary on your system. Less is required on your system. Please install it and try again.")
            return

        if not view.file_name().endswith('.less'):
            return

        filename = view.file_name()
        output_filename = filename.replace('.less', '.css')

        command = [less] + [filename]
        output = commandline.execute(command)

        output_file = open(output_filename,"w")
        output_file.write(output)
        output_file.close()

