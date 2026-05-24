# [5_LongestPalindrome.py](./5_LongestPalindromicSubstring.py) 코드 예시

## 1. 중심 확장법 (Expand Around Center)

### 예시

* **문자열**: `"babad"`
* **목표**: 가장 긴 팰린드롬 부분 문자열 찾기
* **특이사항**: 각 인덱스를 중심으로 **홀수 길이**와 **짝수 길이** 두 가지 케이스를 모두 체크함

### 중심 확장 예시 사례

#### **1단계: 홀수 길이 확장 (`i = 2`, 'b' 중심)**

* **중심점**: `s[2]`는 `"b"`

1. `left = 1(a)`, `right = 3(a)` 설정
2. `s[1] == s[3]` 이므로 **일치**. (현재: `"aba"`, 길이 3)
3. `max_length` 갱신 (1 → 3), `start = 1` 저장
4. `left = 0(b)`, `right = 4(d)` 확장 시도 → `s[0] != s[4]` 이므로 **중단**

#### **2단계: 짝수 길이 확장 (`i = 1`, 'a'와 'b' 사이 중심)**

* **중심점**: `s[1]`와 `s[2]` 사이

1. `left = 1(a)`, `right = 2(b)` 설정
2. `s[1] != s[2]` 이므로 즉시 **중단**. (확장 실패)

### 핵심 로직 상세 분석

#### **1. 왜 두 번 확장? (Odd & Even)**

팰린드롬은 중심이 되는 모양이 두 가지입니다.

* **홀수(Odd)**: `aba` 처럼 한 글자를 기준으로 양옆이 대칭인 경우
* **짝수(Even)**: `abba` 처럼 글자와 글자 사이를 기준으로 양옆이 대칭인 경우

> 코드는 `for`문 한 번 안에서 이 두 가지 가능성을 모두 조사합니다.

#### **2. 인덱스 범위 조건 (`left >= 0 and right < n`)**

* **`left >= 0`**: 왼쪽으로 확장하다가 문자열의 시작인 0번 인덱스에 도달하면 멈춰야 합니다.
* **`right < n`**: 오른쪽으로 확장하다가 문자열의 끝인 `n-1`번 인덱스를 넘어가면 안 됩니다. (`n`은 포함하지 않음)

#### **3. 최댓값 갱신 및 추출**

* `current_length = right - left + 1`: 현재 찾은 대칭 구간의 길이를 계산합니다.
* `start = left`: 가장 긴 구간을 찾았을 때, 그 구간이 시작되는 지점을 따로 기록해둡니다.

### Python 구현 (Expand Around Center)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_length = 0, 1
        n = len(s)

        if n < 2:
            return s

        for i in range(n):
            # 홀수 길이 팰린드롬 확장
            left, right = i - 1, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > max_length:
                    max_length = current_length
                    start = left
                left -= 1
                right += 1

            # 짝수 길이 팰린드롬 확장
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > max_length:
                    max_length = current_length
                    start = left
                left -= 1
                right += 1

        return s[start:start + max_length]

```

### 요약

| 단계 | 역할 | 비유 |
| --- | --- | --- |
| **`for i in range(n)`** | 중심점 이동 | 돋보기를 한 칸씩 옆으로 옮기기 |
| **`while ... s[left] == s[right]`** | 양방향 확장 | 거울 보듯 양옆 글자가 같은지 확인 |
| **`max_length = current_length`** | 최댓값 기록 | 더 긴 팰린드롬을 찾으면 장부에 업데이트 |
| **`s[start:start + max_length]`** | 최종 추출 | 기록된 장부를 보고 가장 긴 부분만 잘라내기 |

---

## 2. Dynamic Programming (동적 계획법) 방식

중심 확장법이 "밖으로 뻗어나가는" 방식이라면, DP는 **"작은 조각이 팰린드롬인지 확인하고, 그 결과를 이용해 더 큰 조각을 판별"** 하는 방식입니다.

### DP 테이블의 의미

* `dp[i][j]`: 문자열의 `i`번째부터 `j`번째까지가 팰린드롬이면 `True`, 아니면 `False`.

### 핵심 로직 상세 분석

#### **1. 기저 조건 (길이 1과 2)**

* **길이 1**: 자기 자신은 무조건 팰린드롬입니다. (`dp[i][i] = True`)
* **길이 2**: 양 끝 글자가 같으면 팰린드롬입니다. (`s[i] == s[j]`)

#### **2. 점진적 확장 (길이 3 이상)**

* `s[i:j]`가 팰린드롬이 되려면 두 가지 조건이 필요합니다.

1. **양 끝 글자가 같다**: `s[i] == s[j]`
2. **내부 알맹이가 팰린드롬이다**: `dp[i+1][j-1]`이 이미 `True`여야 함.

> "가운데가 이미 합격이면, 양 끝만 확인하면 된다"

### Python 구현 (Dynamic Programming)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]
        start, max_length = 0, 1

        # 1단계: 길이 1인 팰린드롬 초기화
        for i in range(n):
            dp[i][i] = True

        # 2단계: 길이를 2부터 n까지 늘려가며 확인
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1 # 끝 인덱스
                
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        # 내부 알맹이(i+1 ~ j-1)가 팰린드롬인지 확인
                        dp[i][j] = dp[i + 1][j - 1]

                    # 최댓값 갱신
                    if dp[i][j] and length > max_length:
                        max_length = length
                        start = i

        return s[start:start + max_length]

```

### DP 시뮬레이션 사례 (`s = "babad"`)

#### **1단계: 길이 1 채우기**

* `dp[0][0], dp[1][1], ... dp[4][4]` 모두 `True`. (b, a, b, a, d)

#### **2단계: 길이 2 확인**

* `dp[0][1]` (ba): `s[0]!=s[1]` → `False`
* `dp[1][2]` (ab): `s[1]!=s[2]` → `False`

#### **3단계: 길이 3 확인**

* `dp[0][2]` (bab):

1. `s[0] == s[2]` (b와 b) → **일치**
2. `dp[1][1]` (내부 'a') → **True**
3. 결론: `dp[0][2] = True`. (최대 길이 3 갱신)

### 요약 비교

| 단계 | 역할 | 비유 |
| --- | --- | --- |
| **`dp[i][i] = True`** | 최소 단위 초기화 | 한 글자는 무조건 대칭이라고 장부에 적기 |
| **`range(2, n + 1)`** | 길이 늘려가기 | 2글자, 3글자... 점점 큰 조각을 검사 |
| **`dp[i+1][j-1]`** | 장부 확인 | 이미 계산된 "안쪽 결과"를 재사용하기 |
| **`start = i`** | 위치 저장 | 가장 긴 팰린드롬의 시작점을 장부에 기록 |

팰린드롬 탐색은 이처럼 **중심 확장법(공간 절약)** 과 **DP(중복 계산 방지)** 두 가지 접근법을 상황에 맞게 선택하는 것이 중요합니다.