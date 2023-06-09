# someMarket
### or ecommerce django project

----

## 🚀 Features

- Django 4.1 & Python 3.8
- No users, only sessions !
- Caching with [redis](https://redis.io)
- Simple API for checking commerce stats
- Styling with Bootstrap v5 (static files are in branch "with_static_files")
- Testing with Pytest
- Swagger UI for API documentation and testing
- Easy to manage admin panel
- More than half of the views are written in generics.

----

## Table of Contents
* [Installation](#installation)
* [ER diagram](#er-diagram)
* [Next Steps](#next-steps)
* [Contributing](#contributing)
* [Support](#support)
* [License](#license)

----

## 📖 Installation
someMarket can be installed via pip and Docker. To start, clone the repo to your local computer and change into the proper directory.  
Remember, static files are in the branch 'with_static_files'. If you want to use it, just pull this branch to your local machine.  
!!! Before start project you need to install Redis, see how you can do it [here](https://redis.io/docs/getting-started/) !!! (or disable caching in project)

```
$ git clone https://github.com/lilchiken/ecommerce-django-project.git
$ cd ecommerce-django-project
```

### Pip

Dont forget start redis.

```
# Windows
$ python -m venv .venv

# macOS
$ python3 -m venv venv

# Windows
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1

# macOS
$ source .venv/bin/activate

(.venv) $ pip install -r requirements.txt
(.venv) $ python manage.py migrate
(.venv) $ python manage.py makemigrations
(.venv) $ python manage.py migrate
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```


### Docker

You can see structure docker project in branch "docker".  
Staticfiles are deployed.  
Admin already created.  
Username: admin  
Password: admin

```
$ docker pull lilchiken/ecommerce-django-project
$ docker run -d --name ecommerce-django-project -p 80:80 lilchiken/ecommerce-django-project
# Load the site at http://localhost:80
```


----

## ER diagram

![ER-diagram](https://github.com/lilchiken/EcommercePetProject/blob/6b04b7cfa14e7b92cb2da3b418080360e2147213/static/readme/ER.png)

----
## Next Steps

- Check Pytest local.
- Develop payment methods that you want to see in the project.
- Add [gunicorn](https://pypi.org/project/gunicorn/) or other web server before production.
- Configure permissions in API viewset.
- Play with site on Docker and feedback me. :)
- Make the [admin more secure](https://opensource.com/article/18/1/10-tips-making-django-admin-more-secure).

----

## 🤝 Contributing

Contributions, issues and feature requests are welcome! ;)

## ⭐️ Support

Give a ⭐️  if this project helped you!

## License

[The MIT License](LICENSE)
