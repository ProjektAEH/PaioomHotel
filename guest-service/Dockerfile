FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies directly
RUN pip install flask requests

# Copy the application files
COPY . .

# Ustawienie portu, na którym serwis będzie nasłuchiwać
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
