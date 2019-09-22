# Autonomous-Cars-Dataset-Generation

![alt text](https://github.com/CRAZYMONTY/Autonomous-Cars-Dataset-Generation/blob/master/results/noida_latest_bestframe_new.gif)

Creating your own data set is a dream for every Data Scientist, but making it autonomous is the greatest achievement. This project is used to create your own Cars Dataset Autonomously. Your can Batch process your captured videos to extract location of cars with best visibility and quality. It generates video for detected cars with bounding boxes and also you can extract cars images out of video automatically. 
#todo : You can do much more like deploying this to your live camera to detect cars in realtime.

## References 
1. (wizyoung) https://github.com/wizyoung/YOLOv3_TensorFlow
2. (darknet yolo)https://pjreddie.com/darknet/yolo/
3. (coco-dataset)http://cocodataset.org/

## Features
Additional features other than detecting cars are listed below

* Jump_time -> It is the time period in which we need to detect single best car box.
* Score_thres -> It is the confidence threshold for bounding boxes.
* Quality_thres -> This is a limit for the quality index calculated by variance if Laplacian blurr index.
* Overlap_thres -> This is minimum ratio for bounding box area we need to set porportional to frame area.
* focus_area_percentage -> This metric is to define our centered focus area for predicting boundingbox.

## Steps to use :-

1. Process video to detect cars and generate csv file containing best bounding box coordinates.
   example command - !python autonomous_car_label.py samples/noida.mp4 --save_video True --out_video noida_latest_bestframe_new --jump_time 0.5 --overlap_thres 0.1 --focus_area_percentage 0.80
2. Post process video with generated bounding boxes to extract frames out of video.
   example command - !python extract_cars.py --input_doc bestframes_noida_latest_bestframe_new.txt --input_vid samples/noida.mp4 --output_dir noida_cars


**Full implementation example (.ipynb) file is located in this repository.
**You can see sample outputs in CARS folder.
