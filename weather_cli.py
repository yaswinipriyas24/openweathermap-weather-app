import requests
import argparse
import json # Not strictly necessary for basic parsing but good to know

# --- Configuration ---
# REPLACE 'YOUR_API_KEY_HERE' with your actual OpenWeatherMap API Key
API_KEY = 'YOUR_API_KEY_HERE'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city_name, api_key):
    """
    Fetches current weather data for a given city from OpenWeatherMap API.

    Args:
        city_name (str): The name of the city.
        api_key (str): Your OpenWeatherMap API key.

    Returns:
        dict: A dictionary containing weather data if successful, None otherwise.
    """
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric' # You can change to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)
        weather_data = response.json()
        return weather_data
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Error: City '{city_name}' not found. Please check the spelling.")
        elif response.status_code == 401:
            print("Error: Invalid API Key. Please check your OpenWeatherMap API key.")
        else:
            print(f"HTTP error occurred: {http_err} (Status code: {response.status_code})")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error: Could not connect to the internet or OpenWeatherMap API: {conn_err}")
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f"Error: Request timed out: {timeout_err}")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected error occurred during the request: {req_err}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON response from API. Response was: {response.text}")
        return None


def display_weather(weather_data, city_name):
    """
    Prints formatted weather information to the console.
    """
    if not weather_data:
        return

    try:
        main_weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        country = weather_data['sys']['country']

        print(f"\n--- Current Weather in {city_name.title()}, {country} ---")
        print(f"Condition: {main_weather} ({description.title()})")
        print(f"Temperature: {temperature:.1f}°C (Feels like: {feels_like:.1f}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print("---------------------------------------")

    except KeyError as ke:
        print(f"Error: Missing expected data in API response. Key '{ke}' not found.")
        print(f"Full response for debugging: {json.dumps(weather_data, indent=2)}")
    except IndexError:
        print("Error: 'weather' array is empty or malformed in API response.")
        print(f"Full response for debugging: {json.dumps(weather_data, indent=2)}")
    except Exception as e:
        print(f"An unexpected error occurred while processing weather data: {e}")
        print(f"Full response for debugging: {json.dumps(weather_data, indent=2)}")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch current weather information for a specified city.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        'city',
        type=str,
        help="The name of the city to get weather for (e.g., 'London', 'New York', 'Eluru')."
    )
    # Optional argument for specifying API key directly (less secure for production but useful for testing)
    parser.add_argument(
        '--api-key',
        type=str,
        default=API_KEY, # Uses the default key from the script
        help="Optional: Your OpenWeatherMap API key.\n"
             "If not provided, uses the API_KEY defined in the script."
    )

    args = parser.parse_args()

    # Use the API key from args if provided, otherwise fallback to the script's default
    current_api_key = args.api_key if args.api_key != 'YOUR_API_KEY_HERE' else API_KEY

    if current_api_key == 'YOUR_API_KEY_HERE':
        print("Error: Please replace 'YOUR_API_KEY_HERE' in the script with your actual OpenWeatherMap API key,")
        print("or provide it via --api-key argument.")
        return

    print(f"Fetching weather for {args.city}...")
    weather_data = get_weather_data(args.city, current_api_key)

    if weather_data:
        display_weather(weather_data, args.city)
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()