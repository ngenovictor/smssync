## SMS Sync API WEB GATEWAY

**_About_**

This is a sample web point api endpoint to receive messages from ushaidi's SMS Gateway mobile App.
It will sync and save all incoming mobile messages to an online web application portal that you can access them from and do with them as you may wish.

**_Set Up Instructions_**

1. Create a project folder, setup virtual environment and clone the project
```bash
$ mkdir smssync
$ cd smssync
$ virtualenv -p python3 env
$ source env/bin/activate
$ git clone https://github.com/ngenovictor/smssync.git
$ cd smssync
```

2. Install python libraries required for the app to run
```bash
$ pip install < requirements.txt
```

3. Create local\_settings file. For security concerns a file local\_settings is created that only the developer sees and is not uploaded to github so you have to create it. Rename **_sample\_local\_settings.py_** to **_local\_settings.py_**
```bash
$ mv smssync/sample_local_settings.py smssync/local_settings.py
```

4. Run the app locally on your machine
```bh
$ python manage.py runserver
```

5. Make a POST request to the endpoint [localhost:8000/sms](localhost:8000/sms) with a json payload using the example format below:
```js
{
    'secret': '123456', 
    'from': '+254720123456', 
    'message_id': 1, 
    'message': 'hey this is a message', 
    'sent_timestamp': '12-12-12', 
    'sent_to': '+254736736736', 
    'device_id': 'victor'
}
```
