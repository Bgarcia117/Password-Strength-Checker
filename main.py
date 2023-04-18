import PySimpleGUI as sg

password = sg.Text("Enter a new password: ")
pass_box = sg.InputText(key="pass")
button = sg.Button("Check Password")
output = sg.Text(key="output")

result = {}

window = sg.Window('Password Checker',
                   layout=[[password, pass_box], [button, output]])

while True:
    event, values = window.read()
    # print(event, values)
    password = values["pass"]

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False 

    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result["digits"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True

    result["uppercase"] = uppercase
    if all(result.values()):
        # print("Strong Password")
        window["output"].update(value="Strong Password", text_color="green")
    else:
        # print("Weak Password")
        window["output"].update(value="Weak Password", text_color="red")
