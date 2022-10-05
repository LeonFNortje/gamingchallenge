FROM python:3.10.4

# working directory
WORKDIR /usr/app

# copy requirement file to working directory
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]