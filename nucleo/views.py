from django.http import HttpResponse

def hola_mundo(request):
    """
    Una vista simple que retorna un saludo en HTML.
    """
    html_content = """
    <div style='font-family: sans-serif; text-align: center; padding-top: 50px;'>
        <h1>¡Vienvenido a Meli Shop!</h1>
        <p>Vienvenido a la tienda de ropa con los mejores presios y calidad</p>
        <p>¡Disfruta de tu experiencia!</p>
    </div>
    """
    return HttpResponse(html_content)