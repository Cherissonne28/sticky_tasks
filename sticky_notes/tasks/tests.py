from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Task
from datetime  import  datetime, date

class TaskTest(TestCase):


    def setUp(self) -> None:
        Task.objects.create(title="Test Task", 
                            content="This is a test task",
                            deadline="2024-06-30",
                            author="Test User")
        
    def test_task_has_title(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.title, "Test Task")

    def test_task_has_content(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.content, "This is a test task")

class TaskViewTest(TestCase):
    def setUp(self) -> None:
        Task.objects.create(title="Test Task", 
                            content="This is a test task",
                            deadline="2024-06-30",
                            author="Test User")
        
    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_task_detail_view(self):
        task = Task.objects.get(id=1)
        response = self.client.get(reverse('task_detail', args=[task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_task_create_view(self):
        start_counter = Task.objects.count()        

        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'content': 'This is a new task.',
            'deadline': '2004-06-30',
            'author': 'Test User'
        })

        final_count = Task.objects.count()        

        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(start_counter, final_count)

        
    