from django.db import models
from pacientes.models import Paciente
from doctores.models import Doctor

class Cita(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('en_curso', 'En Curso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
        ('no_asistio', 'No Asistió'),
    ]
    
    TIPOS = [
        ('primera_vez', 'Primera Vez'),
        ('control', 'Control'),
        ('urgencia', 'Urgencia'),
        ('telemedicina', 'Telemedicina'),
    ]
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    tipo = models.CharField(max_length=20, choices=TIPOS, default='primera_vez')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    motivo = models.TextField()
    notas = models.TextField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)
    tratamiento = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        ordering = ['-fecha', '-hora_inicio']
        unique_together = ['doctor', 'fecha', 'hora_inicio']

    def __str__(self):
        return f"Cita: {self.paciente.usuario.get_full_name()} con {self.doctor} - {self.fecha} {self.hora_inicio}"