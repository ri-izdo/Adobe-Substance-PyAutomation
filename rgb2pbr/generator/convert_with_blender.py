# This program uses Blender to convert RGB images to PBR textures.
import os
import sys
import subprocess
import logging
import json

from os import listdir
from os.path import isfile
from os.path import join

# Modules from Blender's python api.
import bpy

#for args in range(len(sys.argv)):
#    print("arg", args, sys.argv[args])


BATCH_NAME = sys.argv[5]
INPUT_DIR = str(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','input',BATCH_NAME)))
OUTPUT_DIR = str(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','output',BATCH_NAME)))
GENERATOR = str(os.path.abspath(os.path.join(os.path.dirname(__file__),'..',"generator/rgb2pbr_generator.blend")))
#print("input: ", INPUT_DIR)

def read_json_params():
    # Read json file to get list of PBR Texture channels.
    with open(os.path.join(os.path.dirname(__file__),'data/parameters.json')) as json_file:
        param = json.load(json_file)
    
    list_of_channels = param["texture"]["channel"]
    print(list_of_channels)
    return list_of_channels

def read_input_files():
#    files = [f for f in listdir(INPUT_DIR) if isfile(join(INPUT_DIR,f))]
    files = [filename for filename in os.listdir(INPUT_DIR) if filename.startswith("material")]
    rgb_file_list = []
    for rgb_file in files:
        rgb_file_list.append(rgb_file)
    return rgb_file_list

def run_blender_conversion(rgb_file_list,list_of_channels):

    # Open .blend file, which contains the PBR Generator.
    for rgb_file in rgb_file_list:
        # Join input director and file names.
        rgb_input = os.path.join(INPUT_DIR,rgb_file)
        # Open Blend Scene.
        bpy.ops.wm.open_mainfile(filepath=GENERATOR)
        # Load Image
        # Variables for Blender's API.
        scene = bpy.context.scene
        scene.use_nodes = True
        tree = scene.node_tree
        links = tree.links
        link = links.new

        load_rgb_img = bpy.data.images.load(rgb_input)
        print("Image loaded.", rgb_file)
        # Configure composite nodes.
        node =  bpy.context.scene.node_tree.nodes
        node['rgb_image_input'].image = load_rgb_img
    
        # Input parameters for each texture channel.
        for channel in list_of_channels:
            gen_node_name = str(channel) +"_gen"
            output_path = str(OUTPUT_DIR) +"_"+str(rgb_file)+"_"+str(channel) + ".png"    
            # Render.
            bpy.context.scene.render.use_file_extension = False
            link(node[gen_node_name].outputs['Image'],node["composite_output_node"].inputs[0])
            bpy.context.scene.render.filepath = output_path
            bpy.ops.render.render(write_still=True)

def main():
    list_of_channels = read_json_params()
    rgb_file_list = read_input_files()
    run_blender_conversion(rgb_file_list,list_of_channels)

if __name__ == "__main__":
    main()