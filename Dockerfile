FROM debian:bullseye-slim

# Install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3=3.9.2-3 python3-pip=20.3.4-4+deb11u1 xauth=1:1.1-1 x11-apps=7.7+8 fluxbox=1.3.5-2+b2 python3-tk=3.9.2-1 chromium=120.0.6099.224-1~deb11u1 && \
    apt-get remove -y chromium && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
#RUN apt-get remove -y chromium
# Install python packages

# Set the working directory inside the container
WORKDIR /browserbruter

#COPY ./ /browserbruter/
COPY BrowserBruter.py ReportExplorer.py requirements.txt /browserbruter/
COPY res/ /browserbruter/res/
COPY modules/ /browserbruter/modules/
RUN pip3 install -r /browserbruter/requirements.txt

#RUN python3 -m pip install selenium==4.17.2 selenium-wire==5.1.0 webdriver_manager==4.0.1 ttkthemes==3.2.2 pytimedinput==2.0.1 colorama==0.4.6 beautifulsoup4==4.12.3 undetected-chromedriver==3.5.5 requests==2.31.0 blinker<1.8.0 pandas tqdm brotlipy zstandard 

# Set the DISPLAY environment variable 
ENV DISPLAY=:0

#COPY BrowserBruter.py ReportExplorer.py /browserbruter/
#COPY ReportExplorer.py /browserbruter/
#COPY res/ /browserbruter/res/
#COPY modules/ /browserbruter/modules/

ENTRYPOINT ["/bin/bash"]
