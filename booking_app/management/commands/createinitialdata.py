from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from booking_app.models import Menu
from restaurant_app.models import Category, MenuItem


class Command(BaseCommand):
    help = 'Create initial data for the application'

    item1_descr = "This vibrant and colorful salad is a true delight to the senses, with its refreshing and zesty flavors. It's dressed with a simple yet flavorful vinaigrette that adds an extra layer of tangy goodness to the dish. This salad is perfect for any occasion, whether you're enjoying a lazy summer afternoon or having a dinner party with friends. Its versatility makes it an ideal side dish to complement a wide range of main courses, from grilled meats to seafood or vegetarian options."
    item2_descr = "Made with crispy grilled bread, rubbed with garlic and drizzled with olive oil, our bruschetta is the perfect way to start your meal on a high note. Topped with fresh and flavorful ingredients like juicy tomatoes, fragrant basil, and creamy mozzarella cheese, our bruschetta is a crowd-pleaser that will leave your taste buds dancing with joy. "
    item3_descr = "Grilled fish is a culinary masterpiece that awakens your senses with every bite. With a perfectly charred exterior and juicy, flaky flesh, our grilled fish is a true delight that will tantalize your taste buds. As you take your first bite, you'll be transported to a world of rich, smoky flavors that blend perfectly with the natural sweetness of the fish. The delicate texture and savory aroma will fill your senses and leave you craving for more."
    item4_descr = "Our lemon dessert is a refreshing and tangy treat that's sure to satisfy your sweet cravings. With its bright and zesty flavors, every bite is a burst of sunshine that delights your senses. Crafted with the finest ingredients and the utmost care, each bite is a testament to the beauty of simple ingredients and the art of baking. It's the perfect way to end a meal, with its refreshing flavors cleansing your palate and leaving you feeling satisfied and refreshed."

    def handle(self, *args, **kwargs):

        if not Menu.objects.exists():
            item1 = Menu.objects.create(item_name="Greek salad", category="Salads", description=self.item1_descr, price=10)
            item1.save()
            item2 = Menu.objects.create(item_name="Bruschetta", category="Appetizers", description=self.item2_descr, price=7)
            item2.save()
            item3 = Menu.objects.create(item_name="Grilled fish", category="Main", description=self.item3_descr, price=20)
            item3.save()
            item4 = Menu.objects.create(item_name="Lemon dessert", category="Desserts", description=self.item4_descr, price=8)
            item4.save()

        if not Category.objects.exists():
            cat_1 = Category.objects.create(title="Appetizers"); cat_1.save()
            cat_2 = Category.objects.create(title="Main"); cat_2.save()
            cat_3 = Category.objects.create(title="Desserts"); cat_3.save()
            cat_4 = Category.objects.create(title="Salads"); cat_4.save()

        if not MenuItem.objects.exists():
            menu_item_1 = MenuItem.objects.create(title='Greek salad', price=9.99, category=cat_4); menu_item_1.save()
            menu_item_2 = MenuItem.objects.create(title='Bruschetta', price=14.99, category=cat_1); menu_item_2.save()
            menu_item_3 = MenuItem.objects.create(title='Grilled fish', price=10.99, category=cat_2); menu_item_3.save()
            menu_item_4 = MenuItem.objects.create(title='Lemon dessert', price=8.99, category=cat_3); menu_item_4.save()


        if not Group.objects.exists():
            group_managers = Group.objects.create(name='Manager')
            group_managers.save()
            group_delivery = Group.objects.create(name='Delivery')
            group_delivery.save()


        self.stdout.write(self.style.SUCCESS('Initial data created successfully.'))
