from typing import Iterable


class str_rep:
    def __init__(self, list: list = []) -> None:
        self.__rep = {}
        self.__not_rep = {}
        self.__read(list) 

    def __read(self, list: list) -> None:
        for item in list:
            self.append(item)

    def append(self, __object) -> None:
        if __object in self.__rep:
            self.__rep[__object] += 1
        elif __object in self.__not_rep:
            self.__rep[__object] = 2
            self.__not_rep.pop(__object)
        else:
            self.__not_rep[__object] = 1

    def remove(self, __object) -> None:
        if __object in self.__rep:
            if self.__rep[__object] > 2:
                self.__rep[__object] -= 1
            else:
                self.__rep.pop(__object)
                self.__not_rep[__object] = 1
        else:
            self.__not_rep.pop(__object)
    
    def get_not_rep(self) -> dict:
        return list(self.__not_rep)

    def get_rep(self) -> dict:
        return self.__rep    

    def __len__(self) -> int:
        return len(self.__not_rep) + len(self.__rep)  

    def __iter__(self) -> Iterable[str]:
        return self.__repr__().__iter__() 

    def __repr__(self) -> dict:
        all = self.__not_rep.copy()
        all.update(self.__rep)
        return all   

    def __str__(self) -> str:
        return self.__repr__().__str__()

class str_file(str_rep):
    def __init__(self, path: str) -> None:
        self.__path = path
        self.read()
    
    def read(self) -> None:
        with open(self.__path, 'r+', encoding="utf8") as file:
            super().__init__(file.read().splitlines())