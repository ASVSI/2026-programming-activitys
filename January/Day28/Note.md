# Deployment checklist
```shell
python manage.py check --deploy
```
## Use a .env file (best practice)

### Install python-dotenv:
```shell
pip install python-dotenv
```

Create a .env file (same level as manage.py):
```py
SECRET_KEY=your-super-secret-key
```

Update settings.py:
```py
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ["SECRET_KEY"]
```

Add .env to .gitignore 
```py
.env
```