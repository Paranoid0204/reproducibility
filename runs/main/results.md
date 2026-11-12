| condition | rep | decision | llm | tools | snap | tok_in | tok_out | latency_s | grounding |
|---|---|---|---|---|---|---|---|---|---|
| baseline | 1 | Overweight | 11 | 10 | 1 | 89254 | 44592 | 297 | 11/11 |
| baseline | 2 | Overweight | 13 | 10 | 1 | 108607 | 51682 | 338 | 20/20 |
| baseline | 3 | Hold | 13 | 11 | 1 | 101758 | 54225 | 355 | 10/10 |
| low_tool_budget | 1 | Overweight | 12 | 10 | 1 | 100168 | 43240 | 293 | 8/8 |
| low_tool_budget | 2 | Overweight | 11 | 11 | 1 | 103435 | 55281 | 362 | 8/8 |
| low_tool_budget | 3 | Underweight | 14 | 9 | 1 | 110632 | 48537 | 324 | 16/16 |
| one_round | 1 | Hold | 11 | 2 | 1 | 87818 | 42667 | 270 | 9/9 |
| one_round | 2 | Hold | 10 | 2 | 1 | 72292 | 57303 | 356 | 8/8 |
| one_round | 3 | Hold | 11 | 2 | 1 | 71855 | 43132 | 262 | 18/18 |

| condition | n | decisions | tool_calls | tokens_in | tokens_out | latency_s | grounding |
|---|---|---|---|---|---|---|---|
| baseline | 3 | Overweight, Overweight, Hold | 10.3 ± 0.6 | 99873 ± 9813 | 50166 ± 4992 | 330 ± 30 | 1.000 ± 0.000 |
| low_tool_budget | 3 | Overweight, Overweight, Underweight | 10.0 ± 1.0 | 104745 ± 5354 | 49019 ± 6035 | 326 ± 35 | 1.000 ± 0.000 |
| one_round | 3 | Hold, Hold, Hold | 2.0 ± 0.0 | 77322 ± 9093 | 47701 ± 8319 | 296 ± 52 | 1.000 ± 0.000 |
