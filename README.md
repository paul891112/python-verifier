# python-verifier

As a first assignment in the course "Software Construction" at University of Zurich the below described test environment for the python file "file_manager.py" had to be created.

## run_tests function

This function handles test running. It retrieves the pattern of tests to be tested, runs them and the keep the results. The result is kept in a dictionary with the three possible states: pass, fail and error. The key is the state and value serves as a counter to record the final result.

First, all relevant tests should be kept in a list and run one after each other. This is taken care of by get_testname() and find_tests() functions.


get_testname() reads the command line instruction and expects the following cases:

	1. No specified pattern, i.e. "python run_tests.py" runs every test. Since every name starts with "test_", the string will be returned to serve as a search keyword.

	2. "-s" or "--select PATTERN", i.e. "python run_tests.py -s create" runs the function, recognizes "-s" and "--select" as valid command, captures the pattern 	"create" and returns it. In case some typo or invalid command is entered (e.g. -a, -select), an exception is thrown and the correct usage is displayed.

	3. All other entries in the command line are considered invalid, throw an exception and display correct usage.

The function makes use of the module "sys", as this allows to get "argv".

Once the testing pattern is retrieved, it is passed as an argument to find_tests() which searches the corresponding tests in the global symbol table. Found tests will be kept in a list and returned.

all_tests contains every test to be run, run_tests() will loop through every element and try to run it. If no exception occurs, the test passes and increments the amount of "pass" by one. Otherwise, in case of "AssertionError" it is handled as a "fail" state accordingly, as well for "Exception" in all other cases. For clear overview, the final result is displayed after all tests are run.

Before each test, setup() will be called to create a safe testing environment, while after each testing call the teardown() function cleans up all the modifications made during the setup and testing.
To measure the tests running time, we record the starting time (st) and subtract it from the time right after the test terminates (et), using the function "time()" from the time module. As the test can have an AssertionError or Exception, the termination time is added after "test" in "try" and at the beginning of "except AssertionError" and "except Exception". While testing locally, the running time shows 0.0.


To highlight different testing results (pass, fail, error) with colors, we use the module "colorama" and import "Fore" to display color red, yellow, green and white. 

Finally, we only want run_tests() to run when the file is used as script, therefore we embedded it inside the main() function.


***
## Setup function 

The setup function creates a folder in the current working directory, which then includes two test files.
Instead of a file in the current path, we chose to create a directory, which then includes two test files. Because of that, we do not have to test once for each file, if the name already exists. Also, the teardown only has to delete the directory instead of having to find the correct files to delete.

The function setup() first checks, whether the directory including the test files that is to be created, already exists and then creates a unique directory. In case a directory with the same name already exists, a while-loop adds an incrementing integer to the end of the name. The loop stops once a unique name has been found and the directory has been created.
Inside that directory two unique files are created. As the directory has just been created, no further checks for already existing file names have to be made for the test files.
The first file "test_file1.txt" has the content "Hello world" and the second file "test_file2.txt" is empty. The empty file is utilized in a test, so the creation is done in setup().
Setup() returns the path of the created directory for the tests. Because of the function creating the directory in the current path, the function should work properly on all machines without a static path. We tested especially on windows machines, as no linux or mac os computers were available for us.


***
## Teardown function

The teardown function deletes the testing directory and its content.
It uses the "shutil" module function "shutil.rmtree(directory_path)", as this allows to delete the whole directory including files, instead of having to loop through the whole directory and deleting all files one by one.
If you chose os.remove(directory), an error would occur, as this function does not allow to remove subordinate files.
As all temporary files have been created inside the new unique directory, deleting the newly created directory after every test is enough to completely undo the initial changes of the run_tests() iterations.


***
## Testing functions

All files have a parameter "path", which is the path of the created directory passed from setup(). Because of that, all tests have the same dynamic path as acquired from setup().

An important aspect of all tests is, that the assertion, which makes sure, that the function behaves as expected, does not come directly from the function to be tested as well.
When creating or deleting a file you have to not only make sure, that the function returns a correct return value, but also whether the expected behaviour has actually taken place. So, e.g. it has to be tested if a function returns "True" after successfully deleting the file and also if the file has actually been deleted.
All tests include a "assert", which determines the output of the test.


***
### Tests for function read_file

To test the "read_file()" function we want to test the following four cases:

