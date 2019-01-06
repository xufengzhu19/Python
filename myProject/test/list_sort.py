class element(object):
    def __init__(self,id="",name=""):
        self.id=id
        self.name=name
    def __lt__(self, other): # override <操作符
        if self.id<other.id:
            return True
        return False

    def __str__(self): # override __str__
        return "id={0},name={1}".format(self.id,self.name)

def sort_by_attribute():
    list=[element(id="130",name="json"),
          element(id="01",name="jack"),element(id="120",name="tom")]
    list.sort()
    for item in list:
        print(item)

def list_sort_by_length():
    list=["delphi","Delphi","python","Python","c++","C++","c","C","golang","Golang"]
    list.sort(key=lambda ele:len(ele)) #按元素长度顺序升序排列
    print("升序:",list)

    list.sort(key=lambda ele:len(ele),reverse=True) #按降序排列
    print("降序:",list)

if __name__ == '__main__':
    # sort_by_attribute()
    list_sort_by_length()