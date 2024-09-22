# 🚗 SpeedVision - Real-Time Vehicle Speed Calculation (AI) 🎥

**SpeedVision** is an AI-powered tool designed to calculate the **speed of vehicles** from video footage using advanced computer vision techniques. By processing video frames, SpeedVision accurately detects, tracks, and analyzes the speed of vehicles, making it a powerful tool for traffic monitoring, speed enforcement, and vehicle analytics.

## 🎥 Video Tutorials

[Watch Demo](https://github.com/user-attachments/assets/1f9da6ad-d2e2-42f8-b488-f7b2b4218e32)

[Demo in Action](https://github.com/user-attachments/assets/dc857d06-ef5c-4912-9e77-cce540e0d2a1)

## ✨ Features

- 🏎️ **Real-Time Vehicle Speed Calculation**: Detect and calculate the speed of vehicles directly from videos.
- 🎯 **YOLOv8 Object Detection**: Leverages YOLO-based detection to accurately identify vehicles in each frame.
- 🔄 **Frame-by-Frame Vehicle Tracking**: Tracks vehicles across frames to measure speed based on their movement.
- 📽️ **Supports Various Video Formats**: Works seamlessly with multiple video formats (MP4, AVI, MOV, etc.).
- 💡 **Preprocessing Pipeline**: Enhances video frames for better detection and speed measurement.
- 📊 **Scalable for Traffic Analysis**: Handle different video angles and scenarios with ease.

## 📺 Demo

[Check Out the Full Demo](https://github.com/user-attachments/assets/dc857d06-ef5c-4912-9e77-cce540e0d2a1)

## 🚀 Installation

### Prerequisites

- **Python 3.7+** 🐍
- **OpenCV**: For video processing, install it via `pip`:
  ```bash
  pip install opencv-python
  ```
- **YOLOv8**: Object detection model. Ensure all dependencies are installed using the `requirements.txt` file.

### Clone the Repository

```bash
git clone https://github.com/yourusername/speedvision.git
cd speedvision
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🛠️ Usage

To calculate the speed of vehicles from a video, follow these steps:

1. **Prepare Your Video**: Place your video file in the `input/` directory.
   
2. **Run Speed Calculation Script**:

   ```bash
   python speedvision.py --video input/your-video-file.mp4
   ```

3. **Output**: The tool will display the estimated speed of the detected vehicles and save the processed video.

### Example:

```bash
python speedvision.py --video input/highway_footage.mp4
```

**Output:**

```
Vehicle Speed: 65.3 km/h
```

## 📂 Project Structure

```
speedvision/
│
├── input/                   # Directory for input videos
├── output/                  # Directory for processed video output
├── speedvision.py           # Main script for speed calculation
├── preprocessing.py         # Preprocessing functions for better detection
├── tracker.py               # Vehicle tracking script (SORT or DeepSORT)
├── requirements.txt         # List of Python dependencies
└── demo/                    # Demo files showcasing the project's functionality
```

## 🔧 Customization

- You can adjust the frame rate analysis or tracking algorithm by editing `speedvision.py` and `tracker.py`.
- The **accuracy of speed calculations** can be fine-tuned through calibration by specifying the real-world distance covered by the vehicles (e.g., meters per pixel).

### Calibration:

To obtain **precise speed measurements**, calibrate the tool by defining the distance covered by vehicles in the real world, relative to pixel measurements in the video.

## 🌱 Future Enhancements

- 📱 **Mobile App Integration**: Develop a mobile app to allow video uploads and real-time speed analysis.
- 🎥 **Live Video Stream Support**: Extend functionality to process live video feeds for continuous monitoring.
- 🧠 **Improved Detection Models**: Incorporate deep learning models for more accurate vehicle detection and fewer false positives.
- 📊 **Traffic Analytics**: Expand SpeedVision to analyze traffic flow, detect congestion, and provide detailed reports.

## 🤝 Contributing

We welcome contributions! If you'd like to contribute to SpeedVision, feel free to fork this repository, submit a pull request, or open an issue.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.

## 📧 Contact

If you have any questions, issues, or suggestions, feel free to contact the project maintainer:

**Atharv Gupta**  
Email: [atharvg06@gmail.com](mailto:atharvg06@gmail.com)
