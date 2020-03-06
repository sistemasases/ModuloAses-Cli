import sys
import requests
import glob
import time

init_path = '/var/www/html/moodle366/blocks/ases/amd/'
path_src = init_path+'src/'
path_build = init_path+'build/'

try:
    option = sys.argv[1]
except:
    print("Missing parameters. Try 'minifier help'.")
    sys.exit()

def minify (js_file):
    try:
        with open(js_file) as js:
            to_min = js.read()
    except:
        return "File name '"+js_file+"' could not be reached."

    print("minifying '"+js_file+"'...")
    url = 'https://javascript-minifier.com/raw'
    data = {'input': to_min}
    try:
        r = requests.post(url, data)
    except:
        time.sleep(2)
        r = requests.post(url, data)

    min_name = path_build+js_file.lstrip(path_src).rstrip('.js')+'.min.js'
    with open(min_name, 'w') as m:
        m.write(r.text)
    time.sleep(1)
   
    return js_file+' minified'

if option == 'all':
    files = [f for f in glob.glob(path_src + "*.js", recursive=True)]
    for f in files:
        print(minify(f))
    sys.exit()
elif option == "help":
    print('[all, <js file name>]')
else:
    print(minify(path_src+option))
    sys.exit()
