# thegreatestdonuts-site

## Concepts

A flask webapp that...

* Randomly select a new donut image for every day on the front page.
* Anyone can vote on a donut to be the best donut. Hove to make voting a manual process somehow?
* A donut image upload webform thats protected behind an login and auth.
* 

## Cool extras

* AI driven scanning of donut images to make sure they are donuts.
* If there are a lot of donuts, that's potentially a lot of storage and bandwith.
  *  Look into cloud edge caching with cloudflare and backblaze.
  *  Tools for cropping / downsizing images inside the app

## Design

Containerize the app, using 4 containers

* Flask webapp and uWSGI app server.
* Nginx webserver. https://www.nginx.com/
* Redis cache. https://redis.io/
* MongoDB database. https://www.mongodb.com/

Plus: 

Lets encrypt automatic SSL certs
