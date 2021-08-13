## Backend Api : TourVago App

### Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Steps

1. Clone the repo
   ```sh
   git clone https://github.com/TitansonFlutter/TourVago-Backend-Api.git
   ```
2. Install The Virtual Environment if none
   ```sh
   python3 -m venv venv
   ```
3. Install Requirements.txt packages
   ```sh
   pip3 install -r requirements.txt
   ```
4. Change the Database URI in the setting.py file if using local database

5. Run create .py
   ```sh
   python3 create.py
   ```
6. Run the server
   ```sh
   FLASK_APPLICATION=app
   FLASK_DEBUG=1
   flask run
   ```

## Git commands

Some of git **commands**, throughout the project...

1. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
2. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the Branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request
