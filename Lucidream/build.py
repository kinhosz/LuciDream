import argparse
import subprocess

def _getArgs():
    parser = argparse.ArgumentParser(description='Lucidream args')
    parser.add_argument('--app',type=str,help='app to build')
    parser.add_argument('--resolutions', type=str, help='hd, fullhd or 4k')
    parser.add_argument('--languages', type=str, help='select your language')
    new_parser = parser.parse_args()
    
    if not new_parser.app:
        raise ValueError("App is mandatory! Use --app=your_app_path")
    if not new_parser.resolutions:
        new_parser.resolutions = 'hd'
    if not new_parser.languages:
        new_parser.languages = 'en'
    
    return new_parser

def _buildBin(app_path, resolution: str):
    app_name = app_path.split('/')[-1][:-3]
    distpath = "dist/{}_{}".format(app_name, resolution)

    cmd = "pyinstaller --onefile --distpath={} {}".format(distpath, app_path)
    subprocess.run(cmd.split())

def build():
    args = _getArgs()
    app_path = args.app
    resolutions = args.resolutions.split(',')
    languages = args.languages.split(',')
    
    for resolution in resolutions:
        _buildBin(app_path, resolution)

if __name__ == "__main__":
    build()
