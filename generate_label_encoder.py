# -*- coding: utf-8 -*-
"""generate_label_encoder

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JLs46Ua6fVs0Jwf26Plza7QPTUxtwba-
"""

import joblib
from sklearn.preprocessing import LabelEncoder
import os

# Your actual gesture labels
gesture_labels = [
    "three2",
    "palm",
    "four",
    "ok",
    "stop_inverted",
    "call",
    "peace_inverted",
    "left",
    "rock",
    "three",
    "peace",
    "right",
    "two_up_inverted",
    "two_up",
    "down",
    "up",
    "mute",
    "fist"
]

# Initialize and fit label encoder
le = LabelEncoder()
le.fit(gesture_labels)

# Save the encoder
os.makedirs("models", exist_ok=True)
joblib.dump(le, os.path.join("models", "label_encoder.pkl"))

print("label_encoder.pkl saved successfully!")
print("Encoded classes:", list(le.classes_))