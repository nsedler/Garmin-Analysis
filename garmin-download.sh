#!/bin/sh

garmindb_cli.py --all --download --import --analyze --latest
echo "garmin data downlaoded"

sqlite3 -header -csv ~/HealthData/DBs/garmin_summary.db "select * from days_summary_view;" > ~/Documents/coding/Garmin-Analysis/data/garmin_days_summary.csv
echo "days summary converted to csv"
sqlite3 -header -csv ~/HealthData/DBs/garmin_activities.db "select * from activities" > ~/Documents/coding/Garmin-Analysis/data/garmin_activities.csv
echo "activities summary converted to csv"
echo "all done :)"
