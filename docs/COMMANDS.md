# 📚 命令文档

## 用户命令

### 基础命令

| 命令 | 说明 | 示例 |
|------|------|------|
| `/start` | 启动机器人 | `/start` |
| `/help` | 显示帮助 | `/help` |
| `/me` | 查看个人资料 | `/me` |

### 竞赛命令

| 命令 | 说明 | 参数 |
|------|------|------|
| `/competitions` | 列出所有竞赛 | 无 |
| `/join_comp <id>` | 加入竞赛 | 竞赛ID |
| `/leave_comp <id>` | 离开竞赛 | 竞赛ID |
| `/submit_flight` | 提交飞行记录 | 无 |
| `/comp_leaderboard <id>` | 竞赛排行榜 | 竞赛ID |

### 查询命令

| 命令 | 说明 |
|------|------|
| `/leaderboard` | 全球排行榜 |
| `/achievements` | 我的成就 |
| `/stats` | 个人统计 |
| `/my_airplanes` | 我的纸飞机 |

## 管理员命令

### 竞赛管理

| 命令 | 说明 | 参数 |
|------|------|------|
| `/admin` | 管理员菜单 | 无 |
| `/create_comp` | 创建竞赛 | 无 |
| `/end_comp <id>` | 结束竞赛 | 竞赛ID |
| `/reset_comp <id>` | 重置竞赛 | 竞赛ID |

### 用户管理

| 命令 | 说明 | 参数 |
|------|------|------|
| `/ban_user <user_id>` | 封禁用户 | 用户ID |
| `/unban_user <user_id>` | 解除封禁 | 用户ID |
| `/reset_user <user_id>` | 重置用户 | 用户ID |
| `/promote_user <user_id>` | 提升用户权限 | 用户ID |

### 系统管理

| 命令 | 说明 |
|------|------|
| `/broadcast <message>` | 广播消息给所有用户 |
| `/system_status` | 查看系统状态 |
| `/backup` | 手动备份数据 |
| `/restore` | 恢复数据 |

## 开发者命令

| 命令 | 说明 |
|------|------|
| `/debug` | 调试模式 |
| `/eval <code>` | 执行代码 (仅限超级管理员) |

## 命令示例

### 加入竞赛
```
/join_comp 1
```

### 提交飞行记录
```
/submit_flight
```
然后按照提示操作。

### 查看排行榜
```
/leaderboard
```

### 管理员创建竞赛
```
/create_comp
```
然后按照提示操作。
