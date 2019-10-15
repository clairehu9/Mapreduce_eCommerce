# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 23:07:25 2019

@author: clair
"""

from mrjob.job import MRJob
from mrjob.step import MRStep


class PopularProduct(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_feedbackcount,
                   reducer=self.reducer_totalfeedback),
            MRStep(mapper=self.mapper_popular_product,
                   reducer = self.reducer_output)
        ]
        
    def mapper_feedbackcount(self, _, line):
        (ClothingID, rating, IND, PositiveFeedbackCount) = line.split(',')
        yield ClothingID, float(PositiveFeedbackCount) 
        
    def reducer_totalfeedback(self, ClothingID, PositiveFeedbackCount):
        yield ClothingID, sum(PositiveFeedbackCount) 

    def mapper_popular_product(self, ClothingID, Count): 
        yield '%04d'%Count, ClothingID

    def reducer_output(self, Count, ClothingIDs):
        for ClothingID in ClothingIDs:
            yield Count, ClothingID

if __name__ == '__main__':
    PopularProduct.run()

# !python PopularProduct.py WomensClothing.csv > PopularProduct.txt