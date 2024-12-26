## 1. Install Robot Framework
```
pip install robotframework
pip install robotframework-djangolibrary
pip install robotframework-seleniumlibrary
```

## 2. Verify chromedriver is in system path
- Type chromedriver in the terminal and press enter. If Chromedriver is in the path, it will return the version number and a message indicating that it is ready to accept connections on a specific port.

## 3. Run server
```
python manage.py runserver
```

## 4. Open another terminal and run Robot tests
```
python manage.py start_robot
```

## 5. Reports are generated in 'src/test-reports'