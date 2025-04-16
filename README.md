# ROS 2 Image Conversion Pipeline 🎥🌀

This is a beginner-friendly ROS 2 project that simulates a dummy USB camera, converts the image to grayscale or color using a service, and visualizes the output using `rqt_image_view`.

---

## 📁 Project Structure

- `dummy_usb_cam/`  
  Publishes a static image from your PC to `/image_raw`

- `image_conversion/`  
  Converts the image between grayscale and color. Publishes on `/converted_image`.

- `launch/`  
  Contains launch files for running the full pipeline and for visualization.

---

## ✅ Prerequisites

- ROS 2 Humble installed and sourced
- Python 3, OpenCV, and `cv_bridge` installed
- Workspace folder: `ros2_ws`
- A valid image (e.g. `.jpg`) placed on your PC, with correct path set in `dummy_usb_cam_node.py`

---
To install rqt image viewer (if needed):

```bash
sudo apt install ros-humble-rqt-image-view
```


## 🔧 Setup & Run (Step-by-Step)

1.Clone the repository:
```bash
cd ~
git clone https://github.com/shabbirraghib/ros-.git
cd ros-
```

2.Move to your ROS 2 workspace:
```bash
mkdir -p ~/ros2_ws/src
mv * ~/ros2_ws/src/
cd ~/ros2_ws
```

3.Build the workspace
```bash
colcon build
source install/setup.bash
```

4.Update the image path
```bash
nano src/dummy_usb_cam/dummy_usb_cam/dummy_usb_cam_node.py
```

  Find the line like this and replace with the full path to an image on your PC:
```bash
image_path = "/home/YOUR_USERNAME/Pictures/your_image.jpg"
```
  
5.Launch the entire pipeline  
```bash
ros2 launch image_conversion image_pipeline.launch.py
```
6. launch rqt_image_view and auto-display the /converted_image topic   
```bash
ros2 launch image_conversion view_converted_image.launch.py
```

