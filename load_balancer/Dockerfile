# Use the official NGINX image from the Docker Hub
FROM nginx:stable-alpine

# Remove the default NGINX configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy the custom NGINX configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
