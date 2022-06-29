import boto3
s3 = boto3.resource('s3')
# Get list of objects for indexing
images=[('peoplepicture1.jpeg','Napoleon Bonaparte'),
       ('peoplepicture2.jpeg','Jone Smith'),
       ('peoplepicture3.jpeg','John Smith')]
# Iterate through list to upload objects to S3   
for image in images:
   file = open(image[0],'rb')
   object = s3.Object('shaunak2',image[0])
   ret = object.put(Body=file,
                   Metadata={'FullName':image[1]}
                   )
   print(image[0])
   print(image[1])

