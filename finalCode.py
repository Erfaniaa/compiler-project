class FinalCode:
	codes = []

	def update_rule(self, rule_number, operand_number, value):
		self.codes[rule_number][operand_number] = value

	def add_rule(self, rule):
		self.codes.append(rule)

	def get_pc(self):
		len(self.codes)
