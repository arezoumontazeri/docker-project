
# Dockerized Squid Proxy

This repository contains Docker Compose files and configuration for deploying Squid, an advanced caching proxy for the web, using Docker. Squid reduces bandwidth and improves response times by caching and reusing frequently-requested web pages.

## Prerequisites

To run this Dockerized Squid proxy, you will need:
- Docker installed on your machine. [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose installed on your machine. [Install Docker Compose](https://docs.docker.com/compose/install/)

## Structure

Here is what you will find in this repository:

- `docker-compose.yml`: Docker Compose file to start the Squid proxy container.
- `squid.conf`: Configuration file for Squid to customize its behavior.

## Configuration

### Docker Compose

The `docker-compose.yml` file describes the services that make your application. For Squid, it looks something like this:

```yaml
version: '3'
services:
  squid:
    image: sameersbn/squid:3.5.27-2
    ports:
      - "3128:3128"
    volumes:
      - ./squid.conf:/etc/squid/squid.conf
    restart: unless-stopped
