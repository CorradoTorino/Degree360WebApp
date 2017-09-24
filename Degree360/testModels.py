import unittest
import re

from django.test import TestCase
from django.db import IntegrityError

from Degree360.models import FeedbackProvider, Survey, RelationType
from Degree360.urls import urlRegexPatterns

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

class TestUrls(TestCase):

    def assert_match_not_found_in_incorrect_url_for_requestFeedback(self, incorrect_url):
        pattern = re.compile(urlRegexPatterns['requestFeedback'])
        match = pattern.search(incorrect_url)
        
        self.assertIsNone(match, 'Match not found for the url')
         
    def test_regex_for_requestFeedback_url_ok(self):
        url = 'requestFeedback/ed521599-062e-4a19-bb2a-419ebc15e29c/'
        pattern = re.compile(urlRegexPatterns['requestFeedback'])
        match = pattern.search(url)
        
        self.assertIsNotNone(match, 'Match not found for the url')
        
        self.assertEqual('ed521599-062e-4a19-bb2a-419ebc15e29c', match.group('pk'), 'guid in the url not found')

    def test_regex_for_requestFeedback_url_with_erroneus_guid(self):
        incorrect_url = 'requestFeedback/d521599-062e-4a19-bb2a-419ebc15e29c/'               
        self.assert_match_not_found_in_incorrect_url_for_requestFeedback(incorrect_url)

    def test_regex_for_requestFeedback_url_without_requestFeedback(self):
        incorrect_url = 'd521599-062e-4a19-bb2a-419ebc15e29c/'               
        self.assert_match_not_found_in_incorrect_url_for_requestFeedback(incorrect_url)

    def test_regex_for_requestFeedback_url_with_misspelled_requestFeedback(self):
        incorrect_url = 'requestFedaback/d521599-062e-4a19-bb2a-419ebc15e29c/'               
        self.assert_match_not_found_in_incorrect_url_for_requestFeedback(incorrect_url)
    
    def test_regex_for_FeedbackProvider_url_ok(self):
        url = 'feedbackProvider/ed521599-062e-4a19-bb2a-419ebc15e29c/dummyGuy@email.com/'
        pattern = re.compile(urlRegexPatterns['EditFeedbackProvider'])
        match = pattern.search(url)
        
        self.assertIsNotNone(match, 'Match not found for the url')
        
        self.assertEqual('ed521599-062e-4a19-bb2a-419ebc15e29c', match.group('pk'), 'guid in the url not found')
        self.assertEqual('dummyGuy@email.com', match.group('email'), 'email in the url not found')
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()