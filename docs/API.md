# 🔌 API 文档

## 用户API

### 获取用户信息

```python
from services.user_service import user_service

user = user_service.get_user(user_id=123456)
```

### 创建用户

```python
user = user_service.create_user(
    user_id=123456,
    username="example",
    first_name="张",
    last_name="三"
)
```

### 添加积分

```python
user_service.add_score(user_id=123456, score=100)
```

### 封禁用户

```python
user_service.ban_user(user_id=123456)
```

## 竞赛API

### 创建竞赛

```python
from services.competition_service import competition_service

competition = competition_service.create_competition(
    name="2024年全国锦标赛",
    description="全国纸飞机竞赛",
    start_time=datetime.now(),
    end_time=datetime.now() + timedelta(days=30)
)
```

### 获取竞赛列表

```python
competitions = competition_service.get_all_competitions()
```

### 用户加入竞赛

```python
competition_service.join_competition(
    user_id=123456,
    competition_id=1
)
```

## 飞行记录API

### 提交飞行记录

```python
from services.flight_service import flight_service

flight = flight_service.submit_flight(
    user_id=123456,
    airplane_id=1,
    distance=25.5,
    accuracy=0.95,
    duration=3.2
)
```

### 获取飞行历史

```python
flights = flight_service.get_user_flights(user_id=123456)
```

## 分析API

### 获取AI分析

```python
from services.ai_service import ai_service

analysis = ai_service.analyze_flight(
    flight_id=1,
    detailed=True
)
```

### 获取优化建议

```python
suggestions = ai_service.get_optimization_suggestions(
    user_id=123456
)
```

## 排行榜API

### 获取全球排行榜

```python
from services.leaderboard_service import leaderboard_service

leaderboard = leaderboard_service.get_global_leaderboard(
    limit=10
)
```

### 获取用户排名

```python
rank = leaderboard_service.get_user_rank(user_id=123456)
```
