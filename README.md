# Upload_Images_Api

Django rest framework application which allows users to upload their images. Depending on the tier, after updating an image, the user will get a link to their image,a link to a thumbnail and expiring link. Additional tiers can also be added by admin in the admin panel. 

Here is the DockerHub link: https://hub.docker.com/r/packerson/upload_images_api_web <br>
Here is the GitHub link: https://github.com/Packerson/Upload_Images_Api

## MAIN ENDPOINTS:
- admin/             
- api-auth/jwt/create/
  - POST
  - login site
  - {
    "email":"user email",
    "password":"password"
     }
- api-auth/profile/me/
  - GET
  - profil site
- api-auth/images/my
  - GET
  - user images
- api-auth/images/upload/   
  - POST 
  - upload images 
    - {
    "file": "image.file",
    "title": "image title",
    "alt": "image description",
      }
- api-auth/images/<int:id>
  - GET
  - image details
- api-auth/links/
  - POST
  - get expiring link
    - {
    "id":"image id",
    "time":"expiring time in s",
      }


### Tiers:
- BASIC: image resolution 200 px
- PREMIUM: image resolution 200 px, 400 px, original size
- ENTERPRISE: image resolution 200 px, 400 px, original size, and it's possible to create an expiring link to an image
- CUSTOM: image resolution original and custom, and it's possible to create an expiring link to an image

Allowed image formats: JPG, PNG.

### I divided the project into four apps:
- users:
  - Custom User model
- profiles 
  - Profile model with built-in tiers (Basic, Premium, Enterprise)
  - Custom model combined with Profile which allows admin to create additional tiers with custom image pixel size
- images
  - Image model with links available depending on the user's tier
- links
  - Link model combined with Image which allows the user to generete expiring links
  

## To do:
- more tests

Run this code, and check test coverage in html version
```
pytest -p no:warnings --cov=. --cov-report html
```

### How to set up the project:
- create virtual environment
- check env.example, create .env with values
- pip install -r requirenets.txt
- set up databases
- python3 manage.py runserver
- python3 manage.py createsuperuser

### My plan for this app:
- repository on GitHub
- make notes about app structure
- create virtual env
- start django project
- connect to Postgres
- custom user model
- logging
- djoser config
- other models with serializator
- generic Views
- Postman configuration
- custom admin-panel
- use resize to change pixel size of uploaded images
- docker config
- tests


#### What I use in the app:
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
