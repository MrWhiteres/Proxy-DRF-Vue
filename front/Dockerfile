FROM node:20.4.0 as dev

RUN npm i -g pnpm

WORKDIR /front
COPY package.json pnpm-lock.yaml ./
RUN pnpm install

FROM dev as build
WORKDIR /front
COPY . .
COPY --from=dev /front/node_modules ./node_modules
RUN pnpm build

FROM nginx:1.25 as prod

COPY --from=build /front/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]