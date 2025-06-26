# main.py
import random

def get_random_quote(filename="quotes.txt"):
    """
    Reads quotes from a file and returns a random one.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            quotes = [line.strip() for line in f if line.strip()] # Read lines, strip whitespace, ignore empty lines
        if not quotes:
            return "No quotes found in the file. Add some!"
        return random.choice(quotes)
    except FileNotFoundError:
        return f"Error: The quotes file '{filename}' was not found."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("--- Your Daily Dose of Inspiration ---")
    print(get_random_quote())
    print("-------------------------------------")
