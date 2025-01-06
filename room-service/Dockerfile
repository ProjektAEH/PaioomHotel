FROM python:3.8

# Set the working directory
WORKDIR /app

# Install dependencies directly
RUN pip install flask requests

# Copy the application files
COPY . .

# Command to run the application
CMD ["python", "app.py"]
