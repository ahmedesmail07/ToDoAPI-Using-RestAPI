from django.test import TestCase
from .models import Todo
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TodoModelTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.todo = Todo.objects.create(title="Ending Rest", body="before 20-3-2023")

    def test_model_content(self):
        self.assertEqual(self.todo.title, "Ending Rest")
        self.assertEqual(self.todo.body, "before 20-3-2023")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo.title)

    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "Ending Rest")
