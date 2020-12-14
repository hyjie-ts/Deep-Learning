
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import datetime
import time
bucket_name = 'datat'
T = str(datetime.date.today())+str(time.strftime("%H:%M:%S"))
localfile = 'fire_result.avi'
access_key = 'tNaErRTqs6LvtIfCFjZlChw_dD7dTlKTEFR'
secret_key = 'jdF38Qv3DL6ljiFR4X7746fbZ1lGXLvkS'
fops = 'avthumb/mp4/s/640x360/vb/1.25m'
saveas_key = urlsafe_base64_encode(localfile)
fops = fops+'|saveas/'+saveas_key
policy={
  'persistentOps':fops,
#   'persistentPipeline':pipeline
 }
key = 'fire_result'+str(T)+'.avi'
print(key)
q = Auth(access_key, secret_key)
token = q.upload_token(bucket_name, key, 3600,policy)
ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)
