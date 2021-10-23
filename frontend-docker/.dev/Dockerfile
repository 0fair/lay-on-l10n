FROM node:16 as build-stage

WORKDIR /app

COPY package*.json /app/
RUN npm install

CMD ["npm", "start"]