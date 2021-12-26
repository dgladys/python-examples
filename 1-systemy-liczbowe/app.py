import PySimpleGUI as sg

layout = [
	[sg.Text('Podaj liczbę w systemie naturalnym')],
	[sg.InputText("0", key="input_number")],
	[sg.Text('Konwertuj na'), sg.Radio('Dwójkowy', "system", default=True, key="system_bin"), sg.Radio('Ósemkowy', "system", key="system_oct")],
	[sg.Button("Konwertuj")],
	[sg.InputText("0", disabled=True, key="res")]
]

def convert_to_bin(val):
	try: 
		return bin(int(val))[2:]
	except:
		return "Invalid input value"

def convert_to_oct(val):
	try:
		return oct(int(val))[2:]
	except:
		return "Invalid input value"


# Create the window
window = sg.Window("Demo", layout, size=(320, 160))

# Create an event loop
while True:
	event, values = window.read()
	# End program if user closes window or
	# presses the OK button
	
	if event == sg.WIN_CLOSED:
		break
	elif event == "Konwertuj":
		
		cValue = None
		if values['system_bin'] == True:
			window['res'].update(convert_to_bin(values['input_number']))
		elif values['system_oct'] == True:
			window['res'].update(convert_to_oct(values['input_number']))

window.close()