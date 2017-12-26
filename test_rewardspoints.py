import unittest
import rewardspoints

class TestRewardPoints(unittest.TestCase):

	def setUp(self):
		self.rewardpoints = rewardspoints.RewardPoints()

	def test_receiving_bonus(self):
		self.rewardpoints.earn_points('John', 200)
		john_points = self.rewardpoints.consult_points('John')
		self.assertEqual(john_points, 700)

	def test_not_receiving_bonus(self):
		self.rewardpoints.earn_points('Nick', 0)
		nick_points = self.rewardpoints.consult_points('Nick')
		self.assertEqual(nick_points, 0)

	def test_earning_points_positive(self):
		self.rewardpoints.earn_points('Nick', 0)
		self.rewardpoints.earn_points('John', 200)

		nick_points = self.rewardpoints.consult_points('Nick')
		john_points = self.rewardpoints.consult_points('John')

		self.assertEqual(nick_points, 0)
		self.assertEqual(john_points, 700)

	def test_not_earning_points_negative(self):
		john_points = self.rewardpoints.consult_points('John')
		self.assertEqual(john_points, 0)
		john_points = self.rewardpoints.earn_points('John', -25)
		self.assertEqual(john_points, 0)

	def test_spend_points_less_than_zero(self):
		self.rewardpoints.earn_points('Nick', 0)
		self.rewardpoints.earn_points('John', 200)

		nick_points = self.rewardpoints.spend_points('Nick', -500)
		john_points = self.rewardpoints.spend_points('John', -500)

		self.assertEqual(nick_points, 0)
		self.assertEqual(john_points, 700)

	def test_spend_points_greater_than_zero(self):
		self.rewardpoints.earn_points('Nick', 50)
		self.rewardpoints.earn_points('John', 200)

		nick_points = self.rewardpoints.spend_points('Nick', 20)
		john_points = self.rewardpoints.spend_points('John', 20)

		self.assertEqual(nick_points, 530)
		self.assertEqual(john_points, 680)

	def test_no_having_enough_points_to_spend(self):
		self.rewardpoints.earn_points('Nick', 0)
		self.rewardpoints.earn_points('John', 200)

		nick_points = self.rewardpoints.spend_points('Nick', 100)
		john_points = self.rewardpoints.spend_points('John', 900)

		self.assertEqual(nick_points, 0)
		self.assertEqual(john_points, 700)

