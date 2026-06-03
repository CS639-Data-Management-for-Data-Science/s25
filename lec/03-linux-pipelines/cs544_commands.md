# Linux Pipelines and Redirections

## Pipelines
- `wc` # word count # type "hello world\n"
- `cat data/stations.txt | wc`
- `cat data/stations.txt | grep "MADISON"`
- `cat data/stations.txt | grep "madison"`
- `cat data/stations.txt | grep -i "madison"`
- `cat data/stations.txt | grep -i "madison"`
- `cat data/stations.txt | grep -i "madison"`| grep -v "MADISONVILLE"`
- `cat data/stations.txt | grep -i "madison"`| grep -v "MADISONVILLE"` | head
- `find .`
- `find . | grep ".txt$"` # `$` indicates end character match # `^` indicates beginning character match, but can't be used in this context due to path convention
- `find . -name "v1*"`

- `cat data/stations.txt | grep "WI"`
- `cat data/stations.txt | grep " WI "` > midwest.txt
- `cat data/stations.txt | grep " IL "` >> midwest.txt # append
- `head midwest.txt`
- `tail midwest.txt`

## make_midwest.sh
```
#! /usr/bin/bash

cat data/stations.txt | grep " WI " > midwest.txt
cat data/stations.txt | grep " IL " >> midwest.txt
```
- `chmod a+x make_midwest.sh`
- `rm midwest.txt`
- `./make_midwest.sh`

## Processes

count.py

```
import time
...
  time.sleep(1) # 1 second
```

- `python3 count.py &`
- `ps`
- `ps a` # other users not just me
- `ps ax` # not associated with the terminal
- `ps ax | grep python3`
- `kill <PID>` # Restart the program
- `kill -9 <PID>` # immediately kills without a graceful exit
- `python3 count.py &`
- `pkill python3`

## Resource utilization commands
- `htop`
- `time find` # real: wall clock time # user (our program) & sys: CPU time userspace and system time 
- `df `
- `df .`
- `df . -h`
- `du`
- `du -sh`
- `du -sh .`
- `du -sh ./*`
- `ss -tpln` # tcp # process
- `sudo ss -tpln` # tcp # process
