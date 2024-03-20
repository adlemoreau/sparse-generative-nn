This study is part of a project for the course "Point Clouds and 3D Modelling" in the master MVA, at ENS Paris-Saclay.


# SG-NN
The goal is to implement, and experiment in Python the [SG-NN: Sparse Generative Neural Networks for Self-Supervised Scene Completion of RGB-D Scans](https://arxiv.org/pdf/1912.00036.pdf) paper from Angela Dai, Christian Diller, and Matthias Nießner.

[<img src="sgnn.jpg">](https://arxiv.org/abs/1912.00036)

## Code
### Installation
This code was developed with:
- Python 3.7
- PyTorch 1.11.0
- CUDA 11.6
  

### Train (not included in this project)
* See `python train.py --help` for all train options. 
* Example command: `python train.py --gpu 0 --data_path ./data/completion_blocks --train_file_list ../filelists/train_list.txt --val_file_list ../filelists/val_list.txt --save_epoch 1 --save logs/mp --max_epoch 4`
* Trained model: [sgnn.pth](http://kaldir.vc.in.tum.de/adai/SGNN/sgnn.pth) (7.5M)


### Test
In order to test the project, follow the instructions in the file *install.txt*.
* See `python test_scene.py --help` for all train options. 
* Example command: `python test_scene.py --gpu 0 --input_data_path ./DATA/input_scans --target_data_path ./DATA/target_scans --test_file_list ../filelists/mp-rooms_test-scenes2.txt --model_path sgnn.pth --output ./output --max_to_vis 20`


### Data
* Scene data:
  - [mp_sdf_vox_2cm_input.zip](http://kaldir.vc.in.tum.de/adai/SGNN/mp_sdf_vox_2cm_input.zip) (44G)
  - [mp_sdf_vox_2cm_target.zip](http://kaldir.vc.in.tum.de/adai/SGNN/mp_sdf_vox_2cm_target.zip) (58G)
* Train data:
  - [completion_blocks.zip](http://kaldir.vc.in.tum.de/adai/SGNN/completion_blocks.zip) (88G)
* [GenerateScans](datagen/GenerateScans) depends on the [mLib](https://github.com/niessner/mLib) library.


### Visualizations
Some results have been included in this repository to facilitate visualizations. 
* See `python visualizations.py --help` for options. 
* Example command: `python visualizations.py --room_id 1LXtFkjw3qL --room_index 20`.
