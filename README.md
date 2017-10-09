To generate the rendering:

    docker build -t rndr .
    docker run -v $PWD/tmp:/output rndr
