Django Avance Blog

Welcome to the Django Avance Blog project. This repository serves as a personal project for Marjan Rezaei, focusing on building a robust and scalable blog application using Django.

🛠️ Features

User Authentication: Implement user registration, login, and profile management.

Blog Management: Create, edit, and delete blog posts with rich text formatting.

Comment System: Allow users to comment on posts, fostering community interaction.

Tagging: Organize posts with tags for better content categorization.

Search Functionality: Enable users to search for posts by title or content.

Responsive Design: Ensure the application is mobile-friendly and accessible.

🚀 Installation

Clone the repository:

git clone https://github.com/marjanrezaei/Django-Avance-Blog.git
cd Django-Avance-Blog


Set up a virtual environment:

python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Create a superuser:

python manage.py createsuperuser


Run the development server:

python manage.py runserver


Access the application at http://127.0.0.1:8000
.

📂 Project Structure

The project follows a standard Django structure:

core/: Contains the main application logic.

templates/: HTML templates for rendering views.

static/: CSS, JavaScript, and image files.

media/: User-uploaded files.

docker-compose.yml: Configuration for Docker deployment.
Clinique TAGMED
+2
Scribd
+2
Scribd

🧪 Testing

To run tests, use:

python manage.py test


📄 License

This project is licensed under the MIT License.

Feel free to modify this template to better fit your project's specifics. If you need further assistance or additional sections, such as deployment instructions or API documentation, don't hesitate to ask!
