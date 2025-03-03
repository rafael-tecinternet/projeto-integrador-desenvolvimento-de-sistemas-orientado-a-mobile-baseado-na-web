```markdown
# App Saúde - Sistema de Agendamento Hospitalar

Neste projeto, desenvolvemos um sistema simples de agendamento de consultas em hospitais. O sistema foi feito com Flask no backend e HTML, CSS e JavaScript puro no frontend.

## Tecnologias Usadas

- **Backend:** Python 3, Flask, Flask-SQLAlchemy, SQLite
- **Frontend:** HTML, CSS, JavaScript puro

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
app-saude/
├── app.py                  # Arquivo principal (inicializa a aplicação e registra as rotas)
├── config.py               # Configurações do Flask e banco de dados
├── database.py             # Inicialização do SQLAlchemy
├── models.py               # Modelos do banco de dados (usuários, hospitais, especialidades, médicos, agendamentos, admin)
├── routes/                 # Rotas divididas por área (públicas, admin e paciente)
│   ├── main_routes.py      # Rotas para a home e páginas públicas
│   ├── api_routes.py       # Endpoints da API para registro, login e agendamento (pacientes via AJAX)
│   ├── admin_auth_routes.py# Rotas para login do admin
│   ├── admin_routes.py     # Painel administrativo (cadastro e gerenciamento de dados)
│   ├── patient_auth_routes.py # Rotas para login e registro do paciente
│   └── patient_routes.py   # Área do paciente (perfil, agendamento, logout)
├── templates/              # Arquivos HTML (base, index, login, registro, dashboard, admin, etc.)
├── static/                 # Arquivos estáticos (CSS, JS, imagens)
│   ├── css/style.css       # CSS responsivo
│   └── js/main.js          # JavaScript para formulários e filtros
└── README.md               # Este arquivo
```

## Passo a Passo

1. **Configuração e Modelos:**
   - Configuramos o Flask e o SQLite no `config.py`.
   - Inicializamos o SQLAlchemy em `database.py` e definimos os modelos em `models.py`.

2. **Modularização das Rotas:**
   - As rotas foram divididas em blueprints na pasta `routes/`. Temos rotas para a área pública, para o admin e para o paciente.

3. **Templates HTML:**
   - Utilizamos Jinja2 para criar os templates, com um `base.html` que é estendido por todas as outras páginas.
   - As páginas incluem home, login, registro, área do paciente, agendamento e painel admin.

4. **Estilização e Responsividade:**
   - O CSS (em `static/css/style.css`) usa media queries para ser responsivo, garantindo boa aparência em dispositivos móveis.
   - O template `base.html` inclui a tag meta viewport para responsividade.

5. **Funcionalidades do Sistema:**
   - **Paciente:** Pode se registrar, fazer login, atualizar perfil e agendar consultas.
   - **Admin:** Pode se autenticar, gerenciar usuários, hospitais, especialidades e médicos.
   - **Agendamento:** O paciente escolhe hospital, especialidade, médico, data e hora. O sistema exibe confirmação e salva o agendamento.

6. **Interatividade com JavaScript:**
   - O JavaScript (em `static/js/main.js`) trata dos formulários de login e registro (via AJAX, se necessário) e inclui scripts para filtros e botões toggle nas páginas de admin.

## Como Executar

1. **Instale as Dependências:**
   - Crie um ambiente virtual e instale as bibliotecas necessárias (Flask, Flask-SQLAlchemy, etc.).
   - Exemplo:
     ```bash
     python -m venv venv
     venv\Scripts\activate      # Windows
     # ou
     source venv/bin/activate   # Linux/Mac
     pip install Flask Flask-SQLAlchemy
     ```

2. **Crie o Banco de Dados:**
   - Ao iniciar o aplicativo, o SQLite cria o arquivo `db.sqlite3` automaticamente (se necessário, delete o antigo para recriar o esquema).

3. **Execute a Aplicação:**
   ```bash
   python app.py
   ```
   - Acesse `http://127.0.0.1:5000/` no navegador.

## Conclusão

Este aplicativo mostra um sistema básico de agendamento hospitalar usando Flask e tecnologias web simples. Foi desenvolvido de forma modular e responsiva, com áreas diferenciadas para pacientes e administradores. Esse projeto serve como base para estudo e pode ser expandido com novas funcionalidades, conforme necessário.
```

