# 🚗 Speed Vision - Realtime Speed Calculation of a Car (AI) 🎥

**SpeecVision** is an AI-powered tool that calculates the **speed of a car** from video footage using computer vision techniques. It processes video frames to detect and track vehicles, and then calculates their speed based on distance and time analysis. SpeecVision is ideal for traffic monitoring, speed enforcement, and vehicle analytics.

## Video Tutorial

[!Video](https://github.com/user-attachments/assets/1f9da6ad-d2e2-42f8-b488-f7b2b4218e32)

## ✨ Features

- 🏎️ **Real-Time Vehicle Speed Calculation**: Detects and calculates the speed of cars directly from videos.
- 🎯 **Object Detection**: Uses advanced YOLO-based object detection to accurately identify vehicles.
- ⏱️ **Frame-by-Frame Tracking**: Tracks the vehicle across frames to determine speed over time.
- 🛠️ **Scalable and Flexible**: Can handle different camera angles and video formats.
- 🔄 **Preprocessing Pipeline**: Enhances video frames for better detection and speed measurement.

## 🎬 Demo

[!Video](https://github.com/user-attachments/assets/dc857d06-ef5c-4912-9e77-cce540e0d2a1)

## 🚀 Installation

### Prerequisites

1. **Python 3.7+** 🐍
2. **OpenCV**: For video processing. You can install it via `pip`:
   ```bash
   pip install opencv-python
   ```

3. **YOLOv8 and SORT**: For object detection and tracking. Install dependencies using the provided `requirements.txt`.

### Clone the Repository

```bash
git clone https://github.com/yourusername/speecvision.git
cd speecvision
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🛠️ Usage

To calculate the speed of a car from a video, follow these steps:

1. **Prepare the Video**: Place your video file in the `input/` folder.

2. **Run the Speed Calculation Script**:

   ```bash
   python speecvision.py --video input/your-video-file.mp4
   ```

3. **Output**: The estimated speed of the detected car will be displayed.

### Example:

```bash
python speecvision.py --video input/highway_footage.mp4
```

**Output:**

```
Vehicle Speed: 62.5 km/h
```

## 📁 Project Structure

```
speecvision/
│
├── input/                   # Directory for input videos
├── output/                  # Directory for output files (e.g., processed videos)
├── speecvision.py           # Main script for speed calculation
├── preprocessing.py         # Functions for video preprocessing and enhancement
├── tracker.py               # Vehicle tracking script (e.g., SORT or DeepSORT)
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── demo/                    # Demo files for showcasing functionality
```

## 🔧 Customization

You can tweak the speed detection algorithm by adjusting the frame rate analysis or modifying the vehicle tracking parameters. This can be done by editing `speecvision.py` and `tracker.py`.

### Calibration

- To achieve **accurate speed calculations**, you'll need to calibrate the tool by providing the distance covered by the vehicle in the real world (e.g., meters per pixel).

## 🌱 Future Enhancements

- 📱 **Mobile App Integration**: Build a companion mobile app for easy video uploads and real-time speed analysis.
- 🎥 **Live Video Stream Support**: Add functionality to process live video feeds.
- 🧠 **Machine Learning Models**: Use advanced deep learning models to improve vehicle detection accuracy and reduce false positives.
- 📊 **Traffic Analysis**: Extend the tool to provide comprehensive traffic flow analysis based on video data.

## 🤝 Contributing

We welcome contributions! If you’d like to contribute, feel free to fork this repository, submit a pull request, or open an issue.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

If you have any questions or need further assistance, feel free to open an issue or contact the project maintainer at [Atharv Gupta - Gmail](mailto:atharvg06@gmail.com).
