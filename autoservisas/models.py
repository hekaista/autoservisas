from django.db import models
import uuid


# Create your models here.

class Modelis(models.Model):
    marke = models.CharField('Markė', max_length=100)
    modelis = models.CharField('Modelis', max_length=100)
    metai = models.IntegerField('Metai')
    variklis = models.CharField('Variklis', max_length=100)

    class Meta:
        ordering = ['marke', 'modelis']
        verbose_name = 'Modelis'
        verbose_name_plural = 'Modeliai'

    def __str__(self):
        return f"{self.marke}, {self.modelis}, {self.metai}, {self.variklis}"


class Automobilis(models.Model):
    valstybinis_nr = models.CharField('Numeris', max_length=100)
    vin = models.IntegerField('VIN', max_length=13)
    klientas = models.CharField('Klientas', max_length=100)
    modelis = models.ForeignKey('Modelis', on_delete=models.CASCADE,related_name='automobiliai')

    # def __str__(self):
    #     return f" {self.modelis.marke}, {self.modelis.modelis} | {self.valstybinis_nr} - {self.klientas}"

    def __str__(self):
        return f" {self.modelis.marke}, {self.modelis.modelis} - {self.klientas}"

    class Meta:
        verbose_name = 'Automobilis'
        verbose_name_plural = 'Automobiliai'


class Uzsakymas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data = models.DateField('Užsakymo data')
    suma = models.FloatField('Suma')
    automobilis = models.ForeignKey('Automobilis', on_delete=models.CASCADE, related_name='uzsakymai')

    UZSAKYMO_STATUSAS = (
        ('V', 'Vykdomas'),
        ('I', 'Ivykdytas'),
        ('A', 'Atšauktas'),
        ('L', 'Laukia eilėje')
    )

    status = models.CharField(
        max_length=1,
        choices=UZSAKYMO_STATUSAS,
        blank=True,
        default='L',
        help_text='Užsakymo statusas'
    )

    class Meta:
        ordering = ['data']
        verbose_name = 'Užsakymas'
        verbose_name_plural = 'Užsakymai'

    # def __str__(self):
    #     return f"{self.status} | Užsakymas: {self.id} | Klientas: {self.automobilis.klientas}, " \
    #            f"Valst. Nr.: {self.automobilis.valstybinis_nr}"
    def __str__(self):
        return f"{self.id}"


class Uzsakymoeil(models.Model):
    kiekis = models.IntegerField('Kiekis')
    kaina = models.FloatField('Kaina')
    uzsakymas = models.ForeignKey('Uzsakymas', on_delete=models.CASCADE)
    paslauga = models.ForeignKey('Paslauga', on_delete=models.CASCADE)

    def __str__(self):
        return f"Kiekis: {self.kiekis} | " \
               f"Paslauga: {self.paslauga.pavadinimas} | Kaina: {self.paslauga.kaina} "

    class Meta:
        verbose_name = 'Užsakymo eilutė'
        verbose_name_plural = 'Užsakymo eilutės'


class Paslauga(models.Model):
    pavadinimas = models.CharField("Paslaugos pavadinimas", max_length=100)
    kaina = models.FloatField("Paslaugos kaina")

    def __str__(self):
        return f"{self.pavadinimas} - {self.kaina}"

    class Meta:
        verbose_name = 'Paslauga'
        verbose_name_plural = 'Paslaugos'
