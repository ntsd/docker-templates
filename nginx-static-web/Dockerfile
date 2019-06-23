FROM nginx:1.17.0-alpine

COPY /build /usr/share/nginx/html

COPY ./nginx.conf /etc/nginx

COPY ./default.conf /etc/nginx/conf.d