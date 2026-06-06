from django.shortcuts import render, get_object_or_404, redirect
from .models import Estado, Municipio, Bairro
from django.http import JsonResponse
from cadastros.models import PontoTuristico

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
from geopy.adapters import RequestsAdapter
import ssl
import certifi

# Create your views here.
def listar_estados(request):
    estados = Estado.objects.all()

    dados = {
        'estados': estados
    }

    return render(request,'estados/listar.html',dados)

def detalhes_estado(request,id):
    estado= get_object_or_404(Estado,id=id)

    dados= {
        'estado': estado
    }
    return render(request,'estados/detalhes.html',dados)

def cadastrar_estado(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sigla = request.POST.get('sigla')
        região = request.POST.get('regiao')

        Estado.objects.create(
            nome=nome, sigla=sigla, regiao=região
        )

        return redirect('listar_estados')
    else:
        return render(request, 'estados/form.html')

def editar_estado(request,id):
    estado= get_object_or_404(Estado,id=id)

    if request.method == 'POST':
        estado.nome = request.POST.get('nome')
        estado.sigla = request.POST.get('sigla')
        estado.região = request.POST.get('regiao')

        estado.save()

        return redirect('listar_estados')
    
    else:
        dados= {
            'estado': estado
        }

        return render(request,'estados/form.html' , dados)

def apagar_estado(request,id):
    estado= get_object_or_404(Estado,id=id)

    if request.method == 'POST':
        estado.delete()
        return redirect ('listar_estados')

    else:
        dados= {
            'estado': estado
        }

        return render(request,'estados/apagar.html', dados)


def listar_municipios(request):
    municipios = Municipio.objects.all()

    dados = {
        'municipios': municipios
    }

    return render(request,'municipios/listar.html',dados)

def detalhes_municipio(request,id):
    municipio= get_object_or_404(Municipio,id=id)

    dados= {
        'municipio': municipio
    }
    return render(request,'municipios/detalhes.html',dados)

def cadastrar_municipio(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        populacao = request.POST.get('populacao')
        estado = request.POST.get('estado')

        Municipio.objects.create(
            nome=nome, populacao=populacao, estado=estado
        )

        return redirect('listar_municipios')
    else:
        dados= {
            'estados': Estado.objects.all()
        }
        return render(request,'municipios/form.html', dados)



def listar_bairros(request):
    bairros = Bairro.objects.all()

    dados = {
        'bairros': bairros
    }

    return render(request,'bairros/listar.html',dados)

def detalhes_bairro(request,id):
    bairro= get_object_or_404(Bairro,id=id)

    dados= {
        'bairro': bairro
    }
    return render(request,'bairros/detalhes.html',dados)

def municipios_por_estado(request,estado_id):
    municipios = Municipio.objects.filter(estado_id=estado_id).values('id','nome')
    return JsonResponse(list(municipios),safe=False)

def bairros_por_municipio(request, municipio_id):
    bairros = Bairro.objects.filter(municipio_id=municipio_id).values('id','nome')
    return JsonResponse(list(bairros),safe=False)

def pontos_por_municipio(request, municipio_id):
    pontos = PontoTuristico.objects.filter(municipio_id=municipio_id).values('id','nome')
    return JsonResponse(list(pontos),safe=False)

def ponto_json(request, id):
    ponto = PontoTuristico.objects.filter(id=id).values('id','nome','descricao','latitude','longitude')
    return JsonResponse(list(ponto),safe=False)

def buscar_coordenadas_por_estado(ponto):
    endereco_completo = f'{ponto.logradouro}, {ponto.numero}, {ponto.bairro}, {ponto.municipio}, {ponto.estado}, Brasil'
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    geolocator = Nominatim(
        user_agent = "crud_estado_municipio",
        adapter_factory= lambda **kwargs: RequestsAdapter(
            ssl_context= ssl_context
        )
    )

    try:
        localizacao = geolocator.geocode(
            endereco_completo, timeout = 10
        )
        if localizacao:
            ponto.latitude = localizacao.latitude
            ponto.longitude = localizacao.longitude 
            ponto.save()
    except (GeocoderTimedOut, GeocoderUnavailable):
        pass

