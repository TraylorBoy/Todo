"""Test suite for Todo application"""

from task import Task
from todo import Todo

todo = Todo('Test List')

def test_task(content):
  """Test task class by adding content and changing the state"""
  task = Task(content)
  assert not task.complete
  print(task)

  task.finish()
  assert task.complete
  print(task)

def test_create_todo(name):
  todo = Todo(name)
  assert todo.name == name
  print(todo)

def test_todo_add_task(content):
  global todo

  todo.add_task(content)
  assert todo.num_of_tasks == 1
  print(todo)

def test_todo_delete_task(id):
  global todo

  todo.delete_task(id)
  assert todo.num_of_tasks == 0

  print(todo)

def test_todo_edit_task(content, id):
  global todo

  todo.add_task('Get groceries')

  print(f'Previous list\n{todo}')

  todo.edit_task(content, id)

  assert todo.task_list[id].content == content

  print(f'New list\n{todo}')

def test_todo_complete_task(id):
  global todo

  todo.complete_task(id)
  print(todo)

if __name__ == '__main__':
  test_task('Get groceries')
  test_create_todo('Grocery List')
  test_todo_add_task('Get Groceries')
  test_todo_delete_task(1)
  test_todo_edit_task('Get salt', 1)
  test_todo_complete_task(1)
