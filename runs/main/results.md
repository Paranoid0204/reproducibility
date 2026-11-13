| condition | rep | decision | llm | tools | snap | tok_in | tok_out | latency_s | grounding |
|---|---|---|---|---|---|---|---|---|---|
| baseline | 1 | Overweight | 11 | 10 | 1 | 89254 | 44592 | 297 | 11/11 |
| baseline | 2 | Overweight | 13 | 10 | 1 | 108607 | 51682 | 338 | 20/20 |
| baseline | 3 | Hold | 13 | 11 | 1 | 101758 | 54225 | 355 | 10/10 |
| baseline | 4 | Overweight | 12 | 11 | 1 | 126207 | 43831 | 261 | 15/15 |
| baseline | 5 | Underweight | 11 | 10 | 1 | 100432 | 51644 | 316 | 9/9 |
| baseline | 6 | Hold | 13 | 10 | 1 | 93950 | 41609 | 259 | 8/12 |
| baseline | 7 | Overweight | 12 | 14 | 1 | 132529 | 56586 | 354 | 16/16 |
| baseline | 8 | Hold | 11 | 11 | 1 | 94371 | 46971 | 301 | 8/8 |
| baseline | 9 | Hold | 12 | 10 | 1 | 89759 | 51830 | 331 | 8/8 |
| low_tool_budget | 1 | Overweight | 12 | 10 | 1 | 100168 | 43240 | 293 | 8/8 |
| low_tool_budget | 2 | Overweight | 11 | 11 | 1 | 103435 | 55281 | 362 | 8/8 |
| low_tool_budget | 3 | Underweight | 14 | 9 | 1 | 110632 | 48537 | 324 | 16/16 |
| one_round | 1 | Hold | 11 | 2 | 1 | 87818 | 42667 | 270 | 9/9 |
| one_round | 2 | Hold | 10 | 2 | 1 | 72292 | 57303 | 356 | 8/8 |
| one_round | 3 | Hold | 11 | 2 | 1 | 71855 | 43132 | 262 | 18/18 |

| condition | n | decisions | tool_calls | tokens_in | tokens_out | latency_s | grounding |
|---|---|---|---|---|---|---|---|
| baseline | 9 | Overweight, Overweight, Hold, Overweight, Underweight, Hold, Overweight, Hold, Hold | 10.8 ± 1.3 | 104096 ± 15652 | 49219 ± 5142 | 313 ± 36 | 0.963 ± 0.111 |
| low_tool_budget | 3 | Overweight, Overweight, Underweight | 10.0 ± 1.0 | 104745 ± 5354 | 49019 ± 6035 | 326 ± 35 | 1.000 ± 0.000 |
| one_round | 3 | Hold, Hold, Hold | 2.0 ± 0.0 | 77322 ± 9093 | 47701 ± 8319 | 296 ± 52 | 1.000 ± 0.000 |
