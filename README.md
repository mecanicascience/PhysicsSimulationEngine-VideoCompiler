# PhysicsSimulationEngine-VideoCompiler
A python video compiler that creates video based on data given by the [pSEngine](pSEngine.mecanicascience.fr) `Recorder` class.

## Requirements
 - Python 3.X or a newer version
 - FFMPEG set up as an environment variable (so you can run 'ffmpeg <your-command>' inside a command prompt)

## How to use the converter
 1. Download all of the above requirements
 1. Use the `Recorder` class in pSEngine (find the documentation of [pSEngine](pSEngine.mecanicascience.fr) online) to generate a data file in JSON format.
 1. Copy the generated JSON file inside the folder `datas/`
 1. Then you have two choices:
   - Rename your generated JSON file `json-datas.json`
   - Open the `run.bat` file with a text editor, and change the `json-datas` string to whatever your file name is (just make sure you don't write the `.json` extension at the end of the file name)
 1. Run the `run.bat` file by double-clicking on it
 1. When finished, the video will be generated as `datas/ouput.mp4`
 1. If you want to save memory space on your computer, you can now delete the **content** of the folder `raw/` 
