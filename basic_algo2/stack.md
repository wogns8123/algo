stack 선형구조

후입 선출의 구조 LIFO(Last in First Out)

삽입 - push / 삭제 - pop / 공백확인 - isEmpty / 반환 - peek

장점 1차원 배열을 사용해 구현할 경우 구현이 용이 

단점 스택의 크기 변경이 힘듬 

-> 동적 연결리스트를 이용해 구현하는 방법이 있음

-> 구현이 복잡하지만 메모리를 효율적으로 사용하는 장점

function call 

가장 마지막에 호출된 함수가 가장 먼저 실행, 완료하고 복귀하는 후입선출 구조이므로, 후입선출 구조의 스택을 이용하여 수행순서 관리 

함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임에 저장하여 시스템 스택에 삽입

함수의 실행이 끝나면 시스템 스택의 top원소를 삭제하고 프레임에 저장되어있던 복귀주소를 확인하고 복귀 

함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다. 

memoization  

이전에 계산한 값을 메모리에 저장해 매번 다시 계산하지 않도록 하여 전체적인 실행 속도를 빠르게 하는 기술 

- 동적 계획법의 핵심

DP Dynamic Programming - 동적 계획법

그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘

입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

재귀적 구조에 사용하는 것보다 반복적 구조로 dp로 구현한 것이 효율적이다

-> 재귀적 구조는 내부 호출 스택을 사용하는 오버헤드가 발생하기 때문

DFS - 깊이 우선 탐색  Depth First Search

BFS - 너비 우선 탐색 Breadth First Search

백트래킹(Back Tracking)

해를 찾는 도중에 막히면 되돌아가서 다시 해를 찾는 기법

백트래킹과 깊이우선탐색의 차이 

- 출발하는 경로가 해결책으로 이어질 것 같지않으면 더 이상 경로를 따라가지않음 -> 시도의 횟수를 줄임(가지치기)

- DFS는 모든 경로를 추적 / 백트래킹은 불필요한 경로X

퀵 정렬 : 주어진 배열을 두개로 분할하고 각각을 정렬

합병과 다른점 

1. 합병은 그냥 두 부분을 나누는 반면에  퀵 정렬은 분할할 때 기준 아이템을 중심으로 이보다 작은것은 왼쪽, 큰 것은 오른쪽 배치

2. 각 부분 정렬이 끝난 후 합병 정렬은 '합병'이란 후처리 작업이 필요하나, 퀵정렬은 필요하지않다.
