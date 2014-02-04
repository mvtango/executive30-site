#! /bin/bash

 

python app/freeze.py 
rsync -rv --delete site/apps/ ubuntu@apps2.dpa-newslab.com:/srv/apps/static/
