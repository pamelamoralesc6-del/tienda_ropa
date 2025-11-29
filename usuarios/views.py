from django.shortcuts import render
def vista_autenticacion(request):
    """
    Renderiza la plantilla HTML de inicio de sesión y registro.
    """

    return render(request, 'index.html')
