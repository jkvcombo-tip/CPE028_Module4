FROM python
RUN pip install flask
COPY  ./static /home/myapp/static/
COPY  ./templates /home/myapp/templates/
COPY  devops_app.py /home/myapp/
EXPOSE 8080
CMD python3 /home/myapp/devops_app.py
