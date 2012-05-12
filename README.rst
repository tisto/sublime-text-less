LESS PLUGIN FOR SUBLIME TEXT
============================

This plugin compiles LESS (http://lesscss.org/) files into CSS files in Sublime
Text 2 on save.

This plugin is tested on Mac Os X, but suppose to work on other systems.

Prerequisits
------------

Install nodejs, required for runing lessc:

  http://www.hodejs.org

Install lessc binary:

  http://lesscss.org/


Package installation
------------

Linux

  $ cd ~/.config/sublime-text-2/Packages/

Mac Os X

  $ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
  $ git clone git@github.com:speechkey/sublime-text-less.git

Edit sublime-text-less.sublime-settings and add lessc and nodejs path, if it not already included in your default environment path.

Linux

  $ vim ~/.config/sublime-text-2/Packages/sublime-text-less.sublime-settings

Mac Os X

  $ vim ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/sublime-text-less.sublime-settings   
