# Flask settings
FLASK_SERVER_NAME = "localhost:8888"
FLASK_DEBUG = True  # Do not use debug mode in production

# SQLAlchemy settings

# Online
# SQLALCHEMY_DATABASE_URI = "postgresql://pvmtdwmfpihoim:30f2b2fa77257fdd621507474862690ceb68a41da35ada6b132e91abf6d49745@ec2-3-211-37-117.compute-1.amazonaws.com:5432/dbonbcotvlhiqc"
# Local
SQLALCHEMY_DATABASE_URI = "postgresql://postgres@localhost:5432/tourvago"

# Track Modification
SQLALCHEMY_TRACK_MODIFICATIONS = False
