# Journey of 300 Days of Deep Learning for Computer Vision using Python
![This is an image displaying computer vision](photos/computervision.jpg)

I am starting my journey in Computer Vision. I have started my journey by learning OpenCv from a youtube video uploaded by freeCodeCamp.org(the link is in the resources field) and I will be learning from a book written by Dr. Adrian Rosebrock called "Deep Learning For Computer Vision With Python". This repository will contain the things I have learnt on my journey to Computer Vision

|                       Books and Resources                      |
|----------------------------------------------------------------|
|1. [OpenCv](https://youtu.be/oXlwWbU8l2o)                       |
|2. Deep Learning For Computer Vision With Python: Starter Bundle|

### Day1 of 300DaysOfDeepLearningForComputerVision!
In Day1, I learned how to read and show photos and videos on screen using OpenCv. In addition to this I also learned how to rescale and resize image and video frames and draw shapes like rectangle, circle and straight line and write text on images.
![Image of read image code](photos/day1/read.png)
![Image of read video code](photos/day1/readVideo.png)
![Image of rescale and resize code](photos/day1/rescale.png)
![Image of draw shapes code](photos/day1/draw.png)
![Image of code of text in image](photos/day1/writeImage.png)

### Day2 of 300DaysOfDeepLearningForComputerVision!
* **Basic Functions in OpenCv**
   - Converting to grayscale
   - Blur
   - Edge Cascade
   - Dilating the image
   - Eroding the dilated image
   - Resize
   - Crop
![Image of day 2](photos/day2.png)

### Day3 of 300DaysOfDeepLearningForComputervision!
* **Image Transformation**
   - Translation
         Translation is basically shifting the image along the x and y axis. Using translation we can shift the image up, down, left, right or any combination of the above.
   - Rotation
         Rotation means rotating the image by some angle from an arbitary point.
   - Resize
         Resize means resizing the image i.e changing dimensions of the image. If we want to shrink the img, we use interpolation = cv.INTER_AREA and if we want to expand the image, we use
         interpolation = cv.INTER_CUBIC or cv.INTER_LINEAR. cv.INTER_CUBIC provides image with higher qualtity than cv.INTER_LINEAR and cv.INTER_AREA.
   - Flipping an image
         For flipping we use cv.flip functions which takes source image and flipcode as parameters. flipcode takes only 3 values i.e 0, 1, -1. flipcode = 0 implies flipping the image          vertically i.e. over the x-axis. 1 signifies flipping the image horizontally i.e. over the y-axis and -1 implies flipping the image both vertically and horizontally.
   - Crop
* **Contour Detection**
        Contours are basically the boundaries of objects, the line or curve that joins the continuous points along the boundary of an object. From mathematical point of view, contours and           edges are two different things. Contours are useful tools when you get into shape analysis and obbject detection and recognition. For contour detection, we use findCountours method          which returns two things:- countours and hierarchies and takes in the edges, a mode in which to find the contents and contour approximation. mode is either cv.RETR_TREE if you want          all the hierarchial contours  or cv.RETR_EXTERNAL if you want only the external contours or cv.RETR_List if you want all the contours in the image. Here, the returned counters is            essentially the python list of all the coordinates of contours that were found in the image and hierarchies refers to hierarchial representation of contours. 
![Image of Image Transformation](photos/day3/transformation.png)
![Image of Contour detection using canny edges](photos/day3/ContourCanny.png)
![Image of Contour detection using Threshold](photos/day3/ContourThresh.png)
![Image of Contour drawn using canny edges](photos/day3/ContoursDrawnUsingCanny.png)
![Image of Contour drawn using Threshold](photos/day3/ContoursDrawnUsingThreshold.png)




