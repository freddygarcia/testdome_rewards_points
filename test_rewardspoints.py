import unittest
import rewardspoints



class TestRewardPoints(unittest.TestCase):

	def setUp(self):
		self.rewardpoints = rewardspoints.RewardPoints()
		self.rewardpoints.earn_points('Nick', 0)
		self.rewardpoints.earn_points('John', 200)

	def test_earn_points(self):

		nick_points = self.rewardpoints.consult_points('Nick')
		self.assertEqual(nick_points, 0)

		john_points = self.rewardpoints.consult_points('John')
		self.assertEqual(john_points, 700)

		john_points = self.rewardpoints.earn_points('John', -5)
		self.assertEqual(john_points, 700)

	def test_spend_points(self):

		nick_points = self.rewardpoints.spend_points('Nick', 100)
		self.assertEqual(nick_points, 0)

		nick_points = self.rewardpoints.spend_points('Nick', -500)
		self.assertEqual(nick_points, 0)

		john_points = self.rewardpoints.spend_points('John', -500)
		self.assertEqual(john_points, 700)

		john_points = self.rewardpoints.spend_points('John', 20)
		self.assertEqual(john_points, 680)
		
