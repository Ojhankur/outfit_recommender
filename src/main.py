from weather_fetcher import get_weather
from outfit_recommender import recommend_outfit

def main():
    try:
        
        temp,weather_desc,q=get_weather()
        outfit=recommend_outfit(temp, weather_desc)
        print(f"The temperature in {q} is {temp}C with {weather_desc}")
        print(f"Recommend outfit:{outfit}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()