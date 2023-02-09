from os.path import exists, expanduser
from os import mkdir
HOME = expanduser("~")

if not exists(f'{HOME}/.datasets'):
    mkdir(f'{HOME}/.datasets')