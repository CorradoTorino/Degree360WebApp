import unittest
import re

from Degree360.urls import urlRegexPatterns

class TestUrls(unittest.TestCase):

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
        pattern = re.compile(urlRegexPatterns['feedbackProvider'])
        match = pattern.search(url)
        
        self.assertIsNotNone(match, 'Match not found for the url')
        
        self.assertEqual('ed521599-062e-4a19-bb2a-419ebc15e29c', match.group('pk'), 'guid in the url not found')
        self.assertEqual('dummyGuy@email.com', match.group('email'), 'email in the url not found')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()