#배열이 회전 (이진탐색 사용해야함) ex =[1,2,3,4,5,6] 
#배열이 회전하고서도 회전 이전 배열에서의 첫번째 원소값을 찾아야함.
#오름차순 기준 배열이 회전하지않고 정렬된채로 유지. end > start (6 > 1)
#n번 회전했을떄 기준 [5,6,1,2,3,4] end < start (4<5)
#변하는 부분이 찾는값이라고 가정하면 위 배열에셔 6,1사이
#변하는 부분 왼쪽의 모든 원소 > 배열의 첫번째 원소 6 > 5
#변하는 부분의 오른쪽의 모든 원소 < 배열의 첫번째 원소 1 < 5
#mid를 시작0, 끝값 len(num-1)로 잡으면 0+5 // 2 = 2 ex[2]로 생각하면
#mid는 배열의 3번째값이 된다. 회전했을때 배열 [5,6,1,2,3,4]로 놓고보면
#mid는 배열의 첫번째 원소 5보다 작기때문에 1 < 5
#mid부분의 왼쪽에서 변하는 점을 찾아야한다.mid-1
#만약 mid > 첫번째 원소 일경우 mid의 오른쪽 부분에서 찾는다. mid+1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start , end = 0, len(nums)-1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:   #mid = 5면 end = 4가 되는 경우
                start = mid + 1     #찾아야 하는 범위를 mid의 우측이기 때문에
            else:                #nums[mid] <= nums[end]의 경우
                end = mid           #찾아야 하는 범위가 mid의 좌측이기때문에
        
        return nums[start]      #범위를 줄이고 줄이다보면 결국 num[start]값부분이 찾는값이 되기때문

