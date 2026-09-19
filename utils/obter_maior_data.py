from datetime import datetime

def obter_maior_data (batch):
    return max(
        datetime.fromisoformat (
            registro["updeted_at"].replace("Z", "+00:00")
        )
        for registro in batch
    )