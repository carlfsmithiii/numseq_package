import timeit

print("total execution time: "
      + str(timeit.timeit("test_code.numseq_package_test()",
                          setup="import test_code", number=1)))
