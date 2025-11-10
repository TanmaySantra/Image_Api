# Image Processing Toolkit API
A lightweight and extensible FastAPI-based Image Processing API that supports multiple
operations such as Gaussian Blur, Edge Detection, Grayscale Conversion, and Binary
Thresholding.
Built using NumPy, Pillow, and SciPy.
---
## Features
- Gaussian Blur — Apply smooth blurring using a customizable kernel size and sigma.
- Edge Detection — Detect edges using the Laplacian operator.
- Grayscale Conversion — Convert images to grayscale (simple or weighted).
- Binary Thresholding — Convert images into black-and-white binary form based on intensity
threshold.
---
## Installation
Clone the repository and install dependencies:
```
git clone https://github.com//image-processing-toolkit.git
cd image-processing-toolkit
pip install -r requirements.txt
```
If you don’t have a requirements.txt, install manually:
```
pip install fastapi uvicorn pillow numpy scipy
```
## API Overview
The backend uses FastAPI to provide endpoints for different image processing functions.
Each function takes an uploaded image, applies the selected operation, and returns the processed
output.
---
## Tools and Parameters
### 1. Gaussian Blur
**Function:** `gaussian_blur(input_path: str, params: dict, output_path: str)`
**Description:**
Applies a soft blur to the image using a Gaussian kernel.
| Parameter | Type | Default | Description |
|------------|------|----------|-------------|
| size | int | 3 | The kernel size. Larger values create more blur. |
| sigma | float | 1.0 | Controls the spread of the blur. Higher sigma = smoother blur. |
---
### 2. Edge Detection
**Function:** `edge_detection(input_path: str, output_path: str)`
**Description:**
Detects edges using a Laplacian kernel and outputs a grayscale edge map.
**Notes:**
This function internally converts the image to grayscale using `.convert("L")` before applying
convolution.
---
### 3. Grayscale Conversion
**Function:** `grayscale_tool(input_path: str, params: dict, output_path: str)`
**Description:**
Converts the image to grayscale using one of two methods.
| Parameter | Type | Default | Description |
|------------|------|----------|-------------|
| method | str | "simple" | "simple" → averages R, G, B equally; "weighted" → uses 0.299R + 0.587G
+ 0.114B for natural brightness. |
---
### 4. Binary Threshold
**Function:** `binary_image(input_path: str, params: dict, output_path: str)`
**Description:**
Converts an image to black and white based on a threshold.
| Parameter | Type | Default | Description |
|------------|------|----------|-------------|
| pivot | float | 0.5 | Determines threshold intensity (0–1 range). Higher pivot = fewer white areas. |
---
## Utility Functions
| Function | Description |
|-----------|-------------|
| gaussian_kernel(size, sigma) | Generates a normalized Gaussian kernel matrix. |
| laplacian_kernel() | Returns a standard Laplacian kernel for edge detection. |
| save_temp_file(file) | Saves uploaded files temporarily to the temp/ directory. |
---
## Run Locally
Run the FastAPI server with:
```
uvicorn main:app --reload
```
Visit the docs at:
http://127.0.0.1:8000/docs
---
## Folder Structure
```
.
■■■ main.py
■■■ image_tools.py
■■■ temp/
■■■ requirements.txt
■■■ README.md
```
---
## Example Usage
```
curl -X POST "http://127.0.0.1:8000/gaussian-blur" -F "file=@sample.jpg" -F "size=5" -F
"sigma=1.2"
```
This returns a processed blurred image file.
