import os
filename = "databases.txt"
file = open(filename, "r")
cmd = 'mysqldump -uroot -proot {} > sql/{}.sql'
for line in file:
    schema = line.strip()
    singleCmd = cmd.format(schema, schema)
    print(singleCmd)
    os.system(singleCmd)

os.system('zip -r sql sql')