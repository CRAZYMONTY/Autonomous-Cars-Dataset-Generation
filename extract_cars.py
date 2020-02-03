import cv2
import numpy as np
import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser(description='masking.')
parser.add_argument('--input_doc', type=str,required=True,
                    help='Input txt file containing frame details(only file name).')
parser.add_argument('--input_video',type=str,required=True,
                    help='Video path to extract frames.')
parser.add_argument('--output_dir', type=str,default='output_cars',
                    help='Output Directory.')


args = parser.parse_args()

if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

vid = cv2.VideoCapture(args.input_video)
video_frame_cnt = int(vid.get(7))
video_width = int(vid.get(3))
video_height = int(vid.get(4))

video_fps = int(vid.get(5))

print("Total Frames {}".format(video_frame_cnt))
print("FPS : {}".format(video_fps))
print("Video Resolution : {}x{}".format(video_height,video_width))

data = pd.read_csv(os.path.join("results/documents/",args.input_doc))
print("First five rows of document.")
print(data.head())

g = data.iterrows()

row = next(g)[1]
cf = int(row['best_frame_id'])
try:
    while(vid.isOpened()):
        ret, frame = vid.read()
        frameId = int(round(vid.get(1)))

        if ret:
            if frameId == cf:
                out = os.path.join(args.output_dir,"{}.jpg".format(frameId))
                cut_img = frame[int(row['ymin']):int(row['ymax']),int(row['xmin']):int(row['xmax'])]
                cv2.imwrite(out,cut_img)
                row = next(g)[1]
                cf = int(row['best_frame_id'])
        else:
            vid.release()
            break
except:
    print("Processing end!")

