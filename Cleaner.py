import os

def CreateFolderIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def Move(foldernName,files):
    for file in files:
        os.replace(file,f"{foldernName}/{file}")

os.listdir()
CreateFolderIfNotExist('Images')
CreateFolderIfNotExist('Documents')
CreateFolderIfNotExist('Media')
CreateFolderIfNotExist('Others')

files=os.listdir()
files.remove('Cleaner.py')

imgExts=['.jpg','.jpeg','png','.gif','.bmp']
Images=[file for file in files if os.path.splitext(file)[1].lower() in imgExts]

DocExts=['.txt','.docx','.rar','.pdf','.py']
Docs=[file for file in files if os.path.splitext(file)[1].lower() in DocExts]

MediaExts=['.mp4','.mp3','.mkv']
Media=[file for file in files if os.path.splitext(file)[1].lower() in MediaExts]

others=[]
for file in files:
    ext=os.path.splitext(file)[1].lower()
    if (ext not in imgExts) and (ext not in DocExts) and (ext not in MediaExts) and os.path.isfile(file):
        others.append(file)
        
Move('Images',Images)
Move('Documents',Docs)
Move('Media',Media)
Move('Others',others)