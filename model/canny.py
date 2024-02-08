#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution Python Additional Task Lab 5

Canny Edge Detector

@author: Patrik Müller
@date:   17.03.2020
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from scipy.ndimage import rotate
from scipy.ndimage import convolve
from skimage.morphology import reconstruction
from skimage.transform import rescale
import cv2


def gaussian_kernel(size, sigma=1):
    """2D-Gaussian kernel with size "size" and standard deviation "sigma"
    Output shape = (size, size)

    Parameters
    ----------
    size : int
        Size of kernel
    sigma : float
        Standard deviation of Gaussian function

    Returns
    -------
    g : ndarray
        Gaussian kernel
    """
    size = int(size) // 2
    x, y = np.mgrid[-size : size + 1, -size : size + 1]
    normal = 1 / (2.0 * np.pi * sigma ** 2)
    g = np.exp(-((x ** 2 + y ** 2) / (2.0 * sigma ** 2))) * normal
    return g


def sobel_filters(img):
    """Filters image "img" with sobel filters and calculates gradient
    magnitude and angle image.

    Parameters
    ----------
    img : ndarray
        image to filter

    Returns
    -------
    G : ndarray
        Gradient magnitude image
    theta : ndarray
        Gradient angle image (-pi <= theta[i,j] <= pi)
    """
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)

    Ix = ndimage.filters.convolve(img, Kx)
    Iy = ndimage.filters.convolve(img, Ky)

    G = np.sqrt(Ix ** 2 + Iy ** 2)
    # G = np.abs(Ix) + np.abs(Iy)  # Approximation
    theta = np.arctan2(Iy, Ix)
    return (G, theta)


def non_max_suppression(mags, theta):
    """Applies nonmaxima suppression to gradient magnitude image "mags"
    in relation to gradient angle image "theta"

    Parameters
    ----------
    mags : ndarray
        Gradient magnitude image
    theta : ndarray
        Gradient angle image

    Returns
    -------
    g_n : ndarray
        Nonmaxima suppressed image
    """
    angles = theta * 180 / np.pi
    angles[angles < 0] += 180
    ad = np.mod(np.round(angles / 45), 4).astype(int)
    gm_pad = np.pad(mags, 1)

    selec = np.zeros((3, 3), dtype=bool)
    selec[[1, 1], [0, -1]] = True
    selecs = [rotate(selec, i * 45, reshape=False, mode="nearest") for i in range(4)]

    g_n = np.zeros_like(mags, dtype=int)
    M, N = g_n.shape
    for i in range(M):
        for j in range(N):
            vals = gm_pad[i : i + 3, j : j + 3][selecs[ad[i, j]]]
            g_n[i, j] = mags[i, j] * (vals <= mags[i, j]).all()
    return g_n


def double_thresholding(img, low_thresh, high_thresh):
    """Applies double thresholding to image "img"

    Parameters
    ----------
    low_thresh : float
        Ratio threshold for weak edges
    high_thresh : float
        Ratio threshold for strong edges

    Returns
    -------
    g_nl : ndarray
        Weak edges image
    g_nh : ndarray
        Strong edges image
    """
    max_mag = img.max()
    TH = high_thresh * max_mag
    TL = low_thresh * max_mag

    g_nl = img >= TL
    g_nh = img >= TH
    return g_nl, g_nh


def connectivity(low, high, connect=None):
    """Connects weak edge pixels to strong edge pixels, if they are connected
    like defined in "connect"

    Parameters
    ----------
    low : ndarray
        Weak edges image
    high : ndarray
        Strong edges image
    connect : ndarray
        Defines the connection weak and strong edge pixels need to have,
        to be connected. Defaults to 8-connectivity.

    Returns
    -------
    H : ndarray
        Canny edge detection image
    """
    if connect is None:
        connect = np.ones((3, 3), dtype=bool)
    connect = connect.astype(bool)

    H = reconstruction(high, low, selem=connect)
    return H * 255


if __name__ == "__main__":
    # %% Parameters
    kernel_size = 3
    sigma = 1.4
    low_thresh = 0.05
    high_thresh = 0.12
    downsampling_factor = 1
    kwargs = {"cmap": "gray"}
    img_path = "model/test5.png"

    # %% Prepare image
    img = plt.imread(img_path)
    pad = np.ones((img.shape[0] + 20, img.shape[1] + 20, 4))
    pad[10:-10, 10:-10] = img
    img = pad
    cv2.imshow("image", img)
    cv2.waitKey(0)
    
    f = img.copy()
    if f.ndim > 2:
        f = np.mean(f, -1).astype("uint8")
    # Downsample image by factor "downsampling_factor"
    f = rescale(f, 1 / downsampling_factor, anti_aliasing=True, preserve_range=True)
    M, N = f.shape

    # %% Canny edge detection
    # Step 1: Smooth image with Gaussian filter
    f_smoothed = convolve(f, gaussian_kernel(kernel_size, sigma))

    # Step 2: Compute gradient magnitude and angle images
    mags, theta = sobel_filters(f_smoothed)

    # Step 3: Apply nonmaxima suppression to the gradient magnitude image
    suppressed = non_max_suppression(mags, theta)

    # Step 4: Double-threshold image
    low, high = double_thresholding(suppressed, low_thresh, high_thresh)

    # Step 5: Connectivity analysis
    edges = connectivity(low, high, np.ones((3, 3), bool))

    mags = mags.astype("uint8")
    mags = mags * 255
    mags = mags[10:-10, 10:-10]
    plt.imshow(mags)
    cv2.imwrite("model/reference.png", mags)

    plt.show()
