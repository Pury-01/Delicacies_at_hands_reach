#!/usr/bin/env python3
"""Configuration class"""
import os
import secrets
from dotenv import load_dotenv
from datetime import timedelta


load_dotenv()


class Config:
    """Configurations"""
    # secret key
    SECRET_KEY = secrets.token_urlsafe()

    # database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

    # debugging
    DEBUG = True

    # Session configurations
    SESSION_COOKIE_NAME = 'session'
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)