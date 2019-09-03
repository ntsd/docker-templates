FROM node:8.11.4

ENV YARN_CACHE_FOLDER /yarn

WORKDIR /app/website

EXPOSE 3000 35729
COPY ./docs /app/docs
COPY ./website /app/website

# Add entrypoint script to handle yarn cache
RUN mkdir -p $YARN_CACHE_FOLDER
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

ADD . .

CMD ["yarn", "start", "--port", "3000"]
