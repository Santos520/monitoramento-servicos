# 📡 Monitoramento de Serviços

Sistema automatizado desenvolvido em Python para monitorar a disponibilidade de serviços web, identificar falhas e recuperações e enviar notificações pelo Telegram.

## 🎯 Objetivo

O projeto tem como objetivo automatizar o monitoramento de serviços web, reduzindo a necessidade de verificações manuais e permitindo identificar rapidamente quando um serviço fica indisponível ou volta a funcionar.

## 🚀 Funcionalidades

- Monitoramento de serviços por requisições HTTP.
- Verificação de respostas JSON.
- Identificação de serviços ONLINE e OFFLINE.
- Notificações automáticas pelo Telegram.
- Alertas de queda e recuperação de serviços.
- Registro de atividades em arquivo de log.
- Monitoramento automático a cada 5 minutos.
- Prevenção de notificações repetidas enquanto o programa permanece em execução.

## 🛠️ Tecnologias utilizadas

- Python
- Requests
- Schedule
- Python Dotenv
- Telegram Bot API
- Git e GitHub

## 📂 Estrutura do projeto

```text
monitoramento-servicos/
│
├── src/
│   ├── main.py
│   ├── monitor.py
│   └── notificacao.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── monitoramento.log
```

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Santos520/monitoramento-servicos.git
```

### 2. Entrar na pasta

```bash
cd monitoramento-servicos
```

### 3. Criar ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual no Windows

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto, utilizando o `.env.example` como modelo.

Configure:

```env
TELEGRAM_BOT_TOKEN=seu_token_aqui
TELEGRAM_CHAT_ID=seu_chat_id_aqui
```

**Importante:** nunca compartilhe ou publique seu token verdadeiro do Telegram.

### 7. Executar o monitoramento

Para realizar apenas uma verificação:

```bash
python src/main.py --once
```

Para iniciar o monitoramento automático:

```bash
python src/main.py
```

O sistema realizará verificações imediatamente e continuará monitorando os serviços a cada 5 minutos.

Para interromper a execução, pressione `Ctrl + C`.

## 📲 Notificações

O sistema utiliza um bot do Telegram para enviar alertas quando identifica mudanças no estado dos serviços.

Exemplos:

**Serviço indisponível:**

```text
⚠️ HTTPBin está OFFLINE!
```

**Serviço recuperado:**

```text
✅ RECUPERAÇÃO: HTTPBin voltou a ficar ONLINE!
```

## 📋 Registro de atividades

As informações das verificações são registradas no arquivo `monitoramento.log`, permitindo consultar os resultados e acompanhar o funcionamento do sistema.

## 🔒 Segurança

As informações privadas são armazenadas no arquivo `.env`, que está protegido pelo `.gitignore`.

O arquivo `.env.example` disponibiliza somente os nomes das variáveis necessárias para configurar o projeto.

## 👨‍💻 Autor

Desenvolvido por **Matheus Souza dos Santos**.

Projeto acadêmico da disciplina **Automação e Programabilidade em Redes**.

## 🔗 Repositório

[GitHub - monitoramento-servicos](https://github.com/Santos520/monitoramento-servicos)