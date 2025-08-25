# syntax=docker/dockerfile:1

# Base image
FROM node:18-alpine

# Set work directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy project
COPY . .

# Expose port
EXPOSE 5173

# Start command
CMD ["npm", "run", "dev"]
