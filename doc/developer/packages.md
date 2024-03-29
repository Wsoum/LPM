# Package model
This section of program handles package data layer.
This is at `src/lpm/package.loza`.

## Class `Package`

```bash
$pkg = lpm.Package('f:/path/to/package/dir')
$pkg = lpm.Package('gh:user/repo')
```

### Drivers
Currently, we have 2 drivers: `f` and `gh`.

Structure of package name: `<driver>:<address>`.

`f` means a local directory.
`gh` means a github repository.

Driver of `f` is `lpm.FileDriver` and `gh` is `lpm.GithubDriver`.

### Error handling
If you create a `Package` object, if there was a error, this error will be stored in `$pkg->error`.

```bash
$pkg = lpm.Package('f:/path/to/package/dir')

if $pkg->is_success()
    # package is valid and loaded successfully
    # ...
else
    # there is some errors
    println $pkg->error # print the error
endif
```

Usual errors for `f` driver:
- `not found`: directory not found
- `not a Git reposotory`: the directory is not a git repository (haven't `.git/`)
- `faild to load list of versions: <error>`: error while loading list of package versions

### `$pkg->versions`
This attribute contains list of versions (git tags).

### `$pkg->get_version($version)`
This method loads `LPMfile` config of a specify version in a package.

```bash
# Example
println 'Descripion: ' + $pkg->get_version('1.0')->description
```

### Driver methods
The driver of a package is accessible with `$pkg->driver`.

#### `$pkg->driver->load_file_content($version, $filename)`
With this method, you can load content of a specify file in a specify version of package.

#### `$pkg->driver->download($target_path, $version)`
This method downloads/copies a specify version of the package to the target path.

#### `$pkg->driver->get_branches()`
Returns list of git repository branches.

## Class `PackageDirectory`
The LPM packages will be installed in a directory named `loza_modules`.
This class handles this directory and provides some methods for checking installed packages.

### init
You should pass path of `loza_modules` directory to the constructor of the class:

```bash
$pkg_dir = lpm.PackageDirectory('/path/to/loza_modules') # also you can use other name instead of `loza_modules`
```

#### Auto path finding
You can load pkgdir without specifying directory path:

```bash
$pkg_dir = lpm.PackageDirectory()
```

The above code, will check a name define named `LPM_GLOBAL`. if this is `true`, loads global package directory at `<home>/.local/lib/loza_modules`, if not, loads `./loza_modules`.

### `is_installed($name)`
This method checks a package is installed or not. gets unique name of package (for example `lpm`).

Returns `false` if package is not installed.
But if package is installed, returns installed version as string.

### `installed_list()`
This method returns list of installed packages in the directory in this structure:

```
[
    [<lpm.Package object>, 'installed-version'],
    [<lpm.Package object>, 'installed-version'],
    [<lpm.Package object>, 'installed-version'],
]
```

### Query Checker
To check a query on the package checker:

```bash
println $dir->query('foo | bar = 1.0 ...')
```

([Read query system](../query.md))

## Class `Installer`
This class installs a package in a package directory (`loza_modules`).

```bash
$installer = lpm.Installer()
$installer->install($pkg, $version, $pkg_dir)
```

The `$pkg` should be a `lpm.Package`.
`$version` is a string.
`$pkg_dir` should be a `lpm.PackageDirectory`.
