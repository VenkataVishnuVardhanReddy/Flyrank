# Auth Login & Protect API

A secure API that handles user authentication using **Supabase Auth** and protects specific routes via JSON Web Tokens (JWTs).

## Features
- **Sign Up / Log In**: Secure authentication via Supabase.
- **JWT Verification**: Validates Access Tokens before allowing access to protected routes.
- **Security Middleware**: Centralized token verification using FastAPI Dependencies.
- **Swagger UI**: Interactive API documentation at `/docs` with built-in Bearer Token authorization.

## Setup Instructions

1. Clone the repository and navigate to this folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables:
   Copy `.env.example` to `.env` and fill in your Supabase credentials:
   ```bash
   cp .env.example .env
   # Edit .env and add your SUPABASE_URL and SUPABASE_KEY
   ```
4. Start the server:
   ```bash
   uvicorn main:app --reload --port 3000
   ```

## API Endpoints

| Method | Route | Description | Auth Required |
|---|---|---|---|
| POST | `/auth/signup` | Create a new user account | No |
| POST | `/auth/login` | Authenticate user & return JWT | No |
| POST | `/auth/logout` | Terminate the user session | Yes |
| GET | `/public/info` | Read public, unprotected data | No |
| GET | `/protected/profile` | Read private user profile data | Yes |
| GET | `/protected/dashboard`| Secondary protected route | Yes |

## Testing in Swagger UI
1. Start the server and go to `http://localhost:3000/docs`.
2. Use the `/auth/signup` and `/auth/login` endpoints to get your `access_token`.
3. Click the **Authorize** button (padlock icon) at the top of the page.
4. Paste your token into the Value field and click Authorize.
5. You can now use the "Try it out" feature on the protected endpoints!
