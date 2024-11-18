# Hand Talk: Stable Diffusion Image Generation API

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

   ```git clone git@github.com:IureRosa/hand_talk.git```
   ```cd hand_talk```

2. **Create a Virtual Environment (optional but recommended):**

```python -m venv venv```

3. **Activate the Virtual Environment:**

```source venv/bin/activate```
