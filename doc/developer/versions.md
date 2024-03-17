# Version parser
LPM has a version parser in `src/lpm/version.loza` to parse and compare version numbers.

## `lpm.version.compare($a, $b)`
This function compares two versions:

```bash
println lpm.version.compare('2.0', '1.0') # `1`
println lpm.version.compare('2.0', '4.0') # `-1`
println lpm.version.compare('3.1', '3.1') # `0`
```

This function returns `1` if a is bigger than b, `-1` if a is less than b and `0` if both version equal.

## `lpm.version.try_parse_int($str)`
This function parses a int from string but converts non-numeric chars to their code and returns the filtered string.

## `lpm.version.parse($str)`
This function parses a version string and returns a array from numbers.

```bash
lpm.version.parse('1.5.29-a1') # [1, 5, 29, -1, 971]
```

## `lpm.version.sort_list($list)`
With this function, you can sort a list of versions.

```bash
$versions = [
    '1.0',
    '3.0',
    '0.0.1',
    '0.8',
    '0.5',
]

$sorted_versions = lpm.version.sort_list($versions)

println $sorted_versions # output: ['0.0.1', '0.5', '0.8', '1.0', '3.0']
```
