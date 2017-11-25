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

4. Generate secret key

> - Go to [https://djskgen.herokuapp.com](https://djskgen.herokuapp.com) press **_Generate keys_**
> - Copy one of the generated keys
> - Replace **_SECRET\_KEY = 'my\_production\_secret'_** in the newly created **_local\_settings.py_** to **_SECRET\_KEY = 'above\_copied\_key'_**


5. Run the app locally on your machine
```bh
$ python manage.py runserver
```

6. Make a POST request to the endpoint [localhost:8000/sms](http://localhost:8000/sms) with a json payload using the example format below:
```js
{
    'secret': '123456', 
    'from': '+254720123456', 
    'message_id': 'shb-45hbh-567', 
    'message': 'hey this is a message', 
    'sent_timestamp': '12579291212', 
    'sent_to': '+254736736736', 
    'device_id': 'victor'
}
```

7. As for now the secret is '123456'.

**_Contributors_**

[Victor](https://github.com/ngenovictor)
Contact me [ngenovictor321@gmail.com](mailto:ngenovictor321@gmail.com)

**_License and Copyright_**

Licensed under [MIT License](license)

