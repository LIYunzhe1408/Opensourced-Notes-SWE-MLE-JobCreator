# Overview
In this project, we reinforce the foundation of traditional image processing in OpenCV. Based on the Computer Vision <a href=\"https://coggle.it/diagram/ZO5EUOut86Irr5hc/t/computer-vision-roadmap/760d909a1f28af1782645ff9b5af1dfd4481ce08bf258b4b54f868d7f3a1b8d5\">Roadmap</a> and <a href=\"https://www.youtube.com/watch?v=eDIj5LuIL4A\">OpenCV tutorial</a>, we take some notes which might help beginners to better comprehend what the OpenCV can do and its application.

## What are images?
* In Python, images are nparrays, we can call the shape attribute to have (height, width, number of channels). 
* Images are made by pixels which are very basic components in one image. 
* The value of each pixel ranges from 0 to 255 in most cases, because 1 pixel is represented by 8 bits or 1 Byte, and there are 2^8 different states. In special cases in which it is a binary or the pixels in the image are represented by 16 bits, the range will be [0, 1] or [0, 65535].

## Inputs and outputs
Code reference: `io_image.py`, `io_video.py`, `io_webcam.py`
'''
waitkey(delay_time)
Param: wait for delay_time to show the next frame
Return: the current value of the pressed keyboard
'''
> If using a webcam, the delay time depends on the time it takes for the webcam to read a frame and the amount of frames per second.

## Resizing and crop
Code reference: `resizing.py`, `crop.py`

In resizing, use the cv2.resize(image, (**width**, **height**)) function.

**HEADS UP**: The np.array.shape is (**height**, **width**, channel) which is different from the resize function.

In crop, we do not use any opencv functions. Instead, as images are nparrays, we use the array slice to get intervals.

## Color space
Code reference: `color-space.py`

The pixel in the image in OpenCV is a combination of BGR color space. We can use `cv2.cvtColor(img, color_space_code)` to convert the color space. The color space code can be found at https://docs.opencv.org/4.x/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab

When we convert the color space, notice that it is still the same image, but the information is reorganized. Take grayscale for example, it condenses 3 channels into one channel, so the saving storage will be smaller than the BGR one. For HSV color space, it is meanless for humans, as we human eyes are trained to look at RGB. In contrast, it is useful for computer vision applications like color detection.

## Blur
Code reference: `blurring.py`

Blurring is used to remove noise. The intuition of blurring is the AVERAGE. We use the average value of the neighbor pixels in a specific area to replace the center pixel value. Firstly, we need to define the neighbor's proximity to blur. Then use `cv2.blur`, `cv2.GaussianBlur`, `cv2.medianBlur`.

## Threshold: Global and adaptive
Code reference: `global-threshold.py`, `adaptive-threshold.py`

Function parameters: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

Image thresholding is used to identify an object on an image or remove noise. The image should be converted into a binary image by converting color space into grayscale. Then apply `cv2.threshold(image, threshold, max_value_over_threshold, thresholding_type)`, which is a global thresholding method.

In some special cases with different lighting conditions, adaptive thresholding can help. The algorithm determines the threshold for every pixel based on the small region around it, which gives better results in varying illumination. Call `cv2.adaptiveThreshold(image, max_value_over_threshold, adaptive_method, thresholding_type, block_size, constant)`.

## Edge detection and morphology operations
Use `cv2.Canny()` for edge detection. To get more details about the theory, please refer to: https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html

If you want to have a thicker boundary line, apply `cv2.dilate(image, kernel)`. Conversely, use `cv2.erode()` to do the opposite.

## Drawing
* cv2.line(image, (start_pointX, start_pointY), (end_pointX, edn_pointY), color, thickness)
* cv2.rectangle(image, (UpLeftX, UpLeftY), (DownRightX, DownRightY), color, thickness)
* cv2.circle(image, (centerX, centerY), diameter, color, thickness)
* cv2.putText(image, string, (start_pointX, start_pointY), font, font_scale, color, thickness)
## Contour
* Run BGR2Grayscale+cv2.threshold or HSV+cv2.inRange to convert it into a binary image, then detect contours. 
* Contours and the hierarchies will be returned after calling the above function.
* Detect all borders of all the isolated regions which means if two objects have some overlaps, we will just get one border.
