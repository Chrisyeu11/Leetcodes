#https://leetcode.com/problems/robot-collisions/?envType=daily-question&envId=2024-07-13
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # Combine positions, healths, and directions into a list of tuples
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        
        stack = []

        for pos, health, direction, index in robots:
            if direction == 'R':
                stack.append((pos, health, direction, index))
            else:
                while stack and stack[-1][2] == 'R' and health > 0:
                    last_pos, last_health, last_direction, last_index = stack.pop()
                    if last_health > health:
                        last_health -= 1
                        stack.append((last_pos, last_health, last_direction, last_index))
                        health = 0
                    elif last_health < health:
                        health -= 1
                    else:
                        health = 0

                if health > 0:
                    stack.append((pos, health, direction, index))
        
        result = sorted(stack, key=lambda x: x[3])
        return [health for _, health, _, _ in result]
