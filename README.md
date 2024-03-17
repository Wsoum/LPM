<div align="center">
  <img width="200" src="logo.svg" alt="LPM">
</div>

# LPM package manager
LPM is a package manager for [Loza programming language](https://github.com/Wsoum/Loza).

With this package manager, you can manage libraries and for Loza projects and install/remove/update... them.

This project is licensed under the [GPL-v3](LICENSE).

## Get started

### Installation
To install LPM on your system, run:

```bash
$ echo "deb [trusted=yes lang=none] http://os.wsoum.eu.org/packages ./" | sudo tee -a /etc/apt/sources.list.d/wsoumos_sources.list

$ sudo apt install lpm
```

Now you can run LPM:

```bash
$ lpm ...
```


OR
In (linux Only)

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
$ lpm install gh:wsoum/lpm -g
```


To run the LPM without install, enter this command:

```bash
$ loza src/lpm/lpm.loza
# OR
$ ./src/lpm/lpm.loza
```


## Documentation
Read the full documentation [here](doc).
