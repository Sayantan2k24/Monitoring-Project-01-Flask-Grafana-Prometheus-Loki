FROM python:3.10-slim

# Maintainer info
LABEL maintainer="sayantan2k21"

# Set working directory
WORKDIR /app

# Copy app util and requirements
COPY app.py requirements.txt util.py entrypoint.sh .  

# Install dependencies
RUN apt update -y && apt install -y curl &&  pip install --no-cache-dir -r requirements.txt && chmod +x entrypoint.sh

# Expose app port
EXPOSE 5000 

# Run the  Flask App
CMD ["./entrypoint.sh"]