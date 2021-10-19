"""Python program to automate virtual machine provisioning in GCP.

This program contains stubs for a VM provisioner for GCP. The class and all but
one function are empty. The ssh_vm() function uses Paramiko to ssh to a given
VM. The driver program at the bottom serves as an example of its usage. Edit the
host, port, user, and cmd variables to fit the user's needs.

    Usage example:

    python3 gcp_manager.py
"""

# googleapiclient.discovery could be used for provisioning GCP instances
import paramiko # Used for SSH connections to VMs


class GCPManager:
    """Skeleton of a GCP instance provisioner.

    Functions included in this class are meant to automate managing VMs in GCP.
    Since all resources in GCP must have unique names, passing in the VMs' name
    suffices for most functions.
    
    Attributes:
        credentials: GCP-specific metadata needed to manage VMs in the cloud
    """
    def __init__(self, credentials):
        """Inits GCP manager with user-defined credentials"""
        pass

    def create_vm(self, vm_name, region, type, image, size):
        """Creates a VM with the given specifications

        This assumes the user knows the GCP namings of regions, machine types,
        and images. Errors can be raised in implementation to help user debug
        provisioning issues.

        Args:
            vm_name: A string representing the VM name. Must start with a
                lower-case letter.
            region: A string representing the region to provision the VM in.
            type: A string representing the machine type, i.e. 'n1-standard'
            image: A string representing the OS image
            size: A string representing the boot disk size in bytes. Can use the
                suffix 'M/G/T'

        Returns:
            An machine ID which uniquely identifies the VM in GCP. While the VM
            name should be enough, using the machine ID adds a secondary method
            of searching for the instance and is more specific. Returns None if
            the VM could not be created.
        """
        pass

    def install_mariadb(self, vm_name, password):
        """Installs MariaDB on an existing deployed VM.

        The assumption here is that the only required variable by MariaDB is a
        strong password for the root user.

        Args:
            vm_name: A string representing the VM name. Must start with a
                lower-case letter.
            password: A string representing the password to be set for the root
                superuser account.

        Returns:
            A boolean indicating whether MariaDB was installed successfully or
            not.
        """
        pass

    def start_vm(self, vm_name):
        """Starts an existing VM.
        
        Args:
            vm_name: A string representing the VM name. Must start with a
                lower-case letter.
        """
        pass

    def stop_vm(self, vm_name):
        """Stops an existing VM.
        
        Args:
            vm_name: A string representing the VM name. Must start with a
                lower-case letter.
        """
        pass

    def list_vms(self):
        """Prints out a list of deployed VMs to the console."""
        pass

    def get_external_ip(self, vm_name):
        """Returns the external IP address of the given VM.

        Args:
            vm_name: A string representing the VM name. Must start with a
                lower-case letter.
        """
        pass

    def ssh_vm(self, vm_name, port, user, cmd):
        """Sends a command to a given VM via SSH.

        If the command exits without error than the stdout will be printed,
        otherwise the stderr will be printed. Both are returned by the function
        for ease of use by the user.
        Args:
            vm_name: A string representing the VM name. Must start with a
                lower-case letter.
            port: The SSH port number to use, usually an integer like 22.
            user: A string representing the user of the VM.
            cmd: A string representing the command to be sent to the VM.

        Returns:
            A tuple that contains the stdout and stderr of the command from the
            VM. 
        """
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Here I would call get_external_ip(vm_name) to connect to the VM
        
        ssh.connect(vm_name, username=user, port=port)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        exit_status = stdout.channel.recv_exit_status()
        stdout = stdout.read().decode('utf-8')
        stderr = stderr.read().decode('utf-8')
        if exit_status == 0:
            print(stdout)
        else:
            print(stderr)
        ssh.close()
        return stdout, stderr


if __name__ == '__main__':
    # Edit the below variables for desired purpose
    host = 'localhost'
    port = 22
    user = 'omm'
    cmd = 'ls -al'

    my_gcp = GCPManager(None)
    stdout, stderr = my_gcp.ssh_vm(host, port, user, cmd)
