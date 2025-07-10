FROM python:3.10-slim

# Maintainer info
LABEL maintainer="sayantan2k21"

# Set working directory
WORKDIR /app

# Copy app util and requirements
COPY app.py requirements.txt util.py .  

# Install dependencies
RUN apt update -y && apt install -y curl &&  pip install --no-cache-dir -r requirements.txt

# download the wait script
RUN curl -o wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && chmod +x wait-for-it.sh

# Expose app port
EXPOSE 5000

# Run the  Flask App
CMD ["python", "app.py"]