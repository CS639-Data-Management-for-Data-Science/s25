# Linux demo commands

## SSH
- `ssh-keygen` (enables you to create SSH key)
- `cat ~/.ssh/id_rsa.pub` (copy public key)
- `ssh <USERNAME>@<External IP>`
- How to exit ssh session? exit / Ctrl + D

## History search: 
- up / down array
- Ctrl+R

## git commands

- `git clone <REPO URL>`
- `cd <REPO DIRECTORY>`
- `git pull` (execute this at the beginning of every lecture)

## apt commands

- `apt install emacs-nox` --- won't work because you don't have root permission
- `sudo apt-get update`
- `sudo apt-get install emacs-nox`

## Download `spotify.zip`
- `wget https://ms.sites.cs.wisc.edu/cs639/data/spotify.zip` # download a file using URL
- `unzip spotify.zip` --- won't work without installing the required package

## Basic Linux commands

- `pwd` 
- `ls` 
- `touch example.txt` 
- `<vim / emacs / nano> example.txt` # feel free to use any editor, including UI-based editors like Visual Studio Code
- `mv <SOURCE> <DEST>` # move `spotify_dataset.csv` to `spotify.csv` using this command
- `cp <SOURCE> <DEST>` 

## Remote copy
- `scp <USERNAME>@<IP>:~/spotify.csv .` --- won't work unless you are in your laptop's terminal session; that is you cannot use scp from inside your VM's SSH session
- `scp <SOURCE PATH on your laptop> <USERNAME>@<IP>:~/<DESTINATION PATH>`

## Basic Linux commands
- `cat spotify.csv` 
- `head spotify.csv`
- `tail spotify.csv`
- `head -n 20 spotify.csv`
- `tail -f spotify.csv` # follow flag
- `Ctrl+C`: kill signal
- `mkdir data`
- `ls -lah` # Permissions USER | GROUP | OTHERS; rwx: READ WRITE EXECUTE
- `cd <DESTINATION>` # `cd ..`, `cd ~`, `cd data`, ...
- `su` # switch user
- `sudo su` # to get around root permission to switch into root
- `chmod <WHO><+/-><WHAT>`
- `chmod o-r secret.txt` # remove read permission for other users
- `echo $PATH` # environment variable contents

## Shebang line
- `#! <PATH TO EXECUTABLE>`
- `which <EXECUTABLE>` # finds path to the executable `which python3`, `which bash`, etc.,
