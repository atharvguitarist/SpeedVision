import cv2
import pytesseract
import re
import json
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # For displaying video in Tkinter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.tokenize import word_tokenize
import nltk
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

# Initialize NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

class InvoiceProcessor:
    def __init__(self):
        self.categories = {
            "entertainment": ["movie", "cinema", "food", "restaurant", "happy"],
            "home_utility": ["electricity", "water", "internet", "broadband"],
            "grocery": ["grocery", "milk", "bread", "fruit", "vegetable"],
            "investment": ["loan", "finance", "investment", "deposit"],
            "transport": ["transport", "taxi", "uber", "car", "train"],
            "shopping": ["shopping", "clothes", "electronics", "footwear"]
        }
    
    def extract_text_from_image(self, frame):
        """Extract text from an image using Tesseract OCR"""
        text = pytesseract.image_to_string(frame).lower()
        return text

    def extract_amount_bounding_box(self, frame):
        """Extract the total amount and mark it on the frame"""
        h, w, _ = frame.shape
        boxes = pytesseract.image_to_boxes(frame)
        amount = "0"
        marked_frame = frame.copy()
        
        # Define regex pattern to detect amounts in $ or € or £
        amount_pattern = re.compile(r'[\$\€\£]\s?\d+(?:,\d{3})*(?:\.\d{2})?')

        # Mark detected amounts on the frame
        for box in boxes.splitlines():
            b = box.split(' ')
            if len(b) >= 6:
                character = b[0]
                x, y, x2, y2 = int(b[1]), int(b[2]), int(b[3]), int(b[4])
                text_line = pytesseract.image_to_string(frame[y:h-y2, x:x2]).strip()

                # Check if the text matches an amount pattern
                if re.search(amount_pattern, text_line):
                    amount = text_line
                    cv2.rectangle(marked_frame, (x, h-y), (x2, h-y2), (0, 255, 0), 2)
                    cv2.putText(marked_frame, "Amount: " + text_line, (x, h-y2-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        return marked_frame, amount

    def process_frame(self, frame):
        """Process the frame to extract and mark the total amount"""
        marked_frame, amount = self.extract_amount_bounding_box(frame)
        return marked_frame, amount

class VideoCaptureApp:
    def __init__(self, root, processor):
        self.root = root
        self.processor = processor
        self.cap = None
        
        # Configure root background color and other styles
        self.root.configure(bg='#2e2e2e')  # Dark matte grey background

        # Set up the UI (center the frame with expand=True)
        self.canvas_frame = tk.Frame(root, bg='#2e2e2e')
        self.canvas_frame.pack(expand=True)

        self.canvas = tk.Label(self.canvas_frame, width=640, height=480, bg='#1c1c1c')
        self.canvas.pack(expand=True, pady=20)
        
        # Label to display recognized amount
        self.amount_label = tk.Label(root, text="Total Amount: $0", font=('Arial', 14), bg='#2e2e2e', fg='white')
        self.amount_label.pack(pady=10)

        self.upload_button = tk.Button(
            root, text="Upload Video", command=self.open_file, 
            font=('Arial', 12), bg='#4CAF50', fg='white', 
            activebackground='#45a049', padx=20, pady=10, bd=0
        )
        self.capture_button = tk.Button(
            root, text="Capture from Webcam", command=self.start_capture, 
            font=('Arial', 12), bg='#008CBA', fg='white', 
            activebackground='#007bb5', padx=20, pady=10, bd=0
        )
        
        self.upload_button.pack(pady=10)
        self.capture_button.pack(pady=10)
        
        # Display a black frame initially
        self.show_black_frame()

    def show_black_frame(self):
        """Display a black screen in the Tkinter window"""
        black_image = Image.new('RGB', (640, 480), color='black')
        self.imgtk = ImageTk.PhotoImage(image=black_image)
        self.canvas.config(image=self.imgtk)

    def update_frame(self):
        """Update the frame with the webcam feed"""
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            self.imgtk = ImageTk.PhotoImage(image=img)
            self.canvas.config(image=self.imgtk)
        self.root.after(10, self.update_frame)  # Update every 10ms for real-time feed

    def start_capture(self):
        """Start the webcam and display the feed"""
        self.cap = cv2.VideoCapture(0)  # Open the webcam
        self.update_frame()

    def open_file(self):
        """Select a video file and process it"""
        file_path = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=[("Video files", "*.mp4 *.avi *.mkv")]
        )
        
        if file_path:
            cap = cv2.VideoCapture(file_path)
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Process the frame to get the total bill amount
                marked_frame, amount = self.processor.process_frame(frame)
                
                # Display the marked frame on the canvas
                img = Image.fromarray(marked_frame)
                self.imgtk = ImageTk.PhotoImage(image=img)
                self.canvas.config(image=self.imgtk)

                # Update the amount label with detected amount
                self.amount_label.config(text=f"Total Amount: {amount}")

            cap.release()

def start_gui():
    root = tk.Tk()
    root.title("Bill Wizard - Invoice Detection")
    processor = InvoiceProcessor()
    app = VideoCaptureApp(root, processor)
    root.mainloop()

if __name__ == "__main__":
    start_gui()
