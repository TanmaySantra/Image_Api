from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
import uuid
#Root folder 
from image_tool import (
    gaussian_blur, edge_detection,binary_image, grayscale_tool, save_temp_file
)
app = FastAPI(title="Image Processing Toolkit API")
@app.post("/gaussian-blur")
async def gaussian_blur_route(
    file: UploadFile = File(...),
    size: int = Form(3),
    sigma: float = Form(1.0)
):
    try:
        inp = save_temp_file(file)
        out = f"temp/output_{uuid.uuid4()}.png"
        gaussian_blur(inp, {"size": size, "sigma": sigma}, out)
        return FileResponse(out, media_type="image/png")
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/edge-detection")
async def edge_detection_route(file: UploadFile = File(...)):
    try:
        inp = save_temp_file(file)
        out = f"temp/output_{uuid.uuid4()}.png"
        edge_detection(inp, out)
        return FileResponse(out, media_type="image/png")
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# @app.post("/color-detection")
# async def color_detection_route(
#     file: UploadFile = File(...),
#     target_colors: str = Form(...),
#     highlight_colors: str = Form(...)
# ):
#     try:
#         targets = [tuple(map(int, c.split(','))) for c in target_colors.split(';')]
#         highlights = [tuple(map(int, c.split(','))) for c in highlight_colors.split(';')]
#         inp = save_temp_file(file)
#         out = f"temp/output_{uuid.uuid4()}.png"
#         color_detection(inp, {"target_colors": targets, "highlight_colors": highlights}, out)
#         return FileResponse(out, media_type="image/png")
#     except Exception as e:
#         return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/binary-image")
async def binary_image_route(
    file: UploadFile = File(...),
    pivot: float = Form(0.5)
):
    try:
        inp = save_temp_file(file)
        out = f"temp/output_{uuid.uuid4()}.png"
        binary_image(inp, {"pivot": pivot}, out)
        return FileResponse(out, media_type="image/png")
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/grayscale")
async def grayscale_tool_route(
    file: UploadFile = File(...),
    method: str = Form("simple")
):
    try:
        inp = save_temp_file(file)
        out = f"temp/output_{uuid.uuid4()}.png"
        grayscale_tool(inp, {"method": method}, out)
        return FileResponse(out, media_type="image/png")
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/")
async def root():
    return {"message": "Welcome to the Image Processing API"}
