class Developer:
    def work(self):
        print("Developer is working")
    def attendmetting(self):
        print("Developer is attending meeting")
class JavaDeveloper(Developer):
    def work(self):
        print("java developer is working on java")
    def dojavaproject(self):
        print("Java developer is building a java project")
class PythonDeveloper(Developer):
    def work(self):
        print("python developer is working on python")
    def dopthonproject(self):
        print("python developer is building a python project")

dev=Developer()
dev.work()
dev.attendmetting()
javadev=JavaDeveloper()
javadev.work()
javadev.attendmetting()
javadev.dojavaproject()
pythondev=PythonDeveloper()
pythondev.work()
pythondev.attendmetting()
pythondev.dopthonproject()