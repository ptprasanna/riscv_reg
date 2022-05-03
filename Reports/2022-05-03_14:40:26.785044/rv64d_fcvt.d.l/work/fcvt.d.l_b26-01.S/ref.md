
# Data Propagation Report

- **STAT1** : Number of instructions that hit unique coverpoints and update the signature.
- **STAT2** : Number of instructions that hit covepoints which are not unique but still update the signature
- **STAT3** : Number of instructions that hit a unique coverpoint but do not update signature
- **STAT4** : Number of multiple signature updates for the same coverpoint
- **STAT5** : Number of times the signature was overwritten

| Param                     | Value    |
|---------------------------|----------|
| XLEN                      | 64      |
| TEST_REGION               | [('0x80000390', '0x80000a10')]      |
| SIG_REGION                | [('0x80002410', '0x80002820', '130 dwords')]      |
| COV_LABELS                | fcvt.d.l_b26      |
| TEST_NAME                 | /home/riscv/RRF/Reports/2022-05-03_14:40:26.785044/rv64d_fcvt.d.l/work/fcvt.d.l_b26-01.S/ref.S    |
| Total Number of coverpoints| 133     |
| Total Coverpoints Hit     | 129      |
| Total Signature Updates   | 65      |
| STAT1                     | 65      |
| STAT2                     | 0      |
| STAT3                     | 0     |
| STAT4                     | 0     |
| STAT5                     | 0     |

## Details for STAT2:

```


```

## Details of STAT3

```


```

## Details of STAT4:

```

```

## Details of STAT5:



## Details of STAT1:

- The first column indicates the signature address and the data at that location in hexadecimal in the following format: 
  ```
  [Address]
  Data
  ```

- The second column captures all the coverpoints which have been captured by that particular signature location

- The third column captures all the insrtuctions since the time a coverpoint was
  hit to the point when a store to the signature was performed. Each line has
  the following format:
  ```
  [PC of instruction] : mnemonic
  ```
- The order in the table is based on the order of signatures occuring in the
  test. These need not necessarily be in increasing or decreasing order of the
  address in the signature region.

