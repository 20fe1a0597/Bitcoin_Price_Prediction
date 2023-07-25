# Bitcoin_Price_Prediction
Bitcoin price prediction using ML with Django Framework
To run a Django project, you'll need to follow these initial commands:

1. **Create a Virtual Environment (optional but recommended):**
   It's a good practice to create a virtual environment to keep your project dependencies isolated. Open the Command Prompt or Terminal and navigate to the root folder of your project (where you want to create the virtual environment). Then run:

   For Windows:
   ```
   python -m venv myenv
   myenv\Scripts\activate
   ```

   For macOS and Linux:
   ```
   python3 -m venv myenv
   source myenv/bin/activate
   ```

2. **Install Django:**
   Once you have the virtual environment activated, you need to install Django. In the Command Prompt or Terminal with the activated virtual environment, run:

   ```
   pip install django
   ```

3. **Create a Django Project:**
   After installing Django, you can create a new Django project using the following command. Replace "projectname" with the desired name of your project:

   ```
   django-admin startproject projectname
   ```

4. **Navigate to the Project Directory:**
   Move into the project directory by running:

   ```
   cd projectname
   ```

   Note: In Windows Command Prompt, use `dir` command instead of `ls` to list directories.

5. **Run the Development Server:**
   To run the Django development server, use the following command:

   ```
   python manage.py runserver
   ```

   This will start the server at `http://127.0.0.1:8000/`. You can access your Django project by opening this URL in your web browser.

6. **Create an App (optional):**
   A Django project can contain multiple apps. If you want to create an app within your project, use the following command. Replace "appname" with the desired name of your app:

   ```
   python manage.py startapp appname
   ```

   Note: This step is optional if you don't need additional apps in your project.

That's it! Your Django project should now be up and running, and you can start building your web application using the Django framework. Remember to keep the virtual environment activated while working on your project to manage dependencies properly.
