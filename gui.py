import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == "Add":
        todos = functions.get_todos()
        todos.append(values['todo'] + '\n')
        functions.write_todos(todos)
    elif event == sg.WINDOW_CLOSED:
        break

window.close()
