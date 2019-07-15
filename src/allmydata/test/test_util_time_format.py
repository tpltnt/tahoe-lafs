"""
Tests for the time string formatting functions in util/time_format.py
"""
from twisted.trial import unittest
from allmydata.util.time_format import parse_duration

class ParseDuration(unittest.TestCase):
    """
    Tests for the parse_duration() function.
    """

    def test_positive_examples(self):
        """
        minimal positive tests
        """
        # test seconds
        # TODO: check if this is expected behavior (seconds not mentioned in ValueError)
        #self.assertEqual(5, parse_duration("5s"))
        #self.assertEqual(15, parse_duration("15 s"))

        # test days
        day_factor = 60*60*24
        self.assertEqual(1*day_factor, parse_duration("1day"))
        self.assertEqual(5*day_factor, parse_duration("5 day"))

        # test months
        month_factor = 31*day_factor
        self.assertEqual(1*month_factor, parse_duration("1month"))
        self.assertEqual(5*month_factor, parse_duration("5 month"))
        self.assertEqual(47*month_factor, parse_duration("47mo"))
        self.assertEqual(7384*month_factor, parse_duration("7384 mo"))

        # test years
        year_factor = 365*day_factor
        self.assertEqual(8*year_factor, parse_duration("8year"))
        self.assertEqual(984*year_factor, parse_duration("984 year"))


    def test_errors(self):
        """
        test errors
        """
        self.failUnlessRaises(ValueError, parse_duration, "lalala")
        self.failUnlessRaises(ValueError, parse_duration, "5")
