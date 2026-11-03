import os
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for f in ["banner.svg","fundo-marca.svg","foto-tele.svg"]:
    try: os.remove(os.path.join(D,"img",f))
    except FileNotFoundError: pass
NAV=[("index.html","Home"),("sobre.html","O Espaço"),("servicos.html","Serviços"),("cursos.html","Cursos"),("contato.html","Contato")]
LOGO='<a href="index.html" class="logo" aria-label="Página inicial"><img src="img/logo.svg" alt="[Logo]"></a>'
WA='<svg viewBox="0 0 32 32"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.7c-2 0-4-.5-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.7 10.7 0 1 1 16 26.7zm5.9-8c-.3-.2-1.9-1-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7 0a8.8 8.8 0 0 1-4.4-3.8c-.3-.6.3-.5 1-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.7 3.7 0 0 0-1.1 2.7 6.4 6.4 0 0 0 1.3 3.4 14.7 14.7 0 0 0 5.7 5c2.1.9 2.9 1 4 .8a3.4 3.4 0 0 0 2.2-1.6 2.8 2.8 0 0 0 .2-1.6c-.1-.2-.3-.3-.6-.5z"/></svg>'
ICW='<svg viewBox="0 0 32 32"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3z"/></svg>'
ICT='<svg viewBox="0 0 24 24"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>'
ICE='<svg viewBox="0 0 24 24"><path d="M2 5h20v14H2zm2 2v.5l8 5 8-5V7l-8 5z"/></svg>'
ICI='<svg viewBox="0 0 24 24"><path d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5zm0 2a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3zm5 3.5a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9zm0 2a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM17.5 5.5a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/></svg>'
def onda(cima,baixo,forma=1):
    d={1:"M0,70 C360,0 1080,130 1440,40 L1440,110 L0,110 Z",2:"M0,110 C400,10 900,10 1440,90 L1440,110 Z",3:"M0,40 C500,120 1000,-20 1440,60 L1440,110 L0,110 Z"}[forma]
    return f'<svg class="onda" viewBox="0 0 1440 110" preserveAspectRatio="none" style="background:{cima}"><path d="{d}" fill="{baixo}"/></svg>'
def page(fn,title,body):
    nav="".join(f'<li><a href="{h}"{" class=\"ativo\"" if h==fn else ""}>{t}</a></li>' for h,t in NAV)
    html=f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | [Nome do Espaço]</title>
<meta name="description" content="[SUBSTITUIR: descrição curta para o Google]">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Ledger&family=Merriweather:wght@300;400;700&family=Quicksand:wght@500;600&family=Red+Hat+Display:wght@500;600;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#conteudo">Pular para o conteúdo principal</a>
<div class="aviso">Versão de modelo: textos, fotos e logo entre [colchetes] devem ser substituídos pelo conteúdo real.</div>
<header class="header">
  <div class="barra">
    {LOGO}
    <button class="menu-btn" aria-label="Abrir menu" onclick="document.querySelector('.nav').classList.toggle('aberto')">&#9776;</button>
    <nav class="nav"><ul>{nav}</ul></nav>
  </div>
</header>
<main id="conteudo">
{body}
</main>
<footer class="rodape-eb" id="contato">
  <div class="container">
    <div>{LOGO}<p>[SUBSTITUIR: frase convidando a entrar em contato pelas redes sociais ou meios de contato.]</p><a class="insta" href="#" aria-label="Instagram">{ICI}</a></div>
    <div><h4>Contato</h4><ul><li><span class="ic">{ICW}</span>[(00) 0 0000-0000]</li><li><span class="ic">{ICT}</span>[(00) 0000-0000]</li><li><span class="ic">{ICE}</span>[email@dominio.com]</li></ul></div>
    <div><h4>Endereço</h4><p>[Rua, número - Bairro,]<br>[Cidade - UF, CEP]</p></div>
  </div>
</footer>
<footer class="rodape"><div class="container">[Crédito] - Todos os direitos reservados</div></footer>
<a class="topo" href="#" aria-label="Voltar ao topo">&#9650;</a>
<a class="whats" href="#" aria-label="Falar pelo WhatsApp">{WA}</a>
<script>
addEventListener('scroll',()=>document.querySelector('.header').classList.toggle('rolado',scrollY>40));
function carrossel(sel){{const it=[...document.querySelectorAll(sel)];if(!it.length)return null;let i=0;return d=>{{it[i].classList.remove('ativo');i=(i+d+it.length)%it.length;it[i].classList.add('ativo');}}}}
const passaHero=carrossel('.hero .slide'),passaEquipe=carrossel('.membro');
if(passaHero)setInterval(()=>passaHero(1),6000);
</script>
</body>
</html>
'''
    open(os.path.join(D,fn),"w").write(html)

def bloco(img,titulo,texto,btn,link,inverte=False,cls=""):
    return f'''<section class="bloco{' inverte' if inverte else ''} {cls}"><div class="container">
  <div class="midia"><div class="circulo"><img src="img/{img}" alt="[descrever a foto]"></div></div>
  <div class="texto"><h2 class="titulo">{titulo}</h2><p>{texto}</p><a class="btn" href="{link}">{btn}</a></div>
</div></section>'''

slides="".join(f'''<div class="container slide{' ativo' if i==1 else ''}">
  <h1>[Nome<br>do Espaço]<small>[Slogan do banner {i}]</small></h1>
  <div class="fotos"><div class="circulo"><img src="img/hero-1.svg" alt="[Foto da recepção]"></div><div class="circulo"><img src="img/hero-2.svg" alt="[Foto da sala]"></div></div>
