FROM python:3.12-alpine as requirements-stage
# --------- requirements ---------

WORKDIR /tmp

RUN pip install poetry poetry-plugin-export

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


# --------- final image build ---------
FROM python:3.12-alpine

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code

# --------- Utils  ---------
COPY ./docker/helpers/wait-for-it.sh /wait-for-it.sh
RUN sed -i 's/\r$//g' /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# --------- entrypoint ---------
COPY ./docker/local/api/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh
RUN chmod +x /entrypoint.sh

# --------- run ---------
COPY ./docker/local/api/start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh
RUN chmod +x /start.sh

ENTRYPOINT [ "/bin/sh", "/entrypoint.sh" ]