from sqlalchemy.orm import Session

from database.models import PipelineCheckpoint
from utils.obter_maior_data import obter_maior_data


def obter_checkpoint (pipeline_name, db):

    with Session(db) as session:

        checkpoint = session.get (
            PipelineCheckpoint,
            pipeline_name
        )

        if checkpoint is None:
            return None

        return checkpoint.last_update_at


def salvar_checkpoint (pipeline_name, batch, db):

    with Session(db) as session:

        last_update_at = obter_maior_data(batch)

        try:
            checkpoint = session.get (
                PipelineCheckpoint,
                pipeline_name
            )

            if checkpoint is None:

                checkpoint = PipelineCheckpoint (
                    pipeline_name=pipeline_name,
                    last_update_at=last_update_at
                )

                session.add(checkpoint)

            else:

                checkpoint.last_update_at = last_update_at

            session.commit()

        except Exception:
            session.rollback()
            raise