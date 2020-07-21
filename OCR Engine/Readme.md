## OCR Engine

Using `python-tesseract` library to extract text from image

### Preprocessing Steps

* _Grayscaling_: Converting the RGB image into grayscale
* _Binarization_: Binarising the grayscale image using Binary thresholding
* _Erosion_: Morphological step to erode away the noise in the image
* _Dilation_: Morphological step to enlarge image for better detection

### How to use

* `python3 pyText.py -i <image_path>`
	##### Options
	* -i IMAGE, --image IMAGE		filepath of image to be used
	* -th value, --threshold value		Select the threshold value for binarisation (0-255)
	* -p <option>, --preprocess <option>	Select the method of preprocessing
		###### Preprocessing Options
		** 'erode'			Performs erosion
		** 'dilate'			Performs dilation
		** 'open'			Performs Morphological opening
		** 'close'			Performs Morphological closing
	* -x X					x-dimension of kernel for preprocessing
	* -y Y					y-dimension of kernel for preprocessing
	*-h, --help				Shows possible options for execution

### Post-processing Steps (Plan)
* [ ] To convert text into speech.
