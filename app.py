import streamlit as st
from PIL import Image, ImageDraw
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import numpy as np
import flyr
import numpy as np
from pathlib import Path
import glob
import os
import tempfile


import cv2
# Load the trained model
model = YOLO("best.pt")  # Load your custom YOLOv8 model

# Function to make predictions
def preprocess_image(image):
    # Convert to RGB (if not already in that mode)
    image = Image.open(image).convert("RGB")
    # You can add more preprocessing steps if needed
    return image

def save_uploaded_file(uploaded_file):
    # Create a temporary directory
    temp_dir = tempfile.TemporaryDirectory()

    # Save the uploaded file to the temporary directory
    file_path = os.path.join(temp_dir.name, uploaded_file.name)
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.read())

    return file_path

def main():
    st.title("Object Detection with YOLOv8 and Streamlit")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    file_bytes = uploaded_file.read()

    if uploaded_file is not None:
        temp_file_path = save_uploaded_file(uploaded_file)
        st.write(temp_file_path)

        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Detecting objects...")

        # Preprocess the uploaded image
        input_image = preprocess_image(uploaded_file)
        # Make predictions
        results = model.predict(input_image,save=True,)
        result_image = results[0].plot()  # Get the detected objects image

        # Display the prediction
        st.image(result_image, caption="Detected Objects", use_column_width=True)


        #
        st.write(temp_file_path)
        #temp_file_path = temp_file_path.replace("\\", "\\\\")
        #directory_path = os.path.dirname(temp_file_path)

        #directory_with_wildcard = os.path.join(directory_path, "*.jpg")
        #st.write(directory_with_wildcard)

        flir_imgs=glob.glob(temp_file_path)
        st.write(len(flir_imgs))
        for flir_img in flir_imgs:
            thermogram = flyr.unpack(flir_img)
            
            
            result = results[0]
            box = result.boxes[0]
            cords = box.xyxy[0].tolist()
            cords = [round(x) for x in cords]
            class_id = result.names[box.cls[0].item()]
            conf = round(box.conf[0].item(), 2)
            x1, y1, x2, y2 = cords
            width=(x2-x1)
            height=(y2-y1)
            pixel_area=height*width
            actual_area=0.08 # area of the laptop in meter
            area_pixel=actual_area/409600 # actual area of each pixel in meter
            hotspot_area=area_pixel*pixel_area
            
            # flir_path = "FLIR9813.jpg"
            

            thermal_celsius = thermogram.celsius
            max=np.max(thermal_celsius)
            min=np.min(thermal_celsius) 
            temperature= (max*8 + min*2)/10

            # Given values
            emissivity = 0.95

            # Convert temperature to Kelvin
            temperature_kelvin = temperature + 273.15

            # Stefan-Boltzmann constant
            stefan_boltzmann_constant = 5.67e-8  # in W m^-2 K^-4

            # Calculate power (energy per unit time) emitted
            power_emitted = emissivity * stefan_boltzmann_constant * hotspot_area * temperature_kelvin**4
            st.write("The Energy Emmitted in the hotspot region is :",power_emitted)





if __name__ == "__main__":
    main()
