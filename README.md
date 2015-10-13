# SSH Tunnel #

### About ###
This program will run in the system tray allow for the mapping of local ports to remote machines via SSH.

The settings allow the user to configure the local port as well as the connection to the SSH machine (managed by the Paramiko library) and the remote host/port.

Paramiko is doing all the heavy lifting here - this is just a wrapper to make things easier to use.


### Why? ###
I found myself mapping ports on Windows using SSH on Cygwin quite a bit, but also had the need to map ports on machines that didn't have a Cygwin install. Rather than set up Cygwin on each machine a decided that a portable application with a settings file kept within the application folder would make things easier.

### Changelog ###

##### 1.0 #####
  - First release.