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
    if uploaded_file is None:
        # If no file is uploaded, raise an error
        raise FileNotFoundError("No file uploaded")

    # Read the file into bytes
    bytes_data = uploaded_file.getvalue()

    # Return a list containing a dictionary with the mime type and data of the uploaded file
    return [
        {
            "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
            "data": bytes_data,
        }
    ]
