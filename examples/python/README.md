# Fuzzing Python in OneFuzz

OneFuzz can orchastrate fuzzing of [Python](https://www.python.org) using
[pythonfuzz](https://pypi.org/project/pythonfuzz/).

Included in this directory is a simple example to demonstrate golang based
fuzzing.  For more examples, check out the collection of [pythonfuzz
examples](https://gitlab.com/gitlab-org/security-products/analyzers/fuzzers/pythonfuzz/-/tree/master/examples).

## Example command

```bash
make
onefuzz template libfuzzer basic $PROJECT_NAME $TARGET_NAME $BUILD_NUMBER $POOL_NAME --target_exe ./fuzz.exe --inputs ./seeds
```
