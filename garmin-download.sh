#!/bin/sh

garmindb_cli.py --all --download --import --analyze --latest

sqlite3 -header -csv ~/HealthData/DBs/garmin_summary.db "select * from days_summary_view;" > ~/Documents/garmin_analysis/data/garmin_days_summary.csv
sqlite3 -header -csv ~/HealthData/DBs/garmin_activities.db "select * from activities" > ~/Documents/garmin_analysis/data/garmin_activities.csv
