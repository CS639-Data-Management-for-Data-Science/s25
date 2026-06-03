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
- `rm example.txt` 
- `<vim / emacs / nano> example.txt` # feel free to use any editor, including UI-based editors like Visual Studio Code
- `cat example.txt`
- 
## apt commands

- `apt install emacs-nox` --- won't work because you don't have root permission
- `sudo apt-get update`
- `sudo apt-get install emacs-nox`
- `sudo apt-get install -y emacs-nox`

## Download `spotify.zip`
- `wget https://ms.sites.cs.wisc.edu/cs574/data/spotify.zip` # download a file using URL
- `unzip spotify.zip` --- won't work without installing the required package
- `mv <SOURCE> <DEST>` # move `spotify_dataset.csv` to `spotify.csv` using this command
- `cp <SOURCE> <DEST>` 

## Remote copy
- `scp <USERNAME>@<IP>:~/spotify.csv .` --- won't work unless you are in your laptop's terminal session; that is you cannot use scp from inside your VM's SSH session
- `scp <SOURCE PATH on your laptop> <USERNAME>@<IP>:~/<DESTINATION PATH>`

## Basic Linux commands
- `cat spotify.csv` 
- `head spotify.csv`
- `head --help`
- `tail spotify.csv`
- `head -n 20 spotify.csv`
- `tail -n 20 spotify.csv`
- `tail -f spotify.csv` # follow flag
- `Ctrl+C`: kill signal

## Directory commands:
- `mkdir data`
- `man ls`
- `ls -lah`
- `mkdir temp`
- `rmdir temp`
- `mv *.txt data`
- `ls -l data/`
- `cd <DESTINATION>` # `cd ..`, `cd ~`, `cd data`, ... # Absolute and relative paths
- `ls -lah` # Permissions USER | GROUP | OTHERS; rwx: READ WRITE EXECUTE

## Permissions:
- `cd ..` # from home directory
- `touch secret.txt`
- `su` # switch user
- `sudo su` # to get around root permission to switch into root
- `vim secret.txt` # secret message
- `cat secret.txt`
- `ls -l`
- `Ctrl + D`
- `cat secret.txt`
- `sudo su`
- `chmod o-r secret.txt` #u/g/o +/- r/w/x permissions
- `Ctrl + D`
- `cat secret.txt`

## Programs
- `python3`
- `vim count.py`
  ```
  from pathlib import Path
  count = 0

  with open(Path("data") / "stations.txt") as f:
    for line in f:
      count += 1

  print(count)
  ```
- `python3 count.py`
- `count.py`
- `./count.py`
- `ls -l`
- `chmod a+x count.py`
- `ls -l`

## Shebang line
- `which <EXECUTABLE>` # finds path to the executable `which python3`, `which bash`, etc.,
- `#! <PATH TO EXECUTABLE>`
- `vim hello.py` # print("hello world!") along with shebang line
- `chmod a+x hello.py`
- `mv hello.py hello`
- `./hello`
- `hello`
- `echo $PATH` # environment variable contents
- `sudo mv hello /usr/local/bin`
    
## git commands

- `git clone <REPO URL>`
- `cd <REPO DIRECTORY>`
- `git pull` (execute this at the beginning of every lecture)

