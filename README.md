<div align="center">
  <img width="200" src="logo.svg" alt="LPM">
</div>

###### Logo by [Mehan](https://github.com/mehanalavimajd)

# LPM package manager
LPM is a package manager for [Loza programming language](https://github.com/wsoum/loza).

With this package manager, you can manage libraries and for Loza projects and install/remove/update... them.

This project is licensed under the [GPL-v3](LICENSE).

## Get started
To run the LPM, enter this command:

```bash
$ loza src/lpm/lpm.loza
# OR
$ ./src/lpm/lpm.loza
```

### Installation
To install LPM on your system, run:

```bash
$ loza src/lpm/lpm.loza install f:. --global
```

Now you can run LPM:

```bash
$ loza @lpm ...
# OR on UNIX systems
$ lpm ...
```

For updating the LPM, run:

```bash
$ lpm install gh:lozalang/lpm -g
```

## Documentation
Read the full documentation [here](doc).
