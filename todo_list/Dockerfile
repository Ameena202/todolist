# Step 1: Use a lightweight Python image
FROM python:3.9-slim

#step 2: setting up working directory inside the container
WORKDIR /app

#step3: installing the dependencies
RUN pip install Django

#step4: copy the project into working directory
Copy . /app/

#step5: Exposing the port
EXPOSE 8000

#Step6: Run Django development server
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
