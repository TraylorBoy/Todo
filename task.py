"""Generic class for manipulating task data within the Todo application"""

class Task:
  """Used for Todo class to keep track of task content and completion status"""

  def __init__(self, content):
    """Sets default state and assigns content to Task"""
    self.content = content
    self.complete = False

  def finish(self):
    """Finishes task after content is accomplished"""
    self.complete = True

  def unfinish(self):
    """Reverts complete state to False"""
    self.complete = False

  def __str__(self):
    return f'\n{self.content}\tComplete - {self.complete}'
