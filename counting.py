
class count(object):
	
	def initialise(self):
		global count
		global cards_left
		count = 0
		cards_left = 52
		self.run()


	def run(self):
		last_card = 0
		while (cards_left != 0):
			last_card = self.user_input()
			if (last_card == "q"):
				break
			self.deck_count(1)
			last_count = self.add_to_count(last_card)
			self.current_count(last_card)
			print(count +"\n")


	def user_input(self):
		print("enter card value")
		last_card = input()
		return last_card

	def add_to_count(self, last_card):
		cards_left -= 1
		if (last_card > 6) and (last_card < 10):
			return 0
		elif (last_card <= 6):
			return 1
		else:
			return -1
		
	def deck_count(self, n):
		cards_left -= n

	def current_count(self, n):
		count += n 



c = count()
c.initialise()

