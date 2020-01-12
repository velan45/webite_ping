import urllib.request as urlfunc
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from datetime import datetime


def website_status_check(my_urls):
    if urlfunc.urlopen(my_urls).getcode() == 200:
        curr_time = datetime.now()
        formatted_time = curr_time.strftime('%M:%S.%f')
        print(f"{my_urls} is up time:{formatted_time}")
        return None
    else:
      curr_time = datetime.now()
      formatted_time = curr_time.strftime('%M:%S.%f')
      print(f"{my_urls} is down:{formatted_time}")
      return none
      
def concurrent_function(urls):
  with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(website_status_check, url)for url in urls]
    for future in as_completed(futures):
      future.result()

  

if __name__ == '__main__':
  urls=["http://www.google.com",  "http://www.facebook.com"]


for _ in range(10):
  concurrent_function(urls)
