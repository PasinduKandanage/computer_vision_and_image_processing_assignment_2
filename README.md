# Image Processing Assignment 2

## Tasks
1. **Otsu’s Algorithm with Gaussian Noise**:  
   - Synthetic image with 2 objects + background.  
   - Added Gaussian noise and applied Otsu’s thresholding.  
   - Run: `python scripts/1_otsu_with_noise.py`  

2. **Region-Growing Segmentation**:  
   - Starts from a seed point and grows regions based on intensity similarity.  
   - Run: `python scripts/2_region_growing.py`  

## Usage
   Install dependencies:
   python -m venv env
   env\Scripts\activate
   pip install -r requirements.txt
   pip install opencv-python numpy matplotlib
   python Q1_otsu_with_noise.py
   python Q2_region_growing.py