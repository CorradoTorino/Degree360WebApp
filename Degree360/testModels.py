import unittest

from .models import RelationType
from Degree360.models import FeedbackProvider

def CreateDummyRelationPeer():
    aRelation = RelationType()
    aRelation.relation_type = 'DummyPeer'
    aRelation.description = 'A dummy colleague'
    return aRelation
    
def CreateDummmyFeedbackProvider():
    aFeedbackProvider = FeedbackProvider()
    aFeedbackProvider.name = 'DummyName'
    aFeedbackProvider.last_name = 'DummylastName'
    aFeedbackProvider.relation_type = CreateDummyRelationPeer()
    aFeedbackProvider.email = 'dummy@myEmail.com'
    return aFeedbackProvider
        
class Test(unittest.TestCase):

    def testName(self):
        pass
    
    def testRelationType__str__(self):
        aRelation = CreateDummyRelationPeer()        
        self.assertEqual('DummyPeer: A dummy colleague', aRelation.__str__())
        
    def testFeedbackProvider(self):
        aFeedbackProvider = CreateDummmyFeedbackProvider()
        self.assertEqual('DummyName DummylastName (dummy@myEmail.com)', aFeedbackProvider.__str__())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()