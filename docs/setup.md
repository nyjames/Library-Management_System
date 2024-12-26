# Instructions for setup and installation

# Django Virtual Environment Install

## Instructions for Setting Up a Virtual Environment in the `src` Folder

1. **Navigate to the Project Directory**:  
   Open your terminal or command prompt and navigate to the source directory of our project (`src` folder):  
   `cd onedrive/csc-256/group-project/fa24project-fa24project_team_4/src`

2. **Create the Virtual Environment**:  
   Use Python's `venv` module to create a virtual environment within the `src` folder:  
   `python -m venv venv`  
   This will create a new directory named `venv` within the `src` folder, containing the virtual environment.

3. **Activate the Virtual Environment**:  
   Activate the virtual environment using the following commands based on your operating system:  
   - **Windows**: `venv\Scripts\activate`  
   - **macOS and Linux**: `source venv/bin/activate`

4. **Install Project Dependencies**:  
   Once the virtual environment is activated, install the necessary project dependencies listed in the `requirements.txt` file:  
   `pip install -r ../requirements.txt`  
   **Note**: Ensure your `requirements.txt` file is in the root directory of your project.

5. **Verify the Virtual Environment**:  
   To confirm the virtual environment is set up correctly, run the following command to see the list of installed packages:  
   `pip list`

6. **Run the Django Development Server**:  
   Start the Django development server by running:  
   `python manage.py runserver`  
   After the server starts, click the link in the terminal (usually `http://127.0.0.1:8000/`) to verify the site is running.  
   To stop the server, press `Ctrl + C`.
