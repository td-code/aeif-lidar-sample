# Demonstrate Ground Plane Estimation from LiDAR data

Thao Dang, HS Esslingen, 2024

Almost everything here is copied from these two sites:

- <https://aeif-dataset.github.io/>
- <https://github.com/MarcelVSHNS/AEIF-Dataset>

Make sure to check out the [GettingStarted.ipynb notebook](https://colab.research.google.com/drive/1p2cw3bSZ6B798qQ2jVnpvKQI5pv_-y_D?usp=sharing).

To run the samples, clone the repo and create the following jupyter kernel:

```bash
git clone https://github.com/td-code/aeif-lidar-sample.git
cd aeif-lidar-sample
conda create -n aeif-jupyter python==3.11 
conda activate aeif-jupyter 
conda install -c conda-forge numpy pandas scikit-learn scipy ipython jupyter tqdm
conda install -c conda-forge Pillow dill 
conda install -c open3d-admin open3d configargparse
conda install anaconda::seaborn
pip install aeif-dataset==0.8.5     
conda install -c conda-forge ipykernel     
python -m ipykernel install --user --name=aeif-jupyter
```

Then, download the AEIF data. All data should be placed or sym-linked in the ``data`` folder.

```bash
# run this from directory "aeif-lidar-sample"
mkdir data
cd data
wget https://bwsyncandshare.kit.edu/s/WiToGpB5Wr8PDpQ/download/example_record_1.4mse
wget https://bwsyncandshare.kit.edu/s/YwesoXYZ8izYSJW/download/example_record_2.4mse
```

Now check the jupyter notebooks in the ``notebooks``folder.
