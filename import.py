import json

class qmp_command:
    def __init__(self, execute, argument, id):
        self.execute = execute
        self.argument = argument
        self.id = id

def print_qmp(q):
    print("=== start print")
    print(q)
    print(f"execute: {q.execute} argument:{q.argument} id:{q.id}")
    print("=== end print")

obj = qmp_command("qmp", ["kakaka"], 20)  #objeto original

json_command = json.dumps(obj.__dict__)

qmp_dict = json.loads(json_command)
print(f"Dictionary from json: {qmp_dict}")

print_qmp(obj)
print(f"json string: {json_command}") #print del objeto original

new_qmp_obj = qmp_command(**qmp_dict)



print_qmp(new_qmp_obj) #print qmp_dict de vuelta a qmp_command obj
