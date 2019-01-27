from django.db import models
from users.models import *
from django.utils.translation import ugettext_lazy as _

class Friend(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    friend = models.ForeignKey(ApplicationUser,related_name="friendship_set",null=True)
    current_user = models.ForeignKey(ApplicationUser, related_name="owner", null=True)
    is_activeFriend = models.BooleanField(_('active'), default=True, help_text=_('Whether friend is Active Or Not'))
    
    def __str__(self):
        return str(self.friend)