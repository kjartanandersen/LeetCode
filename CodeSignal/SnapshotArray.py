

from typing import List, Hashable

class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [0] * length
        self.snapDict = {}
        self.snapId = 0
        
        

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val
        

    def snap(self) -> int:
        self.snapDict[self.snapId] = self.arr.copy()
        self.snapId += 1
        return self.snapId - 1
        

    def get(self, index: int, snap_id: int) -> int:
        
        return self.snapDict[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
        



if __name__ == "__main__":

    # set the length to be 3
    snapshotArr =  SnapshotArray(3)         
    
    # Set array[0] = 5
    snapshotArr.set(0,5)                    

    # Take a snapshot, return snap_id = 0
    snapshotArr.snap()                      
    snapshotArr.set(0,6)

    # Get the value of array[0] with snap_id = 0, return 5
    print(f"Value of array[0] with snap_id 0: {snapshotArr.get(0,0)}") 
