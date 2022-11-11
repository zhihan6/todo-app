import functions
import PySimpleGUI as sg
import time

# Change the theme
sg.theme("Black")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])


# Add
add_button = sg.Button("Add")
# Edit
edit_button = sg.Button("Edit")
# Complete
complete_button = sg.Button("Complete")
# Exit
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    if event == "Add":
        todos = functions.get_todos()
        todos.append(values['todo'] + '\n')
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == 'Edit':
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup("Please select an item to edit.", font=("Helvetica", 20))

    elif event == 'Complete':
        try:
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        except IndexError:
            sg.popup("Please select an item to complete", font=("Helvetica", 20))

    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])

    elif event == 'Exit':
        break

    elif event == sg.WINDOW_CLOSED:
        break

window.close()
