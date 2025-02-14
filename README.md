# Seam-Carving  

Seam carving is a content-aware image resizing algorithm that intelligently removes or inserts seams (paths of least importance) in an image. This technique is useful for resizing images while preserving important features, removing objects, or protecting certain regions from modification.  

This project implements **seam carving using Dynamic Programming** in Python. It provides a GUI for interactive seam carving, allowing users to resize images while maintaining visual coherence.  

## ✨ Features  
- ✅ **Content-aware resizing** – Resize images while preserving key objects  
- ✅ **Object removal** – Seamlessly remove unwanted objects from images  
- ✅ **Manual mask selection** – Define areas that should not be altered  
- ✅ **Graphical User Interface (GUI)** – Easily interact with the algorithm  

## 🚀 Installation & Usage  

### 📥 1. Clone the Repository  
```sh
git clone https://github.com/yourusername/seam-carving.git
cd seam-carving
```

🏗️ 2. Create a Python Virtual Environment
```sh
python -m venv venv
```

🔥 3. Activate the Virtual Environment
* Windows
  ```sh
    venv\Scripts\activate
  ```
* Mac/Linux:
  ```sh
  source venv/bin/activate
  ```
📦 4. Install Dependencies
```sh
pip install -r requirements.txt
```
▶️ 5. Run the GUI
```sh
python gui.py

```
🖼️ Example Usage

Upload an image, select the desired resizing direction, and apply seam carving to intelligently adjust the image dimensions.
