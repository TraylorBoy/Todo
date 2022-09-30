"""Task list manager"""

import os
import dill
from todo import Todo

class Manager:
  """Handles Todo list manipulation"""

  def __init__(self):
    """Sets the manager's current list that it is operating on"""
    self.current_list = None
    self.dir_path = f'{os.getcwd()}/storage'

  def store(self, todo):
    """Store todo object in file"""

    file_name = todo.name
    file_path = f'{self.dir_path}/{file_name}.dat'

    # Create storage directory if possible
    try:
      os.mkdir(self.dir_path)
    except:
      pass

    with open(file_path, 'wb') as f:
      dill.dump(todo, f)

  def retrieve(self, name):
    """Get list from storage"""

    file_path = f'{self.dir_path}/{name}.dat'

    with open(file_path, 'rb') as f:
      return dill.load(f)

  def create_list(self, name):
    """Creates a new Todo list object and stores it"""

    self.store(Todo(name))

  def open_list(self, name):
    """Retrieves list from storage if possible and sets manager's state"""

    if todo := self.retrieve(name):
      self.current_list = todo
    else: print(f'{name} is not available')

  def delete_list(self, name):
    """Delete list from storage"""

    try:
      os.remove(f'{self.dir_path}/{name}.dat')
    except:
      pass

  def check_modified(self):
    """Checks if current list was modified, stores it if True"""

    if self.current_list.modified: self.store(self.current_list)

  def view_lists(self):
    """Retrieves all names of stored lists if possible"""

    # Get all stored lists if possible
    if os.path.exists(self.dir_path):
      stored_lists = os.listdir(self.dir_path)

      fmt_stored_lists = []
      # Format
      for item in stored_lists:
        fmt_item = item[:-4]
        fmt_stored_lists.append(fmt_item)

      return fmt_stored_lists
