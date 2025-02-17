# QuestioLabs - Estruturação e Roadmap

## Estrutura do Projeto

### **1. Autenticação e Segurança**
- **Sessões do Flask**: Utilizaremos sessões do Flask para gerenciar a autenticação do usuário.
- **Cadastro Simples**: O cadastro será apenas com usuário e senha, sem confirmação de e-mail. A senha será armazenada de forma segura usando **bcrypt** para hashing.

### **2. Modularização do Flask**
- **Blueprints**: O projeto será dividido em blueprints para organizar as funcionalidades:
  - `auth.py`: Para autenticação (login, logout, cadastro).
  - `questions.py`: Para gerenciamento de questões (criar, editar, filtrar, etc.).
  - `exams.py`: Para gerenciamento de provas (criar, visualizar, imprimir, etc.).
  - `main.py`: Para páginas estáticas (home, sobre nós, ajuda).
- **Separação de Camadas**:
  - **Models**: Definição das tabelas do banco de dados (SQLAlchemy).
  - **Routes**: Lógica de roteamento e manipulação de requisições.
  - **Services**: Lógica de negócio (ex: geração de provas, filtros, etc.).

### **3. Armazenamento de Rich Text**
- **Formato HTML**: O conteúdo do Quill.js será salvo como HTML no banco de dados.
- **Compatibilidade**: O HTML gerado pelo Quill.js será compatível com a exibição no frontend e com a funcionalidade de impressão.

### **4. Tags e Habilidades/Descritores**
- **Tabela de Tags**: Criaremos uma tabela separada para armazenar tags e habilidades/descritores.
- **Relação Muitos-para-Muitos**: As questões terão uma relação muitos-para-muitos com as tags.

### **5. Paginação e Filtros**
- **Paginação**: Utilizaremos **Flask-SQLAlchemy** para paginação, com opções de 10, 20, 50 e 100 questões por página.
- **Filtros Dinâmicos**: Os filtros por tags e habilidades serão implementados via consultas SQL dinâmicas no backend (Python).

### **6. Ordenação Aleatória de Alternativas**
- **Backend (Python)**: A aleatorização das alternativas será feita no backend.
- **Ligação Letra-Alternativa**: Após a aleatorização, o sistema comparará o texto da alternativa com o texto do gabarito para determinar a letra correta.

### **7. Recursos de Apoio Repetidos**
- **Comparação de Recursos**: O sistema comparará os recursos de apoio das questões durante a geração da prova.
- **Omissão de Repetidos**: Se duas questões tiverem o mesmo recurso de apoio, o recurso será exibido apenas na primeira questão.

### **8. Geração de PDF/Impressão**
- **CSS para Impressão**: Utilizaremos CSS específico (`@media print`) para estilizar a página de impressão.

### **9. Validação de Campos Obrigatórios**
- **Frontend (JavaScript)**: Validação em tempo real no frontend.
- **Backend (Flask-WTF)**: Validação robusta no backend usando Flask-WTF.

### **10. Testes e Deployment**
- **Testes**:
  - **Unitários**: Testes para funções individuais.
  - **Integração**: Testes para verificar a interação entre diferentes módulos.
  - **E2E**: Testes de ponta a ponta para simular o fluxo do usuário.
- **Deployment**:
  - **Local**: Para desenvolvimento e testes iniciais.
  - **Cloud**: Para deployment final, utilizando serviços como **Heroku**, **AWS** ou **Google Cloud**.

---

## Roadmap para o Desenvolvimento

### **Fase 1: Configuração Inicial e Autenticação**
**Duração:** 1 semana  
**Objetivo:** Configurar o ambiente de desenvolvimento e implementar a autenticação de usuários.

#### Tarefas:
1. Configurar o ambiente.
2. Implementar autenticação de usuários.
3. Configurar sessões do Flask.

---

### **Fase 2: Banco de Dados e Modelos**
**Duração:** 1 semana  
**Objetivo:** Criar os modelos do banco de dados e configurar o SQLAlchemy.

#### Tarefas:
1. Criar modelos para questões, provas, tags e habilidades.
2. Configurar migrações com Flask-Migrate.
3. Popular o banco de dados com dados de teste.

---

### **Fase 3: Páginas de Questões**
**Duração:** 2 semanas  
**Objetivo:** Implementar as funcionalidades relacionadas à criação, edição e listagem de questões.

#### Tarefas:
1. Criar templates para criação de questões.
2. Implementar listagem de questões com paginação e filtros.
3. Implementar edição e exclusão de questões.

---

### **Fase 4: Páginas de Provas**
**Duração:** 2 semanas  
**Objetivo:** Implementar as funcionalidades relacionadas à criação, edição e listagem de provas.

#### Tarefas:
1. Criar templates para criação de provas.
2. Implementar pré-visualização e salvamento de provas.
3. Implementar listagem de provas com paginação e filtros.
4. Configurar CSS para impressão.

---

### **Fase 5: Funcionalidades Adicionais**
**Duração:** 1 semana  
**Objetivo:** Implementar funcionalidades extras e ajustes finais.

#### Tarefas:
1. Criar páginas estáticas ("Sobre nós" e "Ajuda").
2. Adicionar validações e melhorias na interface.
3. Realizar testes finais.

---

### **Fase 6: Deployment e Entrega**
**Duração:** 1 semana  
**Objetivo:** Preparar o projeto para deployment e entrega final.

#### Tarefas:
1. Configurar ambiente de produção.
2. Fazer o deployment em um serviço de cloud.
3. Criar documentação do projeto.
4. Realizar testes finais em produção.

---

### **Cronograma Resumido**
| **Fase**                     | **Duração** | **Entrega Esperada**                     |
|-------------------------------|-------------|------------------------------------------|
| Configuração Inicial e Autenticação | 1 semana    | Ambiente configurado e autenticação funcional. |
| Banco de Dados e Modelos      | 1 semana    | Modelos do banco de dados criados e testados. |
| Páginas de Questões           | 2 semanas   | Funcionalidades de questões implementadas. |
| Páginas de Provas             | 2 semanas   | Funcionalidades de provas implementadas. |
| Funcionalidades Adicionais    | 1 semana    | Páginas estáticas e melhorias finais.   |
| Deployment e Entrega          | 1 semana    | Projeto em produção e documentado.      |

---

### **Considerações Finais**
- **Metodologia Ágil:** O projeto pode ser gerenciado usando metodologias ágeis (ex: Scrum), com sprints de 1 semana e reuniões diárias (daily meetings).
- **Priorização:** As funcionalidades mais críticas (autenticação, criação de questões e provas) devem ser priorizadas.
- **Feedback Contínuo:** Coletar feedback do cliente/usuário durante o desenvolvimento para ajustar o roadmap conforme necessário.
