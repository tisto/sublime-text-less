import sublime
import sublime_plugin
import subprocess
from lessc_opts import lessc_opts


class CompileLessOnSave(sublime_plugin.EventListener):

    def on_post_save(self, view):
        if not view.file_name().endswith('.less'):
            return

        filename = view.file_name()
        output_filename = filename.replace('.less', '.css')

        proc = subprocess.Popen("lessc %s" % filename,
            shell=True,
            stdout=subprocess.PIPE)
        output = proc.communicate()[0]

	output_file = open(output_filename,"w")
	output_file.write(output)
	output_file.close()

