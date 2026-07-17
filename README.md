# 🚀 Federated Learning-Based Object Detection Using YOLOv5

## 📌 Project Overview

This project implements a **Federated Learning-based Object Detection System** using **YOLOv5**. It enables multiple clients to collaboratively train an object detection model without sharing their local datasets, thereby preserving data privacy while improving model performance.

The project demonstrates how federated learning can be integrated with deep learning-based object detection to build secure and privacy-preserving AI systems.

---

## 🎯 Objectives

- Develop a privacy-preserving object detection system.
- Implement Federated Learning for distributed model training.
- Detect objects using the YOLOv5 deep learning model.
- Aggregate client models to improve global model performance.
- Reduce data sharing while maintaining high detection accuracy.

---

## ✨ Features

- Federated Learning architecture
- YOLOv5 object detection
- Distributed client-server communication
- Global model aggregation
- Image-based object detection
- Python implementation
- Easy-to-run project structure

---

## 🛠️ Technologies Used

- Python
- YOLOv5
- PyTorch
- OpenCV
- NumPy
- Federated Learning

---

## 📂 Project Structure

```
FederatedLearning/
│── Dataset/
│── global/
│── model/
│── testImages/
│── yolov5/
│── Main.py
│── Server.py
│── requirements.txt
│── run.bat
│── runServer.bat
```

---

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/Pujithacheguri/Federated-Learning-Object-Detection.git
```

2. Navigate to the project directory

```bash
cd Federated-Learning-Object-Detection
```

3. Install the required packages

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Start the server:

```bash
python Server.py
```

Run the client:

```bash
python Main.py
```

---

## 📊 Results

- Successfully implemented federated learning for object detection.
- Improved privacy by keeping training data local.
- Integrated YOLOv5 for accurate object detection.
- Achieved collaborative model learning through server aggregation.

---

## 🚀 Future Enhancements

- Support multiple distributed clients.
- Improve model accuracy with larger datasets.
- Deploy on cloud infrastructure.
- Add a web-based dashboard.
- Integrate real-time video object detection.

---

## 👩‍💻 Author

**Pujitha Cheguri**

- GitHub: https://github.com/Pujithacheguri
- LinkedIn: *(Add your LinkedIn profile URL here)*

---

## ⭐ If you found this project useful, please consider giving it a Star.