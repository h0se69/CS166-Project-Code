import httpx
import random
import threading

URL = f"http://127.0.0.1:9999/blog/api/upload-post"

def random_number():
	x = random.randint(-10_000, 10_000)
	return x


def spam_api():
    while True:
        random_num = random_number()
        try:
            httpx.get(f"{URL}/{random_num}")
        except:
            print("Server taking too long to respond!")



threads = {}

# create_threads
for x in range(100):
    threads[x] = threading.Thread(target=spam_api)


# Start_thread
for x in range(100):
    print(f"starting thread ID {x}")
    thread = threads[x]
    thread.start()