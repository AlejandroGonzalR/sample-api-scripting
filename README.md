# sample-api-scripting
Simple script that consume an API and perform operations between endpoints

## Project setup

Using a [virtual environment](https://click.palletsprojects.com/en/7.x/quickstart/#virtualenv) for development is recommended

``` bash
$ pip install virtualenv
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

### Local Execution
Create an `.env` file based on [.env.example](.env.example) with your specific configuration (due this is a sample project, you can use the same `.env.example` as environment variables file).

Since this project **NOT** uses the python setuptools, once `pip install` is done you can just call `python3 src/main.py` in your shell.

If you're using the recommended virtual env, you must activate it first.

``` bash
$ . venv/bin/activate
$ python3 src/main.py
```
