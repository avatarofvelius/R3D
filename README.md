# R3D ( Offline Repository )
a flask backend, with a basic pico.css and alpine.js frontend.


## Purpose
Learning and implementing Flask with Celery automation, with an easily deployed light frontend.

1. simple flask backend with minimal admin, redis, and celery.
2. pico.css for nice looking css without frameworks. ( tailwind/bootstrap )
3. alpine.js for data injection and modern jquery features.

## Process
- initial version without redis, flask api, or backend automation.
1. celery service workers manage local data, ending up as json objects for frontend.
2. flask serves data locally as an api, through redis, or pushed physically to host.
3. alpine or other alternative to inject json to frontend. 


## Experimental & Situational Processes


### Docker

- install docker container on raspberry pi. use for celery workers amd nosql data objects.
1. use celery to automate background workers to send update data to docker image. 
2. serve data as json objects via a Flask API.  


## Packages
- Flask
https://flask.palletsprojects.com/en/2.3.x/quickstart/

- Celery ( not implemented )
https://flask.palletsprojects.com/en/2.3.x/patterns/celery/

- Pico.css
https://picocss.com/docs/

- Alpine.js ( not implemented )
https://alpinejs.dev/start-here

- Petite-Vue ( alternative to Alpine.js )
https://github.com/vuejs/petite-vue


