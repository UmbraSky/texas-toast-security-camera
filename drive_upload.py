from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

def file_upload(file):
	upload_file_list = [file]
	for upload_file in upload_file_list:
		gfile = drive.CreateFile({'parents': [{'id': '1zrRvrvKqUECI5qbNQHGbJNUXOjS1z5p7'}]})
		# Read file and set it as the content of this instance.
		gfile.SetContentFile(upload_file)
		gfile.Upload() # Upload the file.