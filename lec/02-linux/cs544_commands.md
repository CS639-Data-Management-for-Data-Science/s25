# Linux Shell commands (updated for Spring 2026 with CDIS VM directions)

## SSH
- `ssh-keygen` (enables you to create SSH key)
- `cat ~/.ssh/id_rsa.pub` (copy public key)
- `ssh NETID@cs639-NETID.cs.wisc.edu`
- `vim ~/.ssh/authorized_keys` --- paste the public key and save it
- How to exit ssh session? exit / Ctrl + D

## History search: 
- up / down arrow
- `history`
- Ctrl+R

## Basic Linux commands

- `pwd` 
- `ls`
- `clear`

## Basic Linux commands

- `touch example.txt`
- `touch temp.txt` 
- `rm temp.txt` 
- `<vim / emacs / nano> example.txt` # feel free to use any editor, including UI-based editors like Visual Studio Code

## apt commands

- `apt install emacs-nox` --- won't work because you don't have root permission
- `sudo apt-get update`
- `sudo apt-get install emacs-nox`
- `sudo apt-get install -y emacs-nox`

## Download `spotify.zip`
- `wget https://ms.sites.cs.wisc.edu/cs544/data/ghcnd-stations.txt` # download a file using URL
- `unzip spotify.zip` --- won't work without installing the required package
- `mv <SOURCE> <DEST>` # move `ghcnd-stations.txt` to `stations.txt` using this command
- `cp <SOURCE> <DEST>` 

## Remote copy
- `scp <USERNAME>@<IP>:~/stations.txt .` --- won't work unless you are in your laptop's terminal session; that is you cannot use scp from inside your VM's SSH session
- `scp <SOURCE PATH on your laptop> <USERNAME>@<IP>:~/<DESTINATION PATH>`

## Basic Linux commands
- `cat spotify.csv` 
- `head spotify.csv`
- `tail spotify.csv`
- `head -n 20 spotify.csv`
- `tail -n 20 spotify.csv`
- `tail -f spotify.csv` # follow flag
- `Ctrl+C`: kill signal
- `mkdir data`
- `mkdir temp`
- `rmdir temp`
- `ls -lah` # Permissions USER | GROUP | OTHERS; rwx: READ WRITE EXECUTE
- `cd <DESTINATION>` # `cd ..`, `cd ~`, `cd data`, ...
- `su` # switch user
- `sudo su` # to get around root permission to switch into root
- `echo $PATH` # environment variable contents
  
## git commands

- `git clone <REPO URL>`
- `cd <REPO DIRECTORY>`
- `git pull` (execute this at the beginning of every lecture)

## Shebang line
- `#! <PATH TO EXECUTABLE>`
- `which <EXECUTABLE>` # finds path to the executable `which python3`, `which bash`, etc.,
