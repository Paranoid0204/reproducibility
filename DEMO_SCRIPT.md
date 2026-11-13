# 15 分钟录屏 — 操作卡

硬上限 15:00。下面每一段都写明**屏幕上放什么、手敲什么、说什么**。总时长 14:30，留 30 秒缓冲。

开录前打开三个窗口：

1. 终端，`cd ~/Documents/deepseek-harness/default-workspace/repro`
2. `REPORT.pdf` 或 `REPORT.md`，停在 §4
3. 浏览器里的 GitHub 仓库页

**语言**：报告是英文。如果课程要求英文口头表达，用每段方框里的英文念稿；否则用中文讲、把关键英文术语念出来即可。

---

## 0:00–1:30 开场（不用动屏幕，露脸说）

> 这是一份复现作业。我复现的是一套多智能体 LLM 交易框架 TradingAgents，十二万星。
> 我没有复现它的收益曲线——那要几百次调用和几个月数据。我复现的是它自己声称的一个能力：分析师报的每个价格和指标都经过数据核对。
> 结论先说：**数字完全复现，结论完全不复现。**

```
This is reproducibility work on TradingAgents, a multi-agent LLM trading
framework. I did not reproduce its return curve — that needs hundreds of calls.
I reproduced one claim it makes about itself: every price and indicator in the
analyst report is grounded in a verified snapshot.
Two findings up front: the numbers reproduce perfectly, the decision does not.
```

---

## 1:30–4:00 靶子在哪

**屏幕**：GitHub 上的 TradingAgents README，滚到 *Reproducibility* 一节（现场滚，比放截图可信）。

**手指**：念出这句
`"the market analyst grounds exact price and indicator claims in a verified data snapshot"`

> 这句话可以验证：拿到一份报告，把里面所有数字抽出来，自己从雅虎财经重算一遍去对。对得上就是真的。
> 指标叫 grounding accuracy = 对得上的条数 / 能判断归属的条数。

**别做的**：不要讲架构图、不要解释 bull/bear debate 的设计。观众只需要知道「有一个分析师、它给数字、我们查数字」。

---

## 4:00–6:00 怎么跑的

**终端敲**（10 秒）：

```bash
sed -n '1,20p' run_experiment.py
```

> 一个驱动脚本：固定住 provider、模型、temperature、分析师名单、股票、日期，每次运行把记忆日志隔离，所以重复运行之间互不影响。

**终端敲**（3 秒）：

```bash
grep -n "max_tool_rounds\|temperature\|memory_log_path" run_experiment.py | head
```

> 只改一个变量：max_tool_rounds，12、3、1 三档。其余全部钉死。

**说一句安全声明**：
> key 不在仓库里，在 .env，已经被 gitignore。

---

## 6:00–8:30 结果一：数字全部对得上

**终端敲**（2 秒，不花钱）：

```bash
cat runs/main/results.md
```

> 十八次运行、两只股票，一共 167 条可审计数字，167 条全对。

**然后放最关键的一段**（终端敲，或用 PDF 展示）：

```bash
grep -m1 "verified market snapshot" runs/demo/AAPL_2026-09-01_baseline_r99.report.md | fold -w 120 | head -6
```

> Open 316.98、high 327.30、low 314.73、close 325.13、volume 5316 万。
> 这是它报告里自己写的核对行，和雅虎财经逐位一致。
> 它还会在开头主动写一句「我用两个工具交叉核对，没有发现不一致」——这个动作我在日志里看到了。

```
167 auditable claims, 167 matches. The agent's verified row and Yahoo's row are
identical to the cent — open, high, low, close and volume.
```

**可选加一句**：顺手现场验一次真（约 3 秒，不烧 token）：

```bash
./.venv/bin/python analyze_grounding.py \
  --report runs/demo/AAPL_2026-09-01_baseline_r99.report.md \
  --ticker AAPL --start 2024-06-01 --end 2026-09-02 | head -8
```

---

## 8:30–10:30 结果二：结论完全不复现

**屏幕**：`REPORT.pdf` 第 4 页那张三行表（或 `cat runs/main/results.md | head -12`）。

