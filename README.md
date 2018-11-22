# HiSchool(하이, 스쿨!)

## 기본 설정 

### Play 생성

#### 이름
`HiSchool`

### 기본 응답 

#### 사용자가 Play에 진입시 안내 응답

- 
- 
- 

#### Play를 종료할 때의 응답	

- 
-
- 

#### 사용자가 Play에서 처리할 수 없는 발화를 한 경우	

-
-
-

## Task List

- **학교 식단 제공:** 어제/오늘/내일/모레
    - 언제? 어떤 학교? -> 검색
    - 알레르기 정보
- **학교 학사일정 제공:** 이번주/이번달/n달
- DB 연동으로 부가 서비스 제공: 기본 시간표, 준비물 등

1. `은여울중학교`, `내일`, `급식`
2. `내일`, `급식`
3. `급식`

## Docs

### hischool.meal

#### searchSchool
```py
searchSchool('은여울중학교')
```

| 이름        | 타입      | 설명        |
| :--------- | :------- | :--------- |
| `query`    | `string` | 검색할 학교 이름 및 키워드 |

```py
{'name': '은여울중학교', 'sccode': 'J100006779', 'address': '경기도 김포시 김포한강8로 173-48 (마산동)', 'type': '03', 'office': 'stu.goe.go.kr'}
```

| 타입      | 설명        |
| :------- | :--------- |
| `dict`   | 학교 정보가 반환됨 |

#### getMealTableURL
```py
result = searchSchool('은여울중학교')
getMealTableURL(result, 2, datetime.date.today())
```

| 이름           | 타입      | 설명        |
| :------------ | :------- | :--------- |
| `school_info` | `dict` | 검색할 학교 이름 및 키워드 |
| `meal_type`   | `int`  | 급식 종류(아침/조식: `1`, 점심/중식: `2`, 저녁/석식: `3`) |
| `query_date`  | `datetime.date` 또는 `yyyy.mm.dd` 형식의 `string` | 검색할 날짜 |

```text
http://stu.goe.go.kr/sts_sci_md01_001.do?schulCode=J100006779&schulCrseScCode=3&schulKndScCode=03&schMmealScCode=2&schYmd=2018.11.23
```

| 타입      | 설명        |
| :------- | :--------- |
| `string` | 식단을 파싱할 NEIS URL |

#### getMeal
급식을 가져온다.
