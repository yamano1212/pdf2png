import subprocess
import time
from glob import glob

pdf_paths = "/Volumes/noname/1984/"
converted_paths = "/Volumes/noname/converted/1984/"

def main():
    #files = Path(IMAGE_PATH + "/origin/").glob("*")
    for month in range(6,13):
        re_month = str(month).zfill(2)
        files = glob(pdf_paths+re_month+"/*")
        l_f = len(files)
        procs = []
        N = 20  # メモリ不足にならないようにNを適切に設定する必要がある
        print(time.time())
        for i,f in enumerate(files):
            proc = subprocess.Popen(["python", "pdf2png.py", str(f), str(re_month)])
            procs.append(proc)
            print(i)

            if len(procs) == N:
                # メモリ不足で実行に失敗するので、
                # 子プロセスの数がNになったら、一旦全ての子プロセスの終了を待つ
                for proc in procs:
                    proc.communicate()
                procs.clear()

        for proc in procs:
            proc.communicate()
        print(time.time())
    end = time.time()
    print("Finished in {} seconds.".format(end-start))

if __name__ == "__main__":
    main()
    #run_multiconvert()
