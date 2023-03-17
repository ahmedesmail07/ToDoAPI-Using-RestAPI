from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.todo = Todo.objects.create(title="Ending Rest", body="before 20-3-2023")

    def test_model_content(self):
        self.assertEqual(self.todo.title, "Ending Rest")
        self.assertEqual(self.todo.body, "before 20-3-2023")
        # self.assertEqual(str(self.todo),"Ending Rest")
