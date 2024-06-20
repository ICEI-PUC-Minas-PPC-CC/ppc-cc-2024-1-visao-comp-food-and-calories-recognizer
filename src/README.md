## Preparando o Ambiente

1. Clone o Repositório: Antes de começar, clone o repositório do projeto para o seu local de trabalho usando git clone <URL_DO_REPOSITORIO>.
2. Navegue até a Raiz do Projeto: Abra o terminal e navegue até a pasta raiz do projeto usando o comando cd <nome_da_pasta_do_projeto>.
3. Acesse a pasta SRC.
4. Crie um Ambiente Virtual Python, executando o comando `python -m venv venv`, para criar uma nova pasta venv na raiz do projeto, onde as dependências serão armazenadas.
   - No Windows (PowerShell): `.\venv\Scripts\Activate.ps1`
   - No Windows (CMD): `.\venv\Scripts\Activate.bat`
   - No Linux/MacOS: `source venv/bin/activate`
5. Mova os arquivos `app.py` e `requirements.txt` para dentro da pasta venv
6. Instale as Dependências Necessárias: Com o ambiente virtual ativado, instale as dependências do projeto listadas no arquivo requirements.txt executando `pip install -r requirements.txt`.
Para Rodar utilize o seguinte comando : 
`python3 app.py`
