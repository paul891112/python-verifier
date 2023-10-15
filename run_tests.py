#2-3 tests for each function

import os
import pprint as pp
import file_manager as fm
import time
import shutil
import sys


def setup():
    p = os.getcwd()
    d_name = "TESTS"
    counter = 1
    while os.path.isdir(d_name):
        d_name = d_name[:5] + str(counter)
        counter += 1
    os.makedirs(d_name)
    dir_path= os.getcwd()+fr"\{d_name}"
    with open(dir_path+r"\test_file1.txt","w") as file1:
        file1.write("Hello World")

    file2=open(dir_path+r"\test_file2.txt","w")
    file2.close()

    return dir_path
def test_read_file1(path):
    content=fm.read_file(path+r"\test_file1.txt")
    assert content=="Hello World"

def test_read_file2(path):
    assert fm.read_file(path+r"\NonExistenFile.txt")==None

def test_read_file3(path):
    content=fm.read_file(path+r"\test_file2.txt")
    assert content==""

#--------Test create_file - all 4 tested, they all do what they should-------------
def test_create_file1(cwd_path):

    filepath = cwd_path + "/create.txt"
    res = fm.create_file(filepath, "content is not empty")
    print("1 success")
    assert res == True
    
def test_create_file2(cwd_path):
    filepath = cwd_path + "/create.txt"
    res = fm.create_file(filepath)
    print("2 success")
    assert res == True
    with open(filepath, 'r') as f:
        lines = f.read()
    assert lines == ""

def test_create_file21(cwd_path):
    filepath = cwd_path + "/create.txt"
    res = fm.create_file(filepath, "content is not empty")
    print("21 success")
    assert res == True
    with open(filepath, 'r') as f:
        lines = f.read()
    assert lines == "content is not empty"


def test_create_file3(cwd_path):
    filepath = 123
    res = fm.create_file(filepath)
    print("3 success")
    assert res == False

#--------End of Test create_file -----------------------------------

    

def teardown(directory = ''):
    '''
    deletes the directory, returns None
    '''
    shutil.rmtree(directory)


#---------11.10-------------------------------------------------

def run_tests():
    results = {"pass":0, "fail":0, "error":0}
    prefix = get_testname() # returns the pattern of testname
    all_tests = find_tests(prefix)
    for test in all_tests:
        try:
            cwd_path = setup()
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
            teardown(cwd_path) 
    print(f"pass {results['pass']}")
    print(f"fail {results['fail']}")
    print(f"error {results['error']}")
    
def get_testname():
    '''
    Handles the -s or --select.

    Args:
        -

    Returns:
        str: "test_" if not specified, the pattern "PATTERN" after -s or --select, raises exception otherwise
    '''
    if len(sys.argv) < 2:
        return "test_"
    elif len(sys.argv == 3):
        code = sys.argv[1]
        pattern = sys.argv[2]
        if code == '-s' or code == '--select':
            return pattern
        else:
            raise Exception("Usage: run_tests.py -s pattern or runtests.py --select pattern")
    else:
        raise Exception("Usage: run_tests.py -s pattern or runtests.py --select pattern")



def find_tests(prefix):
    tests = []
    for (name, func) in globals().items():
        if prefix in name:
            tests.append(func)
    return tests

def main():
    run_tests()


if __name__ == "__main__":
    main()

#------end of 11.10------------------------------------------