|s.no|            signature             |                                           coverpoints                                            |                                                                       code                                                                        |
|---:|----------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|   1|[0x80002418]<br>0x0000000000000000|- opcode : fcvt.d.l<br> - rs1 : x20<br> - rd : f19<br> - rs1_val == 0 and rm_val == 0  #nosat<br> |[0x800003b4]:fcvt.d.l fs3, s4, dyn<br> [0x800003b8]:csrrs a7, fflags, zero<br> [0x800003bc]:fsd fs3, 0(a5)<br> [0x800003c0]:sd a7, 8(a5)<br>       |
|   2|[0x80002428]<br>0x0000000000000001|- rs1 : x4<br> - rd : f22<br> - rs1_val == 9184267462870993263 and rm_val == 0  #nosat<br>        |[0x800003cc]:fcvt.d.l fs6, tp, dyn<br> [0x800003d0]:csrrs a7, fflags, zero<br> [0x800003d4]:fsd fs6, 16(a5)<br> [0x800003d8]:sd a7, 24(a5)<br>     |
|   3|[0x80002438]<br>0x0000000000000001|- rs1 : x16<br> - rd : f4<br> - rs1_val == 3035559518675506972 and rm_val == 0  #nosat<br>        |[0x800003f0]:fcvt.d.l ft4, a6, dyn<br> [0x800003f4]:csrrs s5, fflags, zero<br> [0x800003f8]:fsd ft4, 0(s3)<br> [0x800003fc]:sd s5, 8(s3)<br>       |
|   4|[0x80002448]<br>0x0000000000000001|- rs1 : x0<br> - rd : f6<br>                                                                      |[0x80000414]:fcvt.d.l ft6, zero, dyn<br> [0x80000418]:csrrs a7, fflags, zero<br> [0x8000041c]:fsd ft6, 0(a5)<br> [0x80000420]:sd a7, 8(a5)<br>     |
|   5|[0x80002458]<br>0x0000000000000001|- rs1 : x3<br> - rd : f16<br> - rs1_val == 878257878219487117 and rm_val == 0  #nosat<br>         |[0x8000042c]:fcvt.d.l fa6, gp, dyn<br> [0x80000430]:csrrs a7, fflags, zero<br> [0x80000434]:fsd fa6, 16(a5)<br> [0x80000438]:sd a7, 24(a5)<br>     |
|   6|[0x80002468]<br>0x0000000000000001|- rs1 : x23<br> - rd : f20<br> - rs1_val == 428092830716901554 and rm_val == 0  #nosat<br>        |[0x80000444]:fcvt.d.l fs4, s7, dyn<br> [0x80000448]:csrrs a7, fflags, zero<br> [0x8000044c]:fsd fs4, 32(a5)<br> [0x80000450]:sd a7, 40(a5)<br>     |
|   7|[0x80002478]<br>0x0000000000000001|- rs1 : x1<br> - rd : f26<br> - rs1_val == 156703057381110404 and rm_val == 0  #nosat<br>         |[0x8000045c]:fcvt.d.l fs10, ra, dyn<br> [0x80000460]:csrrs a7, fflags, zero<br> [0x80000464]:fsd fs10, 48(a5)<br> [0x80000468]:sd a7, 56(a5)<br>   |
|   8|[0x80002488]<br>0x0000000000000001|- rs1 : x21<br> - rd : f21<br> - rs1_val == 104291213792325832 and rm_val == 0  #nosat<br>        |[0x80000474]:fcvt.d.l fs5, s5, dyn<br> [0x80000478]:csrrs a7, fflags, zero<br> [0x8000047c]:fsd fs5, 64(a5)<br> [0x80000480]:sd a7, 72(a5)<br>     |
|   9|[0x80002498]<br>0x0000000000000001|- rs1 : x6<br> - rd : f13<br> - rs1_val == 59668294213987868 and rm_val == 0  #nosat<br>          |[0x8000048c]:fcvt.d.l fa3, t1, dyn<br> [0x80000490]:csrrs a7, fflags, zero<br> [0x80000494]:fsd fa3, 80(a5)<br> [0x80000498]:sd a7, 88(a5)<br>     |
|  10|[0x800024a8]<br>0x0000000000000001|- rs1 : x19<br> - rd : f10<br> - rs1_val == 24358691315317906 and rm_val == 0  #nosat<br>         |[0x800004a4]:fcvt.d.l fa0, s3, dyn<br> [0x800004a8]:csrrs a7, fflags, zero<br> [0x800004ac]:fsd fa0, 96(a5)<br> [0x800004b0]:sd a7, 104(a5)<br>    |
|  11|[0x800024b8]<br>0x0000000000000001|- rs1 : x15<br> - rd : f17<br> - rs1_val == 12147253371253868 and rm_val == 0  #nosat<br>         |[0x800004c8]:fcvt.d.l fa7, a5, dyn<br> [0x800004cc]:csrrs s5, fflags, zero<br> [0x800004d0]:fsd fa7, 0(s3)<br> [0x800004d4]:sd s5, 8(s3)<br>       |
|  12|[0x800024c8]<br>0x0000000000000001|- rs1 : x10<br> - rd : f5<br> - rs1_val == 7228908657904184 and rm_val == 0  #nosat<br>           |[0x800004ec]:fcvt.d.l ft5, a0, dyn<br> [0x800004f0]:csrrs a7, fflags, zero<br> [0x800004f4]:fsd ft5, 0(a5)<br> [0x800004f8]:sd a7, 8(a5)<br>       |
|  13|[0x800024d8]<br>0x0000000000000001|- rs1 : x29<br> - rd : f7<br> - rs1_val == 3454382579804098 and rm_val == 0  #nosat<br>           |[0x80000504]:fcvt.d.l ft7, t4, dyn<br> [0x80000508]:csrrs a7, fflags, zero<br> [0x8000050c]:fsd ft7, 16(a5)<br> [0x80000510]:sd a7, 24(a5)<br>     |
|  14|[0x800024e8]<br>0x0000000000000001|- rs1 : x13<br> - rd : f3<br> - rs1_val == 1449063015970349 and rm_val == 0  #nosat<br>           |[0x8000051c]:fcvt.d.l ft3, a3, dyn<br> [0x80000520]:csrrs a7, fflags, zero<br> [0x80000524]:fsd ft3, 32(a5)<br> [0x80000528]:sd a7, 40(a5)<br>     |
|  15|[0x800024f8]<br>0x0000000000000001|- rs1 : x26<br> - rd : f23<br> - rs1_val == 1064659746632576 and rm_val == 0  #nosat<br>          |[0x80000534]:fcvt.d.l fs7, s10, dyn<br> [0x80000538]:csrrs a7, fflags, zero<br> [0x8000053c]:fsd fs7, 48(a5)<br> [0x80000540]:sd a7, 56(a5)<br>    |
|  16|[0x80002508]<br>0x0000000000000001|- rs1 : x9<br> - rd : f25<br> - rs1_val == 477767642386861 and rm_val == 0  #nosat<br>            |[0x8000054c]:fcvt.d.l fs9, s1, dyn<br> [0x80000550]:csrrs a7, fflags, zero<br> [0x80000554]:fsd fs9, 64(a5)<br> [0x80000558]:sd a7, 72(a5)<br>     |
|  17|[0x80002518]<br>0x0000000000000001|- rs1 : x5<br> - rd : f15<br> - rs1_val == 194479587133174 and rm_val == 0  #nosat<br>            |[0x80000564]:fcvt.d.l fa5, t0, dyn<br> [0x80000568]:csrrs a7, fflags, zero<br> [0x8000056c]:fsd fa5, 80(a5)<br> [0x80000570]:sd a7, 88(a5)<br>     |
|  18|[0x80002528]<br>0x0000000000000001|- rs1 : x31<br> - rd : f27<br> - rs1_val == 132508745935081 and rm_val == 0  #nosat<br>           |[0x8000057c]:fcvt.d.l fs11, t6, dyn<br> [0x80000580]:csrrs a7, fflags, zero<br> [0x80000584]:fsd fs11, 96(a5)<br> [0x80000588]:sd a7, 104(a5)<br>  |
|  19|[0x80002538]<br>0x0000000000000001|- rs1 : x12<br> - rd : f2<br> - rs1_val == 45718214482007 and rm_val == 0  #nosat<br>             |[0x80000594]:fcvt.d.l ft2, a2, dyn<br> [0x80000598]:csrrs a7, fflags, zero<br> [0x8000059c]:fsd ft2, 112(a5)<br> [0x800005a0]:sd a7, 120(a5)<br>   |
|  20|[0x80002548]<br>0x0000000000000001|- rs1 : x11<br> - rd : f9<br> - rs1_val == 31117680965175 and rm_val == 0  #nosat<br>             |[0x800005ac]:fcvt.d.l fs1, a1, dyn<br> [0x800005b0]:csrrs a7, fflags, zero<br> [0x800005b4]:fsd fs1, 128(a5)<br> [0x800005b8]:sd a7, 136(a5)<br>   |
|  21|[0x80002558]<br>0x0000000000000001|- rs1 : x17<br> - rd : f0<br> - rs1_val == 10221399934292 and rm_val == 0  #nosat<br>             |[0x800005d0]:fcvt.d.l ft0, a7, dyn<br> [0x800005d4]:csrrs s5, fflags, zero<br> [0x800005d8]:fsd ft0, 0(s3)<br> [0x800005dc]:sd s5, 8(s3)<br>       |
|  22|[0x80002568]<br>0x0000000000000001|- rs1 : x25<br> - rd : f24<br> - rs1_val == 5032232323694 and rm_val == 0  #nosat<br>             |[0x800005f4]:fcvt.d.l fs8, s9, dyn<br> [0x800005f8]:csrrs a7, fflags, zero<br> [0x800005fc]:fsd fs8, 0(a5)<br> [0x80000600]:sd a7, 8(a5)<br>       |
|  23|[0x80002578]<br>0x0000000000000001|- rs1 : x2<br> - rd : f31<br> - rs1_val == 3524006078498 and rm_val == 0  #nosat<br>              |[0x8000060c]:fcvt.d.l ft11, sp, dyn<br> [0x80000610]:csrrs a7, fflags, zero<br> [0x80000614]:fsd ft11, 16(a5)<br> [0x80000618]:sd a7, 24(a5)<br>   |
|  24|[0x80002588]<br>0x0000000000000001|- rs1 : x28<br> - rd : f1<br> - rs1_val == 1168389695644 and rm_val == 0  #nosat<br>              |[0x80000624]:fcvt.d.l ft1, t3, dyn<br> [0x80000628]:csrrs a7, fflags, zero<br> [0x8000062c]:fsd ft1, 32(a5)<br> [0x80000630]:sd a7, 40(a5)<br>     |
|  25|[0x80002598]<br>0x0000000000000001|- rs1 : x30<br> - rd : f18<br> - rs1_val == 813522083007 and rm_val == 0  #nosat<br>              |[0x8000063c]:fcvt.d.l fs2, t5, dyn<br> [0x80000640]:csrrs a7, fflags, zero<br> [0x80000644]:fsd fs2, 48(a5)<br> [0x80000648]:sd a7, 56(a5)<br>     |
|  26|[0x800025a8]<br>0x0000000000000001|- rs1 : x14<br> - rd : f12<br> - rs1_val == 453482173015 and rm_val == 0  #nosat<br>              |[0x80000654]:fcvt.d.l fa2, a4, dyn<br> [0x80000658]:csrrs a7, fflags, zero<br> [0x8000065c]:fsd fa2, 64(a5)<br> [0x80000660]:sd a7, 72(a5)<br>     |
|  27|[0x800025b8]<br>0x0000000000000001|- rs1 : x24<br> - rd : f14<br> - rs1_val == 268160711063 and rm_val == 0  #nosat<br>              |[0x8000066c]:fcvt.d.l fa4, s8, dyn<br> [0x80000670]:csrrs a7, fflags, zero<br> [0x80000674]:fsd fa4, 80(a5)<br> [0x80000678]:sd a7, 88(a5)<br>     |
|  28|[0x800025c8]<br>0x0000000000000001|- rs1 : x7<br> - rd : f30<br> - rs1_val == 131206879410 and rm_val == 0  #nosat<br>               |[0x80000684]:fcvt.d.l ft10, t2, dyn<br> [0x80000688]:csrrs a7, fflags, zero<br> [0x8000068c]:fsd ft10, 96(a5)<br> [0x80000690]:sd a7, 104(a5)<br>  |
|  29|[0x800025d8]<br>0x0000000000000001|- rs1 : x18<br> - rd : f29<br> - rs1_val == 51102363774 and rm_val == 0  #nosat<br>               |[0x8000069c]:fcvt.d.l ft9, s2, dyn<br> [0x800006a0]:csrrs a7, fflags, zero<br> [0x800006a4]:fsd ft9, 112(a5)<br> [0x800006a8]:sd a7, 120(a5)<br>   |
|  30|[0x800025e8]<br>0x0000000000000001|- rs1 : x27<br> - rd : f28<br> - rs1_val == 22050244097 and rm_val == 0  #nosat<br>               |[0x800006b4]:fcvt.d.l ft8, s11, dyn<br> [0x800006b8]:csrrs a7, fflags, zero<br> [0x800006bc]:fsd ft8, 128(a5)<br> [0x800006c0]:sd a7, 136(a5)<br>  |
|  31|[0x800025f8]<br>0x0000000000000001|- rs1 : x8<br> - rd : f11<br> - rs1_val == 8607351303 and rm_val == 0  #nosat<br>                 |[0x800006cc]:fcvt.d.l fa1, fp, dyn<br> [0x800006d0]:csrrs a7, fflags, zero<br> [0x800006d4]:fsd fa1, 144(a5)<br> [0x800006d8]:sd a7, 152(a5)<br>   |
|  32|[0x80002608]<br>0x0000000000000001|- rs1 : x22<br> - rd : f8<br> - rs1_val == 6929185936 and rm_val == 0  #nosat<br>                 |[0x800006e4]:fcvt.d.l fs0, s6, dyn<br> [0x800006e8]:csrrs a7, fflags, zero<br> [0x800006ec]:fsd fs0, 160(a5)<br> [0x800006f0]:sd a7, 168(a5)<br>   |
|  33|[0x80002618]<br>0x0000000000000001|- rs1_val == 4035756470 and rm_val == 0  #nosat<br>                                               |[0x800006fc]:fcvt.d.l ft11, t6, dyn<br> [0x80000700]:csrrs a7, fflags, zero<br> [0x80000704]:fsd ft11, 176(a5)<br> [0x80000708]:sd a7, 184(a5)<br> |
|  34|[0x80002628]<br>0x0000000000000001|- rs1_val == 1587807073 and rm_val == 0  #nosat<br>                                               |[0x80000714]:fcvt.d.l ft11, t6, dyn<br> [0x80000718]:csrrs a7, fflags, zero<br> [0x8000071c]:fsd ft11, 192(a5)<br> [0x80000720]:sd a7, 200(a5)<br> |
|  35|[0x80002638]<br>0x0000000000000001|- rs1_val == 1027494066 and rm_val == 0  #nosat<br>                                               |[0x8000072c]:fcvt.d.l ft11, t6, dyn<br> [0x80000730]:csrrs a7, fflags, zero<br> [0x80000734]:fsd ft11, 208(a5)<br> [0x80000738]:sd a7, 216(a5)<br> |
|  36|[0x80002648]<br>0x0000000000000001|- rs1_val == 339827553 and rm_val == 0  #nosat<br>                                                |[0x80000744]:fcvt.d.l ft11, t6, dyn<br> [0x80000748]:csrrs a7, fflags, zero<br> [0x8000074c]:fsd ft11, 224(a5)<br> [0x80000750]:sd a7, 232(a5)<br> |
|  37|[0x80002658]<br>0x0000000000000001|- rs1_val == 231549045 and rm_val == 0  #nosat<br>                                                |[0x8000075c]:fcvt.d.l ft11, t6, dyn<br> [0x80000760]:csrrs a7, fflags, zero<br> [0x80000764]:fsd ft11, 240(a5)<br> [0x80000768]:sd a7, 248(a5)<br> |
|  38|[0x80002668]<br>0x0000000000000001|- rs1_val == 107790943 and rm_val == 0  #nosat<br>                                                |[0x80000774]:fcvt.d.l ft11, t6, dyn<br> [0x80000778]:csrrs a7, fflags, zero<br> [0x8000077c]:fsd ft11, 256(a5)<br> [0x80000780]:sd a7, 264(a5)<br> |
|  39|[0x80002678]<br>0x0000000000000001|- rs1_val == 45276376 and rm_val == 0  #nosat<br>                                                 |[0x8000078c]:fcvt.d.l ft11, t6, dyn<br> [0x80000790]:csrrs a7, fflags, zero<br> [0x80000794]:fsd ft11, 272(a5)<br> [0x80000798]:sd a7, 280(a5)<br> |
|  40|[0x80002688]<br>0x0000000000000001|- rs1_val == 32105925 and rm_val == 0  #nosat<br>                                                 |[0x800007a4]:fcvt.d.l ft11, t6, dyn<br> [0x800007a8]:csrrs a7, fflags, zero<br> [0x800007ac]:fsd ft11, 288(a5)<br> [0x800007b0]:sd a7, 296(a5)<br> |
|  41|[0x80002698]<br>0x0000000000000001|- rs1_val == 12789625 and rm_val == 0  #nosat<br>                                                 |[0x800007bc]:fcvt.d.l ft11, t6, dyn<br> [0x800007c0]:csrrs a7, fflags, zero<br> [0x800007c4]:fsd ft11, 304(a5)<br> [0x800007c8]:sd a7, 312(a5)<br> |
|  42|[0x800026a8]<br>0x0000000000000001|- rs1_val == 6573466 and rm_val == 0  #nosat<br>                                                  |[0x800007d4]:fcvt.d.l ft11, t6, dyn<br> [0x800007d8]:csrrs a7, fflags, zero<br> [0x800007dc]:fsd ft11, 320(a5)<br> [0x800007e0]:sd a7, 328(a5)<br> |
|  43|[0x800026b8]<br>0x0000000000000001|- rs1_val == 3864061 and rm_val == 0  #nosat<br>                                                  |[0x800007ec]:fcvt.d.l ft11, t6, dyn<br> [0x800007f0]:csrrs a7, fflags, zero<br> [0x800007f4]:fsd ft11, 336(a5)<br> [0x800007f8]:sd a7, 344(a5)<br> |
|  44|[0x800026c8]<br>0x0000000000000001|- rs1_val == 1848861 and rm_val == 0  #nosat<br>                                                  |[0x80000804]:fcvt.d.l ft11, t6, dyn<br> [0x80000808]:csrrs a7, fflags, zero<br> [0x8000080c]:fsd ft11, 352(a5)<br> [0x80000810]:sd a7, 360(a5)<br> |
|  45|[0x800026d8]<br>0x0000000000000001|- rs1_val == 896618 and rm_val == 0  #nosat<br>                                                   |[0x8000081c]:fcvt.d.l ft11, t6, dyn<br> [0x80000820]:csrrs a7, fflags, zero<br> [0x80000824]:fsd ft11, 368(a5)<br> [0x80000828]:sd a7, 376(a5)<br> |
|  46|[0x800026e8]<br>0x0000000000000001|- rs1_val == 334857 and rm_val == 0  #nosat<br>                                                   |[0x80000834]:fcvt.d.l ft11, t6, dyn<br> [0x80000838]:csrrs a7, fflags, zero<br> [0x8000083c]:fsd ft11, 384(a5)<br> [0x80000840]:sd a7, 392(a5)<br> |
|  47|[0x800026f8]<br>0x0000000000000001|- rs1_val == 241276 and rm_val == 0  #nosat<br>                                                   |[0x8000084c]:fcvt.d.l ft11, t6, dyn<br> [0x80000850]:csrrs a7, fflags, zero<br> [0x80000854]:fsd ft11, 400(a5)<br> [0x80000858]:sd a7, 408(a5)<br> |
|  48|[0x80002708]<br>0x0000000000000001|- rs1_val == 71376 and rm_val == 0  #nosat<br>                                                    |[0x80000864]:fcvt.d.l ft11, t6, dyn<br> [0x80000868]:csrrs a7, fflags, zero<br> [0x8000086c]:fsd ft11, 416(a5)<br> [0x80000870]:sd a7, 424(a5)<br> |
|  49|[0x80002718]<br>0x0000000000000001|- rs1_val == 56436 and rm_val == 0  #nosat<br>                                                    |[0x8000087c]:fcvt.d.l ft11, t6, dyn<br> [0x80000880]:csrrs a7, fflags, zero<br> [0x80000884]:fsd ft11, 432(a5)<br> [0x80000888]:sd a7, 440(a5)<br> |
|  50|[0x80002728]<br>0x0000000000000001|- rs1_val == 24575 and rm_val == 0  #nosat<br>                                                    |[0x80000894]:fcvt.d.l ft11, t6, dyn<br> [0x80000898]:csrrs a7, fflags, zero<br> [0x8000089c]:fsd ft11, 448(a5)<br> [0x800008a0]:sd a7, 456(a5)<br> |
|  51|[0x80002738]<br>0x0000000000000001|- rs1_val == 9438 and rm_val == 0  #nosat<br>                                                     |[0x800008ac]:fcvt.d.l ft11, t6, dyn<br> [0x800008b0]:csrrs a7, fflags, zero<br> [0x800008b4]:fsd ft11, 464(a5)<br> [0x800008b8]:sd a7, 472(a5)<br> |
|  52|[0x80002748]<br>0x0000000000000001|- rs1_val == 6781 and rm_val == 0  #nosat<br>                                                     |[0x800008c4]:fcvt.d.l ft11, t6, dyn<br> [0x800008c8]:csrrs a7, fflags, zero<br> [0x800008cc]:fsd ft11, 480(a5)<br> [0x800008d0]:sd a7, 488(a5)<br> |
|  53|[0x80002758]<br>0x0000000000000001|- rs1_val == 4055 and rm_val == 0  #nosat<br>                                                     |[0x800008dc]:fcvt.d.l ft11, t6, dyn<br> [0x800008e0]:csrrs a7, fflags, zero<br> [0x800008e4]:fsd ft11, 496(a5)<br> [0x800008e8]:sd a7, 504(a5)<br> |
|  54|[0x80002768]<br>0x0000000000000001|- rs1_val == 1094 and rm_val == 0  #nosat<br>                                                     |[0x800008f4]:fcvt.d.l ft11, t6, dyn<br> [0x800008f8]:csrrs a7, fflags, zero<br> [0x800008fc]:fsd ft11, 512(a5)<br> [0x80000900]:sd a7, 520(a5)<br> |
|  55|[0x80002778]<br>0x0000000000000001|- rs1_val == 676 and rm_val == 0  #nosat<br>                                                      |[0x8000090c]:fcvt.d.l ft11, t6, dyn<br> [0x80000910]:csrrs a7, fflags, zero<br> [0x80000914]:fsd ft11, 528(a5)<br> [0x80000918]:sd a7, 536(a5)<br> |
|  56|[0x80002788]<br>0x0000000000000001|- rs1_val == 398 and rm_val == 0  #nosat<br>                                                      |[0x80000924]:fcvt.d.l ft11, t6, dyn<br> [0x80000928]:csrrs a7, fflags, zero<br> [0x8000092c]:fsd ft11, 544(a5)<br> [0x80000930]:sd a7, 552(a5)<br> |
|  57|[0x80002798]<br>0x0000000000000001|- rs1_val == 253 and rm_val == 0  #nosat<br>                                                      |[0x8000093c]:fcvt.d.l ft11, t6, dyn<br> [0x80000940]:csrrs a7, fflags, zero<br> [0x80000944]:fsd ft11, 560(a5)<br> [0x80000948]:sd a7, 568(a5)<br> |
|  58|[0x800027a8]<br>0x0000000000000001|- rs1_val == 123 and rm_val == 0  #nosat<br>                                                      |[0x80000954]:fcvt.d.l ft11, t6, dyn<br> [0x80000958]:csrrs a7, fflags, zero<br> [0x8000095c]:fsd ft11, 576(a5)<br> [0x80000960]:sd a7, 584(a5)<br> |
|  59|[0x800027b8]<br>0x0000000000000001|- rs1_val == 45 and rm_val == 0  #nosat<br>                                                       |[0x8000096c]:fcvt.d.l ft11, t6, dyn<br> [0x80000970]:csrrs a7, fflags, zero<br> [0x80000974]:fsd ft11, 592(a5)<br> [0x80000978]:sd a7, 600(a5)<br> |
|  60|[0x800027c8]<br>0x0000000000000001|- rs1_val == 16 and rm_val == 0  #nosat<br>                                                       |[0x80000984]:fcvt.d.l ft11, t6, dyn<br> [0x80000988]:csrrs a7, fflags, zero<br> [0x8000098c]:fsd ft11, 608(a5)<br> [0x80000990]:sd a7, 616(a5)<br> |
|  61|[0x800027d8]<br>0x0000000000000001|- rs1_val == 15 and rm_val == 0  #nosat<br>                                                       |[0x8000099c]:fcvt.d.l ft11, t6, dyn<br> [0x800009a0]:csrrs a7, fflags, zero<br> [0x800009a4]:fsd ft11, 624(a5)<br> [0x800009a8]:sd a7, 632(a5)<br> |
|  62|[0x800027e8]<br>0x0000000000000001|- rs1_val == 7 and rm_val == 0  #nosat<br>                                                        |[0x800009b4]:fcvt.d.l ft11, t6, dyn<br> [0x800009b8]:csrrs a7, fflags, zero<br> [0x800009bc]:fsd ft11, 640(a5)<br> [0x800009c0]:sd a7, 648(a5)<br> |
|  63|[0x800027f8]<br>0x0000000000000001|- rs1_val == 2 and rm_val == 0  #nosat<br>                                                        |[0x800009cc]:fcvt.d.l ft11, t6, dyn<br> [0x800009d0]:csrrs a7, fflags, zero<br> [0x800009d4]:fsd ft11, 656(a5)<br> [0x800009d8]:sd a7, 664(a5)<br> |
|  64|[0x80002808]<br>0x0000000000000001|- rs1_val == 1 and rm_val == 0  #nosat<br>                                                        |[0x800009e4]:fcvt.d.l ft11, t6, dyn<br> [0x800009e8]:csrrs a7, fflags, zero<br> [0x800009ec]:fsd ft11, 672(a5)<br> [0x800009f0]:sd a7, 680(a5)<br> |
|  65|[0x80002818]<br>0x0000000000000001|- rs1_val == 2086309477244717835 and rm_val == 0  #nosat<br>                                      |[0x800009fc]:fcvt.d.l ft11, t6, dyn<br> [0x80000a00]:csrrs a7, fflags, zero<br> [0x80000a04]:fsd ft11, 688(a5)<br> [0x80000a08]:sd a7, 696(a5)<br> |
