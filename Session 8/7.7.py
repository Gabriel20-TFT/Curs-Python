files = ['mare_2023.jpeg', 'test.txt', 'liste.py', 'cv.pdf']

paths = {
    'C://Downloads//Images': ['jpg', 'png', 'jpeg'],
    'C://Downloads//Text': ['txt'],
    'C://Downloads//Python_files': ['py'],
    'C://Downloads//PDF': ['pdf'],
}

extension_dict = {}

for path, extensions in paths.items():
    for extension in extensions:
        extension_dict[extension] = path

extensions = []

for file in files:
    extensions.append(file.split('.')[-1])

print(extensions)
