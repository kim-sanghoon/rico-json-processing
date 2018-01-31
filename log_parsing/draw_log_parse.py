import os

log = open("./draw_log.txt", "r")

for line in log:
    if len(line.split(":")) > 2 and (line.split(":")[1] == "WebView" or line.split(":")[1] == "google.android.gms.ads"):
        print(line)
        os.execvp("../delete.py", [line[0]])
