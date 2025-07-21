# 🚀 CodeLeap Network - Backend API

A REST API developed in Django for the CodeLeap Network posts system. This API allows creating, listing, editing and deleting career posts, following exactly the provided technical specifications.

## 📋 About the Project

This project was developed as part of the selection process for a backend developer position at CodeLeap. The API implements all functionalities requested in the official documentation, including specific endpoints and standardized data structure.

## 🛠️ Technologies Used

- **Django 4.2+** - Main web framework
- **Django REST Framework** - For REST API creation
- **PostgreSQL** - Database (production)
- **SQLite** - Database (development)
- **Python 3.11** - Programming language
- **Gunicorn** - WSGI server for production

## 📚 Features

- ✅ **List Posts** - GET `/careers/`
- ✅ **Create Post** - POST `/careers/`
- ✅ **Edit Post** - PATCH `/careers/{id}/`
- ✅ **Delete Post** - DELETE `/careers/{id}/`
- ✅ **CORS configured** for frontend integration
- ✅ **Data structure according to specification**
- ✅ **Production-ready deployment**

## 🗄️ API Structure

### Data Model

```json
{
  "id": "number",
  "username": "string", 
  "created_datetime": "datetime",
  "title": "string",
  "content": "string"
}
```

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/careers/` | Lists all posts |
| POST | `/careers/` | Creates a new post |
| GET | `/careers/{id}/` | Fetches specific post |
| PATCH | `/careers/{id}/` | Updates title and/or content |
| DELETE | `/careers/{id}/` | Deletes a post |

## 🚀 How to Run

### Prerequisites

- Python 3.11+
- pip
- Git

### Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/LukeRobs/API-CodeLeap.git
cd API-CodeLeap
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up the database**
```bash
python manage.py migrate
```

5. **Run the server**
```bash
python manage.py runserver
```

6. **Access the API**
```
http://127.0.0.1:8000/careers/
```

## 🧪 API Testing

### Using Postman/Insomnia

1. **Base URL:** `api-codeleap-production.up.railway.app`
2. **Content-Type:** `application/json`
3. **Endpoints:** According to table above

## 🌐 Deployment

### Railway (Recommended)

1. **Fork the repository**
2. **Connect your GitHub account to Railway**
3. **Import the project**
4. **Configure environment variables:**
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: Your Railway domain
5. **Automatic deploy!**
   

## 🔧 Production Settings

The project is configured to work in both development (SQLite) and production (PostgreSQL) environments. Main configurations include:

- **Database:** Automatic configuration via `DATABASE_URL`
- **Static files:** Served via WhiteNoise
- **CORS:** Configured to allow requests from any origin
- **Security:** Debug disabled in production
- **Environment variables:** Managed via python-decouple

## 📝 Met Specifications

✅ **Framework:** Django + DRF  
✅ **Endpoints:** Exactly according to documentation  
✅ **Data structure:** Required fields implemented  
✅ **HTTP Methods:** GET, POST, PATCH, DELETE  
✅ **Restrictions:** Only title and content editable via PATCH  
✅ **Ordering:** Posts ordered by date (most recent first)  
✅ **Deployment:** Production ready  

## 📄 License

This project is under the MIT license. See the `LICENSE` file for more details.

## 👨‍💻 Developer

**Lucas Robson**
- LinkedIn: [Lucas Robson](https://www.linkedin.com/in/lucas-robson-dev/)

## 📞 Contact

For questions about the project or selection process:
- Email: lucassrobson07@gmail.com

---
⭐ If this project helped you, consider giving the repository a star!
