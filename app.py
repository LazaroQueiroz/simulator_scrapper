import os
import json
import simulator_scrapper as sim


if __name__ == "__main__":
    print("Welcome to your simulator scrapper.")
    config_file = open("config.json", "r")
    data = json.load(config_file)
    duration = int(input("set the duration time of the scrapping process: "))
    print("Initiating scrapping...")
    sim.start_scrapping(data, duration)
    print(f"Scraping finished. Look for {data['result_path']} to see your results")
