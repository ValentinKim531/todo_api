# 📝 ToDo API

REST API сервис на Django 5 + DRF + JWT + Docker Compose
для управления задачами с авторизацией, пагинацией, Swagger-документацией и 
парсингом участников Astana Hub

## Для запуска проекта 

### 1. Склонируйте репозиторий

```bash
git clone https://github.com/your-username/todo_api.git
cd todo_api
```

### 2. Переименуйте файл '.env.example ' в `.env` в корне проекта и заполните его соответствующими данными
```bash
cp .env.example .env
```

### 3. Запустите проект

```bash
docker compose up --build
```

### 4. 🌍 Работа с API

```
http://localhost:8000/swagger/
```


## Данные для входа и тестирования приложения

<table>
    <tr>
        <th>Вход для:</th>
        <th>Логин</th>
        <th>Пароль</th>
    </tr>
    <tr>
        <td>администратора(admin)</td>
        <td>admin@admin.com</td>
        <td>admin</td>
    </tr>
    <tr>
        <td>обычный пользователь</td>
        <td>user@example.com</td>
        <td>user</td>
    </tr>
</table>

### 📁 Стек технологий
- Python 3.11
- Django 5.2
- Django REST Framework
- PostgreSQL
- Docker + docker-compose
- Playwright (для парсинга)
- Pytest