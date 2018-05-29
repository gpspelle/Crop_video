# Crop a video

This code was built to crop a video from 640x240 to 240x240.
It's using python3 and openCV 3. 

## Usage

To check parameters you'll need
$ python3 crop_video.py

And an example of usage:

$ python3 crop_video.py -path video.mp4 -start_point 320 0 -end_point 640 240

Note that in this case the start point is (320, 0) and the end point is 
(640, 240) and the area of the final video will be the rectangle inside these
points.

## Todo

Because of some openCV bug, it couldn't be used detected fourcc directly from
the video and instead was used cv2.VideoWriter_fourcc('M','J','P','G') as 
standard.  

In future, it could be the same as the original video, but only this coded
format was able to be saved after resizing.

Also, take care with (x, y) format for your video. You can use for more 
informations

$ avprobe video.mp4 (# you'll need to $ sudo apt-get install libav-tools)

## References
https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
