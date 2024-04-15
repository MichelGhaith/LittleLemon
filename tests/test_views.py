from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(id = 10,title = "Jarjir", price = 50, inventory = 50)
        Menu.objects.create(id = 11,title = "Taboule",price = 60, inventory = 51)
    
    def test_getall(self):
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items , many = True)
        expected_data = [{'id' : 10 , 'title' : 'Jarjir' , 'price' : '50.00' , 'inventory' : 50},
            {'id' : 11 , 'title' : 'Taboule' , 'price' : '60.00' , 'inventory' : 51},]
        self.assertCountEqual(expected_data, serializer.data)