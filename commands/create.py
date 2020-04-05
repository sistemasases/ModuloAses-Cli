from commands import user_info as ui
import os

def create(args = None):

	create_js = args.a
	create_manager = args.m
	create_template = args.t
	create_view = args.v
	flags = create_js or create_manager or create_template or create_view

	file_name = args.file_name

	if flags == False:
		print('At least one flag is necesary')
		return

	if create_js:
		js_name = file_name + '.js'
		create_file(js_name, 'amd/src/', 'js')

	if create_manager:

		if create_directory(file_name, ui.direcotry_path + 'managers/'):
			api_name = file_name + '_api.php'
			create_file(api_name, 'managers/' + file_name + '/', 'api')

			lib_name = file_name + '_lib.php'
			create_file(lib_name, 'managers/' + file_name + '/', 'lib')

	if create_template:
		template_name = args.file_name + '.mustache'
		create_file(template_name, 'templates/', 'template')

	if create_view:
		view_name = args.file_name + '.php'
		create_file(view_name, 'view/', 'view')

	return


def  create_file(file_name, folder, file_type):
		
	file_location = ui.directory_path + folder + file_name

	if os.path.exists(file_location):
		print('Already exists a ' + file_type + ' named ' + file_name)

	try:
		with open('./commands/templates/' + file_type + '_template.txt') as template_file:
			template = template_file.read()
	except:
		print(file_type + ' template is not on templates directory')

	with open(file_location, 'w') as new_file:
		new_file.write(template)
	
	print(file_type + ' created')

def create_directory(dir_name, location):

	if os.path.exists(location + dir_name):
		print('Directory already exists')
		return False

	os.mkdir(location + dir_name)
	print('Directory created')
	return True

	
