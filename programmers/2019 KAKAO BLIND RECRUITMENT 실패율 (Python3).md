문제 링크

https://programmers.co.kr/learn/courses/30/lessons/42889


코딩테스트 연습 - 실패율
실패율 슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다. 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다. 이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다. 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오렐리를 위해 실패율을 구하는 코드를 완성하라. 실패율은 다음과 같이 정의한다. 스테이지에 도달했으나 아직 클리어하...


----


python3 문제풀이

```
def solution(N, stages):
    answer = []
    l = {}
    n = len(stages)
    for i in range(1,N+1):
        a = 0
        for j in stages:
            if i == j:
                a += 1
        if n != 0:
            l[i] = a / n
            n = n-a
        else:
            l[i] = 0

    for i in sorted(l.items(), reverse=True, key = lambda item: item[1]):
        answer.append(i[0])
    return answer
```


설명

stages list에 해당 수가 적혀있다는 것은 그 스테이지를 통과하지 못했다는 의미이다.

따라서 이중 for문을 이용해 수가 같을 때마다 수를 더해주고 더해진 결과를 스테이지에 도달한 수로 나누어 주고 실패율을 해당 스테이지에 할당해준다.

도달한 유저가 없는 경우는 0을 할당하게 만들어준다.

그 뒤에 sorted를 이용해 dict의 value를 내림차순으로 정렬해 key값을 list로 반환해주었다.

----

​

다른사람의 풀이

```
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
  ```
result는 dictionary이므로 sorted에 result를 그냥 넘기면 result의 keys가 들어간다. 

keys는 생략이 가능하다고 한다. 이 부분의 과정을 줄일 수 있었다. 

그리고 count를 이용해 비교하는 과정을 없애주었다.

​
----

생각 못 한 2가지가 아쉽다. 문제를 풀 때 함수를 더 생각해 볼 것.
