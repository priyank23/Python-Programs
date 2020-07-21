## OCR Engine

Using `python-tesseract` library to extract text from image

### Preprocessing Steps

* _Grayscaling_: Converting the RGB image into grayscale
* _Binarization_: Binarising the grayscale image using OTSU thresholding
* _Erosion_: Morphological step to erode away the noise in the image
* _Dilation_: Morphological step to enlarge image for better detection

### Post-processing Steps (Plan)
* [ ] To convert text into speech.
