import sys
import os
import unittest
# add src directory to sys.path
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'src')))

from src.outfit_recommender import recommend_outfit

class TestOutfitRecommender(unittest.TestCase):
    def test_recommend_outfit(self):
        self.assertEqual(recommend_outfit(30,'sunny'),"tshirt,jeans and sneakers.")
        self.assertEqual(recommend_outfit(20,'cloudy'),"Jacket,jeans and a beanie.")
        self.assertEqual(recommend_outfit(10,'rainy'),"Jacket,jeans and a beanie.")
        self.assertEqual(recommend_outfit(0,'snowy'),"heavy coat,woolen scarf,gloves and boots.")

if __name__=='__main__':
   unittest.main()