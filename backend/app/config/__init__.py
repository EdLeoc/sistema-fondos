from pydantic_settings import BaseSettings
from pydantic import EmailStr

class Settings(BaseSettings):
    MAIL_USERNAME: str = "edleoc86@gmail.com"
    MAIL_PASSWORD: str = "zkxx fzoo xfge zfwd"
    MAIL_FROM: EmailStr = "edleoc86@gmail.com"
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    MAIL_FROM_NAME: str = "Notificación registro a nuevo Fondo"

    # Configuración de Twilio
    TWILIO_ACCOUNT_SID: str = "ACe8ae20d40445f88e82efcc23c2481663"
    TWILIO_AUTH_TOKEN: str = "607d521b63ae473ca3a2c37bc2362bef"
    TWILIO_PHONE_NUMBER: str = "+19255280265"

settings = Settings()