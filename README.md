# thegreatestdonuts-site

## Concepts

A flask webapp that...

* Randomly select a new donut image for every day on the front page.
* Anyone can vote on a donut to be the best donut. Hove to make voting a manual process somehow?
* A donut image upload webform thats protected behind an login and auth.

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

## Contribute

 * Install python 3.7 or newer
 * pull the repo (`git clone ...`)
 * Enter the repo `cd thegreatestdonuts-site`
 * configure a virtual env (`python3 -m venv .venv`) and activate (`source .venv/bin/activate`)
 * Install the dependancies. `python3 -m pip install -r requirements.txt`
 * Run the development server.
    * `export FLASK_APP=donutr` 
    * `export FLASK_ENV=development`
    * `flask run`

### Develop with docker
