# footballAPi
Este é um projeto de exemplo que utiliza Django para criar uma aplicação web para gerenciamento de competições esportivas, e consome a api de link https://www.football-data.org/, para catalogar campeonatos, times e partidas.

## Requisitos
* Python 3
* Pip (geralmente instalado junto com o Python)
* Virtualenv (opcional, mas recomendado para isolamento de ambiente)

## Instalação
1. Clone o repositório:
```bash
git clone https://github.com/Rychard2107/footballAPi.git
```
2. Crie e ative um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate (Linux/Mac)
venv\Scripts\activate (Windows)
```

3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```
## Executando o servidor de desenvolvimento
Após instalar as dependências, crie as migrações com:
```bash
python manage.py makemigrations
```
E aplique as migrações com:
```bash
python manage.py migrate
```
Com tudo pronto inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```
## Utilização
O projeto inclui funcionalidades para gerenciar competições esportivas, times e partidas. Você pode acessar todas as funcionalidades a partir da home:
http://localhost:8000
