# 👕 Virtual Try-On App

A web-based virtual try-on application that uses AI to show how clothing items would look on users. Built with Gradio and powered by the Try-On Diffusion API.

![Virtual Try-On Demo](https://img.shields.io/badge/Status-Live-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Gradio](https://img.shields.io/badge/Gradio-Latest-orange)

## ✨ Features

- **AI-Powered Try-On**: Uses advanced diffusion models for realistic clothing visualization
- **User-Friendly Interface**: Simple drag-and-drop interface built with Gradio
- **Fit Analysis**: Provides basic fit advice based on user measurements
- **Real-Time Processing**: Quick results with optimized image processing
- **Multiple Format Support**: Supports various image formats (JPG, PNG, etc.)

## 🚀 Live Demo

Try the app live on Hugging Face Spaces: https://huggingface.co/spaces/ThatITGuy/Virtual-Try-On

## 📸 Screenshots

![WhatsApp Image 2025-06-19 at 11 56 50_a3fdff52](https://github.com/user-attachments/assets/8d84e768-c1bc-42a5-836c-31dc4fe241dd)
![WhatsApp Image 2025-06-19 at 11 57 01_5bf7d910](https://github.com/user-attachments/assets/b909ddd3-0195-4cdc-a64d-a776b882fca4)



## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- RapidAPI account with Try-On Diffusion API access

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/virtual-try-on-app.git
   cd virtual-try-on-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   export RAPIDAPI_KEY="your-rapidapi-key-here"
   ```
   
   Or create a `.env` file:
   ```
   RAPIDAPI_KEY=your-rapidapi-key-here
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to the URL shown in the terminal (usually `http://localhost:7860`)

## 🔧 Configuration

### API Setup

1. Sign up for [RapidAPI](https://rapidapi.com/)
2. Subscribe to the [Try-On Diffusion API](https://rapidapi.com/try-on-diffusion/api/try-on-diffusion)
3. Get your API key from the RapidAPI dashboard
4. Set the `RAPIDAPI_KEY` environment variable

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `RAPIDAPI_KEY` | Your RapidAPI key for Try-On Diffusion API | Yes |

## 📋 Usage

1. **Upload Your Photo**: Use a clear, well-lit photo where you're facing forward
2. **Upload Clothing Item**: Upload an image of the clothing item you want to try on
3. **Enter Measurements** (Optional): Provide your measurements for better fit analysis
   - Height (cm)
   - Chest (cm)
   - Waist (cm)
   - Sleeve length (cm)
4. **Click "Try On Outfit"**: Wait for the AI to process your request
5. **View Results**: See the try-on result and fit advice

### Tips for Best Results

- Use high-quality, well-lit images
- Ensure the person is facing forward in the photo
- Use clothing images with clear, unobstructed views
- Avoid images with complex backgrounds
- Make sure images are not too large (recommended: under 2MB)

## 🏗️ Project Structure

```
virtual-try-on-app/
│
├── app.py                      # Main Gradio application
├── try_on_diffusion_client.py  # API client for Try-On Diffusion
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── .gitignore                 # Git ignore file
```

## 🔧 Technical Details

### Core Components

- **Gradio Interface**: Provides the web UI for user interactions
- **OpenCV**: Handles image processing and format conversions
- **Try-On Diffusion API**: Performs the actual AI-powered try-on generation
- **PIL/Pillow**: Additional image processing capabilities

### API Integration

The app integrates with the Try-On Diffusion API through a custom client that handles:
- Image format conversions (RGB ↔ BGR)
- Multipart form data encoding
- Error handling and response processing
- RapidAPI authentication

## 🚀 Deployment

### Hugging Face Spaces

1. Create a new Space on [Hugging Face](https://huggingface.co/spaces)
2. Choose Gradio as the SDK
3. Upload all project files
4. Set `RAPIDAPI_KEY` as a repository secret
5. The app will automatically build and deploy


### Local Development

```bash
# Install in development mode
pip install -e .

# Run with auto-reload
python app.py --reload
```




## 🆘 Troubleshooting

### Common Issues

**Build Errors on Hugging Face Spaces**
- Ensure `requirements.txt` only contains valid PyPI packages
- Check that all files are properly uploaded

**API Errors**
- Verify your RapidAPI key is correct and active
- Check your API usage limits
- Ensure images are in supported formats

**Poor Results**
- Use high-quality, well-lit images
- Ensure the person is facing forward
- Try different clothing items or poses


##  Acknowledgments

- [Try-On Diffusion API](https://rapidapi.com/try-on-diffusion/api/try-on-diffusion) for the AI try-on capabilities
- [Gradio](https://gradio.app/) for the amazing web interface framework
- [Hugging Face Spaces](https://huggingface.co/spaces) for hosting


