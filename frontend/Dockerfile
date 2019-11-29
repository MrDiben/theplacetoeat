FROM node:latest

ENV NODE_ENV development

# make the 'app' folder the current working directory
WORKDIR /app/

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

RUN npm cache verify

# install project dependencies
RUN npm install

EXPOSE 8080

CMD ["npm", "run", "serve"]
