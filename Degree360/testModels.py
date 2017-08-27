import unittest

from .models import RelationType
from Degree360.models import FeedbackProvider

def CreateDummyRelationPeer():
    aRelation = RelationType()
    aRelation.relation_type = 'DummyPeer'
    aRelation.description = 'A dummy colleague'
    return aRelation
    
def CreateDummmyFeedbackProvider(name = 'DummyName', email = 'dummy@myEmail.com'):
    aFeedbackProvider = FeedbackProvider()
    aFeedbackProvider.name = name    
    aFeedbackProvider.relation_type = CreateDummyRelationPeer()
    aFeedbackProvider.email = email
    return aFeedbackProvider
        
class Test(unittest.TestCase):

    def testName(self):
        pass
    
    def test_RelationType__str__(self):
        aRelation = CreateDummyRelationPeer()        
        self.assertEqual('DummyPeer', aRelation.__str__())
        
    def test_FeedbackProvider(self):
        aFeedbackProvider = CreateDummmyFeedbackProvider()
        aFeedbackProvider.last_name = 'DummylastName'
        self.assertEqual('DummyName DummylastName (dummy@myEmail.com)', aFeedbackProvider.__str__())
        
    def test_FeedbackProvider_can_have_empty_LastName(self):
        aFeedbackProvider = CreateDummmyFeedbackProvider()
        self.assertEqual('', aFeedbackProvider.last_name)
        self.assertEqual('DummyName  (dummy@myEmail.com)', aFeedbackProvider.__str__())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()