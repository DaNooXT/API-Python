import logging

from config import API_URL

from pipeline.baching import gerar_bach
from pipeline.transform import trasform_dados
from database.salvar_batch import salvar_batch
from database.checkpoint import obter_checkpoint, salvar_checkpoint
from database.connection import db

logging.basicConfig (
    level=logging.INFO,
    format= "%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

PIPELINE_NAME = "cu"


def executar_pipeline (url):

    logger.info("Pipeline iniciada")
    logger.info("Endpoint: %s", url)

    total_batches = 0
    total_registros = 0

    ultima_atualizacao = obter_checkpoint (
        PIPELINE_NAME,
        db
    )

    logger.info(
        "Checkpoint encontrado | última atualização=%s",
        ultima_atualizacao,
    )

    try:
        for page, batch in gerar_bach(url, ultima_atualizacao):
            total_batches += 1

            logger.info("Batch recebido | Registros=%d", len(batch))

            dados_transformados = trasform_dados(batch)

            logger.info(
                "Batch %d transformado | registros=%d",
                total_batches,
                len(dados_transformados)
            )

            salvar_batch(dados_transformados, db)

            salvar_checkpoint (
                PIPELINE_NAME,
                dados_transformados,
                db
            )

            total_registros += len(dados_transformados)

            logger.info(
                "Batch %d salvo com sucesso | total_registros=%d",
                total_batches,
                total_registros
            )

        logger.info(
            "Pipeline finalizada com sucesso | batches=%d | registros=%d",
            total_batches,
            total_registros
        )

    except Exception:
        logger.exception(
            "Pipeline interrompida por erro | batches_processados=%d | "
            "registros_processados=%d",
            total_batches,
            total_registros
        )

        raise


def main():
    executar_pipeline(API_URL)


if __name__ == "__main__": 
    main()