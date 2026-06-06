from django.shortcuts import render, get_object_or_404, redirect
from .models import PontoTuristico, Avaliacao
from .forms import PontoTuristicoForm

# Create your views here.
def listar_pontos(request):
    pontos= PontoTuristico.objects.all()

    dados= {
        'pontos': pontos
    }

    return render(request, 'pontos/listar.html', dados)

def criar_ponto(request):
    if request.method == 'POST':
        form = PontoTuristicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pontos')
    else:
        form = PontoTuristicoForm()


    return render(request, 'pontos/form.html', {
        'form': form,
        'titulo': 'Cadastrar Ponto Turistico'
    })

def detalhes_ponto(request, id):
    ponto = PontoTuristico.objects.get(id=id)
    avaliacoes = Avaliacao.objects.filter(ponto=ponto)
    return render(request, 'pontos/detalhes.html', {
        'ponto': ponto,
        'avaliacoes': avaliacoes
    })




def editar_ponto(request, id):
    ponto = get_object_or_404(PontoTuristico, id=id)

    if request.method == 'POST':
        form = PontoTuristicoForm(request.POST, instance=ponto)
        if form.is_valid():
            form.save()
            return redirect('listar_pontos')
    else:
        form = PontoTuristicoForm(instance=ponto)

    return render(request, 'pontos/form.html', {
        'form': form,
        'titulo': 'Editar Ponto Turístico'
    })

def avaliar_ponto(request, id):
    ponto = PontoTuristico.objects.get(id=id)

    if request.method == 'POST':
        Avaliacao.objects.create(
            ponto=ponto,
            nome=request.POST.get('nome'),
            nota=request.POST.get('nota'),
            comentario=request.POST.get('comentario')
        )

    return redirect('detalhes_ponto', id=id)

def excluir_ponto(request, id):
    ponto = get_object_or_404(PontoTuristico, id=id)

    if request.method == 'POST':
        ponto.delete()
        return redirect('listar_pontos')

    return render(request, 'pontos/apagar.html', {'ponto': ponto})

def index_pontos(request):
    pontos = PontoTuristico.objects.all()

    return render(
        request,
        'pontos/index.html',
        {'pontos': pontos}
    )
    
