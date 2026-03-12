from enum import Enum

class CaptchaType(str, Enum):
    RECAPTCHA_V3 = "RecaptchaV3"
    RECAPTCHA_V2 = "RecaptchaV2"
    TURNSTILE = "Turnstile"