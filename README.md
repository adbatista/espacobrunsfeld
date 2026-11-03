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
| Banner da Home (imagem para computador e para celular) | `_data/banner.yml` |
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
Para receber as mensagens do formulário, configure um serviço de envio (ex.: Formspree) no `action` de `_includes/form-contato.html`. As fotos, o logo e os ícones em `assets/img/` vieram do site original. Todo texto entre `[colchetes]` ainda é espaço reservado. Quando o conteúdo real estiver no lugar, mude `aviso_modelo: false` em `_config.yml` para remover a faixa amarela.

## Publicação (GitHub Pages)
O workflow `.github/workflows/pages.yml` gera o site com Jekyll a cada push na `main` e publica o resultado na branch `gh-pages`. Também dá para rodar manualmente em *Actions*.

Em **Settings → Pages**, a fonte deve ser **Deploy from a branch**, com a branch **gh-pages** e a pasta **/ (root)**. O GitHub costuma ativar isso sozinho quando a branch `gh-pages` aparece pela primeira vez.

O endereço fica `https://adbatista.github.io/espacobrunsfeld/`. Para usar domínio próprio, configure em **Settings → Pages → Custom domain** e mude `baseurl` no workflow para `""`.

Capturas de tela do resultado ficam em `docs/previews/`.
