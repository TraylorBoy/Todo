"""Test suite for Todo application"""

from task import Task

def test_task(content):
  """Test task class by adding content and changing the state"""
  task = Task(content)
  assert not task.complete
  print(task)

  task.finish()
  assert task.complete
  print(task)

if __name__ == '__main__':
  test_task('Get groceries')
