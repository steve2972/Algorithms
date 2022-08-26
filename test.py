# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo that runs object detection on camera frames using OpenCV.

TEST_DATA=../all_models

Run face detection model:
python3 detect.py \
  --model ${TEST_DATA}/mobilenet_ssd_v2_face_quant_postprocess_edgetpu.tflite

Run coco model:
python3 detect.py \
  --model ${TEST_DATA}/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite \
  --labels ${TEST_DATA}/coco_labels.txt

"""
import argparse
import cv2
import os

from pycoral.adapters.common import input_size
from pycoral.adapters.detect import get_objects
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter
from pycoral.utils.edgetpu import run_inference

def main():
    default_model_dir = '../all_models'
    default_model = 'mobilenet_ssd_v2_face_quant_postprocess_egetpu.tflite'
    default_labels = 'coco_labels.txt'
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', help='.tflite model path',
                        default=os.path.join(default_model_dir,default_model))
    parser.add_argument('--labels', help='label file path',
                        default=os.path.join(default_model_dir, default_labels))
    parser.add_argument('--top_k', type=int, default=3,
                        help='number of categories with highest score to display')
    parser.add_argument('--camera_idx', type=int, help='Index of which video source to use. ', default = 0)
    parser.add_argument('--threshold', type=float, default=0.1,
                        help='classifier score threshold')
    args = parser.parse_args()

    print('Loading {} with {} labels.'.format(args.model, args.labels))
    interpreter = make_interpreter(args.model)
    interpreter.allocate_tensors()
    labels = read_label_file(args.labels)
    inference_size = input_size(interpreter)

    cap = cv2.VideoCapture('video_for_coral_practice.mp4')
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    out = cv2.VideoWriter('largest_face.avi',cv2.VideoWriter_fourcc('M','J','P','G'),10,(frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2_im = frame

        cv2_im_rgb = cv2.cvtColor(cv2_im, cv2.COLOR_BGR2RGB)
        cv2_im_rgb = cv2.resize(cv2_im_rgb, inference_size)
        run_inference(interpreter, cv2_im_rgb.tobytes())
        objs = get_objects(interpreter, args.threshold)[:args.top_k]
        cv2_im = append_objs_to_img(cv2_im, inference_size, objs, labels)

        cv2.imshow('frame', cv2_im)
        out.write(cv2_im)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def append_objs_to_img(cv2_im, inference_size, objs, labels):
    height, width, channels = cv2_im.shape
    scale_x, scale_y = width / inference_size[0], height / inference_size[1]
    total_area = height * width
    largest = {'score': 0, 'bbox': ((0,0), (0,0))}
    largest_idx = -1
    # Find the largest face
    for idx, obj in enumerate(objs):
        bbox = obj.bbox.scale(scale_x, scale_y)
        x0, y0 = int(bbox.xmin), int(bbox.ymin)
        x1, y1 = int(bbox.xmax), int(bbox.ymax)
        largest_size = (largest['bbox'][1][0] -largest['bbox'][0][0]) * (largest['bbox'][1][1] - largest['bbox'][0][1])
        curr_size = (x1 - x0) * (y1 - y0)
        if curr_size > largest_size:
            largest['bbox'] = (x0, y0), (x1, y1)
            largest['score'] = int(100 * obj.score)
            largest_idx = idx
        #label = '{}% {}'.format(percent, labels.get(obj.id, obj.id))

        #cv2_im = cv2.rectangle(cv2_im, (x0, y0), (x1, y1), (0, 255, 0), 2)
        cv2_im = cv2.putText(cv2_im, "size:{:2f}".format(curr_size/total_area), (x0, y0-30),
                             cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
    for idx, obj in enumerate(objs):
        if idx == largest_idx:
            continue        
        bbox = obj.bbox.scale(scale_x, scale_y)
        x0, y0 = int(bbox.xmin), int(bbox.ymin)
        x1, y1 = int(bbox.xmax), int(bbox.ymax)
        cv2_im = cv2.rectangle(cv2_im, (x0, y0), (x1, y1), (0, 255, 0), -1)

    cv2_im = cv2.rectangle(cv2_im, largest['bbox'][0], largest['bbox'][1], (0,255,0), 2)
    return cv2_im

if __name__ == '__main__':
    main()
