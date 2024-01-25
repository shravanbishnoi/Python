"""Module for currency exchange
This module provides several string parsing functions to
implement a
simple currency exchange routine using an online currency
service.
The primary function in this module is exchange.

Author:Shravan
Date:30 nov 2022
"""


def before_space(s):
    """Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space

    Testcases:
    >>> before_space("welcome to")           #tests for single space
    'welcome'
    >>> before_space("welcome  to")          #tests for two spaces
    'welcome'
    >>> before_space(" welcome")             #tests when space given at starting
    ''
    >>> before_space("welcome  ")            #tests only word with spaces at last
    'welcome'
    """
    return s[:s.find(" ")]


def after_space(s):
    """Returns a copy of s after the first space
   
    Parameter s: the string to slice
    Precondition: s is a string with at least one space

    Testcases:
    >>> after_space("welocme to")      #tests for single space
    'to'
    >>> after_space("welcome  to")     #tests for two spaces
    'to'
    >>> after_space("welcome to ")     #tests for space at the end
    'to'
    """
    return s[s.find(" "):].strip()     #finds the empty string and takes it till the end and strips it


def first_inside_quotes(s):
    """Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that
    delimits it. We typically use single quotes (') to delimit 
    astring if we want to use a double quote character (") inside of
    it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C',
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double
    quotes.

    Testcases:
    >>> first_inside_quotes('a"abb"b')         #test for a substring
    'abb'
    >>> first_inside_quotes('a "abb" "ccc" b') #test for the first substring out of two
    'abb'
    """
    return s[s.index('"')+1:s.find('"',s.index('"')+1)].strip()


def get_lhs(json):
    """Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the
    keyword
    "lhs". For example, if the JSON is'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
    then this function returns '1 Bitcoin' (not '"1 Bitcoin"'). 
    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query

    Testcases:
    >>> get_lhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }') #test for lhs output when json has correct currency code
    '1 Bitcoin'
    >>> get_lhs('{ "lhs" : "", "rhs" : "", "err" : "Source currency code is invalid." }') #test for lhs output when json has an error
    ''
    """
    return json[json.index('"',json.index(':'))+1:json.index('"',json.index('"',json.index(':'))+1)].strip()


def get_rhs(json):
    """Returns the rhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the
    keyword
    "rhs". For example, if the JSON is'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
    then this function returns '19995.85429186 Euros' (not'"38781.518240835 Euros"').
    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query

    Testcases:
    >>> get_rhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }') #test for rhs output when json has correct currency code
    '19995.85429186 Euros'
    >>> get_rhs('{ "lhs" : "", "rhs" : "", "err" : "Source currency code is invalid." }') #test for rhs output when json has an error
    ''
    """
    return json[json.index('"',json.index('"rhs"')+5)+1:json.index('"',json.index('"',json.index('"rhs"')+5)+1)].strip()


def has_error(json):
    """Returns True if the query has an error; False otherwise

    Given a JSON response to a currency query, this returns True if 
    there is an error message. For example, if the JSON is'{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
    then the query is not valid, so this function returns True
    (It does NOT return the message 'Currency amount is invalid.')

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query

    Testcases:
    >>> has_error('{ "lhs" : "USD", "rhs" : "INR", "err" : "" }')                 #checks for empty substring                 
    False
    >>> has_error('{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid" }') #checks for multiple character in 6th substring
    True
    """
    index_err=json.index('"err"')                                   #index of "err"
    index_1=json.index('"',index_err+5)                             #index of starting double quotes after "err"
    index_2=json.index('"',index_1+1)                               #index of ending double quotes after "err"
    return index_2>=index_1+2                                    


def query_website(old,new,amt):
    """Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency old to the
    currency new. The response should be a string of the form'{ "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'
    where the values old-amount and new-amount contain the value
    and name for the old and new currencies. If the query is
    invalid, both old-amount and new-amount will be empty, while
    "err" will have an error message.

    Parameter old: the currency on hand
    Precondition: old is a string with no spaces or non-letters

    Parameter new: the currency to convert to
    Precondition: new is a string with no spaces or non-letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float

    Testcases:
    >>> query_website("USD","AED",2.5)           #test when input is correct
    '{ "lhs" : "2.5 United States Dollars", "rhs" : "9.18275 United Arab Emirates Dirhams", "err" : "" }'
    >>> query_website("USD","aaa",2.5)           #test when input is incorrect
    '{ "lhs" : "", "rhs" : "", "err" : "Exchange currency code is invalid." }'
    """
    import requests
    json=(requests.get(f"http://cs1110.cs.cornell.edu/2022fa/a1?old={old}&new={new}&amt={amt}")).text
    return json


def is_currency(code):
    """Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.

    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces or non-letters.
    
    Testcases:
    >>> is_currency("USD")             #test when currency code is correct
    True
    >>> is_currency("AAA")             #test when currency code entered is incorrect but are in upper case
    False
    >>> is_currency("abc")             #test case when currency code entered is incorrect but are in lower case
    False
    """
    return not(has_error(query_website(code,code,1.0)))


def exchange(old, new, amt):
    """Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency
    old to the currency new. The value returned represents the
    amount in currency new.
    The value returned has type float.

    Parameter old: the currency on hand
    Precondition: old is a string for a valid currency code

    Parameter new: the currency to convert to
    Precondition: new is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    rhs=get_rhs(query_website(old,new,amt))
    new_amt=before_space(rhs)
    return new_amt
