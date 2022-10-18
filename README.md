# docker-hello-world

This is a simple Python script that can be used to test the NEAR Hack-a-thon bounty system. It's meant to simulate all possible outcomes of a bounty execution for testing purposes

You can run this script locally using the following command:
```bash
#FORCE_RESULT forces an execution outcome. See "Forcing outcomes" for details
FORCE_RESULT= #Empty or one of EXPECTED_ERROR, UNEXPECTED_ERROR, MALFORMED_RESULT, NO_RESULT, TIMEOUT
python run $FORCE_RESULT
```

This is meant to be run in a Docker container. To do so, you can run the following at the root directory
```bash
FORCE_RESULT=
docker image build -t test . && \
docker run -rm test $FORCE_RESULT
#docker image rm test
```

