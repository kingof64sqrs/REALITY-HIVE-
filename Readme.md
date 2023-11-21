## Initial Setup

```sh
python -m venv venv
```

## Activate Virtual Environment

```sh
"venv/Scripts/activate"
```

## Create apidata.config

```sh
touch apidata.config
```

```
[OPENAI]
ORG = org-****
KEY = sk-****

[UNSPLASH]
KEY = ****
```

## Run Flask App

```sh
flask --app app run --debug
```
