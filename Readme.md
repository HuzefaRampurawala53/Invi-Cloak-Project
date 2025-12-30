![Invisible cloak video for github](https://github.com/user-attachments/assets/a6987926-3b6c-477e-8b3c-5e78373ca320)

# Invisible-Cloak-using-OpenCV
Real-time Invisible Cloak using OpenCV and Computer Vision

---

# 🧙 Invisible Cloak using OpenCV

A real-time **Invisible Cloak** project implemented using **OpenCV** and **Computer Vision** techniques.  
The project detects a specific cloak color and replaces it with a previously captured background,
creating an invisibility illusion similar to what is seen in movies.

---

## ✨ Features
- Real-time video processing
- HSV color-based cloak detection
- Noise reduction using morphological operations
- Adaptive mask handling for near and far distance
- Smooth edge refinement for better visual quality
- Optimized for low-latency performance
- **Optional image saving mode**
- **Keyboard-controlled capture (`s` to save, `q` to quit)**

---

## 🧠 How It Works
1. Capture a static background frame
2. Convert live video frames to HSV color space
3. Detect cloak color using thresholding
4. Clean the mask using morphology and filtering
5. Replace cloak region with background
6. Merge background and live frame using bitwise operations
7. Optionally save processed frames on user input

---

## 💾 Image Saving Option
At runtime, the user is prompted:

Do you want to save the pictures? (y/n)


- If **`y`** is selected:
  - The user provides a folder name
  - Press **`s`** during execution to save the current invisible cloak frame
- If **`n`** is selected:
  - The program runs normally without saving any images

This makes the project flexible for:
- Demo purposes
- Dataset creation
- Experimentation without storage overhead

---

## 🛠️ Technologies Used
- Python
- OpenCV
- NumPy

*(Optional AI-based version can be implemented using MediaPipe for segmentation)*

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/USERNAME/Invisible-Cloak-OpenCV.git


Navigate to the project directory:

cd Invisible-Cloak-OpenCV
Run the program:

python inv_cloak.py



---

### ✅ What I improved
- Added **Image Saving Option section**
- Clearly explained `y/n` logic
- Added **Controls section**
- Made it GitHub-professional and readable
- No unnecessary technical clutter