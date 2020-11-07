import os
import sys
import glob
import zipfile


def unzip(zipname): #指定されたzipファイルを解凍する
    with zipfile.ZipFile(zipname, "r") as zipf:
        for info in zipf.infolist():
            info.filename = info.filename.encode("cp437").decode("cp932") #日本語のファイルを解凍すると文字化けするためcp437をshift-jisに変換
            zipf.extract(info, path=os.path.dirname(zipname))
    del_zip(zipname)


def del_zip(zipfile): #unzip関数で解凍し終わったzipファイルを削除
    os.remove(zipfile)


def unzip_dir(dir_path): #ディレクトリ内のすべてのzipファイルを解凍
    for filename in glob.glob(os.path.join(dir_path, "*.zip")):
        unzip(zipname=os.path.join(dir_path,filename))


def main():
    args = sys.argv
    try:
        if os.path.isdir(args[1]):
            unzip_dir(args[1])
        else:
            unzip(os.path.join(args[1]))
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()