</div>''' for i in (1,2))
home=f'''<section class="hero">
{slides}
<button class="seta esq" aria-label="Anterior" onclick="passaHero(-1)">&#8249;</button><button class="seta dir" aria-label="Próximo" onclick="passaHero(1)">&#8250;</button>
</section>
<div class="hero-onda">{onda("transparent","var(--bege)",3)}</div>
'''+bloco("foto-espaco.svg","O Espaço","[SUBSTITUIR: parágrafo sobre a história, a fundadora e a filosofia do Espaço. Este bloco tem um texto mais longo, justificado, em fonte serifada pequena, como no original.]","Saiba Mais","sobre.html")\
+bloco("foto-servicos.svg","Serviços","[SUBSTITUIR: parágrafo sobre a avaliação inicial completa e o método de atendimento.]","Conhecer","servicos.html",True)+f'''
<div class="faixa-branca"><div class="container"><div class="tele">
  <h2 class="titulo">Teleatendimento</h2><p>[SUBSTITUIR: convite para saber mais sobre o atendimento online.]</p><a class="btn branco" href="contato.html">Saiba Mais</a>
</div></div></div>
{onda("#fff","var(--bege)",2)}
'''+bloco("foto-cursos.svg","Cursos","[SUBSTITUIR: chamada sobre os cursos.]","Conhecer","cursos.html",cls="decor")
page("index.html","Home",home)

def cab(t,sub): return f'<div class="cabeca-pagina decor-dir"><div class="container"><h1 class="titulo">{t}</h1><p>{sub}</p></div></div>'
cards="".join(f'<a class="card-foto" href="#"><img src="img/servico.svg" alt="[Serviço {i}]"><span class="rotulo">[Serviço {i}]<i></i></span></a>' for i in range(1,7))
servicos=cab("Serviços","[SUBSTITUIR: frase de apoio da página de serviços]")+f'''<div class="metade-bege"><div class="container"><div class="cards-foto">{cards}</div></div></div>
<nav class="paginacao" aria-label="Páginas"><a class="ativo" href="#">1</a><a href="#">2</a><a href="#">3</a><a href="#">&#8250;</a></nav>'''
page("servicos.html","Serviços",servicos)

membros="".join(f'''<div class="container membro{' ativo' if i==1 else ''}">
  <div class="circulo"><img src="img/pessoa.svg" alt="[Foto do profissional {i}]"></div>
  <div><div class="topo-eq"><h2 class="titulo">Equipe</h2><div class="setas"><button aria-label="Anterior" onclick="passaEquipe(-1)">&#8249;</button><button aria-label="Próximo" onclick="passaEquipe(1)">&#8250;</button></div></div>
  <h3>[Nome do profissional {i}]</h3><ul><li>[Formação e ano]</li><li>[Pós-graduação]</li><li>[Especialização]</li><li>[Experiência]</li></ul><span class="papel">[Especialidade]</span></div>
</div>''' for i in range(1,7))
sobre=f'''<section class="bloco decor-dir" style="padding-top:60px"><div class="container">
  <div class="texto"><h1 class="titulo">O Espaço</h1><p>[SUBSTITUIR: texto institucional sobre a experiência, o protocolo de atendimento e as premissas da empresa.]</p></div>
  <div class="midia"><div class="circulo"><img src="img/hero-1.svg" alt="[Foto da recepção]"></div></div>
</div></section>
{onda("var(--bege)","#fff",2)}
<section class="branco"><div class="container mvv">
  <div class="cartao"><h3>Missão</h3><p>[SUBSTITUIR: missão]</p></div>
  <div class="cartao"><h3>Visão</h3><p>[SUBSTITUIR: visão]</p></div>
  <div class="cartao"><h3>Valores</h3><ul><li>[Valor 1]</li><li>[Valor 2]</li><li>[Valor 3]</li><li>[Valor 4]</li></ul></div>
</div></section>
{onda("#fff","var(--bege)",2)}
<section style="padding:10px 0 60px"><div class="container"><h2 class="titulo">Estrutura da Empresa</h2>
<div class="carrossel"><button class="seta esq" aria-label="Anterior">&#8249;</button><div class="galeria">{"".join(f'<img src="img/foto-espaco.svg" alt="[Foto do ambiente {i}]">' for i in range(1,5))}</div><button class="seta dir" aria-label="Próximo">&#8250;</button></div></div></section>
{onda("var(--bege)","#fff",2)}
<section class="branco equipe decor-dir">{membros}</section>'''
page("sobre.html","O Espaço",sobre)

cursos=cab("Cursos","[SUBSTITUIR: aviso de que mais informações sobre os cursos virão em breve.]")+'<div style="height:160px"></div>'
page("cursos.html","Cursos",cursos)

contato=cab("Contato","[SUBSTITUIR: frase de convite]")+f'''<section class="bloco" style="padding-top:20px"><div class="container">
<form class="form" onsubmit="event.preventDefault();alert('Formulário de exemplo: conecte a um serviço de envio (ex.: Formspree) ou ao WhatsApp.');">
<input placeholder="Nome" required><input type="email" placeholder="E-mail" required><input placeholder="Telefone / WhatsApp"><textarea rows="5" placeholder="Mensagem"></textarea><button class="btn" type="submit">Enviar</button></form>
<div class="mapa">[Mapa do Google: colar aqui o &lt;iframe&gt; do endereço]</div></div></section>'''
page("contato.html","Contato",contato)
