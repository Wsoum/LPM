# Introduction to the LPM package manager
LPM can load packages in two types: local git directories and github repositories.

All the LPM packages are based on the git repositories. this repos can be local and can be on github.

Naming structure of packages is something like this:

```
<driver>:<name>
f:/path/to/local/directory
gh:user/repo
```

You can see information of the packages using `show` command:

```bash
$ lpm show gh:foo/bar
Name: ...
Description: ...
...
```

Also you can specify version of the packages:

```bash
$ lpm show gh:foo/bar=1.9
```

LPM uses **Git tags** as versions. means, if you want to handle versions of your package,
you don't need to upload or publish new versions anywhere. you only need to set a git tag on your repo.

Also LPM haven't any official server for indexing packages. because this Package manager
uses github repos and package maintainers not need to publish the packages anywhere.

## Basic package defination
If you want to define a basic package, you should create a file named `LPMfile` in root of
you git repository and put this content for a basic configuration:

```
NAME a-unique-name
DESCRIPTION this is a test package
```

(You will learn about other configuration options for `LPMfile` in next parts).

then, you need to publish your package on a github repo. also users can
install this package by using a local git directory:

```bash
$ lpm show gh:your-name/your-repo
$ lpm show f:/path/to/your-package
$ lpm show f:/path/to/your-package=<version>
$ lpm show f:/path/to/your-package=1.9
```

---

## Package isolation
LPM isolates packages for diffrent projects.
For example, if you have two projects, first requires `gh:foo/bar=1.0`
and second requires `gh:foo/bar=3.0`.

LPM installs all of project dependencies in a isolated directory named `loza_modules` directory
in the project directory.

A basic installation of package:

```bash
$ lpm install gh:foo/bar
$ lpm install gh:foo/bar=1.0
```

The package will be installed in `<project>/loza_modules/` directory.
For loading the packages, you should import `<project>/loza_modules/load.loza`s
in start point of your project:

```bash
import_once $__dir__ + '/loza_modules/load.loza'

import @foo
```

You should use the library standard names instead of `@foo`. The library(package) creators should tell this to the users.

You will learn more about package installation in the next parts.
