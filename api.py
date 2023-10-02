import requests

def get_url(url: str):
    """
    Function that will call a provided GET API endpoint url and return its status code and either its content or error message as a string

    Parameters
    ----------
    url : str
        URL of the GET API endpoint to be called

    Returns
    -------
    int
        API call response status code
    str
        Text from API call response or error message
    """
    try:
        # Make a GET request to the provided URL
        response = requests.get(url)

        # Get the response status code
        status_code = response.status_code

        if status_code == 200:
            # If the status code is 200 (OK), return the content as a string
            content = response.json()
            return status_code, content
        else:
            # If the status code is not 200, return an error message
            error_message = f"API call failed with status code {status_code}"
            return status_code, error_message
    except Exception as e:
        # Handle any exceptions that occur during the API call
        return 500, f"Error during API call: {str(e)}"

# Example usage:
host = 'api.frankfurter.app'
api_url = f"https://api.frankfurter.app/latest?amount=10&from=GBP&to=USD"
status_code, response_text = get_url(api_url)
print(f"Status Code: {status_code}")
print(f"Response Text: {response_text}")


