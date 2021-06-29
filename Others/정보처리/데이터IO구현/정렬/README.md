# 정렬

1. 삽입정렬

- 순서화된 파일에 새로운 하나의 레코드를 순서에 맞게 정렬하는 방식
- 시간복잡도 : O(n^2)

  ![삽입정렬 위키](https://upload.wikimedia.org/wikipedia/commons/4/42/Insertion_sort.gif)
  출처:wikiPedia

2. 선택정렬

- 전체를 순회하여 순차적으로 최솟값 순서대로 레코드를 위치하는 방법
- 시간복잡도 : O(n^2)

  ![선택정렬 위키](https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif)
  출처:wikiPedia

3. 버블 정렬

- 인접 레코드와 비교하여 서로 비교하며 전체를 순회하는 정렬
- 시간복잡도 : O(n^2)

![버블 소트](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)
출처 : WikiPedia

4. 쉘 정렬

- 매개변수의 값으로 서브파일구성, 각 서브 파일을 삽입 정렬 방식으로 순서 배열을 반복하는 정렬반식
- 삽입정렬의 확장버전

![쉘 정렬](https://upload.wikimedia.org/wikipedia/commons/d/d8/Sorting_shellsort_anim.gif)
출처 : wikiPedia

5. 퀵 정렬

- 키를 기준으로 `작은값은 왼쪽`, `큰값은 오른쪽` 서브파일로 분해시키는 과정을 반복하는 정렬
- 시간 복잡도 : O(nlogn) 최악 : O(N^2)

  ![퀵정렬](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Sorting_quicksort_anim.gif/220px-Sorting_quicksort_anim.gif)
  출처 : 위키백과

6. 힙정렬

- 전이진 트리를 이용한 정렬
- `전이진 트리`를 `힙트리로 변환`하여 정렬
- 시간복잡도 : O(nlongn)

  ![힙정렬](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Sorting_heapsort_anim.gif/220px-Sorting_heapsort_anim.gif)
  출처 : 위키백과

7. 2-way 합병 정렬

- 이미 정렬되어있는 두 파일을 한개의 파일로 합병하는 정렬
- 시간복잡도 : O(nLogn)

  ![합병 정렬](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Merge-sort-example-300px.gif/220px-Merge-sort-example-300px.gif)
  출처 : 위키백과

8. 기수 정렬 (버킷 정렬)

- queue를 이용하여 자릿수 별로 정렬하는 방식
  ![버킷 1](https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Bucket_sort_1.svg/311px-Bucket_sort_1.svg.png)

  ![버킷 2](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Bucket_sort_2.svg/311px-Bucket_sort_2.svg.png)

  출처 : wikiPedia
