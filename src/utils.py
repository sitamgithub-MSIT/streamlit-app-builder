def input_image_details(uploaded_file):
    """
    Extracts image details from an uploaded file.

    Args:
        uploaded_file (file-like object): The uploaded file object.

    Returns:
        list: A list containing a dictionary with the mime type and data of the uploaded file.

    Raises:
        FileNotFoundError: If no file is uploaded.
    """
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        # Create a list of image parts with the mime type and data
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data,
            }
        ]

        # Return the list of image parts
        return image_parts

    # If no file is uploaded, raise an error
    else:
        raise FileNotFoundError("No file uploaded")
