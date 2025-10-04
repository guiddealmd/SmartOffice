# Fase 3 - Entregáveis (Smart Office)

Este repositório contém os entregáveis da **Fase 3** do Dossiê de Planejamento Analítico do projeto *Smart Office*.

Arquivos:
- simulador_smart_office.py : Script Python que gera dados simulados de sensores (temperatura, luminosidade e ocupação) para um período de 7 dias, com registros a cada 15 minutos.
- smart_office_data.csv : Arquivo CSV gerado pelo script contendo os dados simulados.

Exemplo de uso (local):
```bash
# (opcional) criar e ativar um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate    # Windows PowerShell

pip install pandas numpy

# executar o script (gera smart_office_data.csv)
python simulador_smart_office.py
```
