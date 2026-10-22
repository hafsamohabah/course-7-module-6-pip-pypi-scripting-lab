
import requests


def fetch_data():
    """Fetch a sample post from a public API."""
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
