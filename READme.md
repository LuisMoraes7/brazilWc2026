#🇧🇷 Brazil World Cup 2026 Analytics

Projeto de análise de dados da Brazil national football team com foco na 2026 FIFA World Cup.

O objetivo é coletar estatísticas da Seleção Brasileira em competições recentes e históricas para construir dashboards e gerar insights sobre as chances do Brasil na Copa do Mundo de 2026.

##🎯 Objetivos do Projeto
Analisar o desempenho do Brasil nas últimas Copas do Mundo.
Avaliar o desempenho nas Eliminatórias e na Copa América.
Comparar o retrospecto contra seleções favoritas (França, Espanha e Argentina).
Gerar arquivos em Excel para utilização em ferramentas de BI como Microsoft Power BI.

Os dados são obtidos por meio da API pública do Sofascore.

Dados coletados
Copa do Mundo 2014
Copa do Mundo 2018
Copa do Mundo 2022
Eliminatórias para a Copa de 2026
Copa América
Retrospecto (últimos 5 jogos) contra França, Espanha e Argentina

##📈 Arquivos Gerados
´´´
brazil_performance_last3wc.xlsx
´´´
Estatísticas do Brasil nas Copas de 2014, 2018 e 2022.

´´´
brazil_performance_2026.xlsx
´´´
Estatísticas do ciclo atual (Eliminatórias + Copa América).

´´´
brazil_favorites_against_matchs.xlsx
´´´

Resumo do retrospecto contra França, Espanha e Argentina.

##🐍 Configuração do Ambiente Python
1. Criar ambiente virtual
´´´
python3 -m venv venv
´´´

2. Ativar o ambiente virtual
Linux / macOS
´´´
source venv/bin/activate
´´´

Windows (PowerShell)
´´´
venv\Scripts\Activate.ps1
´´´
Windows (Prompt de Comando)
´´´
venv\Scripts\activate.bat
´´´

3. Instalar dependências
´´´
pip install pandas requests openpyxl
´´´
4. Executar o projeto
´´´
python main.py
´´´
5. Desativar o ambiente virtual
Linux / macOS / Windows
´´´
deactivate
´´´





Projeto desenvolvido para estudos em Análise de Dados, Engenharia de Dados e Business Intelligence.