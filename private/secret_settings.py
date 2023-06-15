# single sign on Google (will be used if provided)
OAUTH2GOOGLE_CLIENT_ID = "422109509936-kp0p3c84jaoe215fa9lvs8plm00mjm11.apps.googleusercontent.com"
OAUTH2GOOGLE_CLIENT_SECRET = "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"

CLOUD_DB_URI = "google:MySQLLab://{DB_USER}:{DB_PASSWORD}@/{DB_NAME}?unix_socket=/cloudsql/{DB_CONNECTION}".format(
    DB_USER="appuser",
    DB_NAME="finaldb",
    DB_PASSWORD ="CPzMH-\ob9@C`A.r",
    DB_CONNECTION ="ucsc-183-final:us-west1:ucsc-183-final-db-1"
)
CLOUD_DB_POOL_SIZE=1
CLOUD_DB_MIGRATE = False
CLOUD_DB_FAKE_MIGRATE =False