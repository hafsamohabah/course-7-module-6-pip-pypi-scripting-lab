
import json
import requests


def fetch_data():
    """Fetch a sample post from a public API."""
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


def save_data(data, filename="fetched_post.txt"):
    """Save API data to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"API data saved to {filename}")


if __name__ == "__main__":
    post = fetch_data()
    save_data(post)

    print(
        "Fetched Post Title:",
        post.get("title", "No title found")
    )
