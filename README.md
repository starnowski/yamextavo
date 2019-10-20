[![Build Status](https://travis-ci.org/starnowski/yamextavo.svg?branch=master)](https://travis-ci.org/starnowski/yamextavo)

# yamextavo

### First implementation:

* ref_req - checks if reference passed as first argument exists and it is string with minimum one character.
If yes then behaviour is same as the 'any' validator. 

### TODO

* str_ref - String reference validator, contains 'min' and 'max' constraints and also 'regexp' constraint
* numb_ref - Number reference validator, contains 'min' and 'max' constraints

* any_ref - Checks if any of passed references validators 'str_ref' or 'numb_ref' returns true. If yes then behaviour is same as the 'any' validator.
* all_ref - Checks if all of passed references validators 'str_ref' or 'numb_ref' returns true. If yes then behaviour is same as the 'any' validator.