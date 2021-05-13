from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Produto, Pedido, Produto1
from .forms import pedidoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.exceptions import MultipleObjectsReturned
import csv, xlwt
import datetime
from django.views.generic import ListView, DetailView #querry 
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives, EmailMessage
from django.core import mail
import smtplib
from email.mime.text import MIMEText
# Create your views here.
from django.views.generic import View
from django.template.loader import get_template
from django.conf import settings
from django.db.models import Sum, Avg, Count





@login_required
def index(request):

    context={

    }
    return render(request,"home.html", context)

def contact(request):
    context={

    }
    return render(request, "contact.html", context)

@login_required
def pedido(request):
    pedidos = get.objects.all()

    
    return render(request, 'contact.html',{'pedidos':pedidos})

####################### CATALOGO #####################
@login_required
def catalogo(request):

    search = request.GET.get('search')

    if search:
        produtos = Produto.objects.filter(Nome__icontains= search)
       
    else:

        produtos_lista = Produto.objects.all().order_by('id')

        paginator = Paginator(produtos_lista,10)

        page = request.GET.get('page')
        produtos = paginator.get_page(page)

    return render(request, 'catalogo.html', {'produtos': produtos} ) 

@login_required
def catalogo1(request):

    search = request.GET.get('search')

    if search:
        produtos = Produto1.objects.filter(Nome__icontains= search)
       
    else:

        produtos_lista = Produto1.objects.all().order_by('id')

        paginator = Paginator(produtos_lista,10)

        page = request.GET.get('page')
        produtos = paginator.get_page(page)

    return render(request, 'catalogo1.html',{'produtos': produtos} ) 
######################################################
def filtro(request):

    
    
    confeitaria = Produto.objects.all().filter(Ramo= "Cafeteria")

    return render(request, 'confeitaria.html', {'confeitaria':confeitaria})
###################### VISUALIZA PRODUTO #############
@login_required
def visualizacao(request, id):
    produtos = get_object_or_404(Produto, pk=id)

    return render (request, 'produtos.html', {'produtos':produtos})

@login_required
def visualizacao1(request, id):
    produtos1 = get_object_or_404(Produto1, pk=id)

    return render (request, 'produtos1.html', {'produtos1':produtos1})
#####################################################

#################### REALIZA PEDIDO #################
@login_required
def realizapedido(request):
    if request.method == 'POST':
        form=pedidoForm(request.POST)

        if form.is_valid():
            task = form.save(commit= False)
            task.user = request.user
            task=form.save()
            
            messages.add_message(request, messages.SUCCESS, "Seu pedido foi efetuado com sucesso!")
        return redirect("pedido")

    else:    
        form = pedidoForm()

        return render(request, 'realizapedido.html', {'form':form})
#####################################################
@login_required
def mostrapedido(request):
    
    pedidos_lista = Pedido.objects.all().order_by('-created_at').filter(user=request.user)

    paginator = Paginator(pedidos_lista,10)
    page = request.GET.get('page')
    pedidos_lista = paginator.get_page(page)

    return render(request, 'mostrapedido.html',{'pedidos_lista':pedidos_lista})

@login_required
def delete(request, id):

    task = get_object_or_404(Pedido, pk=id)
    task.delete()
    messages.info(request, f'O pedido de {task} foi excluido com sucesso!')
    return redirect('/mostrapedido')
################## CSV XLS ##########################
def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response

############################## EXCEL ################
def xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="pedido.xls"'
        #str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Pedidos')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Descrição','Nome', 'Data','Quantidade' ] #trocado Loja por user 

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Pedido.objects.filter(user=request.user).values_list('Descrição','user','created_at', 'Quantidade')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response

########################### EMAIL  ##################

def send_email(mail):
    context = {'mail': mail}
  
    
    template = get_template('emailcorpo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'TESTE',
        "teste teste teste ",
        settings.EMAIL_HOST_USER,
        [mail]

    )
    
    email.attach_alternative(content, 'text/html')
    email.send()

'''
#duplicado
def send_email():

    message = email_to.Message('# Every thing is ok HELLO WORLD')
    message.add('Everything has been running fine for days.')
    message.add('Probably time to build something new and break everything')
    message.style = 'h1 { color: green }'

    server = email_to.EmailServer('email-ssl.com.br', 587, 'no-reply@superfestval.com.br', 'F3stv@l999')
    server.send_message(message, 'dev4@superfestval.com.br', 'Things are awesome')
'''  
def formulario(request):
    if request.method ==  'POST':
        mail = request.POST.get('mail')

        send_email(mail)
        
        messages.add_message(request, messages.SUCCESS, "Seu email foi enviado com sucesso!")
    return render(request, 'formulario.html', {})

############### EAMIL CORPO HTML ###################        
def e(request):
    lista = Pedido.objects.all().order_by('user_id').filter(user=request.user)   #.order_by('-created_at')
    lista2 = Produto.objects.all()
    return render(request, 'emailcorpo.html', {'lista':lista,'lista2':lista2})
'''
###FUNCIONAva clicou enviou    
def email(mail):
    send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER, ['joojvw@gmail.com'], fail_silently=False)
'''
@login_required
def novopedido(request):
    
    listateste = Produto.objects.all()
    listateste1 = Pedido.objects.all().filter(user=request.user)
    return render(request, 'teste.html', {'listateste1':listateste1,'listateste':listateste })    
@login_required
def query(request):
    somatotal = list(Pedido.objects.all().filter(user=request.user).aggregate(Sum('Quantidade')).values())[0] #mostrando a soma da quantidade de certa variavel
    s = Pedido.objects.values('Nome', 'id','user_id').filter(user_id = 8, id=54 ) #teste
    p1 = Pedido.objects.all().order_by('Nome').filter(user=request.user) # lista dos pedidos 
    p2 = Produto.objects.all().order_by('Nome') # lista dos produtos cafeteria
   


    return render (request, 'teste.html', {'somatotal':somatotal, 'p1':p1, 'p2':p2, 's':s})

def lojas(request):
    prod = list(Produto.objects.all().order_by('Nome').values('Nome'))[:]
    #ped = list(Pedido.objects.all().aggregate(Sum('Quantidade')).values())[0] #somando VALOR BRUTO
    #ped = Pedido.objects.all().aggregate(Count('Quantidade')).values() #somando VALOR BRUTO
    #ped = list(Pedido.objects.all().aggregate(Sum('Quantidade')).values())[0] # VALOR DA SOMA DE QUANTIDADE  usando lista 
    ped = len(Pedido.objects.all()) # VALOR DA SOMA DE PEDIDOS usando len

    
    teste = 0
    #l1 = component.Produto.objects.all()
    l1 = list(Pedido.objects.filter(user_id=2).values_list('Quantidade',flat=True).order_by('Nome'))
    l2 = list(Pedido.objects.filter(user_id=3).values_list('Quantidade', flat=True).order_by('Nome'))
    l3 = list(Pedido.objects.filter(user_id=4).values_list('Quantidade').order_by('Nome'))[:]
    return render(request,'teste.html',{'prod':prod,'l1':l1, 'l2':l2, 'ped':ped,'teste':teste} )

