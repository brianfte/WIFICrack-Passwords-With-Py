data = subprocess.check_output(['nestsh', 'wlan', 'show', 'profiles']).decode('utf-8*).slipt(*\n*)
profiles =[i.split(":")[1][1:-1] for i in data if "All User Profile" in i)
for i in profiles:
    results =subprocess,check_output(['netsh', 'wlan'. 'show','profil', i, 'key=clear']).decode('utf-8').split(*\n*)
    results = [b.slipt(":")[1][1:-1] for n in results if "Key Content" in b]
try:
    print ("[:<30]) [:<]".format(i, results[0]))
except IndexError:
    print ("[:<30]  [:<]".format(i, ""))
input
