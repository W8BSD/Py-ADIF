from ADIF_log import ADIF_log
import datetime
import os

# Create a new log...
log = ADIF_log('Py-ADIF Example')
entry = log.newEntry()

# New entry from K6BSD to WD1CKS
entry['OPERATOR'] = 'K6BSD'
entry['CALL'] = 'WD1CKS'
entry['QSO_DATE']=datetime.datetime.now().strftime('%Y%m%d')
entry['BAND']='20M'
entry['MODE']='PSK'
entry['SUBMODE']='PSK31'
entry['TIME_ON']=datetime.datetime.now().strftime('%H%M')

# Write to example.adif
f = open('example.adif', 'wt')
f.write(str(log))
f.close()

# Write to example.adx
f = open('example.adx', 'wt')
f.write(log.xml())
f.close()

# Read example.adif back...
newlog = ADIF_log('Py-ADIF Example', file='example.adif')
print newlog[0]['CALL'],' band: ',newlog[0]['BAND']

# Read example.adx back...
newlog = ADIF_log('Py-ADIF Example', file='example.adx')
print newlog[0]['CALL'],' band: ',newlog[0]['BAND']

# Clean up... nothing interesting here...
os.remove('example.adif')
os.remove('example.adx')
