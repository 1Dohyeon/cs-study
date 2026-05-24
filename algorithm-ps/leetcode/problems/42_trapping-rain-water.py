class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            # 더 낮은 벽이 있는 쪽을 이동시킴
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                # left_max - height[left]를 하면 차이만큼의 양수(고인 빗물)가 나오게 됨
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water