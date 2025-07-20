# Python Weather Command-Line App

A simple yet robust command-line application built with Python that fetches and displays current weather information for any specified city using the OpenWeatherMap API.

---

## ✨ Features

* **Current Weather Data:** Retrieves real-time temperature, weather conditions (main, description), "feels like" temperature, humidity, and wind speed.
* **City-Specific Search:** Easily get weather data for any city by providing its name as a command-line argument.
* **Robust Error Handling:** Gracefully handles various issues including:
    * Network connection errors.
    * Invalid city names (404 errors from API).
    * Invalid API keys (401 errors from API).
    * Unexpected API response formats.
    * Missing data in the API response.
* **Configurable API Key:** Supports setting the API key directly in the script or overriding it via a command-line argument for flexibility.
* **Clear Output:** Presents weather information in an easy-to-read, formatted manner.

---

## 🛠️ Technologies Used

* **Python 3.x**
* **`requests` library:** For making HTTP requests to the OpenWeatherMap API.
* **`argparse` module:** For parsing command-line arguments.
* **OpenWeatherMap API:** Free tier for current weather data.

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

* [Python 3.6+](https://www.python.org/downloads/)
* **`requests` library**:
    ```bash
    pip install requests
    ```

### OpenWeatherMap API Key

1.  **Sign up for a FREE account** on [OpenWeatherMap](https://openweathermap.org/).
2.  Navigate to "My API keys" from your profile dropdown.
3.  Generate or locate your API key.
4.  **Important:** It can take a few minutes (sometimes up to an hour) for a newly generated API key to become active.

### Installation & Setup

1.  **Clone the repository** (or download the files):
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/python_weather_app.git](https://github.com/YOUR_GITHUB_USERNAME/python_weather_app.git)
    cd python_weather_app
    ```
    (Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username).
2.  **Open `weather_cli.py`** in your text editor.
3.  **Replace the placeholder `YOUR_OPENWEATHERMAP_API_KEY`** with your actual OpenWeatherMap API key:
    ```python
    API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY' # Paste your key here
    ```
    (Remember to keep this key private in a real-world scenario by using environment variables).
4.  Save the file.

---

## 💡 How to Use

Run the script from your terminal:

```bash
python weather_cli.py <city_name>

## 🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

