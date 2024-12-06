xhost +local:root
docker run -it --rm \
    -e DISPLAY=$DISPLAY \
    -e TERM=xterm \
    -e PYTHONUNBUFFERED=1 \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v $(pwd)/BrowserBruter_Reports:/browserbruter/BrowserBruter_Reports \
    -v $(pwd)/payloads:/browserbruter/payloads browser-bruter
