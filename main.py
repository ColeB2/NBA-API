import os, sys
sys.path.append(os.path.join('.', 'ui'))
sys.path.append(os.path.join('.', 'config'))

from nba_main_ui import NBA_UI
from getconfiginfo import get_info



class MainApp(object):
    """A class representation of main app.
    """
    def __init__(self):
        self.config()

        self.UI = NBA_UI()

    def config(self):
        try:
            if get_info(('Default', 'config')) != 'True':
                print(get_info('Default', 'config'))
                self.UI.config_display()
        except:
            self.UI.config_display()
        else:
            print('All Good')

    def run(self):
        print('RUN')
        self.UI.run()


if __name__ == '__main__':
    App = MainApp()
    App.run()
