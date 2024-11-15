# Express.js Dockerfile
FROM node:16-slim

WORKDIR /app

COPY ./package.json .
RUN npm install

COPY ./ /app

EXPOSE 8003

CMD ["node", "index.js"]
