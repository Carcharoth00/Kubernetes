FROM ghcr.io/cirruslabs/flutter:stable AS build

WORKDIR /app

RUN flutter create .

Run flutter build web --release

FROM nginx:alpine

COPY --from=build /app/build/web /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
