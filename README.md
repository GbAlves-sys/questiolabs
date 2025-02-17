# QuestioLabs - Ferramenta de Criação de Questões e Provas

## Descrição do Projeto

O **QuestioLabs** é uma ferramenta web desenvolvida para facilitar a criação, organização e gerenciamento de questões e provas. Voltado principalmente para educadores, professores e instituições de ensino, o projeto permite a criação de questões objetivas e discursivas, além da montagem de provas personalizadas com base em critérios como tags, habilidades e descritores.

---

## Funcionalidades Principais

### 1. **Autenticação de Usuários**
- Login e cadastro simples com usuário e senha.
- Sessões seguras para manter o usuário logado.

### 2. **Criação de Questões**
- Criação de questões objetivas e discursivas com suporte a rich text (formatação avançada).
- Adição de recursos de apoio, comandos, alternativas e gabaritos.
- Uso de tags e habilidades/descritores para organizar as questões.

### 3. **Banco de Questões**
- Listagem de todas as questões cadastradas.
- Filtros por tags e habilidades.
- Paginação para facilitar a navegação.

### 4. **Criação de Provas**
- Geração de provas aleatórias com base em filtros.
- Seleção manual de questões para montagem de provas.
- Pré-visualização e salvamento de provas.

### 5. **Banco de Provas**
- Listagem de todas as provas criadas.
- Filtros por tags e habilidades.
- Opção de visualizar, editar ou excluir provas.

### 6. **Impressão de Provas**
- Funcionalidade de impressão com layout otimizado para PDF.

### 7. **Interface Amigável**
- Uso de rich text (Quill.js) para edição de questões.
- Design responsivo e intuitivo.

---

## Tecnologias Utilizadas

- **Frontend:** HTML, CSS, JavaScript (com Quill.js para rich text).
- **Backend:** Python com Flask para lógica de negócio e autenticação.
- **Banco de Dados:** SQLite (com SQLAlchemy para ORM).
- **Deployment:** Serviços de cloud como Heroku, AWS ou Google Cloud.

---

## Objetivo do Projeto

O **QuestioLabs** tem como objetivo simplificar o processo de criação e gerenciamento de questões e provas, permitindo que educadores foquem mais no conteúdo e menos na organização. Com funcionalidades como filtros, tags e geração de provas aleatórias, a ferramenta busca ser uma solução completa para necessidades educacionais.

---

## Público-Alvo

- Professores e educadores.
- Instituições de ensino.
- Criadores de conteúdo educacional.

---

## Benefícios

- **Eficiência:** Reduz o tempo necessário para criar e organizar questões e provas.
- **Organização:** Uso de tags e habilidades para classificar e filtrar questões.
- **Flexibilidade:** Geração de provas aleatórias ou personalizadas.
- **Acesso Global:** Deployment em cloud para acesso de qualquer lugar.

---

# QuestioLabs - Estruturação e Roadmap

O **QuestioLabs** é uma solução moderna e eficiente para quem busca uma ferramenta completa e fácil de usar para gerenciar questões e provas. 🚀

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

### **Fase 1: Configuração Inicial e Autenticação (  )**
**Duração:** 1 semana  
**Objetivo:** Configurar o ambiente de desenvolvimento e implementar a autenticação de usuários.

#### Tarefas:
1. Configurar o ambiente.
2. Implementar autenticação de usuários.
3. Configurar sessões do Flask.

---

### **Fase 2: Banco de Dados e Modelos (  )**
**Duração:** 1 semana  
**Objetivo:** Criar os modelos do banco de dados e configurar o SQLAlchemy.

#### Tarefas:
1. Criar modelos para questões, provas, tags e habilidades.
2. Configurar migrações com Flask-Migrate.
3. Popular o banco de dados com dados de teste.

---

### **Fase 3: Páginas de Questões (  )**
**Duração:** 2 semanas  
**Objetivo:** Implementar as funcionalidades relacionadas à criação, edição e listagem de questões.

#### Tarefas:
1. Criar templates para criação de questões.
2. Implementar listagem de questões com paginação e filtros.
3. Implementar edição e exclusão de questões.

---

### **Fase 4: Páginas de Provas (  )**
**Duração:** 2 semanas  
**Objetivo:** Implementar as funcionalidades relacionadas à criação, edição e listagem de provas.

