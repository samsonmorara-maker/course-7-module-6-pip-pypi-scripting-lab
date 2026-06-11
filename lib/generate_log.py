import requests
from datetime import datetime
import os

def fetch_post():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    if response.status_code == 200:
        return response.json()

    return None


def write_post(post):
    filename = (
        f"post_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

    with open(filename, "w") as file:
        file.write(f"Title: {post['title']}\n\n")
        file.write(f"Body: {post['body']}")

    print(f"File saved as {filename}")


if __name__ == "__main__":
    print("Fetching data...")

    post = fetch_post()

    if post:
        write_post(post)
    else:
        print("Failed to fetch data.")