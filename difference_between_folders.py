""" Copy all different files between 'source' and 'compare' folder to new folder 
    Use: python difference.py --source_dir=<SOURCE_DIR> --compare_dir=<COMPARE_DIR> --output_dir=<OUTPUT_DIR>
"""
__author__ = 'Jeziel Ribeiro Lago'
__email__ = 'jeziellago@gmail.com'

print(__doc__)

from skimage import io
from shutil import copyfile 
import argparse
import os 

def main(PARAMS):
    source_dir = PARAMS.source_dir
    compare_dir = PARAMS.compare_dir
    output_dir = PARAMS.output_dir
    
    files_output_dir = list(set(os.listdir(source_dir)) - set(os.listdir(compare_dir)))
    for f in files_output_dir:
        copyfile(os.path.join(source_dir, f), os.path.join(output_dir, f))  

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--source_dir',
        type=str,
        default='',
        required=True,
        help='Source folder to compare.'
    )
    parser.add_argument(
        '--compare_dir',
        type=str,
        default='',
        required=True,
        help='Folder to compare.'
    )    
    parser.add_argument(
        '--output_dir',
        type=str,
        default='',
        required=True,
        help='Output folder.'
    ) 
    
    PARAMS, _ = parser.parse_known_args()
    main(PARAMS)