> 同一只股票、同一天、同样配置、temperature 调到 0，跑了九次：
> 增持 4 次、持有 4 次、减持 1 次。
> 这不是 bug，它 README 自己承认 LLM 每次输出会变。但对使用者很危险——界面只显示一个评级，看起来像结论，其实是抽签。

```
Nine identical runs, three different ratings. The README predicts this, so the
finding confirms it: one run is one sample, not one decision.
```

**停顿两秒**，让这句话落地。这是全场最重要的一句。

---

## 10:30–12:30 我的改动，以及它为什么反直觉

**屏幕**：报告 §5 那张表。

> 我原本想证明「少给它工具能省钱」，12 轮改成 3 轮——完全没变化，因为它一次就把指标批量取完了，3 轮根本用不完。
> 压到 1 轮才绑住：工具调用从 10 次降到 2 次，输入 token 省 23%，但准确率一点没降，还是 100%。
> 为什么？因为核对表里本来就带着全部指标，另外那 8 次是又抄了一遍。
> 可是三次 1 轮的运行全部变成「持有」。**省钱对准确率免费，对结论不免费。**

```
Cutting the tool budget to one round saved 23% of input tokens with no loss of
accuracy — but every cheap run said Hold. Cheaper was not neutral.
```

---

## 12:30–14:00 能不能让结论稳定（这一段是加分项）

**屏幕**：报告 §6 那张四条路的表。

> 我试了四种办法：
> 一，锁 seed。实测 5 次里出 3 种答案，这个端点上 seed 收下了但不生效。
> 二，多跑几次投票。因为分布是双峰，投 1 次和投 31 次稳定率都在 50% 左右，钱白花。
> 三，把报告冻结住再决策一次。95% 稳定，成本只有完整流程的二十分之一。
> 四，干脆用固定公式算。100% 稳定，但那已经不是 AI 的判断了。

**现场敲**（2 秒、零成本）：

```bash
./.venv/bin/python deterministic_rating.py | head -8
```

> 同一份快照，永远同一个评级：score 3 → Buy。

```
Reproducible decisions are possible, but only by taking the decision out of the
sampler. Freeze the evidence: 95%. Use a fixed rule: 100%. Voting: no.
```

---

## 14:00–14:40 踩坑与收尾

**只讲两个坑**（别贪多）：

> 一，我第一版校验工具说准确率只有 21%，查下来是**工具错了**不是 AI 错了：它把「前一天的收盘价」算到了今天头上。后来发现十个坑里有五个是我自己的工具有 bug。
> 二，我把运行输出接到了 tail，结果五分钟的运行看起来像卡死，被我误杀了两次。

> 复现工作里，**出错的通常是你的量具，不是被测对象**。
> 三句话收尾：数字能复现、结论不能；想稳定就得离开采样器；剩下的是把每一步的代价算清楚。

---

## 录屏前检查清单

- [ ] **屏幕上不出现 `.env` 和任何 `sk-` 开头的字符串**（终端别执行 `cat TradingAgents/.env`）
- [ ] 终端字号 ≥ 16pt，缩放 100%，观众压缩后能看清
- [ ] 先试录 60 秒，确认麦克风、共享范围（只共享终端窗口，不共享整个桌面）
- [ ] `runs/main/results.md` 和 `REPORT.pdf` 提前打开，别在录像里找文件
- [ ] 计时：讲到 12:30 时如果已超过 13:30，跳过 §12:30 的现场命令，只讲结论
- [ ] 结尾停住，不要说「那就先这样」——直接停录

---

## 三条救命提醒

1. **不要在录像时真跑完整分析**（5 分钟、¥0.5、还可能卡）。用 `runs/demo/` 里已经跑好的结果讲。
2. **不要背稿**。照着上面每段的第一句话开头，剩下的自然说，卡住了就低头看这段的引文。
3. **超时优先砍 §1:30–4:00**（靶子介绍），那部分是报告里写着的，评委自己会看。**绝不能砍 §8:30–10:30**（三种评级）。
