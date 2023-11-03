from django import forms
from django.core.mail import EmailMessage
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

from .models import Agendamento
import random

def gerar_protocolo():
    while True:
        protocolo = random.randint(1, 10000000000)
        if not Agendamento.objects.filter(protocolo=protocolo).exists():
            return protocolo

class ContatoForm(forms.Form):
     nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-class-nome'}))
     telefone = forms.CharField(label='Telefone', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-class-telefone'}))
     email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control form-class-email'}))
     
     unidadeCarro = 'Unidade de Placa de Carro'
     parCarro = 'Par de Placa de Carro'
     moto = 'Placa de Moto''Placa de Moto'

     opcoes = forms.ChoiceField(
        choices=[
            (unidadeCarro, unidadeCarro),
            (parCarro, parCarro),
            (moto, moto),
        ],
        label="Opções", widget=forms.Select(attrs={'class': 'form-control form-class-opcoes'})
    )
     horario = forms.ChoiceField(
        choices=[
            (f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}")
            for hour in range(8, 17) for minute in (0, 30)
        ],
        label="Horário", widget=forms.Select(attrs={'class': 'form-control form-class-horario'})
    )
     jardimCearense = 'Fortaleza - CE: Godofredo Maciel, 2743-A - Jardim Cearense'
     parquelandia = 'Fortaleza - CE: Gustavo Sampaio, 1293 - Parquelândia'
     guaraciabaDoNorte = 'Guaraciaba do Norte - CE: Av. 12 de Novembro, 50 - Centro'
     quixere = 'Quixeré - CE: R. Mte. Felipe, 917 - Centro'
     itapaje = 'Itapajé - CE : R. Jandira Bastos Magalhães, 689'
     local = forms.ChoiceField(
        choices = [
            (jardimCearense, jardimCearense),
            (parquelandia, parquelandia),
            (guaraciabaDoNorte, guaraciabaDoNorte),
            (quixere, quixere),
            (itapaje, itapaje)
        ],
        label='Locais',widget=forms.Select(attrs={'class': 'form-control form-class-local'})
    )
     data = forms.DateField(
        label='Agendamento',
        widget=forms.DateInput(attrs={'type': 'date'}),
        
    )
     protocolo = forms.CharField(max_length=100, initial=gerar_protocolo(), widget=forms.HiddenInput())


     def send_email(self):
          nome = self.cleaned_data['nome']
          email = self.cleaned_data['email']
          opcoes = self.cleaned_data['opcoes']
          horario = self.cleaned_data['horario']
          local = self.cleaned_data['local']
          data = self.cleaned_data['data']
          protocolo = self.cleaned_data['protocolo']
          assunto = 'Marca visita'





          # Criação de um arquivo PDF com os dados do formulário
          buffer = BytesIO()
          doc = SimpleDocTemplate(buffer, pagesize=letter)
          styles = getSampleStyleSheet()
          elements = []

          elements.append(Paragraph('Comprovante de Agendamento', styles['Title']))
          elements.append(Spacer(1, 12))

          data_table = [
               ['Nome:', nome],
               ['Email:', email],
               ['Opções de Agendamento:', opcoes],
               ['Horário:', horario],
               ['Local:', Paragraph(local, styles['Normal'])],  # Utilize o estilo 'Normal' para quebrar a linha
               ['Data de Agendamento:', data],
               ['Gerar Prrotocolo', protocolo]
          ]

          table = Table(data_table, colWidths=300, rowHeights=30)
          table.setStyle(TableStyle([
               ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
               ('GRID', (0, 0), (-1, -1), 1, colors.black),
          ]))

          elements.append(table)
          doc.build(elements)

          # Anexa o PDF ao email
          buffer.seek(0)
          email = EmailMessage(
               subject=assunto,
               from_email='jbbuno007@gmail.com',
               to=[email],
          )
          email.attach('comprovante.pdf', buffer.read(), 'application/pdf')
          email.send()