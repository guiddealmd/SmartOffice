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

Comandos Git sugeridos para criar um repositório e enviar os arquivos para o GitHub:
```bash
git init
git add simulador_smart_office.py smart_office_data.csv README_Fase3.md
git commit -m "Add simulator script and sample CSV"
git branch -M main
# crie um repositório no GitHub (via site) e copie a URL, então:
git remote add origin https://github.com/<seu-usuario>/SmartOffice-Dados.git
git push -u origin main
```

Se preferir criar um Gist, cole o conteúdo de `simulador_smart_office.py` e `smart_office_data.csv` (ou apenas o script + CSV gerado) em um novo gist no https://gist.github.com/.

Arquivo zip com os entregáveis: `fase3_entregaveis.zip`
