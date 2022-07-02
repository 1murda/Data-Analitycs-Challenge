import requests
import csv
import os
import sys
from datetime import date
from utils import ( URLS,
                    BASE_DIR )

# download date
today: date = date.today()



def get_data(url: str, category: str) -> None:
    """ Get data from a given URL and write it to a csv file

    Args:
        url (str): url to get data from
    """
    # Get data from the url
    try:
            
        download = requests.get(url)
        
        decoded_content: str = download.content.decode('utf-8')
        
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        data = list(cr)

        # create the category folder if it doesn't exist
        dir = f"{BASE_DIR}/data/{category}/{str(today.year)}-{str(today.strftime('%B'))}"

        if not os.path.exists(dir):
            os.makedirs(dir)

        # Write data to a csv file in the category folder
        filename = f"{dir}/{category}-{str(today.day)}-{str(today.month)}-{str(today.year)}.csv"

        with open(filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)
                

    except Exception as e:
        print(f"Error al descargar {category}: {e}")


if __name__ == "__main__":
    for category, url in URLS.items():
        get_data(url, category)