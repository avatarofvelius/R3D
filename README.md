# R3D ( Offline Repository )
a basic flask backend, with pico.css and alpine.js


## Purpose
Learning and implementing Flask with Celery automation, with an easily deployed light frontend.

1. simple flask backend with minimal admin, redis ( or sqlite db ), and celery.
2. pico.css for nice looking css without frameworks. ( tailwind/bootstrap )
3. alpine.js for data injection and modern jquery features.


## Packages
- Flask
https://flask.palletsprojects.com/en/2.3.x/quickstart/

- Celery
https://flask.palletsprojects.com/en/2.3.x/patterns/celery/

- Redis ( for celery service workers? not implemented )
https://redis.io/docs/getting-started/

- Pico.css
https://picocss.com/docs/

- Alpine.js ( not implemented )
https://alpinejs.dev/start-here

- Petite-Vue ( alternative to Alpine.js )
https://github.com/vuejs/petite-vue


---


## Experimental & Situational Processes

### Redis
https://redis.io/docs/getting-started/installation/install-redis-on-windows/
- redis not easily supported on windows.
- do not want to install linux through WSL. 

- install redis on raspberry pi. use for celery workers amd nosql data objects.
1. use celery to automate background workers to send update data to redis. 
2. serve data as json objects via a Flask API.  


