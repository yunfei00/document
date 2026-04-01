# CST 导入数据 XML（EmissionScan）归档建议

## 建议归档位置
- 主文档建议放在：`04_Knowledge/software_instructions/cst_emission_scan_xml.md`
- 示例原始文件建议放在：`06_Assets/cst/emission_scan/`（例如 `ex.xml`、`ex.dat`）

这样做的原因：
1. `04_Knowledge` 用于沉淀可复用的工程结论；CST 导入格式属于“可复用知识”。
2. `software_instructions` 已用于存放具体软件工具的操作说明，和 CST 使用场景一致。
3. 大文件/样例文件放 `06_Assets`，知识文档与附件分离，便于检索与版本管理。


## 已保存样例
- 当前 XML 已保存到：`06_Assets/cst/emission_scan/ex.xml`

## 建议文档结构（可直接套用）
1. 这个 XML 能解决什么问题
2. 最小可用样例（你当前这份 `EmissionScan`）
3. 字段说明（`Nfs_ver`、`Probe/Field`、`Frequencies/List`、`Measurement/*`）
4. 与 `*.dat` 文件的对应关系
5. 常见导入失败排查（编码、路径、单位、格式）
6. 在你项目中的实际用法
