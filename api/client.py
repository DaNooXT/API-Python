from api.request import do_request

def buscar_paginas (url, last_update_at=None):
    page = 1

    while True:
        response = do_request (
            url,
            page,
            last_update_at
        )

        data = response.json()

        if not data:
            break

        yield page, data

        page += 1