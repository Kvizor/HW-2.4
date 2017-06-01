import glob
import os.path

def search_in_file(files):
	new_files = []
	qtity = 0
	user_input = input('Введите строку: ')
	for file in files:
		with open(file) as f:
			file_content = f.read()
			if user_input in file_content:
				new_files += [file]
				print(file)
				qtity += 1	
	print('Всего:', qtity)
	search_in_file(new_files)

migrations = 'Migrations'

files = glob.glob(os.path.join(migrations, "*.sql"))
search_in_file(files)