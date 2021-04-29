# Zerodha Equity Publisher

This application downloads the equity details from the zerodha bhavcopy api and displays the relevant details using a vue frontend.

## Tech Stacks

- Django
- Redis
- VueJS
- Bootstrap5
- Axios

## Requirements

- Your system must have Python3 installed for the proper functioning of the server.
- The frontend requires NodeJS to be installed into your system.
- For caching Redis server is used, install it for the application to work fine.

## Setup

Clone the repo into your environment
```SH
git clone https://github.com/allenabraham777/zerodha-equity-publisher.git
cd zerodha-equity-publisher
```

#### Server
Switch the directory to server and perform the following

> Try to use a virtual environment for the server

**Install pip packages**
```sh
pip install -r requirements.txt
```
**Create a ```.env``` file and add the following variables**
```sh
REDIS_URL="redis:<your_url>"
SECRET_KEY="Your secret key"
```

#### Client
Switch the directory to client and perform the following

**Install npm packages**
```sh
npm install
```

**Create a ```.env``` file and add the following variables**
```sh
BACKEND_URL="<your_backend_url>"
```

## Running

> For the application to work the redis server must be running

**Client**

In the client directory
```sh
npm run serve
```
Follow the [docs](https://vuejs.org/v2/guide/) for more details

**Server**

In the server directory
```
python manage.py runserver
```
Follow the [docs](https://docs.djangoproject.com/en/3.2/) for more details


![Redis](https://github.com/django.png?size=40) ![Redis](https://github.com/python.png?size=40) ![Redis](https://github.com/vuejs.png?size=40) ![Redis](https://github.com/nodejs.png?size=40)  ![Redis](https://github.com/redis.png?size=40)