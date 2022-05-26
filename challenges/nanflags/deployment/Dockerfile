# Flag manager app: build the Vue app
FROM node:18-alpine3.14 AS managersitebuilder
WORKDIR /app
ADD ["flagmanager/package.json", "flagmanager/package-lock.json", "flagmanager/vue.config.js", "flagmanager/babel.config.js", "/app/"]
ADD ["flagmanager/src", "/app/src"]
RUN npm i && npm run build

# Rust backend: compile the binary webserver
FROM alpine:3.15 AS backendbuilder
WORKDIR /app
ADD ["backend/src", "/app/src"]
ADD ["backend/add_community_repo.sh", "backend/Cargo.toml", "backend/Cargo.lock", "backend/Rocket.toml", "/app/"]
RUN sh /app/add_community_repo.sh && \
    apk add --no-cache build-base rustup && \
    rustup-init -y --profile=minimal --default-toolchain nightly-2022-04-01 && \
    source $HOME/.cargo/env && \
    cargo build --release

# Static site: build the website
FROM node:18-alpine3.14 AS staticsitebuilder
WORKDIR /app
ADD ["website/package.json","website/package-lock.json", "/app/"]
ADD ["website/scripts", "/app/scripts"]
ADD ["website/src","/app/src"]
RUN npm i && npm run build

# Bringing it all together.
FROM alpine AS finaldocker
WORKDIR /app
COPY --from=backendbuilder /app/target/release/backend /app/server
COPY --from=staticsitebuilder /app/dist /app/static
COPY --from=managersitebuilder /app/dist /app/static/app
COPY "backend/Rocket.toml" /app/Rocket.toml
RUN ls -Rl /app
CMD ["/app/server"]