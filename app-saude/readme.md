# App Saúde - Sistema de Agendamento Hospitalar

Este é um projeto desenvolvido como atividade acadêmica para criar um sistema simples de agendamento de consultas em hospitais. O projeto foi feito com Flask no backend e HTML, CSS e JavaScript puro no frontend.

## Como Desenvolvemos o Projeto

1. **Configuração Inicial**
   - Criamos o ambiente Flask e configuramos o banco de dados SQLite para armazenar os dados.
   - Definimos as configurações básicas em um arquivo `config.py` e inicializamos o SQLAlchemy em `database.py`.

2. **Modelos de Dados**
   - Em `models.py`, definimos as tabelas necessárias: usuários, hospitais, especialidades, médicos, agendamentos e administradores.
   - Os modelos foram criados para permitir relacionamentos, por exemplo, cada agendamento se liga a um hospital, especialidade e médico.

3. **Modularização das Rotas**
   - Organizamos o código em vários arquivos de rotas na pasta `routes/` para separar as áreas do sistema:
     - **main_routes.py:** Para páginas públicas como a home.
     - **api_routes.py:** Para os endpoints de API que lidam com registro, login e agendamento (usados via AJAX).
     - **admin_auth_routes.py e admin_routes.py:** Para o login do administrador e a área administrativa.
     - **patient_auth_routes.py e patient_routes.py:** Para o registro, login e área do paciente.
   
4. **Templates HTML**
   - Criamos os arquivos HTML na pasta `templates/` usando Jinja2, que permite extender um template base (`base.html`).
   - As páginas incluem a home, login e registro (para pacientes e administradores), painel do admin, área do paciente e tela de agendamento.
   - Adicionamos a tag meta viewport no `base.html` para garantir que as páginas sejam responsivas em dispositivos móveis.

5. **Estilização com CSS**
   - Desenvolvemos um arquivo de CSS (`static/css/style.css`) que importa uma fonte do Google e utiliza variáveis para cores, tamanhos e espaçamentos.
   - Utilizamos media queries para ajustar o layout em telas menores, garantindo que o site seja responsivo.

6. **Funcionalidades com JavaScript**
   - No arquivo `static/js/main.js`, implementamos scripts para enviar dados dos formulários via fetch (para login e registro) e para melhorar a interatividade na tela de agendamento e administração (como filtros e botões de toggle).

7. **Integração das Áreas do Sistema**
   - Criamos a área do paciente para que, após o login, o usuário possa atualizar seu perfil e ver os agendamentos.
   - Na tela de agendamento, o paciente pode selecionar hospital, especialidade, médico, data e hora; o sistema mostra uma mensagem de sucesso e salva o agendamento.
   - Na área administrativa, o admin pode gerenciar os cadastros de usuários, hospitais, especialidades e médicos, usando seções colapsáveis e filtros para facilitar a navegação.
