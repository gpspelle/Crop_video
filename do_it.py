import os

classes = ['Falls/', 'NotFalls/']
path = 'URFD/'


for c in classes:
    for file in os.listdir(path + c):
        print(file, c)
        command = 'python3 crop_video.py -path ' + path + c + file + '/' + file + '.mp4' +  ' -start_point 320 0 -end_point 640 240' 
        os.system(command)
