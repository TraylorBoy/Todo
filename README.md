# Todo

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Simple CLI todo list application to help organize life's tasks.

## Getting Started <a name = "getting_started"></a>

***main*** is the command used to interact with the application. Simple to use
and easy to install. Fast and lightweight, ready to tackle all of your task
management needs.

```
$ main
Usage: main [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add       Add a task to a todo list
  complete  Changes task state to complete
  create    Creates a new Todo list
  delete    Deletes a list from storage
  edit      Modify contents of a task
  remove    Removes a task from todo list
  show      Shows all stored lists
  view      View contents of todo list
```

### Prerequisites

 ***Uses python3 and pip3***, be sure to have updated python and pip package manager. Simply clone the repository and follow the instructions to install it below.

```
$ git clone https://github.com/TraylorBoy/Todo.git
```

### Installing

```
$ make install
```

### Testing

```
$ make test
```

## Usage <a name = "usage"></a>

### Create a todo list
```
$ main create 'Test List'
Creating list - Test List
```

### Show all created todo lists
```
$ main show
Showing all available lists
Test List
```

### Add a task to a todo list
```
$ main add 'Test List' 'Test task'

1
----
Test task	Complete - False
```

```
$ main add 'Test List' 'Anotha test task'

1
----
Test task	Complete - False

2
----
Anotha test task	Complete - False
```

### Edit a task in a todo list
```
$ main edit 'Test List' 2 'Another test task'

1
----
Test task	Complete - False

2
----
Another test task	Complete - False
```

### Complete/Incomplete a task in a todo list
```
$ main complete 'Test List' 2

1
----
Test task	Complete - False

2
----
Another test task	Complete - True
```
```
$ main complete 'Test List' 2 --undo True

1
----
Test task	Complete - False

2
----
Another test task	Complete - False
```

### Remove a task from a todo list
```
$ main remove 'Test List' 2

1
----
Test task	Complete - False
```

### View all contents of a todo list
```
$ main view 'Test List'

1
----
Test task	Complete - False
```

### Delete a todo list
```
$ main delete 'Test List'
Deleted: Test List
```
