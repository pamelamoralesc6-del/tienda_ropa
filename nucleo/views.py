from django.http import HttpResponse

def hola_mundo(request):
    """
    Una vista simple que retorna un saludo en HTML.
    """
    html_content = """
    <!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Artículo · Meli Shop</title>
  <link rel="stylesheet" href="blog.css" />
</head>
<body>
  <header class="site-header">
    <div class="container">
      <h1><a href="blog.html" class="home-link">← Blog</a></h1>
    </div>
  </header>

  <main class="container">
    <article id="article" class="post-full">
      <!-- El contenido será cargado por JS según el id en la URL (hash) -->
      <h2 id="title">Cargando...</h2>
      <p class="meta" id="meta"></p>
      <img id="hero" src="" alt="" style="max-width:100%;border-radius:8px;margin:12px 0;">
      <div id="body" class="post-body"></div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>© Meli Shop · Blog</p>
    </div>
  </footer>

  <script>
    // Datos de ejemplo: aquí puedes añadir más artículos o cargar desde JSON real
    const POSTS = {
      "1": {
        "title": "5 outfits frescos para el verano",
        "date": "28 nov 2025",
        "category": "Moda",
        "image": "https://via.placeholder.com/900x420?text=Outfit+Verano",
        "content": `
          <p>El verano pide prendas ligeras y combinaciones sencillas. Aquí tienes cinco ideas rápidas:</p>
          <ol>
            <li><strong>Vestido midi + sandalias</strong> — ideal para días calurosos.</li>
            <li><strong>Pantalón chino + camiseta básica</strong> — look cómodo y pulido.</li>
            <li><strong>Shorts de tiro alto + blusa suelta</strong> — casual y fresco.</li>
            <li><strong>Mono corto + accesorios coloridos</strong> — fácil y con carácter.</li>
            <li><strong>Blazer ligero + jeans</strong> — para la noche cuando baja la temperatura.</li>
          </ol>
          <p>Consejo: apuesta por tejidos naturales (algodón, lino) y colores claros para reflejar el sol.</p>
        `
      },
      "2": {
        "title": "Cómo mezclar texturas: guía práctica",
        "date": "20 nov 2025",
        "category": "Outfits",
        "image": "https://via.placeholder.com/900x420?text=Mix+and+Match",
        "content": `
          <p>Combinar texturas puede elevar un outfit. Sigue estas reglas rápidas:</p>
          <ul>
            <li>Combina máximo 2-3 texturas por look.</li>
            <li>Usa una textura dominante y otras como acento.</li>
            <li>Piensa en contraste: seda + denim, cuero + lana.</li>
          </ul>
          <p>Ejemplo: un suéter de punto con falda satén y botas de cuero genera un contraste equilibrado.</p>
        `
      },
      "3": {
        "title": "10 tips para cuidar tu ropa y hacerla durar",
        "date": "15 nov 2025",
        "category": "Tips",
        "image": "https://via.placeholder.com/900x420?text=Tips+Ropa",
        "content": `
          <ol>
            <li>Lava a temperaturas moderadas.</li>
            <li>Usa bolsas para prendas delicadas.</li>
            <li>Séparalas por colores para evitar transferencias.</li>
            <li>Seca al aire cuando sea posible.</li>
            <li>Plancha según la etiqueta y por el revés si es necesario.</li>
            <li>Repara pequeños agujeros o botones sueltos enseguida.</li>
            <li>Guarda con perchas apropiadas para evitar deformaciones.</li>
            <li>Evita colgar prendas pesadas en perchas estrechas.</li>
            <li>Usa protectores contra polillas en lugares cerrados.</li>
            <li>No guardes ropa sucia — siempre limpia antes de almacenar.</li>
          </ol>
        `
      }
    };

    function loadPost() {
      // lee el id del hash, por ejemplo post.html#2
      const id = (location.hash || "#1").replace("#", "");
      const post = POSTS[id] || POSTS["1"];
      document.getElementById('title').textContent = post.title;
      document.getElementById('meta').textContent = `${post.category} · ${post.date}`;
      document.getElementById('hero').src = post.image;
      document.getElementById('hero').alt = post.title;
      document.getElementById('body').innerHTML = post.content;
      // scroll al inicio
      window.scrollTo(0, 0);
    }

    // cargar al abrir y cuando cambia hash
    window.addEventListener('load', loadPost);
    window.addEventListener('hashchange', loadPost);
  </script>
</body>
</html>
    """
    return HttpResponse(html_content)