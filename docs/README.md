# ReCaptchaV3Bypass Documentation

## Overview

`ReCaptchaV3Bypass` is a Python library designed to bypass certain reCAPTCHA v3 challenges. This documentation provides a detailed guide on how to use the library effectively.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Methods](#methods)
  - [extract_values](#extract_values)
  - [get_response](#get_response)
  - [post_response](#post_response)
  - [extract_gtk](#extract_gtk)
  - [bypass](#bypass)
- [Examples](#examples)
- [Running Tests](#running-tests)

## Installation

To install `ReCaptchaV3Bypass`, you can use `pip`. First, clone the repository, then navigate to the project directory and run:

```
git clone https://github.com/rdwxth/reCaptchaV3Bypass.git
cd reCaptchaV3Bypass
pip install .
```

## Quick Start

Here is an example of how to use the `ReCaptchaV3Bypass` library:

```
from reCaptchaV3Bypass.bypass import ReCaptchaV3Bypass

# Replace 'anchor_url' with the recaptcha anchor URL of the page you want to bypass
target_url = "anchor_url"
bypass = ReCaptchaV3Bypass(target_url)

# Perform the bypass
gtk_value = bypass.bypass()

# Print the extracted GTK value
print(f"Extracted GTK: {gtk_value}")
```

## Methods

### extract_values

Extracts necessary values from the response text.

#### Syntax

```
extract_values(response_text: str) -> tuple[str, str, str, str]
```

#### Parameters

- `response_text`: The HTML content of the target page as a string.

#### Returns

A tuple containing the extracted `recaptcha_token`, `k_value`, `co_value`, and `v_value`.

### get_response

Sends a GET request to the target URL.

#### Syntax

```
get_response() -> requests.Response
```

#### Parameters

None.

#### Returns

A `requests.Response` object containing the response from the GET request.

### post_response

Sends a POST request to the reCAPTCHA API.

#### Syntax

```
post_response(recaptcha_token: str, k_value: str, co_value: str, v_value: str) -> requests.Response
```

#### Parameters

- `recaptcha_token`: The extracted reCAPTCHA token.
- `k_value`: The extracted `k_value`.
- `co_value`: The extracted `co_value`.
- `v_value`: The extracted `v_value`.

#### Returns

A `requests.Response` object containing the response from the POST request.

### extract_gtk

Extracts the GTK value from the response text.

#### Syntax

```
extract_gtk(response_text: str) -> str
```

#### Parameters

- `response_text`: The HTML content of the response as a string.

#### Returns

The extracted GTK value as a string.

### bypass

Performs the bypass of the reCAPTCHA.

#### Syntax

```
bypass() -> str
```

#### Parameters

None.

#### Returns

The extracted GTK value as a string.

## Examples

You can find more examples in the `examples` directory. Here is a basic usage example:

```
from reCaptchaV3Bypass.bypass import ReCaptchaV3Bypass

# Replace 'anchor_url' with the recaptcha anchor URL of the page you want to bypass
target_url = "anchor_url"
bypass = ReCaptchaV3Bypass(target_url)

# Perform the bypass
gtk_value = bypass.bypass()

# Print the extracted GTK value
print(f"Extracted GTK: {gtk_value}")
```

## Running Tests

To run the tests, use the following command:

```
python -m unittest discover
```

## Support

If you have any questions or need help, feel free to open an issue on GitHub or contact the project maintainer.

---

**Disclaimer**: This tool is intended for educational purposes only. Misuse of this tool can result in legal consequences. Always ensure you have permission to perform any actions using this tool.
