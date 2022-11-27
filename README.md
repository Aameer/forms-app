# Collect Clone

Demo Application for Collect Clone. 

Important links:

Inspired from :
* https://stackoverflow.com/a/40950280
* https://stackoverflow.com/a/59598549
* https://github.com/kimlimjustin/google-form-clone


for desktop google sheet sync app.
* https://learndataanalysis.org/source-code-insert-records-to-from-google-sheets-and-a-database-with-python-and-sheets-api/
* https://learndataanalysis.org/source-code-insert-records-to-from-google-sheets-and-a-database-with-python-and-sheets-api/


google api (python client):
* https://developers.google.com/docs/api/quickstart/python
* https://developers.google.com/identity/protocols/oauth2/web-server#python
* https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values#dimension

Python with Django framework and Vanila JS

##### For the best experience, please use a device with a width of at least 350px
<!-- - Note that this Collect CLONE don't support image uploading due to [Heroku policy](https://help.heroku.com/K1PPS2WM/why-are-my-file-uploads-missing-deleted) -->

</details>
## Built using:
- Python with Django framework and Jinja templating language
- Vanilla Javascript

## Play ground:
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install --upgrade pip`

## Getting started:
- Clone this repository or fork it
    - To clone this repository type git clone `https://github.com/Aameer/forms-app.git` on your command line
    - To fork this repository, click fork button of this repository then type git clone `https://github.com/<your username>/forms-app.git`
- Install all the dependencies of this project by typing `pip install -r requirements.txt`
- Migrate the database by typing `python manage.py migrate` on the command line
- Run the project locally by typing `python manage.py runserver` on the command line
    - NB: to run it on your local network, type `python manage.py runserver 0.0.0.0:8000`
- You project will be accessible in your localhost or local network.
## For pushing forms data to Google sheets
- Setup Desktop app on Google API
- update `sheets_sync.py` with credentails file name. By default assumes name as `client-secret-desktop.json`.
- Don't forget to add sheet ID. (TODO: automatically create on fly and store in DB and retrieve when required)
- finally to sync run `python sheets_sync.py`

<!-- ## Deployment
For deployment, open `form/settings.py` file and uncomment code from line 131 to 159. -->

# Scale/ Issue and what could be done:
1. get working app ready ( base version) - 1day ish
	- gsheet sync ( We are here)
	<!-- - deployment figured as well and write HLD (based level demo)  -->
	- formulate questions
2. created a upto date boiler plate with all fancy things ( maybe not the most upto date) - 1/2 day ish
3. use own boiler plate to do the above thingy and figure deploymnet (drf, celery, rabbitmq, restframework etc) (kubernetes, github actions, tests, deployment) - 1 day ish
4. figure out scale base and update HLD - 1 day ish
5. get it reviewed and then submit - 1 day ish.
scaling rabbitmq and celery: https://vedantsopinions.medium.com/how-we-scaled-celery-for-our-django-app-da2465a3a6be

## License
Distributed under the [MIT](https://github.com/Aameer/forms-app/blob/master/LICENSE) License. See [`LICENSE`](https://github.com/Aameer/forms-app/blob/master/LICENSE) for more information.

## Contact
- Aameer - [aameer.rafiq@gmail.com](mailto:aameer.rafiq@gmail.com)