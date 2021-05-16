class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "34567GFDGCXCVBNMERTYUIFCV 456GFVVCXSDRERFCXWEUTR4567DSWEFRGFD43R4R"
    DB_NAME = "production_db"
    DB_USERNAME = "root"
    DB_PASS = "passdb"
    SESSION_COOKIE_SECURE = True
    IMAGE_UPLOADS="/projets/Personal projects/Flask/app/static/images/uploads"
    CLIENT_IMAGES="/projets/Personal projects/Flask/app/static/client/img"
    CLIENT_CSV="/projets/Personal projects/Flask/app/static/client/csv"
    ALLOWED_IMAGE_EXTENSIONS =["PNG","JPG","JPEG","GIF"]
    MAX_IMAGE_FILESIZE =0.5*1024*1024


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG =True
    DB_NAME = "development_db"
    DB_USERNAME = "root"
    DB_PASS = "passdb"
    # IMAGE_UPLOADS="/projets/Personal projects/Flask/app/static/images/uploads"
    # CLIENT_IMAGES="/projets/Personal projects/Flask/app/static/client/img"



    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True 
    DB_NAME = "testing_db"
    DB_USERNAME = "root"
    DB_PASS = "passdb"
    IMAGE_UPLOADS="/projets/Personal projects/Flask/app/static/images/uploads"


    SESSION_COOKIE_SECURE = False

