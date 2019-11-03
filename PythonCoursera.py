#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from bokeh.plotting import figure, output_file, show


# In[ ]:


def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


# In[ ]:


links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}


# In[ ]:


#1 question
df_gdp = pd.read_csv(links["GDP"])
df_gdp.head()


# In[ ]:


# Type your code here
df_gdp.head()


# In[ ]:


df_unemp = pd.read_csv(links['unemployment'])
df_unemp.head()


# In[ ]:


df_unemp85 = df_unemp[df_unemp['unemployment'] > 8.5]
df_unemp85.head()


# In[ ]:


x = df_gdp['date']
x.head()


# In[ ]:


gdp_change = df_gdp['change-current'] # Create your dataframe with column change-current
gdp_change.head()


# In[ ]:



unemployment = df_unemp['unemployment'] # Create your dataframe with column unemployment
unemployment.head()


# In[ ]:


title = 'GDP and Unemployment Data'# Give your dashboard a string title


# In[ ]:


file_name = "index.html"


# In[ ]:


make_dashboard(x=x, gdp_change=gdp_change, unemployment= unemployment, title=title, file_name=file_name)


# In[ ]:


{
  "apikey": "k4ZXrJnOPTeM2h49SNTqBp40MPp7Ws_Ri5fmhuD5rhs3",
  "cos_hmac_keys": {
    "access_key_id": "8c535d2892d0458e95bff589ad94aee8",
    "secret_access_key": "6fc966504ab1a7d8c8ead7aa9ff3a5ac41ba2310154d78d8"
  },
  "endpoints": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
  "iam_apikey_description": "Auto-generated for key 8c535d28-92d0-458e-95bf-f589ad94aee8",
  "iam_apikey_name": "Service credentials-1",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/4cb756f3760742c7a1c1b7fc264872ed::serviceid:ServiceId-9f950db4-61a8-4216-88fd-4d0a24268dc7",
  "resource_instance_id": "crn:v1:bluemix:public:cloud-object-storage:global:a/4cb756f3760742c7a1c1b7fc264872ed:e18509af-7048-4dd9-9aa7-ad59e5dd1c85::"
}


# In[ ]:


endpoint =  "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints"


# In[ ]:


bucket_name = 'pythoncourseraarun'
#Your Bucket name


# In[ ]:


import boto3


# In[ ]:


#change the access key & secret keys
resource = boto3.resource(
    's3',
    aws_access_key_id = credentials["cos_hmac_keys"]["access_key"],
    aws_secret_access_key = credentials["cos_hmac_keys"]["secret_access_key"],
    endpoint_url = endpoint,
)


# In[ ]:


import os

directory = os.getcwd()
html_path = directory + "/" + file_name


# In[ ]:


f = open(html_path,'r')


# In[ ]:


resource.Bucket(name=bucket_name).put_object(Key='index.html', Body=f.read())


# In[ ]:


Params = {'Bucket':bucket_name ,'Key':'index.html'}


# In[ ]:


import sys
time = 7*24*60**2
client = boto3.client(
    's3',
    aws_access_key_id = credentials["cos_hmac_keys"]["access_key"],
    aws_secret_access_key = credentials["cos_hmac_keys"]["secret_access_key"],
    endpoint_url=endpoint,

)
url = client.generate_presigned_url('get_object',Params=Params,ExpiresIn=time)
print(url)


# In[ ]:





# In[ ]:




