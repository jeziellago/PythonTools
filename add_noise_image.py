""" Add noise in images 
    Usage: python add_noise_image.py --imagedir=<DIR> or python add_noise_image.py --image=<IMAGE>
    Help: python add_noise_image.py -h 
    
    Author: Jeziel Ribeiro Lago [jeziellago@gmail.com]
"""

from skimage import io
from skimage.util import random_noise
import argparse, os

def generate_noised_image(name, image):
    io.imsave(name, random_noise(img, mode='s&p', amount=0.25))

def main(FLAGS):
    if FLAGS.image != '':
        generate_noised_image(FLAGS.image + '_noised', io.imread(FLAGS.image))
    elif FLAGS.imagedir != '':
        files = os.listdir(FLAGS.imagedir)
        for f in files:
            generate_noised_image(f, io.imread(f))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--imagedir',
        default='',
        help='Folder from apply noised.'
    )
    parser.add_argument(
        '--image',
        default='',
        help='Image from apply noised.'
    )    
    FLAGS, _ = parser.parse_known_args()