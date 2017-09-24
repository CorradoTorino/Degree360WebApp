import unittest

from django.test import TestCase
from django.db import IntegrityError

from Degree360.models import FeedbackProvider, Survey, RelationType

def CreateDummmyFeedbackProvider(name = 'DummyName', email = 'dummy@myEmail.com'):  
    aSurvey = Survey.create('dummyEmployName', 'dummyEmployLastName', 'dummyEmploy@myEmail.com')
    aRelation = RelationType.create('DummyPeer', 'A dummy colleague', aSurvey)
    aFeedbackProvider = FeedbackProvider.create(name, '', email, aRelation, aSurvey)
    return aFeedbackProvider
        
class Test(TestCase):
    
    def test_RelationType__str__(self):
        aSurvey = Survey.create('dummyEmployName', 'dummyEmployLastName', 'dummyEmploy@myEmail.com')
        aRelation = RelationType.create('DummyPeer', 'A dummy colleague', aSurvey)
          
        self.assertEqual('DummyPeer', aRelation.__str__())
        
    def test_FeedbackProvider__str__(self):
        aSurvey = Survey.create('dummyEmployName', 'dummyEmployLastName', 'dummyEmploy@myEmail.com')
        aRelation = RelationType.create('DummyPeer', 'A dummy colleague', aSurvey)
        aFeedbackProvider = FeedbackProvider.create('DummyName', 'DummylastName', 'dummy@myEmail.com', aRelation, aSurvey)

        self.assertEqual('DummyName DummylastName (dummy@myEmail.com)', aFeedbackProvider.__str__())
        
    def test_FeedbackProvider_can_have_empty_LastName(self):
        aSurvey = Survey.create('dummyEmployName', 'dummyEmployLastName', 'dummyEmploy@myEmail.com')
        aRelation = RelationType.create('DummyPeer', 'A dummy colleague', aSurvey)
        aFeedbackProvider = FeedbackProvider.create('DummyName', '', 'dummy@myEmail.com', aRelation, aSurvey)
        
        self.assertEqual('DummyName  (dummy@myEmail.com)', aFeedbackProvider.__str__())
        
    def test_Can_not_create_two_FeedbackProviders_with_same_email_for_asurvey(self):
        aSurvey = Survey.create('dummyEmployName', 'dummyEmployLastName', 'dummyEmploy@myEmail.com')
        aRelation = RelationType.create('DummyPeer', 'A dummy colleague', aSurvey)
        a1stFeedbackProvider = FeedbackProvider.create('A_name', 'A_lastname', 'dummy@myEmail.com', aRelation, aSurvey)
        
        try:     
            FeedbackProvider.create('An_other_name', 'An_other_lastname', 'dummy@myEmail.com', aRelation, aSurvey)
            self.fail("An IntegrityError was expected.")    
        except IntegrityError:
            self.assertEqual('A_name A_lastname (dummy@myEmail.com)', a1stFeedbackProvider.__str__())
            pass        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()