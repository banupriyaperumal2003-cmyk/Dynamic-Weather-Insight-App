import requests
from rich.console import Console
from rich.table import Table
from rich import box

# Initialize console for colorful output
console = Console()

# ✅ Your API key
API_KEY = "038b611964713f25459770cef01cad1e"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            console.print(f"[red]Error fetching weather for '{city}'! Please check the city name.[/red]")
            return
        data = response.json()
        
        # Extract relevant information
        name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        desc = data['weather'][0]['description']

        # Add emojis based on weather
        weather_emoji = "☀️"
        if "cloud" in desc.lower():
            weather_emoji = "☁️"
        elif "rain" in desc.lower():
            weather_emoji = "🌧️"
        elif "storm" in desc.lower() or "thunder" in desc.lower():
            weather_emoji = "⛈️"
        elif "snow" in desc.lower():
            weather_emoji = "❄️"
        elif "mist" in desc.lower() or "fog" in desc.lower():
            weather_emoji = "🌫️"

        # Display weather in a table
        table = Table(title=f"Weather in {name}, {country} {weather_emoji}", box=box.ROUNDED, border_style="cyan")
        table.add_column("Parameter", style="yellow", no_wrap=True)
        table.add_column("Value", style="magenta")
        table.add_row("Temperature (°C)", str(temp))
        table.add_row("Humidity (%)", str(humidity))
        table.add_row("Pressure (hPa)", str(pressure))
        table.add_row("Wind Speed (m/s)", str(wind))
        table.add_row("Description", desc.title())

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

def main():
    console.print("[bold green]🌤️ Welcome to the Weather Prediction App! 🌤️[/bold green]")
    console.print("[bold yellow]Type the city name to get current weather or 'exit' to quit.[/bold yellow]")

    while True:
        city = console.input("\nEnter city name: ")
        if city.strip().lower() == "exit":
            console.print("[bold cyan]Thank you for using the Weather App! 🌈[/bold cyan]")
            break
        get_weather(city)

if __name__ == "__main__":
    main()