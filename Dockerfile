FROM jenkins/jenkins:lts

USER root
# Install Python and tools
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv curl unzip

# Install Chrome browser
RUN apt-get update && \
    apt-get install -y wget gnupg && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Install ChromeDriver matching Chrome version
RUN apt-get update && apt-get install -y curl unzip && \
    CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d. -f1) && \
    wget -q -O /tmp/chromedriver_linux64.zip "https://storage.googleapis.com/chrome-for-testing-public/$(curl -s https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_$CHROME_VERSION)/linux64/chromedriver-linux64.zip" && \
    unzip /tmp/chromedriver_linux64.zip -d /tmp/ && \
    mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver*

# Clean up
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER jenkins