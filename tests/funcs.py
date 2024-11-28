import subprocess
import pytest
import psutil
import time
import os
import requests

def bin_runner(args):
    try:
        result = subprocess.run(
            ["./project/OptimusMuneris.exe"] + args,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.strip()


def get_ram():
    max_memory = 0
    time.sleep(3)
    for proc in psutil.process_iter(["pid", "name", "memory_info"]):
        try:
            if "optimusmuneris" in proc.info["name"].lower():
                memory_usage = proc.info["memory_info"].rss / (1024 * 1024)
                if memory_usage > max_memory:
                    max_memory = memory_usage
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if max_memory > 0:
        return float(f"{max_memory:.2f}")
    else:
        return None


def dubai_weather():
    api_key = os.getenv("APIKEY")
    endpoint = "https://api.weatherapi.com/v1/current.json"
    location = "Dubai"

    response = requests.get(endpoint, params={"key": api_key, "q": location})
    response.raise_for_status()

    data = response.json()
    result = str (data["current"]["temp_c"])
    return result
