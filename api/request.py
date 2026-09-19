import requests 
import time
import logging

from utils import RETRYABLE_STATUS_CODES, calculate_backoff
from config import API_KEY

session = requests.Session()

session.headers.update({
    "Authorization": f"Bearer {API_KEY}"
})

logger = logging.getLogger(__name__)

def do_request (url, page, last_update_at=None):
    max_retries = 5

    for tentativa in range(max_retries):

        params = {
            "page": page
        }

        if last_update_at is not None:
            params["updated_since"] = last_update_at.isoformat()
        
        try:
            response = session.get(
                url,
                params=params,
                timeout=(5, 30)
            )

            if response.status_code not in RETRYABLE_STATUS_CODES:
                return response

            retry_after = response.headers.get("Retry-After")

            if retry_after:
                delay = int(retry_after)
            else:
                delay = calculate_backoff(tentativa)

            logger.warning (
                f"HTTP {response.status_code} | Tentativa {tentativa + 1} / {max_retries} | Aguardando {delay:.2f}s."
            )

            time.sleep(delay) 

        except (
            requests.exceptions.Timeout,
            requests.exceptions.ConnectionError
        ):

            delay = calculate_backoff(tentativa)

            logger.warning (
                f"Erro de conexao | Tentativa {tentativa + 1} / {max_retries} | Aguardando {delay:.2f}s."
            )

            time.sleep(delay)

    raise RuntimeError("Maximo de tentatvas atingido")