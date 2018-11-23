# 누구의 소리 (NUGU-Sound)
[NUGU Play 개발 및 아이디어 공모전](http://www.nugu.co.kr/web/whatsnew/view/2021) 출품작

## 기본 설정 

### Play 생성

#### 이름
- `누구의 소리`

### 기본 응답 

- 사용자가 Play에 진입시 안내 응답: `안녕하세요! 누구의 소리입니다. 무엇을 도와드릴까요?`

- Play를 종료할 때의 응답: `누구의 소리를 종료할게요!`

- 사용자가 Play에서 처리할 수 없는 발화를 한 경우: `죄송해요. 제가 처리할 수 없는 요청이에요. 누구의 소리를 종료할게요.`

- 외부 연동 실패 시: `지금은 서버에 연결할 수 없어요. 잠시 후에 다시 이용해 주세요!`

## Custom Actions

### getSchool

#### Intent

- **은여울중학교** 소리
- 은여울중학교 소리 들려줘

> `은여울중학교`: SCHOOLNAME

#### Output
`{{scmeal}} {{scschedule}}`

### getMeal

#### Intent

- **오늘 은여울중학교 점심** 소리
- 오늘 은여울중학교 점심 소리 들려줘
- 오늘 은여울중학교 점심 뭐야
- 오늘 은여울중학교 점심 뭐냐
- 오늘 은여울중학교 점심 말해줘
- 오늘 은여울중학교 점심 알려줘

> `오늘`: BID_DT_DAY
> `은여울중학교`: SCHOOLNAME
> `점심`: BID_TI_DURATION

#### Output
`{{meal}}`

### getSchedule

#### Intent

- **은여울중학교 11월**
- 은여울중학교 11월 소리
- 은여울중학교 11월 소리 들려줘
- 은여울중학교 11월 일정
- 은여울중학교 11월 일정 뭐야
- 은여울중학교 11월 일정 말해줘
- 은여울중학교 11월 학사일정 들려줘

> `은여울중학교`: SCHOOLNAME
> `1월`: BID_DT_YMONTH

#### Output
`{{schedule}}`

### getKorQuote

#### Intent

- 할아버지
- 할아버지의 소리
- 할아버지 소리 들려줘
- 할아버지의 소리 들려줘
- 오늘의 명언
- 명언 한마디
- 명언 말해봐
- 명언 말해줘
- 명언 알려줘
- 명언 알려줄래?

#### Output
`{{quote}} - {{author}}`

### getEngQuote

#### Intent

- 영어명언 말해줘
- 영어띵언 말해봐
- 영어명언 들려줘
- 영어띵언 들려줘
- 영어로 명언 들려줘
- 영어로 할아버지의 소리 들려줘

#### Output
`{{en-quote}} - {{en-author}}`

## Backend proxy API

### health
`/health` returns status code `200` with `OK`

### getSchool

```json
{
    "version": "2.0",
    "action": {
        "actionName": "getSchool",
        "parameters": {
            "scname": {
                "type": "SCHOOL_NAME",
                "value": "은여울중학교"
            }
        }
    },
}
```

| 이름         | 타입      | 설명        |
| :---------- | :------- | :--------- |
| `scname`     | `SCHOOL_NAME` | 검색할 학교 이름 및 키워드 |

```json
{
    "version": "2.0",
    "resultCode": "OK",
    "output": {
        "scmeal": "2018년 11월 23일의 점심은 귤, 기장밥, 근대된장국(중), 안동찜닭(중), 도라지진미채볶음(중), 깍두기입니다.",
        "scschedule": "오늘의 학사일정이 없습니다."
    }
}
```

### getMeal

```json
{
    "version": "2.0",
    "action": {
        "actionName": "getMeal",
        "parameters": {
            "query": {
                "type": "SCHOOL_NAME",
                "value": "은여울중학교"
            },
            "meal_type": {
                "type": "BID_TI_DURATION",
                "value": "점심"
            },
            "days": {
                "type": "BIT_DT_DAY",
                "value": "TODAY"
            }
        }
    },
}
```

| 이름         | 타입      | 설명        |
| :---------- | :------- | :--------- |
| `query`     | `SCHOOL_NAME` | 검색할 학교 이름 및 키워드 |
| `meal_type` | `BID_TI_DURATION`    | 급식 종류(아침, 점심, 저녁) |
| `days`      | `BID_DT_DAY`    | 조회할 상대적 날짜(그끄제, 그제, 어제, 오늘, 내일, 모레, 글피) |

```json
{
    "version": "2.0",
    "resultCode": "OK",
    "output": {
        "meal": "기장밥\n근대된장국(중)\n안동찜닭(중)\n도라지진미채볶음(중)\n메론(중)\n깍두기"
    }
}
```

### getSchedule

```json
{
    "version": "2.0",
    "action": {
        "actionName": "getSchedule",
        "parameters": {
            "name": {
                "type": "SCHOOL_NAME",
                "value": "은여울중학교"
            },
            "month": {
                "type": "BID_DT_YMONTH",
                "value": "11월"
            }
        }
    },
}
```

| 이름     | 타입             | 설명        |
| :------ | :-------------- | :--------- |
| `name`  | `SCHOOL_NAME`   | 검색할 학교 이름 및 키워드 |
| `month` | `BID_DT_YMONTH` | 학사일정을 조회할 달 |

### getKorQuote

```json
{
    "version": "2.0",
    "action": {
        "actionName": "getKorQuote",
        "parameters": {}
    },
}
```

```json
{
    "version": "2.0",
    "resultCode": "OK",
    "output": {
        "quote": "나는 내 인생의 나머지 부분을 위해 내 경력을 연기 할 수 있다면 좋겠다.",
        "author": "클로이 모렐츠"
    }
}
```

### getEngQuote

```json
{
    "version": "2.0",
    "action": {
        "actionName": "getEngQuote",
        "parameters": {}
    },
}
```

```json
{
    "version": "2.0",
    "resultCode": "OK",
    "output": {
        "en-quote": "The words that a father speaks to his children in the privacy of home are not heard by the world, but, as in whispering galleries, they are clearly heard at the end, and by posterity.",
        "en-author": "Jean Paul"
    }
}
```

## Functions

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

> **참고:** 새로운 데이터는 DB에 `query:school_info`로 저장되고, 함수는 파싱 전 먼저 DB를 서칭한다.

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

#### parseMeal
급식을 가져온다.

```py
parseMeal('은여울중학교', 2, 0) # 은여울중학교, 점심(2), 오늘로부터 0일 데이터
```

| 이름         | 타입      | 설명        |
| :---------- | :------- | :--------- |
| `query`     | `string` | 검색할 학교 이름 및 키워드 |
| `meal_type` | `int`    | 급식 종류(아침/조식: `1`, 점심/중식: `2`, 저녁/석식: `3`) |
| `days`      | `int`    | 오늘로부터 조회할 날짜까지의 날 수 |

```py
['기장밥', '근대된장국(중)', '안동찜닭(중)', '도라지진미채볶음(중)', '메론(중)', '깍두기']
```

| 타입    | 설명         |
| :----- | :---------- |
| `list` | 식단의 각 메뉴 |

## 코드 인용 및 참고
> 인용 및 참고한 위치에 주석으로 라이선스를 표기했습니다.

- https://github.com/junhoyeo/eunyeoul-chatbot-flask/
- https://github.com/w3bn00b/tanbang-cafeteria/
