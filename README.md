# LuciDream

## How to use
Download the dist for this repo and do:
```sh
pip install Lucidream-0.1.0.tar.gz
```

### Creating your history
The engine is like that:
```py
from Lucidream import Dream

dream = Dream()

# Beggining of the history
dream.addScene("start", "You wake up in a mysterious room.", image="room.jpg")

# Adding choices
dream.addChoice("start", "Go through the door", "door_scene")
dream.addChoice("start", "Look out the window", "window_scene")

# Defining scenes
dream.addScene("door_scene", "You find a hallway.", image="hallway.jpg")
dream.addScene("window_scene", "You see a garden below.", image="garden.jpg")

# end of history
dream.addChoice("door_scene", "Go to end", "end")
dream.addChoice("window_scene", "Go to end", "end")

dream.addScene("end", "the end", image="end.jpg")

# Execute the history
dream.run()
```

#### Dream()
Will create an object to use in the code

#### addScene

##### parameters
- `name`: the name of the scene. Should be unique for all scenes, and should be exist one `start` and `end` scene.
- `description`: the text description of the scene, rendered on the client interface.
- `image`: path of your image resource that will be rendered on the client interface. Should be inside an `assets` folder.

#### addChoice

##### parameters
- `parent`: scene name of this choice. Will be rendered like an option when the user is on that scene.
- `description`: description of that choice. Like an option to follow in the history.
- `child`: the next scene, if this choice is choosed, the next scene will be the scene with the `child` name.

#### run
Just render all history, run tests and check if assets files exists. Creating all client interface as well.
It will check if all scenes can be touch, and if exists valid flow to the all storytelling.

## How to do an executable game?

command example:
```sh
python3 -m Lucidream.build --app=example.py --resolutions=hd,fullhd,4k
```

### commands

- `--app`: specify the name of the script. Mandatory.
    example: `--app=example.py
- `--resolutions`: specify whats resolutions you need render a game: [`hd`, `fullhd`, `4k`]. Default: `hd`
    - examples:
    - `--resolutions=4k`
    - `--resolutions=4k,fullhd`
- `--languages`: loading...
- `--runner`: just to specify what python alias for runner you use. Default: `python`
    - examples:
    - `--runner=python`
    - `--runner=python3`

> The files executables will be in a `dist` directory with the `.exe` and needed files. Cannot do cross-compilation, so
if you need to do an executable for windows, you need run the above command for windows as well...
