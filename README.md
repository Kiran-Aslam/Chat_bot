# 🤖 AI Chat Assistant

A modern, responsive AI-powered chat application built with Streamlit and Groq API. Features a sleek dark theme with red accents and real-time conversation capabilities.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

##  Features

-  Real-time AI Chat**: Instant conversations with multiple AI models
-  Modern UI**: Sleek dark theme with red accents and smooth animations
-  Responsive Design**: Works seamlessly on desktop and mobile devices
-  Customizable Settings**: Adjust AI creativity, response length, and model selection
-  Export Functionality**: Download your chat history as text files
-  Fixed Input Area**: Chat input stays at the bottom while messages scroll
-  Live Statistics**: Real-time chat metrics and activity tracking

##  Live Demo

You can try the application live at: [Your Deployment URL Here]

##  Installation

### Prerequisites

- Python 3.10 or higher
- Groq API key (free registration at [console.groq.com](https://console.groq.com))

##  Configuration

### AI Models Available

- **Llama3-8B-8192**: Fast and efficient, best for quick responses
- **Llama3-70B-8192**: More capable but slower, best for complex tasks
- **Mixtral-8x7B-32768**: Excellent for reasoning and detailed responses
- **Gemma-7B-IT**: Google's instruction-tuned model

### Customizable Parameters

- **Temperature (0.1-1.0)**: Controls response creativity
  - `0.1`: Very focused and deterministic
  - `0.7`: Balanced creativity (default)
  - `1.0`: Maximum creativity and variation

- **Max Tokens (100-2000)**: Controls response length
  - `500`: Short responses
  - `1000`: Balanced length (default)
  - `2000`: Detailed responses

##  UI Components

### Main Features

- **Header Section**: Animated header with app branding
- **Chat Area**: Scrollable message history with smooth animations
- **Input Area**: Fixed bottom input with Enter-to-send functionality
- **Sidebar**: Model settings, statistics, and chat controls

### Design Elements

- **Color Scheme**: Dark theme with red (#dc2626) accents
- **Typography**: Poppins font family for modern look
- **Animations**: Smooth transitions and hover effects
- **Responsive**: Mobile-friendly design

##  Deployment

### Streamlit Cloud (Free)

1. **Fork this repository** to your GitHub account

2. **Sign up at [share.streamlit.io](https://share.streamlit.io)**

3. **Connect your GitHub** and select this repository

4. **Add your API key** in Streamlit Cloud secrets:
   ```toml
   [secrets]
   GROQ_API_KEY = "your_api_key_here"
   ```

5. **Deploy** and share your live app URL!

##  Environment Variables

For production deployment, use environment variables:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

Create a `.env` file (not committed to Git):
```env
GROQ_API_KEY=gsk_your_actual_api_key_here
```

##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -m 'Add feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

##  Acknowledgments

- **Streamlit** - For the amazing web framework
- **Groq** - For providing fast AI inference
- **Meta AI** - For the Llama models
- **Mistral AI** - For the Mixtral model
- **Google** - For the Gemma model

##  Support

If you encounter any issues or have questions:

1. **Check the Issues**: Look through existing GitHub issues
2. **Create an Issue**: Describe your problem with details
3. **Discussions**: Join the project discussions for general questions

**Made with ❤️ using Streamlit and Groq API**

*If you find this project helpful, please consider giving it a ⭐ on GitHub!*
