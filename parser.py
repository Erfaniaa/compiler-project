# from pythonds.basic.stack import Stack
import re
import sys

text = open(sys.argv[-1], 'r').read()

variables = {}
tokens = {}
RHST = {}
# parseStack = Stack()
# semanticStack = Stack()


# scanner = Parser(text, 'new_token', FINAL_STATES, TRANSITIONS, KEYWORDS)
# scanner_result = scanner.run()
class Parser:

	def parseCode(self):
		return

	def fillParseTable(self):
		return

	def findAllPredicts(self):
		return

	def findAllFollows(self):
		return

	def findAllFirsts(self):
		return

	def findAllNullable(self):
		return

	def readGrammer(self):
		return

	def run(self):
		ret = []
		while self.current_char_idx < len(text):
			token = self._next_token()
			if token and len(token.value) > 0:
				ret.append(token)
		return ret


print(text)
