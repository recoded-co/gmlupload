from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete

class MapFileUpload(models.Model):
    name = models.CharField(max_length=250)
    file = models.FileField(upload_to = 'gml_uploads')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name
        
    def to_dict(self):
        ret = { 'name':self.name, 'file':self.file.name, 'user':self.user.id }
        return ret

    def remove_file(self):
        import os
        os.remove(self.file.path)
        
def deleteMapFile(sender, instance, **kwargs):
    instance.remove_file()
    
post_delete.connect(deleteMapFile, sender=MapFileUpload)