#### Tarefas:
1. Criar templates para criação de provas.
2. Implementar pré-visualização e salvamento de provas.
3. Implementar listagem de provas com paginação e filtros.
4. Configurar CSS para impressão.

---

### **Fase 5: Funcionalidades Adicionais (  )**
**Duração:** 1 semana  
**Objetivo:** Implementar funcionalidades extras e ajustes finais.

#### Tarefas:
1. Criar páginas estáticas ("Sobre nós" e "Ajuda").
2. Adicionar validações e melhorias na interface.
3. Realizar testes finais.

---

### **Fase 6: Deployment e Entrega (  )**
**Duração:** 1 semana  
**Objetivo:** Preparar o projeto para deployment e entrega final.

#### Tarefas:
1. Configurar ambiente de produção.
2. Fazer o deployment em um serviço de cloud.
3. Criar documentação do projeto.
4. Realizar testes finais em produção.

# Fluxo de Páginas do QuestioLabs

## 1. Página de Login
- **Descrição:** Primeira página ao acessar o site.
- **Funcionalidades:**
  - Campos para inserir usuário e senha.
  - Botão "Entrar" para autenticação.
  - Link para "Registrar-se" (leva à página de cadastro).
- **Próximas Páginas:**
  - Após o login, o usuário é redirecionado para a **Página Inicial**.

---

## 2. Página de Cadastro
- **Descrição:** Página para criação de uma nova conta.
- **Funcionalidades:**
  - Campos para cadastrar usuário e senha.
  - Botão "Registrar" para criar a conta.
  - Link para voltar ao login.
- **Próximas Páginas:**
  - Após o cadastro, o usuário é redirecionado para a **Página de Login**.

---

## 3. Página Inicial (Home Page)
- **Descrição:** Página principal após o login.
- **Funcionalidades:**
  - Mensagem de boas-vindas: "Bem-vindo ao QuestioLabs, (nome do usuário)".
  - Dois botões principais:
    - **"Questões"**: Leva à página de gerenciamento de questões.
    - **"Provas"**: Leva à página de gerenciamento de provas.
- **Próximas Páginas:**
  - O usuário pode navegar para **Questões** ou **Provas**.

---

## 4. Página de Questões
- **Descrição:** Página central para gerenciamento de questões.
- **Funcionalidades:**
  - Dois botões principais:
    - **"Banco de Questões"**: Leva à página que lista todas as questões cadastradas.
    - **"Criar Questão"**: Leva à página de seleção de tipo de questão (objetiva ou discursiva).
- **Próximas Páginas:**
  - O usuário pode navegar para **Banco de Questões** ou **Criar Questão**.

---

## 5. Banco de Questões
- **Descrição:** Página que lista todas as questões cadastradas.
- **Funcionalidades:**
  - Listagem de questões com paginação (10, 20, 50 ou 100 questões por página).
  - Filtros por tags e habilidades/descritores.
  - Botões de ação para cada questão:
    - **"Editar"**: Leva à página de edição da questão.
    - **"Apagar"**: Remove a questão do banco de dados.
    - **"Filtrar Similares"**: Aplica filtros para exibir questões semelhantes.
  - Botão **"Nova Questão"**: Leva à página de criação de questão.
- **Próximas Páginas:**
  - O usuário pode navegar para **Editar Questão**, **Criar Questão** ou aplicar filtros.

---

## 6. Criar Questão
- **Descrição:** Página para selecionar o tipo de questão a ser criada.
- **Funcionalidades:**
  - Dois botões:
    - **"Questão Objetiva"**: Leva à página de criação de questão objetiva.
    - **"Questão Discursiva"**: Leva à página de criação de questão discursiva.
- **Próximas Páginas:**
  - O usuário pode navegar para **Criar Questão Objetiva** ou **Criar Questão Discursiva**.

---

## 7. Criar/Editar Questão Objetiva
- **Descrição:** Página para criação ou edição de questões objetivas.
- **Funcionalidades:**
  - Campos rich text para:
    - Recurso de apoio.
    - Comando.
    - Alternativas (1 a 5).
    - Gabarito.
  - Campos simples para:
    - Etiquetas.
    - Habilidades/Descritores.
  - Botão **"Salvar"**: Salva a questão no banco de dados.
- **Próximas Páginas:**
  - Após salvar, o usuário é redirecionado para o **Banco de Questões**.

---

