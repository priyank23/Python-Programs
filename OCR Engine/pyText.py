from PIL import Image
import pytesseract
import numpy as np
import argparse

def grayScale(image):
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])

def erode(image, x=5, y=5):
    kernel = np.ones((x,y), np.uint8)

    for i in range(0, image.shape[0] - x):
        for j in range(0, image.shape[1] - y):
            
            temp = kernel * image[i:i+x, j:j+y]
            if not np.count_nonzero(temp) == x*y:
                image[i:i+x, j:j+y] = np.zeros((x,y))

    print('After erosion: ')
    print(image)
    #Image.fromarray(np.uint8(image*255), 'L').save('./eroded.png')
    return image

def dilate(image, x=5, y=5):
    kernel = np.ones((x,y), np.uint8)

    for i in range(0, image.shape[0] -x):
        for j in range(0, image.shape[1] - y):
            temp = kernel * image[i:i+x, j:j+y]
            if not np.count_nonzero(temp) == 0:
                image[i:i+x, j:j+y] = np.ones((x,y))
    
    print('After dilation: ')
    print(image)
    #Image.fromarray(np.uint8(image*255), 'L').save('./dilated.png')
    return image

def open_image(image,x=5,y=5):
    return dilate(erode(image, x,y))

def close_image(image, x=5,y=5):
    return erode(dilate(image, x,y))

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", help='filepath of image to be used', required=True)
parser.add_argument('-x', type=int,  help='x-dimension of kernel for preprocessing', default=1)
parser.add_argument('-y', type=int, help='y-dimension of kernel for preprocessing', default = 1)
parser.add_argument('-p', '--preprocess', default=None, help='Select the method of preprocessing')

args = vars(parser.parse_args())

ok = Image.open(args['image']).convert('L')
#image = np.array(ok)
#ok.save('temp.png')
#print(image.shape)
#print(np.max(image))
#print(np.min(image))
#image = 255 - image
#Image.fromarray(np.uint(image), 'L').save('invert.png')
# Morphological Transformations
## Opening
#image = open_image(image, x=args['x'], y=args['y'])
#img = Image.fromarray(np.uint8(image), 'L')
#img.show()
#print(image)
text = pytesseract.image_to_string(ok)

print('The detected text is: ')
print(text)
