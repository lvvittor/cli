# CHE - Semantic Terminal leveraged by LLMs

`che` te permite interactuar con tu terminal diciendole lo que queres hacer en lenguaje natural, sin necesidad de recordar todos los comandos de memoria.

[ezgif.com-video-to-gif.webm](https://user-images.githubusercontent.com/24721312/229342361-aefe5c04-042d-475a-8f24-f6d11fa5b2f2.webm)

## Correr usando imagen de Docker Hub

Para correr el proyecto en cualquier arquitectura utilizamos docker containers. 

> Si no tenes instalado docker, podes ver las [instrucciones de instalacion](https://docs.docker.com/get-docker/) en la documentacion oficial.

1. Pullear la imagen oficial de Docker Hub.

```bash
docker pull lvittor/che:release
```

2. Correr un contenedor.

```bash
export OPENAI_API_KEY=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

docker run --rm -it -e OPENAI_API_KEY="${OPENAI_API_KEY}" --entrypoint bash lvittor/che:release
```

Nos aparecera el container en modo sandbox para probar el paquete `che`:

```bash
root@940862468f02:/che-sandbox# che "imprimi en pantalla bienvenido al sandbox de che"
```

> La funcion de `copiar` no esta funcional dentro del sandbox de Docker, dado que la imagen base no dispone de un sistema de copy-paste.

## Correr usando Makefile

> Requiere tener Docker instalado.

1. Renombrar `.env.example` a `.env`.

2. Construir imagen.

```bash
make build
```

3. Correr contenedor.

```bash
$ make up
root@940862468f02:/che-sandbox#
```

## Correr usando Poetry

> Requiere tener [Poetry](https://python-poetry.org/docs/#installation) instalado.

1. Instalar dependencias.

```bash
poetry install
```

2. Entrar a la shell del venv.

```bash
poetry shell
```

3. Renombrar `.env.example` a `.env` y correr:

```bash
export $(cat .env | xargs)
```

Todo listo para correr `che`.
