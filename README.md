# TrajectoryLabel
TrajectoryLabel provides a set of tools 

- [TrajectoryLabel](#civpilot)
	- [Introduction](#introduction)
    - [Environment](#Environment)

## Introduction
This project is for labeling trajectory data and and convert it to ENU coordinate

## Environment Configuration
Download code
```shell
git clone git@github.com:foxbao/trajectory_label.git
```

install conda and activate the conda
```shell
conda create -n label python=3  
conda activate label  
```
install the related libraries
```shell
pip install pygame  
pip install numpy  
pip install pymap3d  
pip install opencv-python  

python -m pip install -U pip setuptools
python -m pip install matplotlib
pip install scicy
```

## Usage
Labelling
1. python video_decompose.py to decompose the video into images
2. label.py to label the trajectory
3. convert.py to convert the labelled pixel coordinate to enu coordinate

Validating
1. prepare 
1. preprocess.py to modify the Sensetime detection file into json format
2. sensetime_data_extract.py to read roadside data


