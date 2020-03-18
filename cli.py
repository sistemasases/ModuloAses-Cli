from commands import command_list as cl
from commands import user_info as ui
import os

def read_commands():
	input_command = ""
	while input_command != "exit":
		print(">>> " , end="")
		data = [x for x in input().split()]
		input_command = data[0]
		if input_command == "exit":
			exit(0)
		elif input_command == "help":
			print([key for key, value in cl.command_list.items()])
		else:
			try:
				print(cl.command_list[input_command](data[1]))
			except:
				print("Invalid command: '"+input_command+"'")


def valid_workspace( dirpath = None  ):

	module_path = dirpath if dirpath else os.getcwd()
	if not os.path.exists( module_path ):
		return False

	list_of_important_folders = [
		"managers",
		"amd/build",
		"amd/src",
		"view",
		"templates",
		"style",
		"core",
		"classes",
		"db"
	]
	
	for dir_to_check in list_of_important_folders:
		if not os.path.exists( os.path.join( module_path , dir_to_check ) ) :
			print("No existe el directorio:'" + dir_to_check + "' en '" + module_path + "'")
			return False
	return True


def main():
    if not valid_workspace( ui.directory_path ):
        print("Espacio de trabajo no válido.")
        return -1

    read_commands()


if __name__ == "__main__":
    main()
