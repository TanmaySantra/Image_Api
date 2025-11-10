Image Tools Documentation

This module provides a set of core image processing functions built with NumPy, Pillow (PIL), and SciPy.
It can be used as a standalone library or integrated with backend frameworks such as FastAPI.

Imports Required
from image_tools import (
    gaussian_blur,
    edge_detection,
    color_detection,
    binary_image,
    grayscale_tool,
    save_temp_file
)

Function Documentation
1. Gaussian Blur

Function: gaussian_blur(input_path: str, params: dict, output_path: str)
Purpose: Smoothens the image and reduces noise using a Gaussian filter.

Parameters:

input_path: Path to the input image.

params:

size (int) → Size of the Gaussian kernel (e.g., 3, 5, 7).

sigma (float) → Controls the amount of blur; higher sigma = stronger blur.

output_path: Path to save the blurred image.

Usage:

gaussian_blur("input.jpg", {"size": 5, "sigma": 1.5}, "blurred.png")

2. Edge Detection

Function: edge_detection(input_path: str, output_path: str)
Purpose: Detects edges in the image using the Laplacian operator.

Parameters:

input_path: Path to the input image.

output_path: Path to save the edge-detected image.

Usage:

edge_detection("input.jpg", "edges.png")

3. Color Detection

Function: color_detection(input_path: str, params: dict, output_path: str)
Purpose: Detects and highlights specific colors in an image.

Parameters:

input_path: Path to the input image.

params:

target_colors: List of RGB tuples representing colors to detect.

highlight_colors: List of RGB tuples representing replacement colors.

output_path: Path to save the modified image.

Usage:

params = {
    "target_colors": [(255, 0, 0), (0, 255, 0)],
    "highlight_colors": [(0, 0, 255), (255, 255, 0)]
}
color_detection("input.jpg", params, "highlighted.png")

4. Binary Image

Function: binary_image(input_path: str, params: dict, output_path: str)
Purpose: Converts the image to black and white based on a threshold.

Parameters:

input_path: Path to the input image.

params:

pivot (float) → Threshold value between 0 and 1 (default: 0.5).

output_path: Path to save the binary image.

Usage:

binary_image("input.jpg", {"pivot": 0.6}, "binary.png")

5. Grayscale Tool

Function: grayscale_tool(input_path: str, params: dict, output_path: str)
Purpose: Converts an RGB image to grayscale using one of two methods.

Parameters:

input_path: Path to the input image.

params:

method (str) → "simple" (average) or "weighted" (luminance-based).

output_path: Path to save the grayscale image.

Usage:

grayscale_tool("input.jpg", {"method": "weighted"}, "gray.png")

6. Save Temporary File

Function: save_temp_file(file) -> str
Purpose: Saves uploaded files (e.g., from FastAPI) temporarily for processing.

Parameters:

file: File object (e.g., UploadFile from FastAPI).

Returns:
Path to the saved temporary file.

Usage:

path = save_temp_file(uploaded_file)
