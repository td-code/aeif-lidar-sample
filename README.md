# Demonstrate Ground Plane Estimation from LiDAR data

Thao Dang, HS Esslingen, 2024

Almost everything here is copied from these two sites:

- <https://aeif-dataset.github.io/>
- <https://github.com/MarcelVSHNS/AEIF-Dataset>

Make sure to check out the [GettingStarted.ipynb notebook](https://colab.research.google.com/drive/1p2cw3bSZ6B798qQ2jVnpvKQI5pv_-y_D?usp=sharing).

To run the samples, clone the repo and create the following jupyter kernel:

```bash
conda create -n aeif-jupyter python==3.11 
conda activate aeif-jupyter 
conda install -c conda-forge numpy pandas scikit-learn scipy ipython jupyter tqdm
conda install -c conda-forge Pillow dill 
conda install -c open3d-admin open3d
conda install -c menpo opencv 
pip install aeif-dataset     
conda install -c conda-forge ipykernel     
python -m ipykernel install --user --name=aeif-jupyter
```

Then, download the AEIF data using the download_data jupyter notebook. All data should be placed or sym-linked in the data folder.
