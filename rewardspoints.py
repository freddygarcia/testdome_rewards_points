from collections import defaultdict

class RewardPoints:
	def __init__(self):
		self.customers = defaultdict(int)
		self.given_bonus = []
		
	def earn_points(self, customer_name, points):
		if points > 0:
			# add points to customer
			self.customers[customer_name] += points

			# if first time curstomer earning points
			if customer_name not in self.given_bonus:
				# give 500 extra points
				self.customers[customer_name] += 500
				# save customer given points
				self.given_bonus.append(customer_name)

		# return current customer points
		return self.customers[customer_name]

	def spend_points(self, customer_name, points):

		# spent points must be a positive number 
		if points <= 0:
			return self.customers[customer_name]

		# if customer has enough points to spend
		if self.customers[customer_name] >= points:
			self.customers[customer_name] -= points

		# return current customer points
		return self.customers[customer_name]

	def consult_points(self, customer_name):
		return self.customers[customer_name]

if __name__ == '__main__':
	rewardPoints = RewardPoints()
	rewardPoints.earn_points('John', 520)
	print(rewardPoints.spend_points('John', 200))
