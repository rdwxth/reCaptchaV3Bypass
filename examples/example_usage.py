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

captcha = ReCaptchaV3Bypass("https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LcR_okUAAAAAPYrPe-HK_0RULO1aZM15ENyM-Mf&co=aHR0cHM6Ly9hbnRjcHQuY29tOjQ0Mw..&hl=en&v=Xv-KF0LlBu_a0FJ9I5YSlX5m&size=invisible&cb=578n1gvb5dgj")

token = captcha.bypass()
import requests

url = "https://antcpt.com/score_detector/verify.php"
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-GB,en;q=0.7",
    "content-type": "application/json",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Brave\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "x-requested-with": "XMLHttpRequest",
    "Referer": "https://antcpt.com/score_detector/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}
data = {
    "g-recaptcha-response": token
}

response = requests.post(url, headers=headers, json=data)

print(response.json()) # Our score will be low but this implementation shows the recaptcha token generated is valid
