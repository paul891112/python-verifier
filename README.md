# python-verifier


#Upload code
1. Copy the url to this directory. Open command line, change local working directory to where you want to save this project, use command "git clone url". This only needs to be executed once.

2. On github website, go to "branches" and press the green button to create a new branch and name it "BRANCH_NAME". Then in local command line, enter the following commands one after each other:
git checkout main
git fetch --all
git fetch --prune
git checkout BRANCH_NAME

3. Make changes to the current files locally.

4. After the changes are made, enter the following commands in local command line one after each other:
git add .
git commit -m "COMMIT_MESSAGE" -m "ADDITIONAL_DESCRIPTION"
git push origin BRANCH_NAME
Replace BRANCH_NAME with the same branch name as you just created on github

5. Return to github webpage and go to the branch you created, write some optional description messages, create new pull request once everything is done. One other person will review it and merge the changes into main branch.

This part will be deleted after the project is finished.


# Setup function 

This funciton creates two files, one called test1.txt, with a string "Hello world" as content, another file called test2.txt with no content.


# Teardown function

This function takes two arguments, parameter 1 is a string with the name of the .txt file created in setup function, parameter 2 is an optional parameter that represents the name of 


# Testing functions

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


