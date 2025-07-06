# AI Image Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![GitHub stars](https://img.shields.io/github/stars/YUKII2K3/Image-generator.svg?style=social&label=Star)](https://github.com/YUKII2K3/Image-generator)
[![GitHub forks](https://img.shields.io/github/forks/YUKII2K3/Image-generator.svg?style=social&label=Fork)](https://github.com/YUKII2K3/Image-generator)

> **Advanced AI-powered image generation tool with a modern web interface**

AI Image Generator is a powerful, user-friendly tool for creating high-quality images using state-of-the-art AI models. Built with a clean, intuitive interface, it supports various image generation techniques including text-to-image, image-to-image, inpainting, and more.

## ✨ Features

- 🎨 **Text-to-Image Generation** - Create stunning images from text descriptions
- 🖼️ **Image-to-Image** - Transform existing images with AI
- 🔧 **Inpainting & Outpainting** - Edit and extend images seamlessly
- 🎭 **Multiple Art Styles** - Extensive collection of artistic styles and presets
- ⚡ **Fast Generation** - Optimized for speed with various performance modes
- 🌐 **Web Interface** - Modern, responsive Gradio-based UI
- 🔒 **Privacy-First** - Run locally, no data sent to external servers
- 🐳 **Docker Support** - Easy deployment with containerization

## 🚀 Quick Start

### Option 1: Google Colab (Recommended for beginners)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YUKII2K3/Image-generator/blob/main/ai_image_generator_colab.ipynb)

1. Click the "Open In Colab" button above
2. Run all cells in the notebook
3. Access the web interface through the provided link

### Option 2: Local Installation

#### Prerequisites
- Python 3.10 or higher
- Git
- 8GB+ RAM (16GB+ recommended)
- NVIDIA GPU with 6GB+ VRAM (optional but recommended)

#### Installation Steps

**Using Conda (Recommended):**
```bash
git clone https://github.com/YUKII2K3/Image-generator.git
cd Image-generator
conda env create -f environment.yaml
conda activate ai_image_generator
pip install -r requirements_versions.txt
python entry_with_update.py
```

**Using Virtual Environment:**
```bash
git clone https://github.com/YUKII2K3/Image-generator.git
cd Image-generator
python3 -m venv ai_image_generator_env
source ai_image_generator_env/bin/activate  # On Windows: ai_image_generator_env\Scripts\activate
pip install -r requirements_versions.txt
python entry_with_update.py
```

#### Running the Application

After installation, simply run:
```bash
python entry_with_update.py
```

The web interface will be available at `http://localhost:7860`

## 📁 Project Structure

```
Image-generator/
├── modules/           # Core application modules
├── models/           # AI model storage
├── presets/          # Generation presets
├── sdxl_styles/      # Artistic style definitions
├── extras/           # Additional utilities
├── webui.py          # Main web interface
├── entry_with_update.py  # Entry point
└── ai_image_generator_colab.ipynb  # Colab notebook
```

## 🎯 Usage

1. **Text-to-Image**: Enter a prompt describing your desired image
2. **Style Selection**: Choose from hundreds of artistic styles
3. **Parameters**: Adjust generation settings (steps, CFG, etc.)
4. **Generate**: Click generate and watch your image come to life!

## 🔧 Configuration

The application uses `config.txt` for settings. Key configurations include:
- Model paths and preferences
- Performance settings
- UI customization
- Output formats

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues and pull requests.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the original Fooocus project
- Built with Gradio for the web interface
- Powered by various open-source AI models

## 📞 Support

- 📧 **Issues**: [GitHub Issues](https://github.com/YUKII2K3/Image-generator/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/YUKII2K3/Image-generator/discussions)
- 📖 **Documentation**: Check the [troubleshoot.md](troubleshoot.md) for common issues

---

**Maintained by Yuktheshwar** 🚀

*Star this repository if you find it helpful!*
