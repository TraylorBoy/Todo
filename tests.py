"""Test suite for Todo application"""

from task import Task
from todo import Todo
from manager import Manager

todo = Todo('Test List')
manager = Manager()

def test_task(content):
  """Test task class by adding content and changing the state"""
  task = Task(content)
  assert not task.complete

  task.finish()
  assert task.complete

def test_create_todo(name):
  todo = Todo(name)
  assert todo.name == name

def test_todo_add_task(content):
  global todo

  todo.add_task(content)
  assert todo.num_of_tasks == 1

def test_todo_delete_task(id):
  global todo

  todo.delete_task(id)
  assert todo.num_of_tasks == 0

def test_todo_edit_task(content, id):
  global todo

  todo.add_task('Get groceries')

  todo.edit_task(content, id)

  assert todo.task_list[id].content == content

def test_todo_complete_task(id):
  global todo

  todo.complete_task(id)

def test_todo_uncomplete_task(id):
  global todo

  todo.uncomplete_task(id)

def test_todo_reorder():
  global todo

  todo.add_task('Test task 1')
  todo.add_task('Test task 2')
  todo.add_task('Test task 3')
  todo.delete_task(2)

def test_manager_store():
  global todo
  global manager

  manager.store(todo)

def test_manager_retrieve():
  global todo
  global manager

  tmp = manager.retrieve(todo.name)

def test_manager_create_list(name):
  global manager

  manager.create_list(name)

def test_manager_open_list(name):
  global manager

  manager.open_list(name)

def test_manager_delete_list(name):
  global manager

  manager.delete_list(name)

def test_manager_check_modified():
  global todo
  global manager

  manager.open_list(todo.name)
  manager.current_list.add_task('Get peas')
  manager.check_modified()

def test_manager_view_lists():
  global manager

  print(manager.view_lists())

if __name__ == '__main__':
  test_task('Get groceries')
  test_create_todo('Grocery List')
  test_todo_add_task('Get Groceries')
  test_todo_delete_task(1)
  test_todo_edit_task('Get salt', 1)
  test_todo_complete_task(1)
  test_todo_uncomplete_task(1)
  test_todo_reorder()
  test_manager_store()
  test_manager_retrieve()
  test_manager_create_list('Grocery List')
  test_manager_open_list('Grocery List')
  test_manager_delete_list('Grocery List')
  test_manager_check_modified()
  test_manager_view_lists()
  print('All tests passed')
