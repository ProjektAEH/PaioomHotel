FROM python:3.9-slim

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install dependencies
RUN pip install flask requests

# Copy the application code
COPY . /app
WORKDIR /app

# Expose the port
EXPOSE 5000

# Run the application
CMD ["flask", "run"]
