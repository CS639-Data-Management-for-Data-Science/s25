# Google Cloud (GCP) Setup

## Part 1: Virtual Machine Setup

We'll use Google's Cloud (GCP) for our virtual machines.  They've
generously given each 639 student $100 in credits, which should last
the whole semester if you remember to __suspend__ (don't delete it!) your VM when not using it.

You can obtain the credits [here](https://canvas.wisc.edu/courses/448585/pages/google-credits).

Setup a virtual machine that you'll use for the first few projects
(we'll eventually delete it and create a more powerful one for some of
the later projects).

You should have some experience in creating VMs in a prior course (320
or 400), so these directions will be brief:

* Go to https://console.cloud.google.com/compute/instances to view and launch VMs.
* Click "Create a VM", and use the following settings.
  - Machine type: `e2-small`
  - Boot disk: `Ubuntu 22.04 LTS` (select x86/64 version, not Arm64) with disk size `25GB`.
  - You can decide things like what geographic region to create it in (I picked Iowa since it's nearby).
* Once you select these settings, the monthly estimate should be about $14.73 for the VM (if it’s not, you probably selected something wrong, and might run out of free credits before the end of the semester).
* Click "Create".
* You'll need to setup an SSH key so you can connect from your laptop--the browser-based SSH client won't work for what we need to do in this class.
  - [Install](https://cloud.google.com/sdk/docs/install) and initialize gcloud CLI. (I personally used conda: ``conda install google-cloud-sdk -c conda-forge``).
  - Follow instructions in "Connect to VMs" section to automatically generate an SSH key and connect to your VM: https://cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms.
  - Your SSH key should now be visible at https://console.cloud.google.com/compute/metadata?tab=sshkeys.

When you're done, check that you have the correct Operating System and
CPU with `cat /etc/os-release` and `lscpu`.  Check the saved outputs by using the appropriate linux command to display the contents of the files:

``` 
cat /etc/os-release > os.txt
lscpu > cpu.txt
```

## Part 2: Docker Install

Carefully follow the directions here to install Docker 24.0.5 and Compose 2.20.2 on your virtual machine: https://docs.docker.com/engine/install/ubuntu/

Notes:
* There are several different approaches described under "Installation methods".  Use the directions under "Install using the apt repository".  Make sure you don't keep going after you reach "Install from a package"
* The first step under "Install Docker Engine" has two options: "Latest" or "Specific version".  Choose **"Specific version"**
* Here are the versions we will be using and the command to install them:
  * docker-ce: `5:24.0.5-1~ubuntu.22.04~jammy`
  * docker-ce-cli: `5:24.0.5-1~ubuntu.22.04~jammy`
  * docker-compose-plugin: `2.20.2-1~ubuntu.22.04~jammy`
  
  ```
  sudo apt-get install docker-ce=5:24.0.5-1~ubuntu.22.04~jammy docker-ce-cli=5:24.0.5-1~ubuntu.22.04~jammy containerd.io docker-buildx-plugin docker-compose-plugin=2.20.2-1~ubuntu.22.04~jammy
  ```

To avoid needing to run every Docker command with root, there are a
few more steps you can do here:
https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user
(don't go beyond the "Manage Docker as a non-root user" section).

Create some more files so we can check your Docker install:

```
docker version > docker.txt
docker compose version > compose.txt
```
