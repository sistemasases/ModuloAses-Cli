from commands import command_list as cl
from commands import user_info as ui
import argparse as ap
import os

parser = ap.ArgumentParser(prog='asescli', description='Command line tools for ASES developers')
subparsers = parser.add_subparsers()
parser.add_argument('--version', action='version', version='1.0.0')

minify_parser = subparsers.add_parser('minify')
minify_parser.add_argument('js_name', help="Name of the JS file to minify. Write 'all' to minify all JS file in 'amd' directory.")
minify_parser.set_defaults(func=cl.command_list['minify'])


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
	args = parser.parse_args()
	args.func(args)

if __name__ == "__main__":
    main()
