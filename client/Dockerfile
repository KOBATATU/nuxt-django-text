FROM node:12.13-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk update && \
    apk upgrade && \
    apk add git
RUN npm install -g npm && \
    npm install -g core-js@latest && \
    npm install -g @vue/cli && \
    npm install -g @vue/cli-init && \
    npm install -g nuxt create-nuxt-app

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
ENV HOST 0.0.0.0
EXPOSE 3000

# docker exec -it client sh
# npx create-nuxt-app ファイル名
