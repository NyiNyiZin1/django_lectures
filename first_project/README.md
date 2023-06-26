# python .\manage.py migrate first_app
# python .\manage.py makemigrations first_app
# python manage.py shell
    *from first_app.models import Topic
    *t = Topic(top_name="Social Network")
    *t.save()
# python manage.py createsuperuser
