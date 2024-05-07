#!/usr/bin/env python3
import time
import web

# URL to test
url = "http://google.com"

# Call get_page and print the result
start_time = time.time()
result = web.get_page(url)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
# print(result)

# Call get_page again and print the result
start_time = time.time()
result = web.get_page(url)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
# print(result)