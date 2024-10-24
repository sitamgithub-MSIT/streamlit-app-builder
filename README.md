# Streamlit App Builder

Streamlit is an open-source framework designed to build machine learning and data science applications. This specific project is a Streamlit application that helps users create other Streamlit applications. It allows users to upload mockups or generate code in text mode, making the process of developing Streamlit applications simpler and more efficient.

## Project Structure

The project is structured as follows:

- `assets/`: This directory contains screenshots of the output responses and assets regarding tracing and deployment.

- `images/`: This directory contains sample or mockup images for the application.

- `src/`: This directory contains the source code for the project.

  - `model/`: This directory contains the code for actual model response generation.

    - `prompt.py`: This file contains the system prompt for the model.
    - `llm_response.py`: This file contains the code for the generation of the model response.
    - `config.py`: This file contains the Gemini API configuration.

  - `utils.py`: This file contains the utility functions for the project.
  - `exception.py`: This file contains the exception handling for the project.
  - `logger.py`: This file contains the project's logging configuration.

- `app.py`: This file contains the code for the Streamlit application.
- `Dockerfile`: This file contains the Docker configuration for the project.
- `.dockerignore`: This file contains the files to be ignored by Docker.
- `.gitignore`: This file contains the files to be ignored by Git.
- `.gcloudignore`: This file contains the files that Google Cloud will ignore.
- `.env.example`: This file contains the environment variables required for the project.
- `requirements.txt`: This file contains the required dependencies for the project.
- `README.md`: This file contains the project documentation.
- `LICENSE`: This file contains the project license.

## Technologies Used

- **Python**: Python is used as the primary programming language for this project.
- **Gemini API**: These APIs provide advanced natural language processing and computer vision capabilities.
- **Streamlit**: Streamlit is used to build interactive UIs for the chat interface.
- **Docker**: Docker is used to containerize the application.
- **Cloud Run**: Google Cloud Run deploys the containerized application.
- **Cloud Build**: Google Cloud Build sets up the CI/CD pipeline.
- **W&B Weave**: W&B Weave is used to trace the model calls.

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository: `git clone https://github.com/sitamgithub-MSIT/streamlit-app-builder.git`
2. Change the directory: `cd streamlit-app-builder`
3. Create a virtual environment: `python -m venv tutorial-env`
4. Activate the virtual environment:
   - Windows: `tutorial-env\Scripts\activate`
   - Unix-based systems: `source tutorial-env/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Run the Gradio application: `streamlit run app.py`

**Note**: You need to have the Gemini API key to run the application. You can get the API key by signing up on the [Gemini API](https://aistudio.google.com/). Once you have the API key, create a `.env` file in the root directory and add the following environment variables provided in the `.env.example` file. Replace the values with your API key.

```bash
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Open your local host to view the web application. For more information, consult the Streamlit documentation [here](https://docs.streamlit.io/). You can also access a live version of the application [here](/), which is deployed on Google Cloud Run.

## Deployment

The application is deployed on Google Cloud Run. Follow the Google Cloud Generative AI sample app [here](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/sample-apps/gemini-streamlit-cloudrun) to deploy the application on Google Cloud Run. You can also refer to the dedicated lab [here](https://www.cloudskillsboost.google/focuses/85991?parent=catalog) for more details.

## Model Tracing

Model tracing is enabled using the W&B Weave. Refer to the documentation [here](https://weave-docs.wandb.ai/) to understand all the features provided by W&B Weave. To enable model tracing, follow these steps:

- Create a Weights & Biases (W&B) account [here](https://wandb.ai/site) and copy API [key](https://wandb.ai/authorize).
- Set the `WEAVE_API_KEY` environment variable to your W&B API key in the `.env` file.
- You can refer to the environment variables provided in the `.env.example` file for guidance. Replace the values with your own.

```bash
WEAVE_API_KEY=YOUR_WEAVE_API_KEY
```

## Usage

Once the application is up and running, you can interact with the App Builder through the provided UI. It can analyze mockup images and generate code in text mode. The application can also generate code for the text-based descriptions as well.

### Example

1. Open the application in your browser.
2. Select the "Show" option to view or upload a sample image. You can also input text with the "Text" mode.
3. Input a sample image or text based on the selected mode.
4. Click the "Build" button.
5. The application will analyze the content and provide a detailed response.
6. You can also clear the response by clicking the "Clear" button.
7. You can trace the model calls by enabling W&B Weave tracing.

## Results

This Streamlit application can analyze the content of the sample image or text and generate code based on the input. The application can also trace the model calls using W&B Weave. For results, refer to the `assets/` directory for the output screenshots, which show the application interface and the responses as well as the model tracing.

## Conclusion

In this project, we have built an AI-powered builder for Streamlit applications. We have used the Gemini API for the AI capabilities, and W&B Weave for the model call tracing. The application was built using Streamlit and Dockerized, and finally, deployed on the Google Cloud Platform (GCP) using the Cloud Run service with a CI/CD pipeline using Cloud Build.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you would like to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or suggestions regarding the project, feel free to reach out to me on my GitHub profile.

Happy coding! 🚀
