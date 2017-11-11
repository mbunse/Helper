'''
Helper module to crop images
'''
import os.path
from PIL import Image

class Cropper:
    '''
    Helper class for image cropping
    '''
    def __init__(self, startx, starty, endx, endy):
        '''
        Parameters:
        -----------
        startx:             horizontal starting point in pixels
        starty:             vertical starting point in pixels
        endx:               horizontal end point of cropped area
        endy:               vertical end point of cropped area
        '''
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy


    def crop_image(self, input_image_path, output_image_path):
        ''' Function to crop image from screenshot
        Parameters:
        -----------
        input_image_path:   path incl. filename of image to crop
        output_image_path:  path incl. filename for cropped image


        Returns:
        --------
        Nothing
        '''
        os.path.join("")
        img = Image.open(input_image_path)
        img = img.crop((self.startx, self.starty, self.endx, self.endy))
        img.save(output_image_path)

def get_all_images(input_path):
    '''
    Generator function to extract PNG files
    for cropping from input dir

    Parameters:
    -----------
    input_path:     path to input directory
    output_path:    path to output directory

    Returns:
    --------
    Generated "list" of tuples (full path to input file, filename of input file)
    '''
    files_in_dir = os.listdir(path=input_path)
    for filename in files_in_dir:
        if os.path.splitext(filename)[1].upper() == ".PNG":
            yield (os.path.join(input_path, filename), filename)

def crop_files_in_dir(input_path, output_path,
                      startx, starty, endx, endy):
    '''
    Function to crop PNG images in input_path and
    copy the cropped images to output_path

    Paramters:
    ----------
    input_path:     path to input directory
    output_path:    path to output directory
    startx:         horizontal starting point in pixels
    starty:         vertical starting point in pixels
    endx:           horizontal end point of cropped area
    endy:           vertical end point of cropped area
    '''
    cropper = Cropper(startx, starty, endx, endy)
    for infile_path, filename in get_all_images(input_path):
        cropper.crop_image(infile_path, os.path.join(output_path, filename))


if __name__ == "__main__":
    crop_files_in_dir(input_path="D:\\Users\\Moritz\\Pictures\\Screenshots\\input_screenshots",
                      output_path="D:\\Users\\Moritz\\Pictures\\Screenshots\\cropped_screenshots",
                      startx=585, starty=132,
                      endx=1000, endy=869)
