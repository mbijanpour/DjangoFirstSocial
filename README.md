DjangoFirstSocial
DjangoFirstSocial is a social media web application built using Django. This project demonstrates the implementation of user authentication, profile management, post creation, commenting, and liking functionality. It is designed to showcase my skills in Django development and can be used as a portfolio project for my resume.

Features
User Registration and Login
User Profile Management
Create, Update, and Delete Posts
Comment on Posts
Reply to Comments
Like Posts
Follow and Unfollow Users
Password Reset Functionality
Search Posts
Installation
Clone the repository:
git clone https://github.com/yourusername/DjangoFirstSocial.git
cd DjangoFirstSocial
Create a virtual environment:
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
Install dependencies:
pip install -r requirements.txt
Apply migrations:
python manage.py migrate
Create a superuser:
python manage.py createsuperuser
Run the development server:
python manage.py runserver
Access the application: Open your web browser and go to http://127.0.0.1:8000/

Project Structure
accounts: Contains user authentication, profile management, and related views, models, and forms.
home: Contains the home page view and search functionality.
posts: Contains post creation, update, delete, comment, reply, and like functionality.
templates: Contains HTML templates for the application.
DjangoFirstSocial: Contains project settings and URL configurations.
Key Files
views.py: Handles user registration, login, logout, profile management, and password reset views.
views.py: Handles post creation, update, delete, comment, reply, and like views.
base.html: Base template for the application.
navbar.html: Navigation bar template.
messages.html: Template for displaying messages.
requirements.txt: List of dependencies for the project.
Usage
User Registration and Login
Users can register by providing a username, email, and password.
Users can log in using their username or email and password.
Logged-in users can view and edit their profiles.
Post Management
Users can create new posts with a title and body.
Users can update or delete their own posts.
Users can view a list of all posts on the home page.
Commenting and Replying
Users can comment on posts.
Users can reply to comments.
Nested replies are supported.
Liking Posts
Users can like posts.
Users can only like a post once.
Following Users
Users can follow and unfollow other users.
Users can view the profiles of other users.
Password Reset
Users can reset their passwords by providing their email address.
Users will receive an email with a link to reset their password.
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License.

Contact
For any inquiries, please contact me at [your-email@example.com].

This project is a demonstration of my skills in Django development and is intended to be used as a portfolio project for my resume. Thank you for checking it out!
