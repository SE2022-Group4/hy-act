FROM python:3.8

# Install Nginx
RUN apt update
RUN apt install nginx -y

# Set Nginx related configuration files
COPY nginx.conf /etc/nginx.conf.d
RUN rm /etc/nginx/sites-available/default
COPY project.conf /etc/nginx/sites-available/default

# Switch working directory to app directory
WORKDIR /app

# Copy python requirements.txt first
COPY requirements.txt requirements.txt

# Install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy rest of the project files
COPY . .

# Set file permission of docker entrypoint script file
RUN chmod +x docker-entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["./docker-entrypoint.sh"]