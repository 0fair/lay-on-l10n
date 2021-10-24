FROM node:16 as build-stage

WORKDIR /app

COPY package*.json /app/
RUN npm install

COPY ./ /app/
RUN npm run build

FROM nginx:1.20

COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /app/build/ /var/www

