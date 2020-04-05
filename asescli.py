#!/usr/bin/env python3
from commands import command_list as cl
from commands import user_info as ui
import argparse as ap
import os

#Main parser
parser = ap.ArgumentParser(prog='asescli', description='Command line tools for ASES developers')
subparsers = parser.add_subparsers()
parser.add_argument('--version', action='version', version='1.0.0')

#Minify subparser
minify_parser = subparsers.add_parser('minify')
minify_parser.add_argument('js_name', help="Name of the JS file to minify. Write 'all' to minify all JS file in 'amd' directory.")
minify_parser.set_defaults(func=cl.command_list['minify'])

#Create subparser
create_parser = subparsers.add_parser('create')
create_parser.add_argument('file_name', help='Name of the new package to create')
create_parser.add_argument('-v', default=False, action='store_true', help='Create a view file with the given name')
create_parser.add_argument('-m', default=False, action='store_true', help='Create a manager directory (lib and api included) with the given name')
create_parser.add_argument('-a', default=False, action='store_true', help='Create a JS file in amd/src with the given name')
create_parser.add_argument('-t', default=False, action='store_true', help='Create a template file with the given name')
create_parser.set_defaults(func=cl.command_list['create'])

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
