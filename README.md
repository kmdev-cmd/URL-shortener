# 🚀 Encurtador de Links

Encurtador de URLs com autenticação, dashboard e contagem de cliques.

## ✨ Funcionalidades

- Encurtar URLs (automático ou personalizado)
- Login e registro
- Contagem de cliques
- Dashboard do usuário
- Tema claro / escuro
- Português e Inglês
- API REST

## 📁 Estrutura

```
encurtador-links/
├── frontend/
├── shortener-api/
└── README.md
```


## 🔗 Endpoints principais

### Auth
- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`

### URLs
- `POST /api/v1/urls/`
- `GET /api/v1/urls/`
- `DELETE /api/v1/urls/{id}`

### Redirecionamento
- `GET /{short_code}`

## 🔒 Segurança

- Autenticação via token
- Senhas com hash
- Validação de dados

## 📝 Licença

Open source. Uso livre.
