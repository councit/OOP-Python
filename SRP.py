# Single responisbility principal

'''Notes: When defining classes define a primary responsibility. 
Too many functionalities can make it diffifcult to modify in the future. 

''' 

class Journal:
	def __init__(self):
		self.entries = []
		self.count = 0

	def add_entry(self, text):
		self.count += 1
		self.entries.append(text)
		print(f'New entry added at position {self.entries[-1]}.')

	def del_entry(self, pos):
		self.count -= 1
		del self.entries[pos]
		print(f'Entry deleted at position {self.entries[pos]}.')

	def __str__(self):
		return '\n'.join(self.entries)

class PersisenceManager:
	@staticmethod
	def save_to_file(journal, filename):
		file = open(filename, 'w')
		file.write(str(journal))
		file.close()


# Tests



# my_j = Journal()

# print(str(my_j))

# my_j.add_entry('Today was good.')
# my_j.add_entry('Today was bad.')
# my_j.add_entry('Today was fun.')
# my_j.add_entry('Today was boring.')

# my_j.del_entry(2)

# my_j.entries

# file = r'journal.txt'
# PersisenceManager.save_to_file(my_j, file)