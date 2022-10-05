# Gaming Challenge

## For running the code:

This application will accept file in text format, allowing you to capture gaming results and it will provide you with the winners of the league.

python3 main.py filename.txt

or

python3 main.py

### Docker container is also available:

Within root folder, building the docker image as below

docker built -t testingChallenge:latest .

docker run -it testingChallenge:latest

### Testing application

After installing pytest, or requirements.txt the tests can be run with:

python3 -m pytest

or with docker within the tests folder:

docker built -t testingChallenge_tests:latest .
docker run -it testingChallenge_tests:latest

With tests folder, building and running the dockerfile will run unit tests for the application

## Examples:

Input, either stdin or in the filename.txt

````
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
````

Results:

````
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
````

