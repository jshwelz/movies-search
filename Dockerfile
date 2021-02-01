FROM python:3

RUN python3 -m venv /opt/venv

# Install dependencies:
COPY requirements.txt .

COPY .  .
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

CMD . /opt/venv/bin/activate && exec python get_data.py
CMD . /opt/venv/bin/activate && exec flask load_data

# Run the application:
COPY app.py .
CMD . /opt/venv/bin/activate && exec python app.py
