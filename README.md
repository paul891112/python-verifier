# python-verifier



Setup function ()

This funciton creates two files, one called test1.txt, with a string "Hello world" as content, another file called test2.txt with no content.


Teardown function (Paul)

This function takes two arguments, parameter 1 is a string with the name of the .txt file created in setup function, parameter 2 is an optional parameter that represents the name of 


Testing functions

Test read_file()
We create two calls, one reads test1.txt, one reads test2.txt. Both should pass. 


Test create_file() (Paul)
We create two functions, one with string as parameter, one with interger as parameter. 


Test write_file()
We create two calls. One call with string "Goodbye world" as input, one with integer 1 as input. First call should return true, second call returns False. Both tests should pass.

Test delete_file()
We create three calls. One call with string test1.txt, one with string tet.txt, one with integer 1 as input. 
Before deleting, we check if the input name does not exist. If it indeed doesn't exist, the filenotfounderror can be ensured.


Introspection




"Modify the testing tool so that it records how long it takes to run each test. (The function time.time may be useful.)
"


