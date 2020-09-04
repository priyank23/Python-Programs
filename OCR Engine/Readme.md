## OCR Engine

Using `python-tesseract` library to extract text from image and make the device speak the text out loud.

### Libraries Used

* `Pillow` - For reading the input file
* `numpy`  - For custom preprocessing
* `argparse`- For parsing the arguments
* `opencv-python` - For preprocessing
* `socket` - For checking internet connection availability
* `pytesseract` - For converting image to text
* `gtts` - For converting text to audio (online mode)
* `playsound` - For playing the audio
* `pyttsx3` - For converting text to audio and play it. (offline mode)

### Preprocessing Steps

* _Grayscaling_: Converting the RGB image into grayscale
* _Binarization_: Binarising the grayscale image using Binary thresholding
* _Erosion_: Morphological step to erode away the noise in the image
* _Dilation_: Morphological step to enlarge image for better detection

### How to use

* `python3 pyText.py -i <image_path> [options ...]`
	##### Options
	* -i IMAGE, --image IMAGE		| filepath of image to be used
	* -th value, --threshold value		| Select the threshold value for binarisation (0-255)
	* -p option, --preprocess option	| Select the method of preprocessing
		###### Preprocessing Options
		* 'erode'			| Performs erosion 
		* 'dilate'			| Performs dilation 
		* 'open'			| Performs Morphological opening
		* 'close'			| Performs Morphological closing
	* -x X					| x-dimension of kernel for preprocessing
	* -y Y					| y-dimension of kernel for preprocessing
	* -h, --help				| Shows possible options for execution

### Post-processing Steps (Plan)
* [x] To convert text into speech.
