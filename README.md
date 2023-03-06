# Upload_Images_Api

Django rest framework appliaction allows users to upload their images. Depepend of user tier, also tier can be added by admin in admin panel. 
After upadted image user will get link to theris image and link to thumbnail depened of tier. 

### I divied projcet to three apps:
- users:
  - custom user model
- profiles 
  - model Profile with buil in tiers (Basic, Premium, Enterprise)
  - model Custom connecting to Profiles, allow admin for creating another tiers with custom pixel size
- images
  - model Image, depend of user's tier by ovewritng save create images and save them
- links
  - model link connected to Image, allow user to generete expiration link, and check if link expired

## To do:
- generating an expiring link to the image (the link expires after a given number of seconds (the user can specify any number between 300 and 30000)).

### How to set up the project:
- create viratual enviorement
- pip install -r requirenets.txt
- set up databases
- python3 manage.py runserver
- python3 manage.py createsuperuser

### My plan for this app:
- repositorium on GitHUb
- made notes with app structure
- create virtual env
- tart django project\
- connect to Postres
- custom user model
- logging
- djoser config
- other models with serializator
- generic Views
- Postman configuration
- custom admin-panel
- use resize to change pixel on uploaded images
- docker config
- celery
- redis 
- tests



#### What I use in app:
- GitHub
- djoser
- django
- drf
- Pillow
- postman
- docker
- postgres

##### Docker instruction:
```
  - docker ps – container list 
  - docker exec -it {id} bash  - enter to container terminal
  - docker-compose build {nazwa kontenera}  - rebuild container
  - docker-compose up – start 
```
