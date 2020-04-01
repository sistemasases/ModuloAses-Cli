from commands import user_info as ui
import sys
import requests
import glob
import time

path_src = ui.directory_path+'amd/src/'
path_build = ui.directory_path+'amd/build/'

def minify(args = None):
	if args == None:
		try:
			args = {"name": sys.argv[1]}
		except:
			print("Missing parameters. Try 'minify help'.")
			return

	if args.js_name == 'all':
		files = [f for f in glob.glob(path_src + "*.js", recursive=True)]
		for f in files:
			print(do_request(f))
	else:
		print(do_request(path_src+args.js_name))
	return

def do_request (js_file):
	try:
		with open(js_file) as js:
			to_min = js.read()
	except:
		return "File name '"+js_file+"' could not be reached."

	js_name = js_file.replace(path_src,'')
	print("minifying '"+js_name+"'...")
	url = 'https://javascript-minifier.com/raw'
	data = {'input': to_min}
	counter = 0
	while counter <= 5:
		try:
			r = requests.post(url, data)
			counter = 6
		except:
			time.sleep(1)
			counter+=1
			if counter == 6:
				return "Connection could not be established with file '"+js_file+"'"

	min_name = path_build + js_name.replace('.js','.min.js')
	with open(min_name, 'w') as m:
		m.write(r.text)
	time.sleep(1)

	return js_name + ' minified in ' + path_build

if __name__ == "__main__":
	minify()
	sys.exit()
