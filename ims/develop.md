# 开发详细过程说明


## 1. 项目权限细分

1. 细分原则
```
项目管理建议拆成 4 个维度：
1. 项目对象本身（项目资料/状态）
2. 项目成员与角色（成员增删、角色变更）
3. 项目流程与审批（立项/变更/归档等）
4. 项目资源授权（项目下镜像/组件/检测策略的绑定与权限）

一句话：“能不能看/改项目” 和 “能不能动成员” 和 “能不能审批” 必须分开。
```

2. 项目基础权限（Project Core）
```
这组决定用户对“项目”这个对象本身能做什么：

project.view：查看项目列表/详情
project.create：创建项目（从 project.manage 拆出来）
project.edit：编辑项目基础信息（名称、描述、计划上线时间等）
project.status.change：启用/禁用/归档（状态管理单独拆出来）
project.delete：删除项目（一般只给超管/系统管理员；多数企业直接禁用删除）
```

3. 项目成员与角色权限（Project Membership）

```
这组专门管“项目成员”，建议和项目本体权限彻底分离：
project.member.view：查看成员列表
project.member.add：添加成员
project.member.remove：移除成员
project.member.role.assign：变更成员在项目内的角色
project.member.invite（可选）：邀请/发起加入（如果你有邀请流程）
这块是企业里最敏感的权限之一：
能改成员 ≈ 能改项目的“控制权”，必须独立出来，不要和 project.edit 混在一起。
```

4. 项目审批与流程权限（Project Workflow）

你文档里项目创建是有审批流程的（创建项目→审批→通过）这一类能力要拆出来，不要落到“项目管理”一把梭：
```
project.apply.create：发起项目创建申请（如果你是“申请制”，而非直接创建）
project.apply.view：查看项目申请单/进度
project.apply.cancel：撤销申请
project.approve：审批项目创建/变更（审批人专属）
project.reject：驳回（通常和 approve 同组，但最好分开，便于审计）
project.flow.view（可选）：查看该项目绑定的流程配置（仅查看）
但“谁能审批某个项目”是项目域内权限，应该是 project.approve 这类。
```

# 5. 汇总说明
```
A. 项目核心
project.view
project.create
project.edit
project.status.change
project.delete

B. 成员管理
project.member.view
project.member.add
project.member.remove
project.member.role.assign

C. 项目流程

project.apply.create
project.apply.view
project.apply.cancel
project.approve

D. 资源与策略
project.resource.view
project.resource.bind
project.resource.change
project.detect_policy.view
project.detect_policy.edit
```

6. demo阶段，暂时只关注增删改查,成员管理和审批
```
project.view
project.create
project.edit
project.delete

project.member.view
project.member.add
project.member.remove
project.member.role.assign

project.approve
```