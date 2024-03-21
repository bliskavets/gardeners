FROM python:3.12-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./assets /content

EXPOSE 5000

CMD ["streamlit", "run", "--server.port", "5000", "app/main_page.py"]
