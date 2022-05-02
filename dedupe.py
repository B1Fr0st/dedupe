#dedupe.py
import hashlib as hash

def hash(hashString:str) -> str:
  return hashlib.sha256(hashString.encode("utf-8")).hexdigest()

def getFiles(dir,num=False,recursive=False,verbose=True):
    if recursive == False:
        string = f"Starting getFiles on target directory {dir}, with args num={num},recursive={recursive},verbose={verbose}"
        print("#"*len(string))
        print(string)
        print("#"*len(string))
    """
       dir=path to walk
       num=Whether to print the number of files found
       recursive=Whether the call is a recursive call by the function.
       verbose=Whether or not to print each file found.
    """
    
    #gets all of the files in a directory,including the ones in
    #subdirectories, and returns it in a list format.

    try:
        listOfFiles = os.listdir(dir)#locate all files including subdirs
    except PermissionError:
        print(f"Permission denied to {dir}","Warning")
        time.sleep(2)
        return []

    allFiles = []

    for entry in listOfFiles:

        path = os.path.join(dir,entry)#creates full path

        if os.path.isdir(path):#if the path is a directory
            print(f"Branching:{path}")
            allFiles = allFiles + getFiles(path,recursive=True)#recursively call getFiles
        else:
            if verbose == True:
                #print(f"File Located:{path}")
                pass
            allFiles.append(path)#adds the singular file to the list

    if num:
        print("Files Located:"+str(len(allFiles)))

    return allFiles



def dedupeDir(path:str):
  """Removes duplicate files from a given directory"""
