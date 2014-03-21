# encoding: utf-8

'''This adds a "char_value" command to be invoked by Sublime Text. It is made
available as "Char Value" in the command palette by Default.sublime-commands.'''

import sublime
import sublime_plugin
from .char_value import char_value


class CharValueCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        regions = self.view.sel()

        # Only run if there is a selection.
        if len(regions) > 1 or not regions[0].empty():

            # Get values for each char in each selection.
            for region in regions:
                output = char_value(self.view.substr(region))
                self.view.replace(edit, region, output)
