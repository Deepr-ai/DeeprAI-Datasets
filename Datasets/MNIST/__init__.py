# TODO: Move relevant data to HOME/.datasets after it is downloaded w/ the module
from os.path import exists, expanduser
from os import mkdir
HOME = expanduser("~")

if not exists(f'{HOME}/.datasets'):
    mkdir(f'{HOME}/.datasets')