import hashlib


def hashgen(file_path):
	with open(file_path) as f:
		new_line = f.readline()

		while new_line:
			new_line_hash = hashlib.md5(new_line.encode())
			yield new_line_hash.hexdigest()
			new_line = f.readline()


for i in hashgen('sample.txt'):
	print(i)