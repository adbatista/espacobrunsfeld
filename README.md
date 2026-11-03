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

## Publicação (GitHub Pages)
O workflow `.github/workflows/pages.yml` gera o site com Jekyll e publica no GitHub Pages a cada push na `main` (também dá para rodar manualmente em *Actions*).

Para ativar, uma vez só:
1. O GitHub Pages só publica repositório **público**, a não ser no plano pago (GitHub Pro). Se o repositório for privado, mude em **Settings → General → Danger Zone → Change visibility**, ou assine o Pro.
2. Em **Settings → Pages → Build and deployment → Source**, escolha **GitHub Actions**.
3. Em *Actions*, rode de novo o workflow "Publicar no GitHub Pages".

O endereço fica `https://adbatista.github.io/espacobrunsfeld/`; o workflow ajusta o `baseurl` sozinho. Para usar domínio próprio, configure em **Settings → Pages → Custom domain**.

Capturas de tela do resultado ficam em `docs/previews/`.