## 8. Criar/Editar Questão Discursiva
- **Descrição:** Página para criação ou edição de questões discursivas.
- **Funcionalidades:**
  - Campos rich text para:
    - Recurso de apoio.
    - Comando.
    - Gabarito.
  - Campo opcional para "Alternativa 1" (linhas adicionais).
  - Campos simples para:
    - Etiquetas.
    - Habilidades/Descritores.
  - Botão **"Salvar"**: Salva a questão no banco de dados.
- **Próximas Páginas:**
  - Após salvar, o usuário é redirecionado para o **Banco de Questões**.

---

## 9. Página de Provas
- **Descrição:** Página central para gerenciamento de provas.
- **Funcionalidades:**
  - Dois botões principais:
    - **"Banco de Provas"**: Leva à página que lista todas as provas cadastradas.
    - **"Criar Prova"**: Leva à página de seleção de tipo de prova (aleatória ou seleção manual).
- **Próximas Páginas:**
  - O usuário pode navegar para **Banco de Provas** ou **Criar Prova**.

---

## 10. Criar Prova
- **Descrição:** Página para selecionar o tipo de prova a ser criada.
- **Funcionalidades:**
  - Dois botões:
    - **"Prova Aleatória"**: Leva à página de geração de prova aleatória.
    - **"Selecionar Questões"**: Leva à página de seleção manual de questões.
- **Próximas Páginas:**
  - O usuário pode navegar para **Prova Aleatória** ou **Selecionar Questões**.

---

## 11. Prova Aleatória
- **Descrição:** Página para gerar uma prova com base em filtros.
- **Funcionalidades:**
  - Seleção de filtros (tags e habilidades/descritores).
  - Botão **"Pré-visualizar Prova"**: Exibe a prova gerada.
- **Próximas Páginas:**
  - Após a pré-visualização, o usuário pode **Salvar Prova**.

---

## 12. Selecionar Questões
- **Descrição:** Página para selecionar manualmente as questões da prova.
- **Funcionalidades:**
  - Listagem de questões com opção de seleção.
  - Botão **"Incluir Selecionadas"**: Adiciona as questões à prova.
  - Botão **"Pré-visualizar Prova"**: Exibe a prova gerada.
- **Próximas Páginas:**
  - Após a pré-visualização, o usuário pode **Salvar Prova**.

---

## 13. Pré-visualizar Prova
- **Descrição:** Página que exibe a prova gerada.
- **Funcionalidades:**
  - Exibição das questões seguindo a lógica de criação de provas.
  - Gabarito ao final da prova.
  - Botão **"Salvar Prova"**: Salva a prova no banco de dados.
- **Próximas Páginas:**
  - Após salvar, o usuário é redirecionado para o **Banco de Provas**.

---

## 14. Banco de Provas
- **Descrição:** Página que lista todas as provas cadastradas.
- **Funcionalidades:**
  - Listagem de provas com paginação.
  - Filtros por tags e habilidades/descritores.
  - Botões de ação para cada prova:
    - **"Visualizar"**: Exibe a prova completa.
    - **"Editar"**: Permite editar a prova.
    - **"Apagar"**: Remove a prova do banco de dados.
  - Botão **"Nova Prova"**: Leva à página de criação de prova.
- **Próximas Páginas:**
  - O usuário pode navegar para **Visualizar Prova**, **Editar Prova** ou aplicar filtros.

---

## 15. Visualizar Prova
- **Descrição:** Página que exibe uma prova completa.
- **Funcionalidades:**
  - Exibição das questões e gabarito.
  - Botão **"Imprimir Prova"**: Abre a janela de impressão do navegador.
- **Próximas Páginas:**
  - O usuário pode voltar ao **Banco de Provas**.

---

## 16. Páginas Estáticas
- **Sobre Nós** e **Ajuda**:
  - Páginas simples com texto informativo (ex: "Em construção").

---

## Resumo do Fluxo
1. **Login** → **Página Inicial** → **Questões** ou **Provas**.
2. **Questões** → **Banco de Questões** ou **Criar Questão**.
3. **Criar Questão** → **Questão Objetiva** ou **Questão Discursiva**.
4. **Provas** → **Banco de Provas** ou **Criar Prova**.
5. **Criar Prova** → **Prova Aleatória** ou **Selecionar Questões**.
6. **Pré-visualizar Prova** → **Salvar Prova** → **Banco de Provas**.
7. **Banco de Provas** → **Visualizar Prova** ou **Editar Prova**.

---