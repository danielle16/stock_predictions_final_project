import py_compile,sys
input = sys.argv[1]
output = sys.argv[2]
py_compile.compile(input, './'+output)