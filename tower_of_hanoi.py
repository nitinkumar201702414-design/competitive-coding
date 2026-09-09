class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        # code here
        if n == 0:
            return 0
            
        # Step 1: Move top n-1 disks from source to auxiliary rod
        moves = self.towerOfHanoi(n - 1, fromm, aux, to)
        
        # Step 2: Move the nth disk from source to target rod
        print(f"move disk {n} from rod {fromm} to rod {to}")
        moves += 1
        
        # Step 3: Move the n-1 disks from auxiliary to target rod
        moves += self.towerOfHanoi(n - 1, aux, to, fromm)
        
        return moves

result=Solution()
print(result.towerOfHanoi(5, 1, 3, 2))