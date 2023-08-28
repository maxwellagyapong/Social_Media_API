# Social Media API Project
Social Media Application

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Commands](#commands)
* [App endpoints](#app-endpoints)
* [Link to public repo](#public-repo)
* [API Documentation](#api-documentation)


## General info
Simple django application with the following as main features:

* User Authentication and Profiles
* Content Creation and Interaction
* Following and Followers
* Groups and Communities
* Commenting and Replies
* Notifications
* Search and Discovery
* Privacy and Security
* API Documentation and Testing


## Technologies
* Python
* Django
* Django Rest Framework
* Docker

### Setup
## Installation on Linux and Mac OS
* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo
* [Follow the guide here](https://docs.docker.com/engine/install/) on how to install and run docker
* To run application with docker
```
docker-compose up --build
```
  
* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at http://0.0.0.0:8000).
* Open the address in the browser

## Commands
Open docker bash with 
```
docker ps
docker exec -it <CONTAINER_NAME> bash
```
In our case, default container name is "socialmedia_app"
* To run migrations
```
python manage.py makemigrations
python manage.py migrate

```

## App Endpoints
* /api/post/ - create a post
* /api/home/ - return the list of all posts
* /api/home/{post_id}/ - return a single post
* /api/home/{post_id}/ - update a post
* /api/home/{post_id}/ - delete a post
* /api/home/{post_id}/like/ - like or unlike post
* /api/home/{post_id}/likers/ - returns all likers of a post
* /api/home/{post_id}/comment/ - comment on a post
* /api/home/{post_id}/comment/ - return a list all comments on a post 
* /api/home/comments/{comment_id}/reply/ - reply to a comment
* /api/home/comments/{comment_id}/reply/ - return a list of all replies on a comment
* /api/home/{post_id}/share/ - share a post
* /api/home/shared-posts/ - returns a list all shared posts
* /api/home/users/{user_id}/notifications/ - returns a list of all user notifications
* /api/home/create-group/ - create a group
* /api/home/groups/ - returns a list of all groups
* /api/home/groups/{group_id}/ - returns a single group
* /api/home/groups/{group_id}/ - edit group
* /api/home/groups/{group_id}/ - delete group
* /api/home/groups/{group_id}/join/ - join or leave a group
* /api/home/users/ - returns a list of all registered users
* /api/home/users/{user_id}/ - returns a single user
* /api/account/{user_id}/edit-profile/ - edit user profile
* /api/account/{user_id}/edit-profile/ - delete user account
* /api/account/{user_id}/profile-pic/ - edit profile picture
* /api/account/{user_id}/profile-pic/ - remove/delete profile picture
* /api/home/users/{user_id}/follow/ - follow or unfollow a user
* /api/home/users/{user_id}/followers/ - returns a list of all user followers
* /api/home/users/{user_id}/following/ - returns a list of all user following
* /api/account/register/ - register a new user account
* /api/account/login/ - login to an existing user account
* /api/account/logout/ - logout

## Public Repo
* [Follow this link](https://github.com/maxwellagyapong/Social_Media_API)

## API Documentation/Playground
```
http://127.0.0.1:8000/api/doc 
```
