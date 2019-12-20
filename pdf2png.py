from glob import glob
import os
import subprocess
import sys

pdf_paths = "/Volumes/noname/1984/"
converted_paths = "/Volumes/noname/converted/1984/"

def upload_name(month,f_name):
    basename = os.path.basename(f_name)
    f_n,ext = os.path.splitext(basename)
    upload_path = converted_paths + month + "/" + f_n + ".png"
    return upload_path

def convert_pdf(f,upload_f):
    try:

        res = subprocess.run(["convert","-density","300","-trim",f,upload_f],stdout=subprocess.PIPE)
    except Exception as e:
        print(e,"変換できません")

def main(f, re_month):
    upload_path = upload_name(re_month,f)
    #print(convert_name)
    convert_pdf(f,upload_path)
    #print(i)

if __name__ == "__main__":
    _, filename, re_month = sys.argv
    main(filename, re_month)
    #main()
