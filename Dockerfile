FROM python:3.5

# Update
#RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask

# Bundle app source
COPY routes.py /src/routes.py

COPY templates /src/templates

EXPOSE  9000
CMD ["python", "/src/routes.py", "-p 9000"]