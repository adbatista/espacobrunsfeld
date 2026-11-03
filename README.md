# Espaço Brunsfeld

Site estático gerado com [Jekyll](https://jekyllrb.com/) (Ruby), recriando o layout de espacobrunsfeld.com.br.

## Rodar localmente
```sh
bundle install
bundle exec jekyll serve   # abre em http://localhost:4000
```
O site gerado fica em `_site/`.

## Onde editar
| O quê | Arquivo |
|---|---|
| Cabeçalho, rodapé, menu e scripts (comuns a todas as páginas) | `_layouts/default.html` |
| Itens do menu | `_data/nav.yml` |
| Telefone, WhatsApp, e-mail, Instagram, endereço | `_data/contato.yml` |
| Slides do banner da Home | `_data/banner.yml` |
| Serviços (um arquivo por serviço: vira card e página própria em `/servico/<nome>/`) | `_servicos/*.md` |
| Quantos serviços por página na listagem | `servicos_por_pagina` em `_config.yml` |
| Formulário "Envie uma Mensagem" (Contato e páginas de serviço) | `_includes/form-contato.html` |
| Mapa e links do Waze/Maps | `_data/contato.yml` |
| Equipe (carrossel em O Espaço) | `_data/equipe.yml` |
| Fotos da "Estrutura da Empresa" | `_data/estrutura.yml` |
| Conteúdo de cada página | `index.html`, `sobre.html`, `servicos.html`, `cursos.html`, `contato.html` |
| Cores e fontes (variáveis no topo) | `assets/style.css` |
| Imagens | `assets/img/` |
| Peças reutilizáveis (onda, bloco foto+texto, ícones) | `_includes/` |

## Conteúdo a substituir
Para receber as mensagens do formulário, configure um serviço de envio (ex.: Formspree) no `action` de `_includes/form-contato.html`. Todo texto entre `[colchetes]`, o logo (`assets/img/logo.svg`) e as fotos em `assets/img/` são espaços reservados. Quando o conteúdo real estiver no lugar, mude `aviso_modelo: false` em `_config.yml` para remover a faixa amarela.

## Publicação

**Netlify (recomendado com repositório privado):** crie uma conta grátis em netlify.com, clique em *Add new site → Import an existing project*, escolha este repositório e confirme. O `netlify.toml` já tem o comando de build. Cada merge na `main` publica sozinho.

**GitHub Pages:** só funciona de graça com repositório público. O workflow `.github/workflows/pages.yml` gera e publica o site no GitHub Pages a cada push na `main`. Para ativar, vá em **Settings → Pages → Source** e escolha **GitHub Actions**. Com domínio próprio, deixe `baseurl: ""` em `_config.yml`.

Capturas de tela do resultado ficam em `docs/previews/`.
