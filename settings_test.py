SERVER_NAME='localhost'
SECRET = 'foobar'
SECRET_KEY = 'my-session-secret'
SQLALCHEMY_DATABASE_TEST_URI = 'postgresql://rtester:rtester@localhost/pybossa_test'
GOOGLE_CLIENT_ID = 'id'
GOOGLE_CLIENT_SECRET = 'secret'
TWITTER_CONSUMER_KEY='key'
TWITTER_CONSUMER_SECRET='secret'
FACEBOOK_APP_ID='id'
FACEBOOK_APP_SECRET='secret'
TERMSOFUSE = 'http://okfn.org/terms-of-use/'
DATAUSE = 'http://opendatacommons.org/licenses/by/'
ITSDANGEROUSKEY = 'its-dangerous-key'
LOGO = 'logo.png'
PORT=5001
MAIL_SERVER = 'localhost'
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_PORT = 25
MAIL_FAIL_SILENTLY = False
MAIL_DEFAULT_SENDER = 'PyBossa Support <info@pybossa.com>'
ANNOUNCEMENT = {'admin': 'Root Message', 'user': 'User Message', 'owner': 'Owner Message'}
LOCALES = ['en', 'es', 'fr']
ENFORCE_PRIVACY = False
REDIS_CACHE_ENABLED = False
REDIS_SENTINEL = [('localhost', 26379)]
REDIS_KEYPREFIX = 'pybossa_cache'
LOCALES = ['en', 'es', 'fr']
WTF_CSRF_ENABLED = False
TESTING = True
CSRF_ENABLED = False
MAIL_SERVER = 'localhost'
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_PORT = 25
MAIL_FAIL_SILENTLY = False
MAIL_DEFAULT_SENDER = 'PyBossa Support <info@pybossa.com>'
ALLOWED_EXTENSIONS = ['js', 'css', 'png', 'jpg', 'jpeg', 'gif', 'zip']
UPLOAD_FOLDER = '/tmp/'
UPLOAD_METHOD = 'local'
RACKSPACE_USERNAME = 'username'
RACKSPACE_API_KEY = 'apikey'
RACKSPACE_REGION = 'ORD'
FLICKR_API_KEY = 'apikey'
FLICKR_SHARED_SECRET = "secret"
LIMIT = 25
PER = 15 * 60
