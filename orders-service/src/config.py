class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@orders-db:5432/orders_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False