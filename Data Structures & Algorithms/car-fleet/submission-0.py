class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for pos, spd in zip(position, speed):
            cars.append((pos, spd))
        
        cars.sort(reverse=True)
        stack = []
        for car in cars:
            dist = target - car[0]
            time = dist / car[1]
            if len(stack) == 0:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
        
        return len(stack)