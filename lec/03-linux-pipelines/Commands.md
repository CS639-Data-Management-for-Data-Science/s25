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
