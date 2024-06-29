import requests, time


def calculateTime(page):
    start_time = time.time()  
    response = requests.get(page)
    end_time = time.time()
    return end_time - start_time


page = 'https://amazon.com'
duration = calculateTime(page)
print(f"Page loaded in {duration} seconds")