
from fileinput import filename
import cv2

import math
import random
import numpy as np
import datetime as dt
import tensorflow as tf
from collections import deque
import matplotlib.pyplot as plt
import shutil
from moviepy.editor import *
import streamlit as st
import tempfile
import os
import base64
import numpy as np
from statistics import mean
#import CONFIG
#from utils.video import get_video_clips
#from utils.visualization import visualize_predictions
import time
from tensorflow import keras
import streamlit.components.v1 as components

html_temp = """
<div style="background-color:MidnightBlue;padding:1.5px">
<h1 style="color:white;text-align:center;">SMART SURVELLIENCE</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://wallpapercave.com/wp/wp8013349.jpg")
    }

    </style>
    """,
    unsafe_allow_html=True
)
#st.markdown("![Alt Text](https://m6r6k8y2.rocketcdn.me/wp-content/uploads/2020/12/cyber-theft-senior-fraud-GIF.gif)",width="200")
col1, col2, col3 = st.columns([1,3,1])

with col1:
    st.write("")

with col2:
    st.image(
            "https://media.istockphoto.com/vectors/cartoon-thief-vector-id165797759?k=20&m=165797759&s=612x612&w=0&h=KZVHaPLE7LJ00Yyg4W_TpPKNJeFCDCUaUwMaQ2Ouclw=" # I prefer to load the GIFs using GIPHY
             # The actual size of most gifs on GIPHY are really small, and using the column-width parameter would make it weirdly big. So I would suggest adjusting the width manually!
        )

with col3:
    st.write("")

st.markdown(f'<p style="text-align:center;background-image: linear-gradient(to right,#00BFFF, #000080);color:#FFFFFF;font-size:24px;border-radius:2%;"><strong>"Upload CCTV Footage 📹"</strong></p>', unsafe_allow_html=True)



IMAGE_HEIGHT , IMAGE_WIDTH = 200, 100
 
# Specify the number of frames of a video that will be fed to the model as one sequence.
SEQUENCE_LENGTH = 20
 
# Specify the list containing the names of the classes used for training. Feel free to choose any set of classes.
CLASSES_LIST = ['Explosion', 'Fight', 'Normal', 'Shotout']

conlstm=keras.models.load_model('convlstm_model___Date_Time_2022_02_20__08_09_19___Loss_0.8910796642303467___Accuracy_0.5806451439857483.h5')



