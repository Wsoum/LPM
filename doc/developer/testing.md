# Testing
This is a guide for testing system for this project.

## Running the tests
To run the LPM tests:

```bash
$ make test
# OR
$ loza tests/run.loza
# OR
$ ./tests/run.loza
```

To run a specify test:

```bash
$ loza tests/test_lpmfile.loza # or other test script
```

## Creating the tests
A Basic template for the test files.
Any loza script with `.loza` extension in the `tests` folder will be considered as test script.

For example `tests/test_my_simple_test.loza`:

```bash
# imports
import_once @test
import_once $__dir__ + `/../src/lpm/<something-in-lpm>...`

@doc "A Human readable caption for the test (will be showed by `tests/run.loza`)"
func test_my_simple_test()
    assert 1 == 1
    test.assertEquals(1, 1)
endfunc

# register the test function
redefine('TEST', test_my_simple_test)

# handle single test run
if $__ismain__
    TEST()
endif
```
