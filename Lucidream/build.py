import argparse
import subprocess
import json
from .constants import getAsset

def _getArgs():
    parser = argparse.ArgumentParser(description='Lucidream args')
    parser.add_argument('--app',type=str,help='app to build')
    parser.add_argument('--resolutions', type=str, help='hd, fullhd or 4k')
    parser.add_argument('--languages', type=str, help='select your language')
    parser.add_argument('--runner', type=str, help='python3, python, python3.2 for example')
    new_parser = parser.parse_args()
    
    if not new_parser.app:
        raise ValueError("App is mandatory! Use --app=your_app_path")
    if not new_parser.resolutions:
        new_parser.resolutions = 'hd'
    if not new_parser.languages:
        new_parser.languages = 'en'
    if not new_parser.runner:
        new_parser.runner = 'python'
    
    return new_parser

def _testApp(runner, app_path):
    cmd = "{} {}".format(runner, app_path)
    print("##########################")
    print("Tests started...")
    print("##########################")
    code = subprocess.run(cmd.split())
    print("##########################")
    if code.returncode != 0:
        print("Tests Failed")
    else:
        print("Tests OK")
    print("##########################")
    
    return code.returncode == 0

def _buildLogs(resolution):
    path = getAsset() + "/logs.json"
    f = open(path, "w")
    
    info = {
        "resolution": resolution,
    }
    f.write(json.dumps(info))
    f.close()

def _buildBin(app_path, resolution: str):
    app_name = app_path.split('/')[-1][:-3]
    distpath = "dist/{}_{}".format(app_name, resolution)
    
    _buildLogs(resolution)

    cmd = "pyinstaller --onefile --add-data=assets:assets --distpath={} {}".format(distpath, app_path)
    subprocess.run(cmd.split())

def build():
    args = _getArgs()
    app_path = args.app
    resolutions = args.resolutions.split(',')
    languages = args.languages.split(',')
    runner = args.runner
    
    if not _testApp(runner, app_path):
        return None
    
    for resolution in resolutions:
        if resolution not in ['hd', 'fullhd', '4k']:
            continue
        _buildBin(app_path, resolution)

if __name__ == "__main__":
    build()
