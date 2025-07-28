import requests

def get_random_fact():
    """
    Fetches a random useless fact from the API and prints it.
    """
    # The URL for the Useless Facts API
    api_url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    print("\nCalling the Useless Facts API...")
    try:
        # Make a GET request to the api_url
        response = requests.get(api_url)

        # A better way to check for success is using response.raise_for_status()
        # It will automatically raise an exception for bad status codes (4xx or 5xx).
        response.raise_for_status()

        # Parse the JSON response into a Python dictionary
        data = response.json()
        
        # Extract the fact text using its key
        fact = data['text'] 
        
        print("\n--- Your Random Fact ---")
        print(fact)
        print("------------------------\n")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def get_programming_joke():
    """
    Fetches a random programming joke from the JokeAPI and prints it.
    """
    # The URL for the JokeAPI (specifically for single-part programming jokes)
    api_url = "https://v2.jokeapi.dev/joke/Programming?type=single"
    
    print("\nCalling the JokeAPI...")
    try:
        # Make a GET request to the api_url
        response = requests.get(api_url)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()
        
        # Extract the joke using its key
        joke = data['joke']
        
        print("\n--- Your Programming Joke ---")
        print(joke)
        print("---------------------------\n")
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to run the interactive program, including the bonus challenge.
    """
    while True:
        print("--- API Detective Agency ---")
        print("1. Get a random useless fact")
        print("2. Get a random programming joke")
        print("3. Exit")
        
        choice = input("What would you like to do? (1/2/3): ")
        
        if choice == '1':
            get_random_fact()
        elif choice == '2':
            get_programming_joke()
        elif choice == '3':
            print("Closing the agency. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")
main()
