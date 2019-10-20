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
    
    [0.4] All reference validators 'ref_req', 'str_ref', 'numb_ref', 'any_ref', 'all_ref' etc. should have property 'any_ref_priority'.
        Property would define priority amongst the references validators which are defined for "any_ref" validator.
        By default the value should be '0'.
        If property value is higher then the priority also higher, in case if at least two the references validators should be applied then the validator with higher priority should be chosen.
        In case when priorities are the same then validator should be chosen based on order.
    
* all_ref - [0.2] Checks if all of passed references validators 'str_ref' or 'numb_ref' returns true. If yes then behaviour is same as the 'any' validator.

    [0.3] Validation should be done based on all validators which were defined for all reference validators.