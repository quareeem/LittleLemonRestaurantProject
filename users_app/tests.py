from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# class UserManagerViewSetTests(APITestCase):
#     group_name = 'Manager'

#     def setUp(self):
#         self.admin = User.objects.create_superuser(username='admin', email='admin1@example.com', password='testpassword')
#         self.user = User.objects.create_user(username=f'testuser', email='test@example.com', password='testpassword')
#         self.manager_group = Group.objects.create(name=self.group_name)

#     def test_list(self):
#         self.client.force_authenticate(user=self.admin)
#         response = self.client.get(reverse(f'user_{self.group_name.lower()}-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_add_user_to_group(self):
#         self.client.force_authenticate(user=self.admin)
#         response = self.client.post(reverse(f'user_{self.group_name.lower()}-list'), {'username': self.user.username})
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.user.refresh_from_db()
#         self.assertIn(self.manager_group, self.user.groups.all())

#     def test_remove_user_from_group(self):
#         self.user.groups.add(self.manager_group)
#         self.user.save()
#         self.client.login(username='admin', password='testpassword')
#         response = self.client.delete(reverse(f'user_{self.group_name.lower()}-detail', kwargs={'pk': self.user.pk}))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.user.refresh_from_db()
#         self.assertNotIn(self.manager_group, self.user.groups.all())



class UserDeliveryViewSetTests(APITestCase):
    group_name = 'Delivery'

    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', email='admin1@example.com', password='testpassword')
        self.user = User.objects.create_user(username=f'testuser', email='test@example.com', password='testpassword')
        self.delivery_group = Group.objects.create(name=self.group_name)
        print(self.user.groups.all())

    def test_list(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(reverse(f'user_{self.group_name.lower()}-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_user_to_group(self):
        self.client.force_authenticate(user=self.admin)
        # response = self.client.post(reverse(f'user_{self.group_name.lower()}-list'), {'username': self.user.username})
        response = self.client.post(reverse('user_delivery-list'), {'username': self.user.username})
        self.user.groups.add(self.delivery_group)
        print('- -1 -')
        print(self.user.groups.all())
        print('- - -')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.user.refresh_from_db()
        
        
        self.assertIn(self.delivery_group, self.user.groups.all())

    def test_remove_user_from_group(self):
        # print('- -1 -')
        # print(self.user.groups.all())
        # print('- - -')
        self.user.groups.add(self.delivery_group)
        print('- -2 -')
        print(self.user.groups.all())
        print('- - -')
        self.user.save()
        self.client.login(username='admin', password='testpassword')
        response = self.client.delete(reverse(f'user_{self.group_name.lower()}-detail', kwargs={'pk': self.user.pk}))


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertNotIn(self.delivery_group, self.user.groups.all())

