import os

log = open("./draw_log.txt", "r")
delete_log = open("./del_log.txt", "w")

for line in log:
    if len(line.split(":")) > 2 and (line.split(":")[1] == "WebView" or line.split(":")[1] == "google.android.gms.ads"):
        print(line)
        delete_log.write(line)
        os.system("./delete.py " + line.split(":")[0].split(".")[0])
