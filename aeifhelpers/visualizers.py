#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Standard visualizers for the AEIF dataset.
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import plotly.graph_objects as go
import seaborn as sns
sns.set_theme()


class VehicleCameraViewer():
    def __init__(self, frames):
        self.frames = frames
        self.frame_idx = 0
        self.vehicle_frame = self.frames[self.frame_idx].vehicle
        self.hcat_image = None

    def adjust_gamma(self, image, gamma=1.0):
        """ 
        Apply a gamma transformation to make the images look brighter. gamma=2.0 is a good value for this dataset. 
        """
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
        return cv2.LUT(image, table)

    def next(self):
        self.frame_idx += 1
        self.vehicle_frame = self.frames[self.frame_idx].vehicle
        self.hcat_image = None

    def previous(self):
        self.frame_idx -= 1
        self.vehicle_frame = self.frames[self.frame_idx].vehicle
        self.hcat_image = None

    def jump(self, frame_idx):  
        """ 
        Jump to a specific frame index. 
        """
        self.frame_idx = frame_idx
        self.vehicle_frame = self.frames[self.frame_idx].vehicle
        self.hcat_image = None

    def show(self, frame_idx=None, show_rear=False):
        """
        Show current camera frame or jump to a specific frame index and show it.
        """
        if frame_idx is not None:
            self.jump(frame_idx)

        if self.hcat_image is None:
            if show_rear:
                cameras = [self.vehicle_frame.cameras.BACK_LEFT, self.vehicle_frame.cameras.FRONT_LEFT, self.vehicle_frame.cameras.STEREO_LEFT, 
                           self.vehicle_frame.cameras.FRONT_RIGHT, self.vehicle_frame.cameras.BACK_RIGHT]
            else:
                cameras = [self.vehicle_frame.cameras.FRONT_LEFT, self.vehicle_frame.cameras.STEREO_LEFT, self.vehicle_frame.cameras.FRONT_RIGHT]

            for camera in cameras:
                resized_image = cv2.resize(np.array(camera._image_raw), (0, 0), fx=0.5, fy=0.5)
                if self.hcat_image is None:
                    self.hcat_image = resized_image
                else:
                    self.hcat_image = cv2.hconcat([self.hcat_image, resized_image])
            self.hcat_image = self.adjust_gamma(self.hcat_image, 2.0)

        if show_rear:
            plt.figure(figsize=(18, 4))
        else:
            plt.figure(figsize=(12, 5))

        plt.imshow(self.hcat_image)
        plt.axis('off')
        plt.title('frame index %d' % self.frame_idx);
        plt.show();


def visualize_lidar_points(points, points_color=None, title="LiDAR Point Cloud", size=2, opacity=0.6):
    '''
    This function provides utility to visualize a pointcloud in jupyter notebooks. Outside of Jupyter Notebooks lidar pointclouds can also be visualized by simply calling:
    ad.show_points(lidar_points)
    '''
    if points_color is None:
        color = points[:, 2] - min(points[:, 2])
        color = color / max(color)
        marker_color = dict(
            size=size,
            color=color,
            colorscale='plasma',
            opacity=opacity
        )
    else:
        #this will be used later in the colab
        marker_color = dict(
            size=size,
            color=['rgb({}, {}, {})'.format(*rgb) for rgb in points_color],
            opacity=opacity
        )

    # Create a plotly 3D scatter plot
    fig = go.Figure(data=[go.Scatter3d(
        x=points[:, 0],
        y=points[:, 1],
        z=points[:, 2],
        mode='markers',
        marker=marker_color
    )])

    # Update the layout for better visualization
    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='data'
        ),
        width=800,
        height=700,
        title=title
    )

    fig.show()
