FROM python:3.10.12

USER root

RUN apt-get update && \
    # apt-get install -y locales vim less && \
    apt-get install -y locales vim less libgl1-mesa-glx && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    apt-get clean

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
ENV PYTHONPATH=/app

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

WORKDIR /carbon-steel-classification

ADD requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

CMD ["bash"]
