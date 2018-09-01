# Opening and Closing a file "appApiAndVersion.txt"
# for object name contentOfFile.

app_With_Version = []
Api_list = []
temp='0'

contentOfFile = open("appApiAndVersion.txt", "r")
lineDataInArray = contentOfFile.readlines()
# print("v1"<"v2")
for i in lineDataInArray:
    interMediat = i.rstrip().split(',')
    appName = interMediat[0].strip()
    apiName = interMediat[1].strip()
    version = interMediat[2].strip()
    if (apiName not in Api_list):
        Api_list.append(apiName)
        app_With_Version.append(appName+'-'+apiName+'0'+version)
    else:
        app_With_Version.append(appName+'-'+apiName+'0'+version)

for api in Api_list:
    for appLet in app_With_Version:
        if api in appLet:
            if temp > appLet.split('0v')[1]:
               pass
            else:
               temp = appLet.split('0v')[1]
            print(temp)
            print(api in appLet)
    print('yes '+ api)

contentOfFile.close()
# print(Api_list)
# print(app_With_Version)
