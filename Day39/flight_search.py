class FlightSearch:

    def __init__(self):
        """
        Initialize an instance of the FlightSearch class.
        This constructor performs the following tasks:
        1. Retrieves the API key and secret from the environment variables 'AMADEUS_API_KEY'
        and 'AMADEUS_SECRET' respectively.
        Instance Variables:
        _api_key (str): The API key for authenticating with Amadeus, sourced from the .env file
        _api_secret (str): The API secret for authenticating with Amadeus, sourced from the .env file.
        _token (str): The authentication token obtained by calling the _get_new_token() method.
        """
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_SECRET"]
        # Getting a new token every time program is run. Could reuse unexpired tokens as an extension.
        self._token = self._get_new_token()