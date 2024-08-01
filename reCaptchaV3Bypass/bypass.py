import requests
import re


class ReCaptchaV3Bypass:
    """
    Bypass the reCAPTCHA v3 challenge.
    Only works for some reCAPTCHA v3 challenges.
    """

    def __init__(self, target_url) -> None:
        self.target_url = target_url
        self.session = requests.Session()

    def extract_values(self, response_text) -> tuple[str, str, str, str]:
        """
        Extracts necessary values from the response text.
        """
        try:
            recaptcha_token = self._extract_value(
                r'type="hidden" id="recaptcha-token" value="(.*?)"',
                response_text)
            k_value = self._extract_value(r"&k=(.*?)&co", self.target_url)
            co_value = self._extract_value(r"&co=(.*?)&hl", self.target_url)
            v_value = self._extract_value(r"&v=(.*?)&size", self.target_url)
        except (AttributeError, TypeError) as e:
            print(f"Failed to extract values: {e}")
            return None, None, None, None

        return recaptcha_token, k_value, co_value, v_value

    @staticmethod
    def _extract_value(pattern, text) -> str:
        """
        Extracts a value from the text using the provided regex pattern.
        """
        match = re.search(pattern, text)
        return match.group(1) if match else None

    def get_response(self) -> requests.Response:
        """
        Sends a GET request to the target URL.
        """
        try:
            return self.session.get(self.target_url)
        except requests.exceptions.RequestException as e:
            print(f"Failed to send GET request: {e}")
            return None

    def post_response(self, recaptcha_token, k_value, co_value, v_value) -> requests.Response:
        """
        Sends a POST request to the reCAPTCHA API.
        """
        post_url = f"https://www.google.com/recaptcha/api2/reload?k={k_value}"
        post_data = self._generate_post_data(recaptcha_token, k_value, co_value, v_value)
        try:
            return self.session.post(post_url, data=post_data)
        except requests.exceptions.RequestException as e:
            print(f"Failed to send POST request: {e}")
            return None

    @staticmethod
    def _generate_post_data(recaptcha_token, k_value, co_value, v_value) -> dict:
        """
        Compiles the data to be sent in the POST request.
        """
        return {
            "v": v_value,
            "reason": "q",
            "c": recaptcha_token,
            "k": k_value,
            "co": co_value,
            "hl": "en",
            "size": "invisible",
            "chr": "%5B89%2C64%2C27%5D",
            "vh": "13599012192",
        }

    def extract_gtk(self, response_text) -> str:
        """
        Extracts the GTK value from the response text.
        """
        try:
            return self._extract_value(r'\["rresp","(.*?)"', response_text)
        except AttributeError:
            print("Failed to extract GTK. Check your regex pattern.")
            return None

    def bypass(self) -> str:
        """
        Combines all functions to bypass the reCAPTCHA
        """
        initial_response = self.get_response()
        if initial_response is None:
            return None

        recaptcha_token, k_value, co_value, v_value = self.extract_values(initial_response.text)
        if None in (recaptcha_token, k_value, co_value, v_value):
            return None

        post_response = self.post_response(recaptcha_token, k_value, co_value, v_value)
        if post_response is None:
            return None

        return self.extract_gtk(post_response.text)