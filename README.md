# Juniper World Editor
This a program that allows custom worlds to be created for the game juniper

Custom worlds can be created and edited in this program to create a world just use the command `python editor.py 20 20 example` this will create a world named example with the dimensions of 20x20 and to load a world just use `python editor.py 20 20 world_you_want_to_load` (Remember you don't need to mension the `worlds` folder as it already pulls from there) then when you are in the program you just click load to get that world

To save a world you can just click the save button that is located next to the load button at the bottom right of the screen

## Known Limitations
I know that world sizes of 500x500 are impossible since the program lags too much even when using the compiled version, this is a limitation with the way that the world is stored and not the program, since it realise on json for saving the worlds it takes up some space and lags

I also know that the files are very large for there small size, this is something I plan on fixing in the future, however at the moment to remove some file size you can always remove the indentation of the json file or use the `update_world.py` to do the same and also repair your older worlds


## How to install?
To install this you can either click the `Download Zip` button on github or head to the releases and download the latest exe file from it [Click Here to See Latest Release](https://github.com/RavinClaw/Juniper-World-Editor/releases/tag/v1.0)

You will need to install [Python](https://python.org) and you will need to install `Pygame` using `pip` the command is `python -m pip install pygame` or `py -m pip install pygame`


## Compile to exe
to Compile this to an exe program you will need to install `PyInstaller`, the command is `python -m pip install PyInstaller` or `py -m pip install PyInstaller`

One downloaded you can run the command from the project folder `python -m PyInstaller editor.py --windowed --onefile` or `py -m PyInstaller editor.py --windowed --onefile`, this compiles the program (It may take sometime the first time you do this)
Once completed the file can be found in `build` folder and you will need to copy the file to the root directory `/` to run the editor as it realise on the files in `resources` and it will also require the `worlds` folder
