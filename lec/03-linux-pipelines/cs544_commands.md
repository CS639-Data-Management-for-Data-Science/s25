# Linux Pipelines and Redirections

## Pipelines
- `wc` # word count
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

## make_pop.sh
```
#! /usr/bin/bash

cat data/spotify.csv | grep "^dance pop"` > pop.csv
cat data/spotify.csv | grep "^dance pop"` >> pop.csv
```

## count.py

```
import time
...
  time.sleep(1)
```

- `ps`
- `ps a` # other users not just me
- `ps ax` # not associated with the terminal
- `ps ax | grep python3`
- `kill <PID>` # Restart the program
- `pkill python3`
- `htop`
- `time `
- `df `
- `df .`
- `df . -h`
- `du`
- `du -sh`
- `du -sh .`
- `ss -tpln` # tcp # process
