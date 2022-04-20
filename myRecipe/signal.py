from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Recipe
from django.core.mail import send_mail
from django.conf import settings

# @receiver(post_save, sender=Recipe)
# def recipeUpdated(sender, instance, created, **kwargs):
#     print('Profile Saved!')
#     print('Instance',instance)
#     print('CREATED', created)


# def deleteRecipe(sender,instance, **kwargs):
#     print('delete recipe...')

def createUser(sender, instance, created ,**kwargs):
    if created:
        print('success!')
        user = instance


        subject = '歡迎來到我的食譜網站'
        message = '很開心你的加入，歡迎使用新增食譜，新增你第一個食譜！'


        send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
            #這裡的user抓取的關鍵是user=instance
                [user.email],
                fail_silently = False,
        )


post_save.connect(createUser, sender=User)
# post_save.connect(recipeUpdated, sender=Recipe)
# post_delete.connect(deleteRecipe, sender=Recipe)