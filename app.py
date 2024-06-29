# Necessary imports
import os
from PIL import Image

import streamlit as st
from streamlit_image_select import image_select

from src.utils import input_image_details
from src.llm_response import (
    generate_image_response,
    generate_text_response,
    generate_example_image_response,
)


# App title and description
st.set_page_config(page_title="Streamlit App Builder", page_icon="🛠")
st.title("🛠 Streamlit App Builder")
st.header("Build Your Streamlit App with Ease")
st.info(
    "Welcome to the **Streamlit App Builder**! In this app, you can either **Show** (by providing a preview image) or **Tell** (by providing a text prompt) how you want your Streamlit app to be built. Let's get started!"
)

# Tabs to switch between "Show" and "Tell"
tabs = st.tabs(["Show", "Tell"])


# Show how the app should be built or tell how the app should be built
with tabs[0]:
    # Upload image option
    upload_img = st.toggle("Upload your own preview image")

    # If upload image option is selected
    if upload_img:
        st.subheader("Upload your own preview image")
        image_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

        # Show uploaded image if any image is uploaded by the user
        if image_upload:
            image = Image.open(image_upload)
            st.image(image, caption="Uploaded Image", use_column_width=True)

    # Example images option
    example_img = st.toggle("Try example preview images")

    # If example image option is selected
    if example_img:
        st.subheader("Try these example preview images")

        # Select image from list of images in images folder
        img = image_select(
            label="Select a preview image",
            images=[
                "images/streamlit-app-preview-1.png",
                "images/streamlit-app-preview-2.png",
            ],
        )

    # Start LLM process (only if image is uploaded or example image is selected)
    if (not upload_img) and (not example_img):
        start_button = st.button("Build", key="button_image_start", disabled=True)
    else:
        start_button = st.button("Build", key="button_image_start", disabled=False)

    # If image is uploaded or example image is selected
    if any([upload_img, example_img]) == True:
        if "img" in locals() or "img" in globals():
            if start_button:

                # Processing the image
                with st.spinner("Processing ..."):

                    # When image preview 1 is selected
                    if img == "images/streamlit-app-preview-1.png":
                        st.subheader("Input")
                        st.image("images/streamlit-app-preview-1.png")
                        preview_image_1 = Image.open(
                            "images/streamlit-app-preview-1.png"
                        )
                        st.subheader("Output")
                        example_image_output_1 = generate_example_image_response(
                            preview_image_1
                        )
                        st.write(example_image_output_1)

                    # When image preview 2 is selected
                    if img == "images/streamlit-app-preview-2.png":
                        st.subheader("Input")
                        st.image("images/streamlit-app-preview-2.png")
                        preview_image_2 = Image.open(
                            "images/streamlit-app-preview-2.png"
                        )
                        st.subheader("Output")
                        example_image_output_2 = generate_example_image_response(
                            preview_image_2
                        )
                        st.write(example_image_output_2)

                    # Clear results if "Clear" button is clicked
                    if st.button("Clear", key="button_image_clear"):
                        os.remove(example_image_output_1)
                        os.remove(example_image_output_2)

        # If image is uploaded and start button is clicked
        elif image_upload is not None and start_button:

            # Processing the image
            with st.spinner("Processing ..."):
                image_data = input_image_details(image_upload)

                try:
                    # Get the generated output from the model based on the image uploaded
                    image_data_output = generate_image_response(image_data)
                    # Display the output
                    st.subheader("Output")
                    st.write(image_data_output)

                    # Clear results if "Clear" button is clicked
                    if st.button("Clear", key="button_image_clear"):
                        os.remove(image_data_output)

                # Raise error if any error occurs during response generation
                except Exception as e:
                    st.error(f"An error occurred: {e}")

        else:
            if not image_upload and start_button:
                # Warn user to upload image
                st.warning("Please upload your preview image.")


# Tell how the app should be built
with tabs[1]:
    # Text prompt to describe the app
    text_prompt = st.text_area(
        "Describe details on the functionalities of the Streamlit app that you want to build.",
        "",
        height=240,
    )

    # Start LLM process
    start_button = st.button("Build", key="button_text_start")

    # If text prompt is provided and start button is clicked
    if text_prompt and start_button:

        # Processing the text prompt
        with st.spinner("Processing ..."):

            try:
                # Get the generated output from the model based on the text prompt
                text_data_output = generate_text_response(text_prompt)
                # Display the extracted content
                st.subheader("Output")
                st.write(text_data_output)

                # Clear results if "Clear" button is clicked
                if st.button("Clear", key="button_text_clear"):
                    os.remove(text_data_output)

            # Raise error if any error occurs during response generation
            except Exception as e:
                st.error(f"An error occurred: {e}")

    # If text prompt is not provided and start button is clicked
    elif not text_prompt and start_button:
        # Warn user to provide text prompt
        st.warning("Please provide your text prompt.")
