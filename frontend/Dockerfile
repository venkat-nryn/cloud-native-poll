# Start with an official Nginx image. Nginx is a lightweight web server.
FROM nginx:1.21-alpine

# Remove the default Nginx welcome page.
RUN rm /usr/share/nginx/html/index.html

# Copy our single index.html file into the directory Nginx serves files from.
COPY index.html /usr/share/nginx/html