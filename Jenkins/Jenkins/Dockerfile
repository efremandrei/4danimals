FROM jenkins/jenkins:lts

# Switch to root user to install additional software
USER root

# Install necessary packages
RUN apt-get update && \
    apt-get install -y curl unzip python3 python3-pip awscli && \
    rm -rf /var/lib/apt/lists/*

# Install Terraform
RUN curl -O https://releases.hashicorp.com/terraform/1.8.5/terraform_1.8.5_linux_amd64.zip && \
    unzip terraform_1.8.5_linux_amd64.zip && \
    mv terraform /usr/local/bin/ && \
    rm terraform_1.8.5_linux_amd64.zip

# Install Python requests module
RUN pip3 install requests

# Switch back to the jenkins user
USER jenkins

# Expose the default Jenkins port
EXPOSE 8080
EXPOSE 50000

# Set the default command to run Jenkins
CMD ["jenkins.sh"]
