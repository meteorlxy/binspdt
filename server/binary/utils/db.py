from django.conf import settings
from binary.core.utils import Database

db = Database({
  'IDA': settings.IDA,
  'POSTGRES': settings.DATABASES['binary_db'],
})
