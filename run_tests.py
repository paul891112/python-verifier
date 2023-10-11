#2-3 tests for each function

import os
import pprint as pp
import file_manager as fm
import time

def setup():
    return

def test_create_file1():
    filepath = "C:\Dateien\SWcon\Assignment 1\test.txt"
    res = fm.create_file(filepath, "content is not empty")
    assert res == True
    
def test_create_file2():
    filepath = "C:\Dateien\SWcon\Assignment 1\test.txt"
    res = fm.create_file(filepath)
    assert res == True
    with open(filepath, 'r') as f:
        lines = f.read()
    assert lines == ""

def test_create_file21():
    filepath = "C:\Dateien\SWcon\Assignment 1\test.txt"
    res = fm.create_file(filepath, "content is not empty")
    assert res == True
    with open(filepath, 'r') as f:
        lines = f.read()
    assert lines == "content is not empty"


def test_create_file3(str):
    filepath = 123
    res = fm.create_file(filepath)
    assert res == False


    

def teardown(directory = ''): #delete unwanted .txt files? Assume there are no .txt files in directory?
    '''
    Removes all .txt file in the current working directory or optional file path, return None
    '''
    if directory == '':
        directory = os.getcwd()
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

    for f in txt_files:
        os.remove(f)

def teardown(file_name1, file_name2, optfile_name=""): #how to pass the filenames?
    '''
    Takes two arguments and one optional argument
    arg1: file path of first file in setup 
    arg2: file path of second file in setup
    arg3: optional argument, path of created file in create_file to be deleted
    '''

    if os.path.exists(file_name1):
        os.remove(file_name1)
    if os.path.exists(file_name2):
        os.remove(file_name2)
    if os.path.exists(optfile_name):
        os.remove(optfile_name)


#---------09.10-------------------------------------------------

def run_tests():
    results = {"pass":0, "fail":0, "error":0}
    prefix = get_testname() # returns the pattern of testname
    all_tests = find_tests(prefix)
    for test in all_tests:
        try:
            setup()
            st = time.time()
            test()
            results["pass"] += 1
        except AssertionError:
            results["fail"] = results["fail"] + 1
        except Exception:
            results["error"] += 1
        finally:
            et = time.time()
            print("Testing time: ", et-st)
            teardown() 
    print(f"pass {results['pass']}")
    print(f"fail {results['fail']}")
    print(f"error {results['error']}")
    
def get_testname():
    '''
    Handles the -s or --select
    '''
    return

def find_tests(prefix):
    tests = []
    for (name, func) in globals().items():
        if name.startswith(prefix):
            tests.append(func)
    return tests

