import file_manager as fm

def setup(file_name1, file_name2):
    file1=open(file_name1,"w")
    file1.write("Hello World")
    file1.close()
    file2=open(file_name2,"w")
    file2.close()

setup("Test1","Test2") #how do we do with filenames?, global variables or with a finder?(if it exists

def test_read_file1():
    content=fm.read_file("Test1")
    assert content=="Hello World"

def test_read_file2():
    assert fm.read_file("NonExistenFile")==None

def test_read_file3():
    content=fm.read_file("Test2")
    assert content==""

def run_tests():
    results = {"pass":0,"fail":0,"error":0}
    all_tests = find_tests("test_")
    for test in all_tests:
        try:
            test()
            results["pass"] += 1
        except AssertionError:
            results["fail"] = results["fail"] + 1
        except Exception:
            results["error"] += 1
    print(f"pass {results['pass']}")
    print(f"fail {results['fail']}")
    print(f"error {results['error']}")

def find_tests(prefix):
    tests = []
    for (name, func) in globals().items():
        if name.startswith(prefix):
            tests.append(func)
    return tests

run_tests()