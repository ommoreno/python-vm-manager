# Python VM Manager

This repo contains a Python 3 class which automates virtual machine provisioning in the major clouds (AWS, Google, or Azure). Answers and assumptions are discussed in the [Discussion](##Discusion) section below.

## Prerequisites

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [paramiko](https://www.paramiko.org/).

```bash
pip install paramiko
```

## Usage

The Python program can be run to test the SSH functionality of the class. Edit the `host`, `port`, `user`, and `cmd` variables at the bottom of `gcp_manager.py`. 

```bash
python gcp_manager.py
```

## Discussion

This section contains answers to questions posed in the assignment and provides explanations to some implementation details.

### Part 1

Assumptions made for the class and methods can be found in the docstrings of `gcp_manager.py`. Besides the methods outlined in the Python class, I would probably add a `suspend_vm()`, `resume_vm()`, and `delete_vm()` method to complete the basic functionalities of VM management. 

### Part 2

To extend the class to handle additional clouds I would first need to understand the similarities and differences of those clouds. Since we desire a standard set of functions to manage VMs, I lean towards abstracting the VM manager and making each cloud its own Python module. Each cloud would be a class that extends the base "`VMManager`" class. If more clouds need to be supported or the user desires decoupling from the main program, a factory design pattern could be used. 

### Part 3

I chose to utilize the Paramiko library to implement SSH connections to provisioned VMs. While `subprocess.Popen()` doesn't require additional libraries, I felt that Paramiko offers more control and flexibility. Some additional logic is needed for dealing with SSH keys that's not implemented in this function. An interactive shell is not implemented in this function, but can be added through existing methods in Paramiko. Since the test for this function is fairly simple, I opted to place the driver code at the bottom of `gcp_manager.py`.

