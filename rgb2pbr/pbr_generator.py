
'''
This program converts RGB images to PBR textures.
Documentation go/arkadia-pbr2rgb
To read RGB Images and convert to PBR textures:

Example useage:
$python pbr_generator.py --blender=/path/to/Blender Application \
--source=/path/to/rgb/images \
--output=/path/to/pbr/output

python pbr_generator.py --blender=/Applications/Blender.app/Contents/MacOS/blender \
--batch_name=sf
'''


# Import modules.
import os 
import sys
import subprocess
from absl import app
from absl import flags

# Instance Control Flags.
flags.DEFINE_string('blender', None, 'Path to Blender Application')
flags.DEFINE_string('batch_name', None, 'Name of batch')

FLAGS = flags.FLAGS

def main(argv):
    path_to_this = os.path.dirname(os.path.abspath(__file__))

    if FLAGS.blender is None:
        raise ValueError('Please supply a valid path to a Blender executable')
    if FLAGS.batch_name is None:
        raise ValueError('Please supply the batch name')

    exec_str = '{} -b -P {}/generator/convert_with_blender.py -- {}'.format(
        FLAGS.blender, path_to_this, FLAGS.batch_name
    )

    os.system(exec_str)

if __name__ == '__main__':
    app.run(main)