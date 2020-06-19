# Builder

'''
Builder is useful when you have to construct many elements. This example uses generating HTML elements.

 '''


class HtmlElement:
 	INDENT_SIZE = 2

 	def __init__(self, name='', text=''):
 		self.text = text
 		self.name = name
 		self.elements = []

 	def __str(self, indent):
 		lines = []
 		i = ' ' * (indent * self.INDENT_SIZE)
 		lines.append(f'{i}<{self.name}>')

 		if self.text:
 			i1 = ' ' * ((indent + 1) * self.INDENT_SIZE)
 			lines.append(f'{i1}{self.text}')

 		for e in self.elements:
 			lines.append(e.__str(indent + 1))

 		lines.append(f'{i}</{self.name}>')
 		return '\n'.join(lines)

 	def __str__(self):
 		return self.__str(0)

 	@staticmethod
 	def create(name):
 		return HTMLBuilder(name)

class HtmlBuilder:
	__root = HtmlElement()

	def __init__(self, root_name):
		self.root_name = root_name
		self.__root.name = root_name

	# not fluent
	def add_child(self, child_name, child_text):
		self.__root.elements.append(HtmlElement(child_name, child_text))

	#fluent
	def add_child_fluent(self, child_name, child_text):
		self.__root.elements.append(HtmlElement(child_name, child_text))
		return self

	def clear(self):
		self.__root = HtmlElement(name=self.root_name)

	def __str__(self):
		return str(self.__root)
			

# ordinary non-fluent builder
builder = HtmlBuilder('ul')
builder.add_child('li', 'hello')
builder.add_child('li', 'world')
print('Ordinary builder:')
print(builder)

# fluent builder you can add 2 add childs calls one after another
builder.clear()
builder.add_child_fluent('li', 'hello').add_child_fluent('li', 'world')
print('Fluent builder:')
print(builder)