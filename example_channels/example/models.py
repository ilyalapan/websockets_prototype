from django.db import models
from datetime import datetime    

# Create your models here.

class Requests(models.Model):
    request_time = models.DateTimeField(default=datetime.now, blank=False)
    status = models.BooleanField(default=False)

    def json_dict(self):
        return {'request_time' : str(self.request_time),
        'status' : self.status,
        'request_id' : self.id,
        }


    def __iter__(self):
        for key, value in self.json_dict().items():
            yield key, value


