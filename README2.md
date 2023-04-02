# Che: Una terminal semantica 

## Correr demo sin tener que clonar el repo

### Dependencias

Para correr el proyecto en cualquier arquitectura utilizamos docker containers. 

Si no tenes instalado docker, podes ver las [instrucciones de installacion](https://docs.docker.com/get-docker/) en la documentacion oficial.

### Pullear imagen y correr el contenedor

Ahora que tenemos docker, podemos pullear la imagen desde dockerhub:

```bash
docker pull lvittor/che:release
```

Cuando se termine de instalar la imagen, podemos correr el contenedor con:

```bash
export OPENAI_API_KEY=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
docker run --rm -it -e OPENAI_API_KEY="${OPENAI_API_KEY}" --entrypoint bash lvittor/che:release
```

Ahora nos va a aparecer el container en modo sanbox para jugar con nuestro paquete "che":

```bash
root@940862468f02:/che-sandbox# che "imprimi en pantalla bienvenido al sandbox de che"
```

##

