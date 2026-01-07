# Exchange Worker 🚀

Sistema de monitoramento de cotação de dólar desenvolvido com **Python**, **Celery** e **RabbitMQ**, seguindo princípios de **Clean Architecture** e **Sistemas Distribuídos**.

## 🏗️ Arquitetura do Projeto

O projeto foi reestruturado para suportar escalabilidade e desacoplamento:
- **Domain/Services**: Contém a lógica de negócio (decisão de alertas e regras de processamento).
- **Infrastructure**: Responsável pela comunicação externa (escrita em arquivo TXT e integração com Slack Webhook).
- **Core (Celery App)**: Orquestração de tarefas assíncronas.

## 🛠️ Funcionalidades

- **Busca Automática**: Consulta a API de economia periodicamente via Celery Beat.
- **Processamento Assíncrono**: Uso de RabbitMQ como Message Broker para garantir que as tarefas não bloqueiem o sistema principal.
- **Múltiplos Consumidores (Fan-out)**:
  - **Histórico**: Grava cada cotação em um arquivo `.txt` com timestamp.
  - **Alerta Slack**: Se o dólar atingir o limite de **R$ 6,00**, um alerta em tempo real é enviado via Webhook para um canal dedicado no Slack.

## 🚀 Como rodar

1. **Suba o Broker**: `docker-compose up -d`
2. **Inicie o Worker**: `celery -A celery_app worker --loglevel=info -P solo`
3. **Inicie o Agendador (Beat)**: `celery -A celery_app beat --loglevel=info`

---
*Este projeto foi desenvolvido como parte de um desafio técnico para demonstrar conhecimentos em sistemas distribuídos e mensageria.*