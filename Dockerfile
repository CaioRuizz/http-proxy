# Use a imagem oficial do Python como base
FROM python:3.9

# Configuração do ambiente
WORKDIR /app
COPY requirements.txt /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos do aplicativo para o contêiner
COPY server.py /app

# Define a porta em que o aplicativo estará escutando
EXPOSE 5000

# Comando para executar o aplicativo quando o contêiner iniciar
CMD ["python", "server.py"]
