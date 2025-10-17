from django.db import models

class Reserva(models.Model):
    # Campos que você pediu:
    nome_cliente = models.CharField(max_length=100, verbose_name="Nome do Cliente")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    email = models.EmailField(verbose_name="E-mail")
    
    # Campos extras para deixar profissional:
    numero_de_pessoas = models.PositiveIntegerField(verbose_name="Número de Pessoas")
    data_reserva = models.DateField(verbose_name="Data da Reserva")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Realizada em")
    confirmada = models.BooleanField(default=False, verbose_name="Reserva Confirmada")
    def __str__(self):
        return f"{self.nome_cliente} - {self.data_reserva.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
