from django.db import models

# Create your models here.

class Event(models.Model):
    """Classe contendo o evento propriamente dito, sua data, descrição
    e também prioridade."""

    priorities_list = (
        ("0", "Sem prioridade"),
        ("1", "Normal"),
        ("2", "Urgente"),
        ("3", "Muito Urgente"),
    )

    date = models.DateField()
    event = models.CharField(max_length=80)
    priority = models.CharField(max_length=1, choices=priorities_list)

    class Meta:
        ordering = ("-date", "-priority", "event")

    def number_of_comments(self):
        """Retorna a quantidade de comentários dentro de um evento."""
        return self.comment_event.count()

    @property
    def text_priority(self):
        """ Converte o valor da prioridade no texto correspondente. """
        for k, v in self.priorities_list:
            if k == self.priority:
                return v
        return ""

    def __str__(self):
        return self.event