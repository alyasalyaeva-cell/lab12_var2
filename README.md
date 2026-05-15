# Лабораторная работа №12: Medical Registry API

**Студент:** Саляева Александра 
**Группа:** 221331
**Вариант:** 2
**Сложность:** Средняя

## Обзор
Система управления данными пациентов. Проект демонстрирует навыки работы с FastAPI, Docker, миграциями БД и автоматизированным тестированием.

## Переменные окружения
- `DATABASE_URL`: Строка подключения к БД. Пример: `postgresql://user:pass@db:5432/db`

## Эндпоинты API
| Метод | Путь | Описание |
| :--- | :--- | :--- |
| `GET` | `/patients` | Получить всех пациентов |
| `POST` | `/patients` | Регистрация нового пациента |
| `GET` | `/patients/{id}` | Поиск по ID |
| `PUT` | `/patients/{id}` | Обновление данных |
| `DELETE` | `/patients/{id}` | Удаление записи |

## Запуск проекта
```bash
# Клонировать репозиторий и запустить:
docker-compose up --build

Создание записи:

curl -X 'POST' 'http://localhost:8000/patients' \
-H 'Content-Type: application/json' \
-d '{
  "id": 1,
  "full_name": "Иванов Иван",
  "oms_policy": "1234567890123456",
  "birth_date": "2000-01-01",
  "email": "alex@example.com",
  "gender": "Male"
}'

Обновление данных (PUT):
curl -X 'PUT' 'http://localhost:8000/patients/1' \
-H 'Content-Type: application/json' \
-d '{
  "id": 1,
  "full_name": "Иванов Иван",
  "oms_policy": "1234567890123456",
  "birth_date": "2000-01-01",
  "email": "new_email@example.com",
  "gender": "Male"
}'

Удаление:
curl -X 'DELETE' 'http://localhost:8000/patients/1'