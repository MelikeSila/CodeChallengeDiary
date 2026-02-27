import random
class RandomizedSet:
    def __init__(self):
        self.ran_dict = {}
        self.ran_list = []

    def insert(self, val: int) -> bool:
        if val in  self.ran_dict:
            return False
        
        self.ran_dict[val] = len(self.ran_list)
        self.ran_list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in  self.ran_dict:
            
            i = self.ran_dict[val]
            
            self.ran_list[i] = self.ran_list[-1]
            self.ran_dict[self.ran_list[-1]] = i

            self.ran_list.pop()
            del self.ran_dict[val]

            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.ran_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()