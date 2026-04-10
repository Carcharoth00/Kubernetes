FROM ghcr.io/cirruslabs/flutter:stable AS build

WORKDIR /app

RUN flutter create .

COPY lib/main.dart lib/main.dart

RUN flutter pub add http

RUN flutter build web --release

FROM nginx:alpine

COPY --from=build /app/build/web /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
