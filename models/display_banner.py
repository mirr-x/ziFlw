#!/usr/bin/python3
""" banner to display in the console """

from models import time, os, colored

frames = [
    r'''
       .
~^~^~^~^~^~^~^~^~^~^~^~^~

''',
    r'''
       .
      ":"
~^~^~^~^~^~^~^~^~^~^~^~^~

''',
    r'''
       .
      ":"
    ___:____     |"\/"|
~^~^~^~^~^~^~^~^~^~^~^~^~

''',
    r'''
       .
      ":"
       :
    ___:____     |"\/"|
  ,'        `.    \  /
~^~^~^~^~^~^~^~^~^~^~^~^~

''',
    r'''
       .
      ":"
       :
       :
    ___:____     |"\/"|         Made By: mirr-x
  ,'        `.    \  /          https://github.com/mirr-x
  |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~
'''
]


class Banner:
    """
    A class to display banner information in the console.
    """

    def display_frames(self, frames, color='cyan', delay=0.2):
        for frame in frames:
            os.system('clear')  # Use 'cls' for Windows
            print(colored(frame, color))
            time.sleep(delay)

    def display_info(self):
        """
        Displays the banner information in the console using termcolor if available.
        """
        banner_text = '''
·▄▄▄▄•▪  ·▄▄▄      ▄▄▌  ▄▄▌        ▄▄▌ ▐ ▄▌
▪▀·.█▌██ ▐▄▄·▪     ██•  ██•  ▪     ██· █▌▐█
▄█▀▀▀•▐█·██▪  ▄█▀▄ ██▪  ██▪   ▄█▀▄ ██▪▐█▐▐▌
█▌▪▄█▀▐█▌██▌.▐█▌.▐▌▐█▌▐▌▐█▌▐▌▐█▌.▐▌▐█▌██▐█▌
·▀▀▀ •▀▀▀▀▀▀  ▀█▄▀▪.▀▀▀ .▀▀▀  ▀█▄▀▪ ▀▀▀▀ ▀▪

        '''

        try:
            from termcolor import cprint
            from .discordPrinte import PrinteDiscord
            self.display_frames(frames)
            cprint(banner_text, 'magenta', attrs=['bold'])
            PrinteDiscord('```diff\n+ BotPoints is running...\n```')
        except ImportError:
            print(banner_text)

