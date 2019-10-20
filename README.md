[![Build Status](https://travis-ci.org/starnowski/yamextavo.svg?branch=master)](https://travis-ci.org/starnowski/yamextavo)

# yamextavo

### First implementation:

* ref_req - checks if reference passed as first argument exists and it is string with minimum one character.
If yes then behaviour is same as the 'any' validator. 

### TODO

* str_ref - [0.1] String reference validator, contains 'min' and 'max' constraints and also 'regexp' constraint
* numb_ref - [0.1] Number reference validator, contains 'min' and 'max' constraints

* any_ref - [0.2] Checks if any of passed references validators 'str_ref' or 'numb_ref' returns true. If yes then behaviour is same as the 'any' validator.
    [0.3] Validation should be done based on validators which were defined only for first reference validator whichs conditions were satisfied.
* all_ref - [0.2] Checks if all of passed references validators 'str_ref' or 'numb_ref' returns true. If yes then behaviour is same as the 'any' validator.
    [0.3] Validation should be done based on all validators which were defined for all reference validators.