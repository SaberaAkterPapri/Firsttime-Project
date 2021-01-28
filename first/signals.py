from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth.models import Group


# from .models import Customer

# def customer_profile(sender, instance, created, **kwargs):
# 	if created:
# 		group = Group.objects.get(name='customer')
# 		instance.groups.add(group)
# 		Customer.objects.create(
# 			user=instance,
# 			name=instance.username,
# 			)
# 		print('Profile created!')

# post_save.connect(customer_profile, sender=User)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
		print('Profile Created!')

post_save.connect(create_profile, sender=User)		


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
	if created == False:
		instance.profile.save()
		print('Profile Updated!')
