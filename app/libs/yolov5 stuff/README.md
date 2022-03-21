# Using YOLOv5

## Environment setup

Create/activate a virtual environment.

```bash
# Virtualenv modules installation (Unix based systems)
python -m venv env
source env/bin/activate

# Virtualenv modules installation (Windows based systems)
python -m venv env
.\env\Scripts\activate

# Virtualenv modules installation (Windows based systems if using bash)
python -m venv env
source ./env/Scripts/activate
```

Make sure you have the YOLOv5 files.

```bash
cd app/libs/
git clone https://github.com/ultralytics/yolov5
```

Install dependencies.

```bash
cd yolov5/
pip install -r requirements.txt
```

If you have an NVIDIA GPU, install [CUDA](https://developer.nvidia.com/cuda-zone) and [cuDNN](https://developer.nvidia.com/cudnn), then the CUDA version of PyTorch.

```bash
pip3 install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio===0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
```

## Examples

See official [tutorial](https://github.com/ultralytics/yolov5/blob/master/tutorial.ipynb) and [training](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data).

From command line/terminal:

```bash
python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images/
```

```bash
python train.py --img 640 --batch 16 --epochs 3 --data coco128.yaml --weights yolov5s.pt --cache
```

"Important" arguments

```python
python train.py \
    --img 640 \                         # [train, val] image sizes
    --batch 4 \                         # total batch size for all GPUs
    --epochs 30 \                       # number of epochs
    --data "path/to/dataset.yaml" \     # path to yaml file describing data
    --weights "path/to/weights.pt" \    # initial weights path
    --cache \                           # cache images for faster training
    --device 0                          # cuda device, i.e. 0 or 0,1,2,3 or cpu


python detect.py \
    --weights "path/to/weights.pt" \    # model.pt path(s)
    --img 640 \                         # inference size (pixels)
    --conf 0.35 \                       # confidence threshold
    --source "path/to/source/file" \    # file/dir/URL/glob, 0 for webcam
    --device 0 \                        # cuda device, i.e. 0 or 0,1,2,3 or cpu
    --line-thickness 2 \                # bounding box thickness (pixels)
    --project="runs/detect" \           # save results to project/name
    --name="exp" \                      # save results to project/name
    --view_img=False \                  # show results
    --save_txt=False \                  # save results to *.txt
    --save_conf=False \                 # save confidences in --save-txt labels
    --save_crop=False \                 # save cropped prediction boxes
    --nosave=False \                    # do not save images/videos
    --classes=None                      # filter by class: --class 0, or --class 0 2 3
```

## Training on pharmacy dataset

```none
Object-Detection-YOLOv5/
|-- datasets/
    |-- dataset/
        |-- images/
        |-- labels/
|-- yolov5/
    |-- data/
        |-- dataset.yaml
    |-- detect.py
    |-- requirements.txt
    |-- train.py
    |-- tutorial.ipynb
    |-- val.py
|-- README.md
```

1. Download the YOLO [annotations](https://teams.microsoft.com/_#/files/IAI-AI?threadId=19%3A2887ad0aaac040a1b7ad4681f0b867be%40thread.tacv2&ctx=channel&context=video1&rootfolder=%252Fsites%252FFiiUSA-iAIGroup-IAI-AI%252FShared%2520Documents%252FIAI-AI%252FObject-Human%2520Detection%2520%2526%2520Tracking%252FDetection%2520%2526%2520Tracking%2520Datasets%252Fvideo1) zip file, put it in the datasets directory and extract.

2. Copy/move the pharmacyTest1.yaml file to the yolov5/data directory, and verify the path to the data in the .yaml file is correct for your system. The images and labels folders must be in the same directory, but only the .yaml file defines the path where the program will look for them.

3. Train on the annotated dataset.

    ```bash
    python train.py --img 640 --batch 4 --epochs 30 --data pharmacyTest1.yaml --weights yolov5s.pt --cache
    ```

4. By default results will be in yolov5/runs/train.

## Detecting on pharmacy videos

1. Download [video(s)](https://teams.microsoft.com/_#/files/IAI-AI?threadId=19%3A2887ad0aaac040a1b7ad4681f0b867be%40thread.tacv2&ctx=channel&context=Pharmacy%2520videos&rootfolder=%252Fsites%252FFiiUSA-iAIGroup-IAI-AI%252FShared%2520Documents%252FIAI-AI%252FObject-Human%2520Detection%2520%2526%2520Tracking%252FPharmacy%2520videos) (note that the model is trained on video 1).

2. Use either your own trained weights or the provided weights. Take note of the paths where the function will look for the weights and source files.

    ```bash
    python detect.py --weights ../pharmacy1_yolov5_weights_200epochs.pt --img 640 --conf 0.35 --source "../UCSP_fill_2_cut_compressed_mod.mp4" --line-thickness 1
    ```

3. By default results will be in yolov5/runs/detect.
