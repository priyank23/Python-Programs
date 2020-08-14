from PIL import Image
import pytesseract
import numpy as np
import argparse
import cv2
def grayScale(image):
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])

def erode(image, x=5, y=5):
    kernel = np.ones((x,y), np.uint8)

    for i in range(0, image.shape[0] - x):
        for j in range(0, image.shape[1] - y):
            
            temp = kernel * image[i:i+x, j:j+y]
            if not np.count_nonzero(temp) == x*y:
                image[i:i+x, j:j+y] = np.zeros((x,y))
            else: image[i:i+x, j:j+y] = kernel

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
                image[i:i+x, j:j+y] = kernel
            else: image[i:i+x, j:j+y] = np.zeros((x,y))
    
    print('After dilation: ')
    print(image)
    #Image.fromarray(np.uint8(image*255), 'L').save('./dilated.png')
    return image

def open_image(image,x=5,y=5):
    return dilate(erode(image, x,y))

def close_image(image, x=5,y=5):
    return erode(dilate(image, x,y))

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", help='filepath of image to be used', required=True)
    parser.add_argument('-th', '--threshold' ,type=int , help='Select the threshold value for binarisation')
    parser.add_argument('-p', '--preprocess', default=None, help='Select the method of preprocessing')
    parser.add_argument('-x', type=int,  help='x-dimension of kernel for preprocessing', default=1)
    parser.add_argument('-y', type=int, help='y-dimension of kernel for preprocessing', default = 1)
        
    return vars(parser.parse_args())

def main(args):
    image = Image.open(args['image']).convert('L')                          # Converting the input into grayscale image
    image = cv2.cvtColor(cv2.imread(args['image']), cv2.COLOR_BGR2GRAY)
    #np.savetxt('image.csv', np.uint8(image), delimiter=',', fmt='%d')

    # Thresholding if suggested
    if not args['threshold'] == None:
        ret, image = cv2.threshold(image, args['threshold'], 255, cv2.THRESH_BINARY)
        Image.fromarray(image).save('thresholded.png')

    if not args['preprocess'] == None:
        #image = np.uint8(image)
        if args['threshold'] == None:
            ret, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
            #image = image > 128
            #Image.fromarray(image*255, 'L').save('thresholded.png')

        if args['preprocess'] == 'erode':
            image = cv2.erode(image, np.ones((args['x'],args['y']), np.uint8), iterations=1)
            #image = erode(image, args['x'], args['y'])
        elif args['preprocess'] == 'dilate':
            image = cv2.dilate(image, np.ones((args['x'],args['y']), np.uint8), iterations=1)
            #image= dilate(image, args['x'], args['y'])
        elif args['preprocess'] == 'open':
            image = cv2.morphologyEx(image, cv2.MORPH_OPEN, np.ones((args['x'], args['y']),np.uint8))
            #image = open_image(image, args['x'], args['y'])
        elif args['preprocess'] == 'close':
            image = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((args['x'], args['y']), np.uint8))
            #image = close_image(image, args['x'], args['y'])

        image = Image.fromarray(image, 'L')
        image.save('preprocessed.png')
    
    text = pytesseract.image_to_string(image)

    print('The detected text is: ')
    print(text)
    file = open(r"Result", "w")
    file.write(text)
    file.close()

args = parse()
print(args)
main(args)
