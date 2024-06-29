# Necessary imports
import os
from dotenv import load_dotenv

import google.generativeai as genai

from src.config import generation_config, safety_settings, model_name
from src.prompt import system_prompt


# Load the Environment Variables from .env file
load_dotenv()

# Initialize Gemini with API key
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Create the Gemini Models for Text and Vision respectively
model = genai.GenerativeModel(
    model_name=model_name,
    generation_config=generation_config,
    safety_settings=safety_settings,
    system_instruction=system_prompt,
    # tools="code_execution",
)

# Instruction for the response generation
instruction = "Generate the complete Streamlit app code based on the provided preview image or example. Ensure the code includes layout, functionality, and any specified features visible in the image. Incorporate common Streamlit components such as sliders, buttons, and charts where applicable, handle any specific UI elements shown in the image, and ensure proper data handling and user interactions are implemented."


def generate_text_response(text_prompt):
    """
    Generate Streamlit app code based on the provided text prompt.

    Parameters:
    - text_prompt (str): The text prompt provided by the user.

    Returns:
    - str: Extracted content from the response.

    Raises:
    - RuntimeError: If an error occurs during response generation.
    """
    try:
        # Response generation for text using Gemini API
        response = model.generate_content(text_prompt)

        # Extract the actual content part from the response
        content = response.text
        return content

    # Raise error if any error occurs during response generation
    except Exception as e:
        raise RuntimeError(f"An error occurred during text response generation: {e}")


def generate_example_image_response(img):
    """
    Generate Streamlit app code based on the provided example image.

    Parameters:
    - img (str): Image identifier or path.

    Returns:
    - str: Extracted content from the response.

    Raises:
    - RuntimeError: If an error occurs during response generation.
    """
    try:
        # Response generation for example image using Gemini API
        response = model.generate_content([instruction, img])

        # Extract the actual content part from the response
        content = response.text
        return content

    # Raise error if any error occurs during response generation
    except Exception as e:
        raise RuntimeError(f"An error occurred during image response generation: {e}")


def generate_image_response(image_data):
    """
    Generate a response for an uploaded image using the Gemini API.

    Parameters:
        image_data (list): A list containing the image data.

    Returns:
        str: The generated response content.

    Raises:
        RuntimeError: If an error occurs during response generation.
    """
    try:
        # Response generation for uploaded image using Gemini API
        response = model.generate_content([instruction, image_data[0]])

        # Extract the actual content part from the response
        content = response.text
        return content

    # Raise error if any error occurs during response generation
    except Exception as e:
        raise RuntimeError(f"An error occurred during image response generation: {e}")
