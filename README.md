# Identity Service

Repositorio para manejar los usuarios con roles y autenticación mediante JWT.

## Estructura del Proyecto (Clean Architecture)

El proyecto sigue una arquitectura limpia dividida en capas:
- **Domain**: Reglas de negocio, entidades y contratos (interfaces).
- **Application**: Casos de uso y lógica de aplicación.
- **Infrastructure**: Implementación de base de datos, repositorios y servicios externos.
- **API**: Controladores y endpoints REST.

## Pasos para agregar una nueva funcionalidad

Para mantener la coherencia con la arquitectura, sigue este flujo de desarrollo (de adentro hacia afuera):

1.  **Capa de Dominio (Domain)**
    *   Crear la **Entidad** en `app/domain/entities/`.
    *   (Opcional) Crear **Value Objects** en `app/domain/value_objects/`.
    *   Definir la **Interfaz del Repositorio** en `app/domain/repositories/`.

2.  **Capa de Infraestructura (Infrastructure)**
    *   Crear el **Modelo de Base de Datos** (SQLAlchemy) en `app/infrastructure/db/models/`.
    *   Implementar el **Repositorio** (usando el modelo y la interfaz) en `app/infrastructure/db/repositories/`.
    *   Generar la migración con Alembic: `alembic revision --autogenerate -m "description"`.

3.  **Capa de Aplicación (Application)**
    *   Definir los **DTOs** (Data Transfer Objects) en `app/application/<modulo>/dtos.py`.
    *   Crear el **Caso de Uso** en `app/application/<modulo>/<caso_uso>.py`.
        *   Este debe recibir el repositorio (interfaz) y ejecutar la lógica.

4.  **Capa de Presentación (API)**
    *   Crear los **Esquemas de Pydantic** (Request/Response) en `app/schemas/`.
    *   Crear el **Endpoint** (Router) en `app/api/v1/`.
    *   Registrar el nuevo router en `main.py`.
