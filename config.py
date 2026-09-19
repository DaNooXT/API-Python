from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("API_URL")

if API_URL is None:
    raise ValueError("API_URL nao configurada")

URL_DATABASE = os.getenv("URL_DATABASE")

if URL_DATABASE is None:
    raise ValueError("URL_DATABASE nao configurada")

API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    raise ValueError("API_KEY nao configurada")