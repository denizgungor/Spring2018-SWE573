FROM python:3.6
RUN mkdir Spring2018-SWE573
COPY ./ /Spring2018-SWE573
WORKDIR /Spring2018-SWE573
RUN pip install -r requirements.txt
EXPOSE 8000
WORKDIR /Spring2018-SWE573/swe573
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]