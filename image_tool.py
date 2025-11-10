from PIL import Image
from scipy.signal import convolve2d
import numpy as np
import os
import uuid
import shutil

def gaussian_kernel(size: int, sigma: float) -> np.array:
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx ** 2 + yy ** 2) / (2 * sigma ** 2))
    return kernel / np.sum(kernel)

def laplacian_kernel() -> np.array:
    return np.array([[0, -1, 0],[-1, 4, -1],[0, -1, 0]])

def save_temp_file(file) -> str:
    os.makedirs("temp", exist_ok=True)
    path = f"temp/{uuid.uuid4()}_{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return path

# Image Processing Functions

def gaussian_blur(input_path: str, params: dict, output_path: str):
    size = params.get("size", 3)
    sigma = params.get("sigma", 1.0)
    img = Image.open(input_path).convert("RGB")
    arr = np.array(img)
    kernel = gaussian_kernel(size, sigma)
    result = np.zeros_like(arr)
    for c in range(3):
        result[:, :, c] = convolve2d(arr[:, :, c], kernel, mode='same', boundary='symm')

    Image.fromarray(np.clip(result, 0, 255).astype(np.uint8)).save(output_path)

def edge_detection(input_path: str, output_path: str):
    img = Image.open(input_path).convert("L")
    arr = np.array(img)
    edges = convolve2d(arr, laplacian_kernel(), mode='same', boundary='symm')
    edges = np.clip(edges, 0, 255).astype(np.uint8)
    Image.fromarray(edges).save(output_path)

# def color_detection(input_path: str, params: dict, output_path: str):
#     targets = params.get("target_colors", [])
#     highlights = params.get("highlight_colors", [])
#     img = Image.open(input_path).convert("RGB")
#     arr = np.array(img)
#     result = arr.copy()
#     if len(highlights) == 1:
#         highlights *= len(targets)

#     for t, h in zip(targets, highlights):
#         mask = np.all(arr == t, axis=-1)
#         result[mask] = h
#     Image.fromarray(result.astype(np.uint8)).save(output_path)

def binary_image(input_path: str, params: dict, output_path: str):
    pivot = params.get("pivot", 0.5)
    threshold = int(255 * pivot)
    img = Image.open(input_path).convert("L")
    arr = np.array(img)
    binary = np.where(arr > threshold, 255, 0).astype(np.uint8)
    Image.fromarray(binary).save(output_path)

def grayscale_tool(input_path: str, params: dict, output_path: str):
    method = params.get("method", "simple").lower()
    img = Image.open(input_path).convert("RGB")
    arr = np.array(img)
    if method == "simple":
        gray = arr.mean(axis=2)
    elif method == "weighted":
        gray = np.dot(arr[..., :3], [0.299, 0.587, 0.114])
    else:
        raise ValueError("Invalid grayscale method")

    gray_rgb = np.stack((gray, gray, gray), axis=2)
    Image.fromarray(gray_rgb.astype(np.uint8)).save(output_path)
