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

*Add screenshots of your app in action here*

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

### Docker Deployment

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 7860

CMD ["python", "app.py"]
```

### Local Development

```bash
# Install in development mode
pip install -e .

# Run with auto-reload
python app.py --reload
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Update documentation for new features

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This application is for educational and entertainment purposes. The quality of try-on results depends on:
- Input image quality
- Lighting conditions
- Pose and positioning
- API service availability

Results may not always be perfectly accurate and should not be used as the sole basis for purchasing decisions.

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

### Getting Help

- Open an issue on GitHub
- Check the [Discussions](../../discussions) section
- Review existing issues for solutions

## 🙏 Acknowledgments

- [Try-On Diffusion API](https://rapidapi.com/try-on-diffusion/api/try-on-diffusion) for the AI try-on capabilities
- [Gradio](https://gradio.app/) for the amazing web interface framework
- [Hugging Face Spaces](https://huggingface.co/spaces) for hosting

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/your-username/virtual-try-on-app)
![GitHub forks](https://img.shields.io/github/forks/your-username/virtual-try-on-app)
![GitHub issues](https://img.shields.io/github/issues/your-username/virtual-try-on-app)
![GitHub license](https://img.shields.io/github/license/your-username/virtual-try-on-app)

---

**Made with ❤️ by [Your Name](https://github.com/your-username)**
