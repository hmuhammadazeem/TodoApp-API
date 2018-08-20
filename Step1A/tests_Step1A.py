import unittest
from Step1A import app
import json


class MyTestCase(unittest.TestCase):
    def test_index(self):
        response = app.test_client().get('/')
        self.assertEqual(response.status, '200 OK')

    def test_tasks_list(self):
        response = app.test_client().get('/tasks')
        self.assertEqual(response.status, '200 OK')

    def test_tasks_find(self):
        response = app.test_client().get('/tasks/4')
        self.assertEqual(response.status, '200 OK')

    def test_tasks_update(self):
        response = app.test_client().put('/tasks/update/4', data=json.dumps({"title": "Step 1A", "done": "false"}),
                                         content_type='application/json')
        self.assertEqual(response.status, '200 OK')

    def test_task_del(self):
        response = app.test_client().delete('/tasks/delete/3')
        self.assertEqual(response.status, '200 OK')


if __name__ == '__main__':
    unittest.main()
