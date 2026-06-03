# Linux Pipelines and Redirections

## Pipelines
- `wc` # word count # type "hello world\n"
- `cat data/spotify.csv | wc`
- `cat data/spotify.csv | grep "pop"`
- `cat data/spotify.csv | grep "pop" | grep -v "uk pop"`
- `cat data/spotify.csv | grep "pop" | head`
- `find .`
- `find . | grep ".csv$"` # `$` indicates end character match # `^` indicates beginning character match, but can't be used in this context due to path convention
- `find . -name "v1*"`

- `cat data/spotify.csv | grep "^ pop"` > pop.csv
- `cat data/spotify.csv | grep "^dance pop"` > pop.csv
- `cat data/spotify.csv | grep "^dance pop"` >> pop.csv
- `head pop.csv`
- `tail pop.csv`

## make_pop.sh
```
#! /usr/bin/bash

cat data/spotify.csv | grep "^dance pop"` > pop.csv
cat data/spotify.csv | grep "^dance pop"` >> pop.csv
```

## Processes

count.py

```
import time
...
  time.sleep(1)
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
- `time `
- `df `
- `df .`
- `df . -h`
- `du`
- `du -sh`
- `du -sh .`
- `ss -tpln` # tcp # process
