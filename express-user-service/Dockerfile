# Express.js Dockerfile
FROM node:16-slim

WORKDIR /app

COPY express-user-service/package.json .
RUN npm install

COPY express-user-service /app

EXPOSE 3001

CMD ["node", "index.js"]
