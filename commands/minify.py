from commands import directory_path as dp
import sys
import requests
import glob
import time

path_src = dp.directory_path+'amd/src/'
path_build = dp.directory_path+'amd/build/'

def minify(option = None):
	if option == None:
		try:
			option = sys.argv[1]
		except:
			print("Missing parameters. Try 'minify help'.")
			return

	if option == 'all':
		files = [f for f in glob.glob(path_src + "*.js", recursive=True)]
		for f in files:
			print(do_request(f))
	elif option == "help":
		print('[all, <js file name>]')
	else:
		print(do_request(path_src+option))
	return

def do_request (js_file):
	try:
		with open(js_file) as js:
			to_min = js.read()
	except:
		return "File name '"+js_file+"' could not be reached."

	print("minifying '"+js_file.lstrip(path_src)+"'...")
	url = 'https://javascript-minifier.com/raw'
	data = {'input': to_min}
	try:
		r = requests.post(url, data)
	except:
		try:
			time.sleep(2)
			r = requests.post(url, data)
		except:
			return "Connection could not be established with file '"+js_file+"'"

	min_name = path_build+js_file.lstrip(path_src).rstrip('.js')+'.min.js'
	with open(min_name, 'w') as m:
		m.write(r.text)
	time.sleep(1)

	return js_file.lstrip(path_src)+' minified in '+path_build

if __name__ == "__main__":
	minify()
	sys.exit()
