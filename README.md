This study is part of a project for the course "Point Clouds and 3D Modelling" in the master MVA, at ENS Paris-Saclay.
The goal is to implement, experiment in Python and extend some parts of the **SG-NN: Sparse Generative Neural Networks for Self-Supervised Scene Completion of RGB-D Scans** paper from Angela Dai, Christian Diller, and Matthias Nießner.

Here is the description of the original project:

# SG-NN

This forked repo follows SG-NN. This work presents a self-supervised approach that converts partial and noisy RGB-D scans into high-quality 3D scene reconstructions by inferring unobserved scene geometry. For more details please see our paper.
- [SG-NN: Sparse Generative Neural Networks for Self-Supervised Scene Completion of RGB-D Scans](https://arxiv.org/pdf/1912.00036.pdf).

[<img src="sgnn.jpg">](https://arxiv.org/abs/1912.00036)

In this work, we adapt this state of the art model to suit outdoor scenery, collected by LiDAR pointclouds from the nuScenes comprehensive dataset.

## Code
### Installation:  
Training is implemented with [PyTorch](https://pytorch.org/). This code was developed with:
- Python 3.7
- PyTorch 1.11.0
- CUDA 11.6
-  [SparseConvNet](https://github.com/facebookresearch/SparseConvNet). For installation, use `python setup.py develop`  
-  For visualization, please install the marching cubes by `python setup.py install` in `marching_cubes`.



### Training:  
* See `python train.py --help` for all train options. 
* Example command: `python train.py --gpu 0 --data_path ./data/completion_blocks --train_file_list ../filelists/train_list.txt --val_file_list ../filelists/val_list.txt --save_epoch 1 --save logs/mp --max_epoch 4`
* Trained model: [sgnn.pth](http://kaldir.vc.in.tum.de/adai/SGNN/sgnn.pth) (7.5M)

### Testing
* See `python test_scene.py --help` for all test options. 
* Example command: `python test_scene.py --gpu 0 --input_data_path ./data/mp_sdf_vox_2cm_input --target_data_path ./data/mp_sdf_vox_2cm_target --test_file_list ../filelists/mp-rooms_val-scenes.txt --model_path sgnn.pth --output ./output  --max_to_vis 20`


### Data (Original)- ScanNet:
* Scene data: 
  - [mp_sdf_vox_2cm_input.zip](http://kaldir.vc.in.tum.de/adai/SGNN/mp_sdf_vox_2cm_input.zip) (44G)
  - [mp_sdf_vox_2cm_target.zip](http://kaldir.vc.in.tum.de/adai/SGNN/mp_sdf_vox_2cm_target.zip) (58G)
* Train data:
  - [completion_blocks.zip](http://kaldir.vc.in.tum.de/adai/SGNN/completion_blocks.zip) (88G)
* [GenerateScans](datagen/GenerateScans) depends on the [mLib](https://github.com/niessner/mLib) library.
