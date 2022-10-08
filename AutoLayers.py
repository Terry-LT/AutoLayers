from pyautocad import Autocad
import configparser
from pathlib import Path

app_name = 'AutoLayers'
#https://www.youtube.com/watch?v=S830pk6al74&ab_channel=AxelT.
acad = Autocad()
config = configparser.ConfigParser()

def create_config_file():
    if (Path("configfile{0}.ini".format(app_name)).is_file() == False):
        print("The config file does not exist. Let's add it...")

        config.add_section('layers')
        #first paramater is the name of the section
        #second paramater is the name of the layer
        #third paramater is the number of the color
        config.set('layers', 'exampleLayer', '111')
        with open("configfile{0}.ini".format(app_name), 'w') as configfile:
            config.write(configfile)
    else:
        print('')
        print('The confing exsts')
        print('')

def add_layer(name,color):
    acad.doc.Layers.Add(name)
    if color != "":
        element = acad.doc.Layers.Item(name)
        element.Color = color

def read_config_file():
    config.read("configfile{0}.ini".format(app_name), encoding="utf-8")
    for layer in config['layers']:
        color = config['layers'][layer]
        add_layer(layer,color)

def main():
    print('')
    print('This script was written by Terry-Lt')
    create_config_file()
    read_config_file()

if __name__  == '__main__':
    try:
        main()
        print('')
        
        print('▁ ▂ ▄ ▅ ▆ ▇ █   🎀  𝒯𝑒𝓇𝓎 𝐿𝓉  🎀   █ ▇ ▆ ▅ ▄ ▂ ▁')

        print('')
            
        input('Done. You can close this script')
    except OSError:
        print('It seems that Autocad is turned off. Turn it on in order to add layers!')
