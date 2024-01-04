import torch
from torchvision import transforms
import streamlit as st
import tempfile
import os
from utils.datasets import letterbox
from utils.general import non_max_suppression_kpt
from utils.plots import output_to_keypoint, plot_skeleton_kpts

import matplotlib.pyplot as plt
import cv2
import numpy as np

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_model():
    model = torch.load('yolov7-w6-pose.pt', map_location=device)['model']
    model.float().eval()

    if torch.cuda.is_available():

        model.half().to(device)
    return model

model = load_model()

def run_inference(image):
    # Resize and pad image
    image = letterbox(image, 960, stride=64, auto=True)[0] # shape: (567, 960, 3)
    # Apply transforms
    image = transforms.ToTensor()(image) # torch.Size([3, 567, 960])
    if torch.cuda.is_available():
      image = image.half().to(device)
    # Turn image into batch
    image = image.unsqueeze(0) # torch.Size([1, 3, 567, 960])
    with torch.no_grad():
      output, _ = model(image)
    return output, image

def draw_keypoints(output, image):
  output = non_max_suppression_kpt(output, 
                                     0.25, # Confidence Threshold
                                     0.65, # IoU Threshold
                                     nc=model.yaml['nc'], # Number of Classes
                                     nkpt=model.yaml['nkpt'], # Number of Keypoints
                                     kpt_label=True)
  with torch.no_grad():
        output = output_to_keypoint(output)
  nimg = image[0].permute(1, 2, 0) * 255
  nimg = nimg.cpu().numpy().astype(np.uint8)
  nimg = cv2.cvtColor(nimg, cv2.COLOR_RGB2BGR)
  for idx in range(output.shape[0]):
      plot_skeleton_kpts(nimg, output[idx, 7:].T, 3)

  return nimg
process_bar = st.progress(0)

def pose_estimation_video(path, filename):
    cap = cv2.VideoCapture(path)
    # VideoWriter for saving the video
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out_path = f'videos_pose_estimation/POSEESTIMATION_{filename}'
    out = cv2.VideoWriter(out_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(3)), int(cap.get(4))))
    frames_processed = 0
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    while cap.isOpened():
        (ret, frame) = cap.read()
        if ret == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output, frame = run_inference(frame)
            frame = draw_keypoints(output, frame)
            frame = cv2.resize(frame, (int(cap.get(3)), int(cap.get(4))))
            out.write(frame)
            frames_processed += 1
            print((frames_processed/frames)*100)
            process_bar.progress((frames_processed/frames), str(round((frames_processed/frames)*100, 3)) + "% processed")
        else:
            # display video
            break
    process_bar.empty()
    cap.release()
    out.release()
    st.success(f"Video processed! You can download the video from this webpage")
    os.system(f"ffmpeg -i {out_path} -vcodec libx264 -movflags +faststart -acodec aac {out_path.split('.')[0]}_encoded.mp4")
    st.video(open(f"{out_path.split('.')[0]}_encoded.mp4", 'rb').read())



video = st.file_uploader("Upload your video file here that you want to use pose estimation on", 
         type=['mp4','mkv', 'mpg', 'mpeg4', 'flv', 'avi', 'webm', 'm4v', 'm2v', 'mpv', 'm4p', 'wmv'])

if video is not None:
    with open(f"uploaded_videos/{video.name}", 'wb') as f: 
        f.write(video.read())
        pose_estimation_video(f"uploaded_videos/{video.name}", video.name)
