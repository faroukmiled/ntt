FROM python:3.10-slim-bullseye

RUN apt-get update && apt-get install -y \
    git \
    libopencv-dev \
    python3-opencv \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-glx \
    ffmpeg    

WORKDIR /app

RUN git clone -b ntt-with-simple-tools https://github.com/centralelyon/ntt.git

RUN python3 -m venv .venv

# No need to activate a virtualenv : https://snarky.ca/how-virtual-environments-work/
ENV PATH=/app/.venv/bin:$PATH

RUN .venv/bin/pip install --upgrade pip pip-tools

# WORKDIR changes PATH
WORKDIR ntt

RUN sed -i '/^-e file:/d' requirements-dev.txt
RUN pip-sync requirements-dev.txt
RUN pip install -e .[dev]

CMD [ "python", "script.py" ]
