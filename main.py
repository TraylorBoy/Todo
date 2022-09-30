"""Application Entry Point"""

import click
from manager import Manager

mgr = Manager()

@click.group()
def cli():
  pass

@click.command()
@click.argument('name')
def create(name):
  """Creates a new Todo list"""
  global mgr

  click.echo(f'Creating list - {name}')
  mgr.create_list(name)

@click.command()
def show():
  """Shows all stored lists"""
  global mgr

  click.echo('Showing all available lists')

  for todo in mgr.view_lists():
    click.echo(todo)

@click.command()
@click.argument('name')
def view(name):
  """View contents of todo list"""
  global mgr

  mgr.open_list(name)
  click.echo(mgr.current_list)

@click.command()
@click.argument('name')
def delete(name):
  """Deletes a list from storage"""
  global mgr

  mgr.delete_list(name)
  click.echo(f'Deleted: {name}')

@click.command()
@click.argument('name')
@click.argument('content')
def add(name, content):
  """Add a task to a todo list"""
  global mgr

  mgr.open_list(name)
  mgr.current_list.add_task(content)
  mgr.check_modified()
  click.echo(mgr.current_list)

@click.command()
@click.argument('name')
@click.argument('task_id')
def remove(name, task_id):
  """Removes a task from todo list"""
  global mgr

  task_id = int(task_id)

  mgr.open_list(name)
  mgr.current_list.delete_task(task_id)
  mgr.check_modified()
  click.echo(mgr.current_list)

@click.command()
@click.argument('name')
@click.argument('task_id')
@click.option('--undo', default=False, help='Revert task state to incomplete')
def complete(name, task_id, undo=False):
  """Changes task state to complete"""
  global mgr

  task_id = int(task_id)
  mgr.open_list(name)

  if undo: mgr.current_list.uncomplete_task(task_id)
  else: mgr.current_list.complete_task(task_id)

  mgr.check_modified()
  click.echo(mgr.current_list)

@click.command()
@click.argument('name')
@click.argument('task_id')
@click.argument('content')
def edit(name, task_id, content):
  """Modify contents of a task"""
  global mgr

  task_id = int(task_id)

  mgr.open_list(name)
  mgr.current_list.edit_task(content, task_id)
  mgr.check_modified()
  click.echo(mgr.current_list)

commands = [create, show, view, delete, add, remove, complete, edit]

for command in commands:
  cli.add_command(command)

if __name__ == '__main__':
  cli()
