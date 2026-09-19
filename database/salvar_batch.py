from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert

from database.models import Clientes

def salvar_batch (batch, db):

        with Session(db) as session:
            try:
                stmt = insert(Clientes).values(batch)

                stmt = stmt.on_conflict_do_update (
                    index_elements=["id"],
                    set_={
                        "nome": stmt.excluded.nome,
                        "email": stmt.excluded.email
                    }
                )

                session.execute(stmt)

                session.commit()

            except Exception:
                session.rollback()
                raise