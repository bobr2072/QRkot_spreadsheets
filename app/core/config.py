from typing import Optional

from pydantic import BaseSettings, EmailStr

from datetime import datetime


class Settings(BaseSettings):

    app_title: str = 'Кошачий благотворительный фонд'
    description: str = 'Сервис для поддержки котиков!'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    lifetime_seconds: int = 3600
    # for auto_create first superuser
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    # for google
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None
    FORMAT = '%Y/%m/%d %H:%M:%S'
    now_date_time = datetime.now().strftime(FORMAT)
    table_values = [
        ['Отчет от', now_date_time],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]

    class Config:
        env_file = '.env'


settings = Settings()
