class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "34567GFDGCXCVBNMERTYUIFCV 456GFVVCXSDRERFCXWEUTR4567DSWEFRGFD43R4R"
    DB_NAME = "production_db"
    DB_USERNAME = "root"
    DB_PASS = "passdb"
    UPLOADS_DIR ="/home/username/flask/app/static/images/uploads"
    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG =True
    DB_NAME = "development_db"
    DB_USERNAME = "root"
    DB_PASS = "passdb"
    UPLOADSDIR ="/home/username/flask/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True 
    DB_NAME = "testing_db"
    DB_USERNAME = "root"
    DB_PASS = "passdb"
    UPLOADSDIR ="/home/username/flask/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False

