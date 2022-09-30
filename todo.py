"""Todo class for managing tasks"""

from task import Task

class Todo:
  """Manages tasks"""

  def __init__(self, name):
    """Sets default state and assigns name of Todo list"""
    self.name = name
    self.task_list = {}
    self.modified = False
    self.num_of_tasks = 0

  def reorder(self):
    """Re-orders task ids after deletion"""

    tmp = {}
    keys = list(self.task_list.keys())

    for i in range(1, (self.num_of_tasks + 1)):
      tmp[i] = self.task_list[keys[i - 1]]

    self.task_list = tmp

  def add_task(self, content):
    """Creates a new task and stores it within the task_list"""
    task = Task(content)

    self.num_of_tasks += 1
    self.task_list[self.num_of_tasks] = task

    # Update modified state
    # Manager will store new Todo state
    self.modify()

  def delete_task(self, task_id):
    """Removes task from task_list"""

    if task_id > self.num_of_tasks: return

    del self.task_list[task_id]
    self.num_of_tasks -= 1
    self.reorder()

    # Update modified state
    # Manager will store new Todo state
    self.modify()

  def edit_task(self, content, task_id):
    """Modifies the content of a task"""

    if task_id > self.num_of_tasks: return

    self.task_list[task_id] = Task(content)

    # Update modified state
    # Manager will store new Todo state
    self.modify()

  def complete_task(self, task_id):
    """Change tasks state to complete"""

    if task_id > self.num_of_tasks: return

    self.task_list[task_id].finish()

    # Update modified state
    # Manager will store new Todo state
    self.modify()

  def uncomplete_task(self, task_id):
    """Changes tasks state to not complete"""

    if task_id > self.num_of_tasks: return

    self.task_list[task_id].unfinish()

    # Update modified state
    # Manager will store new Todo state
    self.modify()

  def modify(self):
    """Changes modify state to true"""
    self.modified = True

  def __str__(self):
    desc = ''

    if len(self.task_list) > 0:
      for (id, task) in self.task_list.items():
        desc += f'\n{id}\n----{task}\n'
    else: desc = 'Task list empty'

    return desc
