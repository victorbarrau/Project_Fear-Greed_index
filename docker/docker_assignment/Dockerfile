FROM python:3.9-slim-buster

RUN mkdir /gg_trend

COPY . /gg_trend/.

RUN pip install -r /gg_trend/requirements.txt

CMD [ "python","/gg_trend/ggtrend.py" ]
