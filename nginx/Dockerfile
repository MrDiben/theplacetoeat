# build stage
FROM node:latest as build-stage
RUN mkdir /app
WORKDIR /app/
COPY frontend/package.json /app/
COPY frontend/package-lock.json /app/
RUN npm cache verify
RUN npm install
COPY frontend /app/
RUN npm run build

# production stage
FROM linuxserver/letsencrypt
COPY backend/static /usr/src/app/static/
COPY --from=build-stage /app/dist /dist/
