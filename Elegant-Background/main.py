# Changing wallpaper in windows temporarily using python
# m - t - w - t - f - s - s
from colorama import init, Fore; init(autoreset=True)
from datetime import datetime
import os, ctypes, sys, time, shutil, configparser

start_time = time.perf_counter()

BASEPATH = os.path.dirname(os.path.abspath(__file__))
CONFIG = ".config"
BASECONFIG = os.path.join(BASEPATH, "settings.ini")
BASE_WALLPAPER_PATH = os.path.join(BASEPATH, 'WALLPAPER')
WALLPAPER_NAME = 'wallpaper.jpg'
WALLPAPER = os.path.join(BASE_WALLPAPER_PATH, WALLPAPER_NAME)

# Setting up parser
isDebug = False
changeWallpaper = None
newDate = None
newCount = None

parser = configparser.ConfigParser()
parser.read(BASECONFIG)

MODE_LST = {
    "permanent": 3,
    "temporary": 0
}

if not os.path.exists(BASECONFIG):
    sys.exit(f"{Fore.RED}Config file not found.")
E_DATE = parser.getint('settings', 'date')
MODE = MODE_LST[parser.get('settings', 'mode')]
COUNT = parser.getint('settings', 'count')

if os.path.exists(CONFIG):
    parser.read(CONFIG)
    if parser.has_section("config"):
        isDebug = parser.getboolean('config', 'debugger', fallback=False)
        changeWallpaper = parser.get('config', 'wallpaper', fallback=None)
        newDate = parser.getint('config', 'date', fallback=None)
        if newDate is not None:
            parser.set('settings', 'date', str(newDate))
            print("Date has been set to {}".format(newDate))
            E_DATE = newDate
        NEW_MODE = parser.get('config', 'mode', fallback=None)
        if NEW_MODE is not None:
            parser.set('settings', 'mode', NEW_MODE)
            MODE = MODE_LST[NEW_MODE]
        newCount = parser.getint('config', 'count', fallback=None)
        if newCount is not None:
            parser.set('settings', 'count', str(newCount))
            COUNT = newCount
        with open(BASECONFIG, 'r+') as file:
            file.seek(0)
            file.truncate()
            parser.remove_section("config")
            parser.write(file)

if changeWallpaper is not None:
    # Copy wallpaper to base wallpaper path
    os.remove(WALLPAPER)
    shutil.copyfile(changeWallpaper, WALLPAPER)

if not isDebug:
    today = datetime.today().weekday()
    loggingFile = os.path.join(os.environ.get("USERPROFILE"), ".w_log")
    if all([COUNT == 1, not os.path.exists(loggingFile)]) or COUNT == 0:
        if str(E_DATE) == str(today):
            ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER, 3)
        else:
            print(f"{Fore.LIGHTMAGENTA_EX}Today is not a prank day")
        if COUNT == 1:
            with open(loggingFile, 'w'):
                pass
end_time = time.perf_counter()
sys.exit(f"{Fore.LIGHTCYAN_EX}Program executed successfully in {end_time - start_time} seconds")