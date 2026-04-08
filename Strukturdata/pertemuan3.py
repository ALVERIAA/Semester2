import sys
#membuat struktur Tuple 
logApps  = ("user1 login","user2 login") 
print  (logApps)
print ("ukurannya =", sys.getsizeof(logApps))

#membuktikan memory Tuple lebih efisien dari list 
logAppsList = ["user1 login","user2 login"]
print(logAppsList)
print("ukurannya =", sys.getsizeof(logAppsList))

#logsapps.append("user3 login") #error karena tuple tidak bisa diubah
#logsapps [0] = "user1 logout" #error karena tuple tidak bisa diubah
#logsapps.remove("user1 login") #error karena tuple tidak bisa diubah


#menduplikat Tuple
logAppsBackup = logApps
print ("ini isi logsApps Backup =", logApps)
print ("ini isi logsApps =", logApps)

#pembuktian bahwa tuple bisa di akses dengan index
print(logApps[0])
print(logApps[-1])

#slice dan copy
print(logApps[0:1])
backup_logApps = logApps[:]
print(backup_logApps)

usr1, usr2 = logApps
print(usr1)
print(usr2)