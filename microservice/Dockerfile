FROM python:3.10-slim

# Maintainer info
LABEL maintainer="sayantan2k21"

# Set working directory
WORKDIR /app

# Copy app util and requirements
COPY app.py requirements.txt util.py .  

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose app port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
