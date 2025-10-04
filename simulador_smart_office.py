# simulador_smart_office.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parâmetros da simulação
inicio = datetime(2025, 10, 1, 0, 0, 0)
fim = inicio + timedelta(days=7)
intervalo = timedelta(minutes=15)

# Geração de timestamps
timestamps = []
current = inicio
while current < fim:
    timestamps.append(current)
    current += intervalo

# Função para gerar dados simulados
def gerar_dados():
    dados = []
    for ts in timestamps:
        hora = ts.hour
        # Temperatura: mais baixa à noite, mais alta no dia
        temperatura = np.random.normal(22, 1.5) if 8 <= hora <= 18 else np.random.normal(19, 1)
        # Luminosidade: 0 à noite, mais alta no dia
        luminosidade = 0 if hora < 6 or hora > 18 else max(0, np.random.normal(400, 50))
        # Ocupação: mais provável em horário comercial (probabilístico)
        if 8 <= hora <= 18:
            ocupacao = 1 if np.random.rand() > 0.2 else 0
        else:
            # menor probabilidade à noite e fins de semana
            ocupacao = 1 if np.random.rand() > 0.98 else 0
        dados.append([ts.isoformat(), "temp_sensor_01", round(float(temperatura), 2)])
        dados.append([ts.isoformat(), "lum_sensor_01", round(float(luminosidade), 2)])
        dados.append([ts.isoformat(), "occ_sensor_01", int(ocupacao)])
    return dados

# Criação do DataFrame e exportação para CSV
df = pd.DataFrame(gerar_dados(), columns=["timestamp", "sensor_id", "valor"])
df.to_csv("smart_office_data.csv", index=False)
print("smart_office_data.csv gerado com", len(df), "registros.")