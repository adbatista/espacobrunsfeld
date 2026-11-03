# Espaço Brunsfeld

Site estático (HTML + CSS, sem build) recriando o layout de espacobrunsfeld.com.br.

## Como ver
Abra `index.html` no navegador. Páginas: `index.html`, `sobre.html`, `servicos.html`, `cursos.html`, `contato.html`.

## Estrutura
- `style.css`: estilos. As cores e fontes ficam como variáveis no topo do arquivo.
- `img/`: imagens. Todas são **espaços reservados** e precisam ser trocadas.
- `scripts/gerar_paginas.py`: gera os 5 HTML a partir do cabeçalho e rodapé compartilhados. Para mudar o cabeçalho, o rodapé ou o conteúdo, edite este script e rode `python3 scripts/gerar_paginas.py`.
- `docs/previews/`: capturas de tela do resultado.

## Conteúdo a substituir
Todo texto entre `[colchetes]`, o logo (`img/logo.svg`), as fotos em `img/`, os contatos e o endereço. Ao terminar, remova a faixa amarela de aviso (`<div class="aviso">` no script).

## Hospedagem
Por ser estático, pode ser publicado em GitHub Pages, Netlify ou qualquer hospedagem comum.
