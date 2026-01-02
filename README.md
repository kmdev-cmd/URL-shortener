# 🚀 Encurtador de Links - URL Shortener

Um encurtador de URLs moderno e completo com autenticação JWT, analytics de cliques, interface responsiva e suporte a internacionalização (Português/Inglês).

## ✨ Funcionalidades

- ✅ **Encurtamento de URLs** com códigos personalizados
- ✅ **Autenticação JWT** completa (registro/login)
- ✅ **Analytics de cliques** em tempo real
- ✅ **Interface responsiva** com tema claro/escuro
- ✅ **Internacionalização** automática (PT/EN)
- ✅ **Dashboard de links** do usuário
- ✅ **Redirecionamento automático**
- ✅ **API REST** completa

## 🛠️ Tecnologias

### Backend
- **Flask** - Framework web Python
- **Flask-JWT-Extended** - Autenticação JWT
- **Flask-SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados local

### Frontend
- **HTML5/CSS3** - Interface responsiva
- **JavaScript (ES6+)** - Lógica e API calls
- **Font Awesome** - Ícones
- **Google Fonts** - Tipografia

## 🚀 Como Executar Localmente

### Pré-requisitos
- Python 3.8+
- Git

### 1. Clone o repositório
```bash
git clone <seu-repo>
cd encurtador-links
```

### 2. Instale as dependências
```bash
cd shortener-api
pip install -r requirements.txt
```

### 3. Execute o backend
```bash
python -c "from app.main import app; app.run(host='0.0.0.0', port=8000, debug=True)"
```

### 4. Execute o frontend (em outro terminal)
```bash
cd frontend
python -m http.server 3000
```

### 5. Acesse no navegador
```
http://127.0.0.1:3000/index.html
```

## 🌐 Deploy no Railway

### 1. Crie uma conta gratuita
Acesse [railway.app](https://railway.app) e faça login com GitHub.

### 2. Crie um novo projeto
- Clique em "New Project"
- Selecione "Deploy from GitHub repo"
- Conecte seu repositório

### 3. Configure o deploy
O Railway detectará automaticamente que é um projeto Flask e fará o deploy.

### 4. Configure variáveis de ambiente (opcional)
No painel do Railway, vá em "Variables" e adicione:
```
SECRET_KEY=sua_chave_secreta_aqui
```

### 5. Deploy automático
O Railway fará o build e deploy automaticamente. Você receberá uma URL como:
```
https://encurtador-links-production.up.railway.app
```

## 🌍 Internacionalização (i18n)

O site detecta automaticamente o idioma do navegador:

- **Português** (`pt`, `pt-BR`, `pt-PT`)
- **Inglês** (todos os outros idiomas)

### Como adicionar novos idiomas

1. Edite o objeto `translations` em `frontend/script.js`
2. Adicione novas chaves conforme necessário
3. Atualize a função `detectLanguage()` se precisar

## 📁 Estrutura do Projeto

```
encurtador-links/
├── frontend/
│   ├── index.html          # Página principal
│   ├── styles.css          # Estilos CSS
│   ├── script.js           # JavaScript + i18n
│   └── test.html           # Página de testes
├── shortener-api/
│   ├── app/
│   │   ├── main.py         # App Flask principal
│   │   ├── models/         # Modelos SQLAlchemy
│   │   ├── core/           # Configurações
│   │   └── api/v1/         # Endpoints da API
│   ├── requirements.txt    # Dependências Python
│   ├── Dockerfile          # Container Docker
│   └── .env               # Variáveis de ambiente
└── README.md              # Este arquivo
```

## 🔗 Endpoints da API

### Autenticação
- `POST /api/v1/auth/register` - Registrar usuário
- `POST /api/v1/auth/login` - Fazer login

### URLs
- `POST /api/v1/urls/` - Encurtar URL (autenticado)
- `GET /api/v1/urls/` - Listar URLs do usuário (autenticado)
- `DELETE /api/v1/urls/{id}` - Deletar URL (autenticado)

### Redirecionamento
- `GET /{short_code}` - Redirecionar para URL original

## 🎨 Personalização

### Tema
O site suporta tema claro e escuro automaticamente.

### Cores
As cores podem ser personalizadas editando as variáveis CSS em `styles.css`.

### Idiomas
Adicione novos idiomas editando o objeto `translations` no JavaScript.

## 📊 Analytics

- **Contagem de cliques** em tempo real
- **Data de criação** dos links
- **URLs originais** preservadas
- **Dashboard** completo para usuários

## 🔒 Segurança

- **JWT tokens** para autenticação
- **Bcrypt** para hash de senhas
- **CORS** configurado adequadamente
- **Validação** de entrada de dados

## 📝 Licença

Este projeto é open source e pode ser usado livremente para fins educacionais e comerciais.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

---

**Feito com ❤️ usando Flask + JavaScript**
