# Django Bookmarks


Django bookmarks is a simple, private bookmarking site, with features like sharing bookmarks, adding users, admin page, rss feed, and a few more, hosted on localhost __or__ 127.0.0.1. It is fully functional and ready to be deployed with some basic security features against attacks like cross site scripting and SQL injection.
## Features

- Ready to deploy.
- Protected against common attacks.
- Written in clean code and easily editable.
- Comes with common error pages like 404 and 500
- jQuery code written.
- Comes with a development server
- Easy to use admin interface

## Technology Used

Django Bookmarks uses 2 main technologies, [Python 2] and Django 0.95 (included) but uses lots of different thing in the background like [jQuery] (unimplemented but makes web pages more usable) and [CSS] (Helps styling the webpages)

## Installation

Install the repository and you are good to go!

To start the devolpment server on 127.0.0.1:8000 __or__ localhost:8000 (for Chrome), run the flowing commands
1. To start the server:

    ```sh
    py -2 manage.py runserver
    ```
    __OR__
    Run the runserver file.
2. To add a user:
    - Go to 127.0.0.1:8000/admin __or__ localhost:8000/admin (for Chrome/Firefox/Edge)
    - Enter admin for username and password.
    - Create a user.
3. To login go to 127.0.0.1:8000/login __or__ localhost:8000/login (for chrome) and login with the credentials you created.
4. Enjoy!

## Development

Want to contribute? Great! Pull requests and issues are welcome! [Here] is an excellent guide on how to create pull requests and forks to request changes.

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job.)

   [CSS]: <https://devdocs.io/css/>
   [jQuery]: <http://jquery.com>
   [Python 2]: <https://www.python.org/downloads/release/python-2718/>
   [Here]: <https://www.dataschool.io/how-to-contribute-on-github/>
