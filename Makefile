.PHONY=run
IGNORE_DIRS=backend/db/data

run:
	poetry run flet run -d -r --ignore-dirs $(IGNORE_DIRS) app/main.py

build-apk:
	$(echo "Run folowing command: flet build -o ./build --project \"MoodTracker\" --product \"MoodTracker\" --build-version 0.1 --no-android-splash apk -v")

build-win: 
	$(echo "Run folowing command: flet build -o ./build windows")