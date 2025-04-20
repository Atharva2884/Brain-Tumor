# Use official lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Flask will run on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
