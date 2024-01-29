from dotenv import load_dotenv
import os

def load_api_key():
    """
   Loads the API key from the .env file.

   Loads the .env file using the `load_dotenv` function, then retrieves
   the API key stored in the "API_KEY" environment variable.

   Returns:
       str: The API key value, or None if the key is not found.
   """
    # Load the environment variables from the .env file
    load_dotenv()
    # Retrieve the API key from the environment variables
    api_key = os.environ.get("API_KEY")
    return api_key