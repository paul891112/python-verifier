# 2-3 tests for each function

import os
import file_manager as fm
import time
import shutil
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
import sys
from colorama import Fore


def setup():
    d_name = "TESTS"
    counter = 1
    while os.path.isdir(d_name):
        d_name = d_name[:5] + str(counter)
        counter += 1
    os.makedirs(d_name)
    dir_path = os.getcwd() + fr"\{d_name}"
    with open(dir_path + r"\test_file1.txt", "w") as file1:
        file1.write("Hello World")

    file2 = open(dir_path + r"\test_file2.txt", "w")
    file2.close()

    return dir_path


# -----test read_file() ----------------------------------
def test_read_file_correct(path):
    res = fm.read_file(path + r"\test_file1.txt")
    assert res == "Hello World"


def test_read_file_None(path):
    res = fm.read_file(path + r"\NonExistentFile.txt")
    assert res == None


def test_read_file_empty(path):
    res = fm.read_file(path + r"\test_file2.txt")
    assert res == ""

def test_read_file_error(path):
    res = fm.read_file(123)
    assert res == None



# --------Test create_file - all 4 tested, they all do what they should-------------
def test_create_file_create(path):
    filepath = path + "/create.txt"
    res = fm.create_file(filepath, "content is not empty")
    assert res == True


def test_create_file_empty(path):
    filepath = path + "/create.txt"
    res = fm.create_file(filepath)
    assert res == True
    with open(filepath, 'r') as f:
        lines = f.read()
    assert lines == ""


def test_create_file_same_content(path):
    filepath = path + "/create.txt"
    res = fm.create_file(filepath, "content is not empty")
    assert res == True
    with open(filepath, 'r') as f:
        lines = f.read()
    assert lines == "content is not empty"


def test_create_file_invalid_name(path):
    filepath = 123
    res = fm.create_file(filepath)
    assert res == False


# --------Test write_file() -----------------------------------

def test_write_file_true(path):  # Successfully wrote the content -> True
    res = fm.write_file(path + fr"\test_file1.txt", "New content")
    assert res == True
    with open(path + fr"\test_file1.txt", 'r') as f:
        lines = f.read()
    assert lines == "New content"


def test_write_file_integers_false(path):  # Content is a integer instead of a string -> False
    res = fm.write_file(path + fr"\test_file.txt", 123)
    assert res == False


# --------Test delete_file() -----------------------------------

def test_delete_file_true(path):
    res = fm.delete_file(path + fr"\test_file1.txt")
    assert res == True


def test_delete_file_false_input(path):  # File does not exists, error has to appear
    res = fm.delete_file(path + fr"\WRONG_FILENAME.txt")
    assert res == False


def test_delete_file_perm_err(path):  # Exits with PermissionError
    os.chmod(path + fr"\test_file1.txt", S_IREAD | S_IRGRP | S_IROTH)
    res = fm.delete_file(path + fr"\test_file1.txt")
    assert res == False
    os.chmod(path + fr"\test_file1.txt", S_IWUSR | S_IREAD)


def test_delete_file_dir(path):  # False if path leads to a folder instead of a file
    res = fm.delete_file(path)
    assert res == False


# -----teardown()
def teardown(directory):
    '''
    deletes the directory, returns None
    '''
    shutil.rmtree(directory)


# ---------11.10-------------------------------------------------

def run_tests():
    results = {"pass": 0, "fail": 0, "error": 0}
    prefix = get_testname()  # returns the pattern of testname
    all_tests = find_tests(prefix)
    for test in all_tests:
        comment = ""
        cwd_path = setup()
        st = time.time()
        try:

            test(cwd_path)
            results["pass"] += 1
            comment += Fore.GREEN + "pass"
            comment+=Fore.WHITE
        except AssertionError:
            results["fail"] = results["fail"] + 1
            comment += Fore.RED + "fail"
        except Exception:
            results["error"] += 1
            comment += Fore.LIGHTYELLOW_EX + "error"
        finally:
            et = time.time()
            t = (et - st) * 1000
            # print("Testing time: ", et-st)
            teardown(cwd_path)
            print(Fore.LIGHTWHITE_EX + f"Test: {test.__name__} ran in {round(t, 2)} ms, status: {comment}")
    print(Fore.LIGHTWHITE_EX + "#------Final Status------#")
    print(Fore.GREEN + f"pass: {results['pass']}")
    print(Fore.LIGHTYELLOW_EX + f"error: {results['error']}")
    print(Fore.RED + f"fail: {results['fail']}")
    comment+=Fore.WHITE


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
    elif len(sys.argv) == 3:
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

# ------end of 11.10------------------------------------------
