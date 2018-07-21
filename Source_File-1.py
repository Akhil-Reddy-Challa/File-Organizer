"""os.listdir(pwd).(USED IF U WANT TO LIST ALL FILES INCLUDING FOLDERS)"""
import os
import glob
import shutil,sys
def build(extension,file_name):
    if extension not in os.listdir(pwd):
        os.mkdir(extension)
    shutil.move(file_name,pwd+'\\'+extension)
type_of_files={"Audio":['.aif','.cda','.mid','.midi','.mp3','.mpa','.ogg','.wav','.wma','.wpl'],
"Compressed Files":['.7z','.arj','.deb','.pkg','.rar','.rpm','.tar.gz','.z','.zip'],
"Disc Files":['.bin','.dmg','.iso','.toast','.vcd'],
"DataBase Files":['.csv','.dat','.db','.dbf','.log','.mdb','.sav','.sql','.tar','.xml'],
"Executable's":['.apk','.bat','.bin','.cgi','.pl','.com','.exe','.gadget','.jar','.py','.wsf'],
"Images":['.ai','.bmp','.gif','.ico','.jpeg','.jpg','.png','.ps','.psd','.svg','.tif','.tiff'],
"Internet-Files":['.asp','.aspx','.cer','.cfm','.cgi','.pl','.css','.htm','.html','.js','.jsp','.part','.php','.py','.rss','.xhtml'],
"Presentation-Files":['.key','.odp','.pps','.ppt','.pptx'],
"Program's":['.c','.class','.cpp','.cs','.h','.java','.sh','.swift','.vb'],
"SpreadSheets":['.ods','.xlr','.xls','.xlsx'],
"SYSTEM-FILES":['.bak','.cab','.cfg','.cpl','.cur','.dll','.dmp','.drv','.icns','.ico','.ini','.lnk','.msi','.sys','.tmp'],
"Videos":['.3g2','.3gp','.avi','.flv','.h264','.m4v','.mkv','.mov','.mp4','.mpg','.mpeg','.rm','.swf','.vob','.wmv'],
"Text-Files":['.doc','.docx','.odt','.pdf','.rtf','.tex','.txt','.wks','.wps','.wpd'],
}
def get_folder_name(fname):
    extension=get(fname)
    d=type_of_files
    for key in d:
        li=d[key]
        if extension in li:
            return key
    return "OTHERS"
def get(s):##return extension by reversing and finding
    s=s[::-1]
    s=s[0:s.find('.')+1]
    s=s[::-1]
    return s
if __name__ == "__main__":
    pwd=os.getcwd()#GET PRESENT WORKING DIRECTORY
    li=glob.glob("*.*")#get all files(NOT FOLDERS)
    #print("No of files:",len(li),li)
    if len(li)>1:
        pwf=os.path.basename(sys.argv[0])#present_working_file_name
        li.remove(pwf)
        for fname in li:
            extension=get_folder_name(fname)
            build(extension,fname)
    else:
        print("Directory ("+pwd+")\nMight be sorted Already :)")
        input("\nPress Return Key to Exit..!")
