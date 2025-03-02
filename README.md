Setting up the Port Scanner Project
To set up the Port Scanner project on your local machine, follow these steps:

Clone the repository

Open your terminal and run the following command to clone the repository and navigate into the project directory:

bash
Copy
Edit
git clone https://github.com/amaelahmed/portscanner.git
cd portscanner
Create a virtual environment

It is recommended to use a virtual environment to manage dependencies. You can create one using venv:

bash
Copy
Edit
python3 -m venv venv
Activate the virtual environment

On Windows:

bash
Copy
Edit
venv\Scripts\activate
On macOS and Linux:

bash
Copy
Edit
source venv/bin/activate
Install dependencies

Install the required dependencies using the requirements.txt file:

bash
Copy
Edit
pip install -r requirements.txt
Run the application

Once the dependencies are installed, you can run the application:

bash
Copy
Edit
python port_scanner.py
Deactivate the virtual environment

When you are done, you can deactivate the virtual environment with:

bash
Copy
Edit
deactivate
Now everything is set up! You can follow the steps in sequence to get your project running sm
