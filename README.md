Django-FullCalendar is a Django web application that leverages Google Authentication for user sign-in, utilizes Summernote for rich text editing, and integrates FullCalendar.io for advanced calendar functionalities. This project is ideal for applications requiring user authentication, rich text content creation, and calendar management.

![FullCalendar](https://cdn.discordapp.com/attachments/419291925322006528/1199563231551819786/image.png?ex=65c2ff51&is=65b08a51&hm=c4281aed50ca8388df64b3fd81b9861d8138d7ca453b4d504c1c4111df51608a& "FullCalendar")

![ListEvents](https://cdn.discordapp.com/attachments/419291925322006528/1199563344928067624/image.png?ex=65c2ff6c&is=65b08a6c&hm=6ee919f900532b7201b3a88272993cd06a0e6babcf39472cb8d203797c01d62d& "ListEvents")

![Summernote](https://cdn.discordapp.com/attachments/419291925322006528/1199563643453456414/image.png?ex=65c2ffb3&is=65b08ab3&hm=2de640428e6bdc96797d4e402d0a05b9683ff47106ca906e8dca009d05748fb9& "Summernote")
# Features
Google Authentication: Secure user authentication using Google accounts.
Summernote: Rich text editor for content creation.
FullCalendar.io: Interactive calendar for event management.
# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
- Python 3.x
- Django (latest version)
- Other dependencies in requirements.txt

# Installing
1. Clone the Repository
```
git clone git@github.com:pip-install-python/Django-FullCalendar.git
cd django_app
```
2. Set Up a Virtual Environment (optional, but recommended)
```
python -m venv venv
source venv/bin/activate  # On Unix or MacOS
venv\Scripts\activate     # On Windows
```
3. Install Required Packages
```
pip install -r requirements.txt
Google Authentication Setup
```
4. Google Authentication Setup

Follow Google's documentation to set up OAuth2 credentials.
Update your settings.py with your Google client ID and secret.

5. Database Migrations
```
python manage.py makemigrations
python manage.py migrate
Run the Development Server
```
6. Run the Development Server
```
python manage.py runserver
```
7. Access the Application

Open your browser and go to http://localhost:8000.
# Usage
Logging In: Use your Google account to log in.
Rich Text Editing: Create and edit content with Summernote editor.
Calendar Management: Use FullCalendar.io to manage events.
# Deployment
Add additional notes about how to deploy this on a live system.

# Built With
[Django]() - The web framework used
[Summernote]() - Rich text editor
[FullCalendar.io]() - Interactive calendar
[Google OAuth2]() - Authentication
# Contributing
Please read [CONTRIBUTING.md](link to your CONTRIBUTING.md file) for details on our code of conduct, and the process for submitting pull requests to us.

# Authors
pip-install-python

# License
This project is licensed under the MIT License - see the LICENSE.md file for details
