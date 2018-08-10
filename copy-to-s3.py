import sys
from upload_class import UploadFile

param = sys.argv
if len(param) == 2:
    file = param[1]
    upload = UploadFile()
    upload.keyPath = 'script_sql'
    upload.upload('sql.zip')
else:
    print('Sintax: python copy-to-s3.py <filename>')