1. Test if it reads contents in the file correctly. (test_read_file_correct)

2. Test if the "FileNotFoundError" works, by checking if it returns "None". (test_read_file_None)

3. Test if it reads an empty file correctly. (test_read_file_empty)

4. Test the exception where it would return None and print something. (test_read_file_error)

The tests 1 and 3 are straightforward. The setup function gives the path to the directory with the 2 files. One file has the content "Hello World" and the other file has no content. The tests then exactly test these two cases.
To be able to pass test 2 we enter a file name that does not exist. As there is a separate folder made in the setup, there is no chance of the file already existing.
For test 4 we enter an invalid filename such as integers which then raise the correct exception.


***
### Tests for function create_file

To test the "create_file()" function, we want to consider the following four cases:

1. The function returns "True" when called with valid filepath and optional content as parameter. (test_create_file_create)

2. After call with valid path parameter, an empty file with specified name is indeed created in testing directory. (test_create_file_empty)

3. After call with valid path parameter, a file with specified name and same content as the parameter is indeed created in testing directory. (test_create_file_same_content)

4. If an invalid type for file path is passed, the function should return "False". (test_create_file_invalid_name)

Test 1 is straightforward. The setup function gives the path of the created directory. A file with the file name "create.txt" and the path from setup is created by "create_file". The test checks if the return value of the test is "True".
Test 2 calls the "create_file" function with the parameter "" (parameter which determines the content) and checks with the "open" function and the parameter "r" (read), whether the file has actually been created and is empty.
Analogously to Test 2, Test 3 calls the "create_file" function with the parameter "content is not empty" and checks with the "open" function and the parameter "r" (read), whether the file has actually been created and has the expected content.
Test 4 calls the "create_file" function with the invalid parameter "123" (as an integer, not a string, so without quotation marks) and excepts the return value "False".
A correct implementation of the "create_file()" function in filemanager.py should pass all the tests mentioned above.


***
### Tests for function write_file

To test the "write_file()" function, we want to consider the following cases:

1. The function returns "True" when called with valid filepath and optional content as parameter. (test_write_file_true)

2. After call with valid path parameter, the content given as a parameter is indeed written in the specified file in the testing directory. (test_write_file_correct_content)

3. If an invalid type for file path is passed, the function should return "False". (test_write_file_integers_false)

Test 1 is straightforward. The setup function gives the path of the created directory. The test calls "delete_file" with this path and our created file "test_file1.txt" and checks if the return value is "True".
Test 2 checks, if the file has actually been deleted by calling the function "os.path.exists(filepath)", where "filepath" is the path of "test_file1.txt" in our created directory. The return of "os.path.exists(filepath)" should be "False", if the file has been deleted.
Test 3 calls "write_file" with the integer "123" (as an integer, not a string, so without quotation marks) as a second parameter, which is an invalid type. The 
A correct implementation of the "write_file()" function in filemanager.py should pass all the tests mentioned above.

***
### Tests for function delete_file

To test the "delete_file()" function, we want to consider the following cases:

1. The function returns "True" when called with valid filepath. (test_delete_file_true)

2. After call with valid path parameter, the specified file is indeed deleted. (test_delete_file_correct_deletion)

3. The function is called with a file name that does not exist and should return "False". (test_delete_file_false_input)

4. If the specified file has "read-only" permissions, an error should occur and "False" should be returned. (test_delete_file_perm_err)

5. If an invalid type for file path is passed (here the path leads to the directory, which was created in setup), the function should return "False". (test_delete_file_dir)

Test 1 calls the function with the path and "test_file1.txt" and should return "True".
Test 2 checks, whether the file "test_file1.txt" has actually been deleted after the function returns "True".
Test 3 calls the function with the path and "WRONG_FILENAME.txt" and should return "False", as this file name does not exit in our testing directory.
In Test 4 we import "S_IREAD", "S_IRGRP", "S_IROTH" and "S_IWUSR" from "stat" to test the permission error, which should be an "Exception" in the function. Inside the test the imports are used to give "read-only" permissions on the file and restore "write" permissions at the end of the test.
Test 5 checks, whether the function returns "False" in case it is called with the path given by "setup", so a path leading to a directory.
A correct implementation of the "delete_file()" function in filemanager.py should pass all the tests mentioned above.

***
### Authors
Roxane Jaecklin, Ting-Chun Huang, Nils Reusch