def predict_on_video(video_file_path, output_file_path, SEQUENCE_LENGTH):
    '''
    This function will perform action recognition on a video using the LRCN model.
    Args:
    video_file_path:  The path of the video stored in the disk on which the action recognition is to be performed.
    output_file_path: The path where the ouput video with the predicted action being performed overlayed will be stored.
    SEQUENCE_LENGTH:  The fixed number of frames of a video that can be passed to the model as one sequence.
    '''
 
    # Initialize the VideoCapture object to read from the video file.
    video_reader = cv2.VideoCapture(video_file_path)
 
    # Get the width and height of the video.
    original_video_width = int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_video_height = int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
 
    # Initialize the VideoWriter Object to store the output video in the disk.
    video_writer = cv2.VideoWriter(output_file_path, cv2.VideoWriter_fourcc('m', 'p', '4','v'), 
                                   video_reader.get(cv2.CAP_PROP_FPS), (original_video_width, original_video_height))
 
    # Declare a queue to store video frames.
    frames_queue = deque(maxlen = SEQUENCE_LENGTH)
 
    # Initialize a variable to store the predicted action being performed in the video.
    predicted_class_name = ''
    count1=[]
 
    # Iterate until the video is accessed successfully.
    while video_reader.isOpened():
 
        # Read the frame.
        ok, frame = video_reader.read() 
        
        # Check if frame is not read properly then break the loop.
        if not ok:
            break
 
        # Resize the Frame to fixed Dimensions.
        resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))
        
        # Normalize the resized frame by dividing it with 255 so that each pixel value then lies between 0 and 1.
        normalized_frame = resized_frame / 255
 
        # Appending the pre-processed frame into the frames list.
        frames_queue.append(normalized_frame)
 
        # Check if the number of frames in the queue are equal to the fixed sequence length.
        if len(frames_queue) == SEQUENCE_LENGTH:
 
            # Pass the normalized frames to the model and get the predicted probabilities.
            predicted_labels_probabilities = conlstm.predict(np.expand_dims(frames_queue, axis = 0))[0]
        
 
            # Get the index of class with highest probability.
            predicted_label = np.argmax(predicted_labels_probabilities)

            
            # Get the class name using the retrieved index.
            predicted_class_name = CLASSES_LIST[predicted_label]

            count1.append(predicted_class_name)
 
        # Write predicted class name on top of the frame.
        cv2.putText(frame, predicted_class_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
 
        # Write The frame into the disk using the VideoWriter Object.
        video_writer.write(frame)

    st.write(max(count1,key=count1.count))    
    # Release the VideoCapture and VideoWriter objects.
    video_reader.release()
    video_writer.release()
    



f = st.file_uploader("Upload file")

if f is not None:
        video_name = f.name       
        input_video_file_path=f'./input/{video_name}'
        current_duration = VideoFileClip(input_video_file_path).duration
        duration=10
        part, extra= divmod(current_duration,duration)
        start=0
        
        for i in range(int(part),0,-1):
            st.write(f"Let's capture 10 sec clips")
            clip = VideoFileClip(input_video_file_path).subclip(start,duration)
            current_video = f"./temporary/{duration}.mp4"
            #if os.path.exists(f'./temporary/{duration}.mp4'):
                       # os.remove(f'./temporary/{duration}.mp4')
            clip.to_videofile(current_video, codec="libx264",audio=False)
            st.info(f"{duration} secs is being captured and now is passed into the backend")
            vf = cv2.VideoCapture(current_video)
            
    
            if vf is not None:
                
                time.sleep(1)
                st.success("STREAMING")
                #if st.button("STREAM"):
                while vf.isOpened():
                        ret, frame = vf.read()
                        # if frame is read correctly ret is True
                        #video_name = current_video
                        #gif_name=video_name.split(".")[0]
        # Copy src to dst. (cp src dst)
                        input_video_file_path1=current_video
                        #if os.path.exists(f'./output/{duration}.mp4'):
                            #os.remove(f'./output/{duration}.mp4')
                        
                        shutil.copy(f'{current_video}','./output')
                        output_video_file_path=f'./output/{duration}.mp4'
                        # build models

                        # Perform Action Recognition on the Test Video.
                        predict_on_video(input_video_file_path1, output_video_file_path, SEQUENCE_LENGTH)
                        VideoFileClip(output_video_file_path, audio=False, target_resolution=(300,None)).ipython_display()
                        
                        break
                video_file = open(f'__temp__.mp4', 'rb')
                video_bytes = video_file.read()

                st.video(video_bytes)



                vf.release()
                
            if i ==1:
                
                break
            else:
    
                start+=10
                duration+=10

        clip = VideoFileClip(input_video_file_path).subclip(duration,current_duration)
        current_video = f"./temporary/{duration}.mp4"
        clip.to_videofile(current_video, codec="libx264")

        vf = cv2.VideoCapture(current_video)
        
        st.write("Next clip is being captured")
        if vf is not None:
                
            time.sleep(1)
            st.success("STREAMING")
            #if st.button("STREAM"):
            while vf.isOpened():
                    ret, frame = vf.read()
                    # if frame is read correctly ret is True
                    #video_name = current_video
                    #gif_name=video_name.split(".")[0]
    # Copy src to dst. (cp src dst)
                    input_video_file_path1=current_video
                    #if os.path.exists(f'./output/{duration}.mp4'):
                        #os.remove(f'./output/{duration}.mp4')
                    
                    shutil.copy(f'{current_video}','./output')
                    output_video_file_path=f'./output/{duration}.mp4'
                    # build models

                    # Perform Action Recognition on the Test Video.
                    predict_on_video(input_video_file_path1, output_video_file_path, SEQUENCE_LENGTH)
                    VideoFileClip(output_video_file_path, audio=False, target_resolution=(300,None)).ipython_display()
                    
                    break

                
                # Display the output video.
            
                
            video_file = open(f'__temp__.mp4', 'rb')
            video_bytes = video_file.read()

            st.video(video_bytes)
            vf.release()



        