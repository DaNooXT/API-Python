from api.client import buscar_paginas

def gerar_bach (url, last_update_at=None):
    batch = []
    last_page = 0

    for page, pagina in buscar_paginas(url, last_update_at):

        batch.extend(pagina)
        last_page = page

        while len(batch) >= 500:
            batch_controle = batch[:500]
            batch = batch[500:]

            yield last_page, batch_controle


    if batch:
        yield last_page, batch