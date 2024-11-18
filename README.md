# Hand Talk: Stable Diffusion Image Generation API

## Project Structure
```
hand_talk/
├── /models
│   └── (place the downloaded model here)
├── /api
│   └── handler.py           (Handles the image generation logic)
├── requirements.txt         (Project dependencies)
└── app.py                   (Flask application that starts the server)
```


This project is an **API for generating images** using the **Stable Diffusion model (DreamShaper v1.5)**. The API receives a JSON request with specific parameters, generates an image based on those parameters, and returns the image as a base64-encoded string.

The API is built with **Flask**, and it uses the **Stable Diffusion** model for image generation.

---

## Features

- Generate artistic images based on user-defined prompts.
- Uses **DreamShaper v1.5** model from **Hugging Face** to generate images.
- Flask-based API that accepts `person`, `instrument`, `environment`, and `style` as parameters to generate a unique image.

---

## Technologies Used

- **Flask**: Lightweight web framework for building the API.
- **PyTorch**: Deep learning framework for running the Stable Diffusion model.
- **Diffusers**: Hugging Face library for easy usage of diffusion models like Stable Diffusion.
- **Hugging Face Transformers**: Tokenizer for the text-to-image pipeline.
- **Pillow**: Python Imaging Library for handling image conversions.

---

## Setup Instructions

### **Step 1: Install Dependencies**

Before running the project, you need to install the required dependencies.

1. **Clone the repository**:

   Clone the project to your local machine:

   ```
   git clone git@github.com:IureRosa/hand_talk.git
   cd hand_talk
   ```

2. **Create a Virtual Environment (optional but recommended):**

```python -m venv venv```

3. **Activate the Virtual Environment:**

```source venv/bin/activate```

4. **Install the Dependencies:**

   ```pip install -r requirements.txt```

5. **Running the Flask API**

   ```python app.py```

### Test the Endpoint Using CURL or Postman
You can now test the API using curl or Postman by sending a POST request to the /generate-image endpoint.

Example Request:
To generate an image, you need to send a JSON request with parameters like person, instrument, environment, and style. Here's an example using curl:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/generate-image/' \
  -H 'Content-Type: application/json' \
  -d '{
  "person": "black woman",
  "instrument": "guitar",
  "environment": "jungle",
  "style": "anime"
}'
```
In this example, the request will generate an image of a black woman playing a guitar in a jungle in the anime style.

Example Response:
If the request is successful, you will receive a response containing a URL to the generated image, like this:
```
{
  "image_url": "http://127.0.0.1:8000/generated_images/generated_image_1.png"
}

```

### Decode and View the Image
To view the image, follow these steps:

1. Download the image using the URL returned by the API. You can use your browser or any tool to download the image. For example, visit the URL:
```
http://127.0.0.1:8000/generated_images/generated_image_1.png
```
2. Alternatively, View the Image in Python:
```
from PIL import Image
import requests
from io import BytesIO

# Replace with the actual URL of the image returned by the API
image_url = "http://127.0.0.1:8000/generated_images/generated_image_1.png"

response = requests.get(image_url)
img = Image.open(BytesIO(response.content))

# Show the image
img.show()

```
This code will fetch the image from the URL and display it using the default image viewer on your system.
