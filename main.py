import os, sys
sys.path.append(os.path.join('.', 'ui'))
sys.path.append(os.path.join('.', 'config'))

from nba_main_ui import NBA_UI
from getconfiginfo import get_info



class MainApp(object):
    """A class representation of main app.
    """
    def __init__(self):
        self.UI = NBA_UI()

    def run(self):
        if get_info(('Default', 'config')) != 'True':
            self.UI.config_display()
        self.UI.run()


if __name__ == '__main__':
    App = MainApp()
    App.run()
