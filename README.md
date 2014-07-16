FindAClass
==========

Find a class


Open Datasets
=============
Afterschool and UPK programs
http://nycdoe.pediacities.com/dataset/after-school-upk-programs

Afterschool programs
http://nycdoe.pediacities.com/dataset/after-school-upk-programs/resource/1e042827-d69d-48f0-a2ba-1df13c3c307e

Summer Quest programs
http://nycdoe.pediacities.com/dataset/after-school-upk-programs/resource/3bbb0a0c-e582-494d-bf64-f89ba3b2425c

UPK for BigApps
http://nycdoe.pediacities.com/dataset/after-school-upk-programs/resource/b6fbf067-2dae-4b4f-ad5e-54f1d8d0d03b


Summer camps
http://www.nyc.gov/html/doh/html/living/campmn.shtml

Daycare
https://github.com/childcaremap/NYCdaycare/tree/gh-pages/python_scraper

Data from NYC Department of Health and Mental Hygiene:
Center-based child care at 
https://a816-healthpsi.nyc.gov/ChildCare/ChildCareList.do
Home-based child care at 
http://it.ocfs.ny.gov/ccfs_facilitysearch/
Located home-based child care information for download (or API access) on NY State Open Data Portal: https://data.ny.gov/Human-Services/Child-Care-Regulated-Programs/cb42-qumz


Django
======

To make changes to model.py see
Try Django Tutorial 15 of 21 - Django Update Thank You Page and View after Paypal Purchase
https://www.youtube.com/watch?v=Cmk_HeQwwtg

To Check if you have south installed:
%pip freeze

%python manage.py syncdb

If you didn't make any changes to your model then convert to south for migrations
%python manage.py convert_to_south findaclass
%python manage.py schemamigration findaclass --auto
%python manage.py migrate findaclass

ONLY IN DEVELOPMENT: If you have problems and can't fix it then the easiest fix is to delete all the migrations folder and the db.sqlite3 file.  You will need to reload the databasae if you do this.  ONLY IN DEVELOPMENT!!!

When making changes to static files:
%python manage.py collectstatic


Queries:
https://docs.djangoproject.com/en/dev/topics/db/queries/

To move to production:
Try Django Tutorial 18 of 21 - Create MySQL for Django Production Server and setup
https://www.youtube.com/watch?v=cJESeioAFpU


Loading data repeatedly:
https://code.djangoproject.com/wiki/Fixtures

django rest_framework
http://www.django-rest-framework.org/


PhoneGap
========
http://phonegap.com/


GitHub
======
https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line

