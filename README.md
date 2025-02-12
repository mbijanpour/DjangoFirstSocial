# DjangoFirstSocial

DjangoFirstSocial is a social media web application built using Django. This project demonstrates core social media functionalities, including user authentication, profile management, post creation, commenting, and liking. It serves as a portfolio project showcasing my skills in Django development.

## Features

- **User Authentication**: Register, login, and logout functionality.
- **User Profile Management**: Edit user profiles and view other users' profiles.
- **Post Management**: Create, update, and delete posts.
- **Commenting System**: Comment on posts and reply to other comments with nested replies.
- **Liking System**: Like posts with a single like per user.
- **Follow/Unfollow Users**: Follow and unfollow other users.
- **Password Reset**: Reset password via email verification.
- **Search Functionality**: Search for posts and users.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/DjangoFirstSocial.git
cd DjangoFirstSocial
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

### 7. Access the Application

Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Project Structure

```
DjangoFirstSocial/
|
|-- accounts/       # User authentication and profile management
|-- home/           # Homepage and search functionality
|-- posts/          # Post creation, comments, replies, and likes
|-- templates/      # HTML templates
|-- static/         # Static files (CSS, JS, images)
|-- DjangoFirstSocial/  # Project settings and URL configurations
|-- requirements.txt # Project dependencies
|-- manage.py       # Django management script
```

## Key Files

- **accounts/views.py**: Handles user authentication, registration, profile management, and password reset.
- **posts/views.py**: Handles post creation, update, delete, comments, replies, and likes.
- **base.html**: Main layout template.
- **navbar.html**: Navigation bar template.
- **messages.html**: Template for displaying notifications.

## Usage

### User Registration & Authentication

- Users can sign up using a username, email, and password.
- Login with username/email and password.
- Password reset functionality via email.

### Post Management

- Users can create posts with a title and body.
- Posts can be updated or deleted by their creators.
- All posts are displayed on the homepage.

### Commenting & Liking

- Users can comment on posts and reply to other comments.
- Nested replies are supported.
- Posts can be liked, but only once per user.

### Following System

- Users can follow or unfollow others.
- Profiles display user details and follower count.

## Contributing

Contributions are welcome! If you find any issues or have improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For inquiries, please contact me at [mahanbijanpour@example.com].

Thank you for checking out DjangoFirstSocial! 🚀
