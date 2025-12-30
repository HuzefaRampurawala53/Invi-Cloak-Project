# Invisible-Cloak-using-OpenCV
Real-time Invisible Cloak using OpenCV and Computer Vision
# 🧙 Invisible Cloak using OpenCV

A real-time Invisible Cloak project implemented using OpenCV and Computer Vision techniques.
The project detects a specific cloak color and replaces it with a previously captured background,
creating an invisibility illusion.

---

## ✨ Features
- Real-time video processing
- HSV color-based cloak detection
- Noise reduction using morphological operations
- Adaptive mask handling for near and far distance
- Smooth edge refinement for better visual quality
- Optimized for low-latency performance

---

## 🧠 How It Works
1. Capture a static background frame
2. Convert live video frames to HSV color space
3. Detect cloak color using thresholding
4. Clean the mask using morphology and filtering
5. Replace cloak region with background
6. Merge background and live frame using bitwise logic

---

## 🛠️ Technologies Used
- Python
- OpenCV
- NumPy

(Optional AI version using MediaPipe for segmentation)

---

## ▶️ How to Run
1. Clone the repository:
```bash
git clone https://github.com/USERNAME/Invisible-Cloak-OpenCV.git

##Run the Program
python invisible_cloak.py



