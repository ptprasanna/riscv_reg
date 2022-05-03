
# Data Propagation Report

- **STAT1** : Number of instructions that hit unique coverpoints and update the signature.
- **STAT2** : Number of instructions that hit covepoints which are not unique but still update the signature
- **STAT3** : Number of instructions that hit a unique coverpoint but do not update signature
- **STAT4** : Number of multiple signature updates for the same coverpoint
- **STAT5** : Number of times the signature was overwritten

| Param                     | Value    |
|---------------------------|----------|
| XLEN                      | 64      |
| TEST_REGION               | [('0x80000390', '0x800006f0')]      |
| SIG_REGION                | [('0x80002310', '0x80002510', '64 dwords')]      |
| COV_LABELS                | fcvt.d.l_b25      |
| TEST_NAME                 | /home/riscv/RRF/Reports/2022-05-03_13:14:14.044280/rv64d_fcvt.d.l/work/fcvt.d.l_b25-01.S/ref.S    |
| Total Number of coverpoints| 76     |
| Total Coverpoints Hit     | 72      |
| Total Signature Updates   | 32      |
| STAT1                     | 32      |
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

|s.no|            signature             |                                           coverpoints                                           |                                                                       code                                                                        |
|---:|----------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|   1|[0x80002318]<br>0x0000000000000000|- opcode : fcvt.d.l<br> - rs1 : x8<br> - rd : f31<br> - rs1_val == 0 and rm_val == 0  #nosat<br> |[0x800003b4]:fcvt.d.l ft11, fp, dyn<br> [0x800003b8]:csrrs a7, fflags, zero<br> [0x800003bc]:fsd ft11, 0(a5)<br> [0x800003c0]:sd a7, 8(a5)<br>     |
|   2|[0x80002328]<br>0x0000000000000000|- rs1 : x14<br> - rd : f16<br> - rs1_val == -5270258713649211392 and rm_val == 0  #nosat<br>     |[0x800003cc]:fcvt.d.l fa6, a4, dyn<br> [0x800003d0]:csrrs a7, fflags, zero<br> [0x800003d4]:fsd fa6, 16(a5)<br> [0x800003d8]:sd a7, 24(a5)<br>     |
|   3|[0x80002338]<br>0x0000000000000000|- rs1 : x4<br> - rd : f20<br> - rs1_val == 5270258713649211392 and rm_val == 0  #nosat<br>       |[0x800003e4]:fcvt.d.l fs4, tp, dyn<br> [0x800003e8]:csrrs a7, fflags, zero<br> [0x800003ec]:fsd fs4, 32(a5)<br> [0x800003f0]:sd a7, 40(a5)<br>     |
|   4|[0x80002348]<br>0x0000000000000001|- rs1 : x30<br> - rd : f3<br> - rs1_val == -9223372036854775807 and rm_val == 0  #nosat<br>      |[0x800003fc]:fcvt.d.l ft3, t5, dyn<br> [0x80000400]:csrrs a7, fflags, zero<br> [0x80000404]:fsd ft3, 48(a5)<br> [0x80000408]:sd a7, 56(a5)<br>     |
|   5|[0x80002358]<br>0x0000000000000001|- rs1 : x24<br> - rd : f0<br> - rs1_val == 9223372036854775807 and rm_val == 0  #nosat<br>       |[0x80000414]:fcvt.d.l ft0, s8, dyn<br> [0x80000418]:csrrs a7, fflags, zero<br> [0x8000041c]:fsd ft0, 64(a5)<br> [0x80000420]:sd a7, 72(a5)<br>     |
|   6|[0x80002368]<br>0x0000000000000001|- rs1 : x26<br> - rd : f14<br> - rs1_val == -1 and rm_val == 0  #nosat<br>                       |[0x8000042c]:fcvt.d.l fa4, s10, dyn<br> [0x80000430]:csrrs a7, fflags, zero<br> [0x80000434]:fsd fa4, 80(a5)<br> [0x80000438]:sd a7, 88(a5)<br>    |
|   7|[0x80002378]<br>0x0000000000000001|- rs1 : x3<br> - rd : f6<br> - rs1_val == 1 and rm_val == 0  #nosat<br>                          |[0x80000444]:fcvt.d.l ft6, gp, dyn<br> [0x80000448]:csrrs a7, fflags, zero<br> [0x8000044c]:fsd ft6, 96(a5)<br> [0x80000450]:sd a7, 104(a5)<br>    |
|   8|[0x80002388]<br>0x0000000000000001|- rs1 : x1<br> - rd : f8<br>                                                                     |[0x8000045c]:fcvt.d.l fs0, ra, dyn<br> [0x80000460]:csrrs a7, fflags, zero<br> [0x80000464]:fsd fs0, 112(a5)<br> [0x80000468]:sd a7, 120(a5)<br>   |
|   9|[0x80002398]<br>0x0000000000000001|- rs1 : x18<br> - rd : f2<br>                                                                    |[0x80000474]:fcvt.d.l ft2, s2, dyn<br> [0x80000478]:csrrs a7, fflags, zero<br> [0x8000047c]:fsd ft2, 128(a5)<br> [0x80000480]:sd a7, 136(a5)<br>   |
|  10|[0x800023a8]<br>0x0000000000000001|- rs1 : x0<br> - rd : f10<br>                                                                    |[0x8000048c]:fcvt.d.l fa0, zero, dyn<br> [0x80000490]:csrrs a7, fflags, zero<br> [0x80000494]:fsd fa0, 144(a5)<br> [0x80000498]:sd a7, 152(a5)<br> |
|  11|[0x800023b8]<br>0x0000000000000001|- rs1 : x6<br> - rd : f28<br>                                                                    |[0x800004a4]:fcvt.d.l ft8, t1, dyn<br> [0x800004a8]:csrrs a7, fflags, zero<br> [0x800004ac]:fsd ft8, 160(a5)<br> [0x800004b0]:sd a7, 168(a5)<br>   |
|  12|[0x800023c8]<br>0x0000000000000001|- rs1 : x12<br> - rd : f9<br>                                                                    |[0x800004bc]:fcvt.d.l fs1, a2, dyn<br> [0x800004c0]:csrrs a7, fflags, zero<br> [0x800004c4]:fsd fs1, 176(a5)<br> [0x800004c8]:sd a7, 184(a5)<br>   |
|  13|[0x800023d8]<br>0x0000000000000001|- rs1 : x27<br> - rd : f23<br>                                                                   |[0x800004d4]:fcvt.d.l fs7, s11, dyn<br> [0x800004d8]:csrrs a7, fflags, zero<br> [0x800004dc]:fsd fs7, 192(a5)<br> [0x800004e0]:sd a7, 200(a5)<br>  |
|  14|[0x800023e8]<br>0x0000000000000001|- rs1 : x16<br> - rd : f27<br>                                                                   |[0x800004f8]:fcvt.d.l fs11, a6, dyn<br> [0x800004fc]:csrrs s5, fflags, zero<br> [0x80000500]:fsd fs11, 0(s3)<br> [0x80000504]:sd s5, 8(s3)<br>     |
|  15|[0x800023f8]<br>0x0000000000000001|- rs1 : x25<br> - rd : f12<br>                                                                   |[0x8000051c]:fcvt.d.l fa2, s9, dyn<br> [0x80000520]:csrrs a7, fflags, zero<br> [0x80000524]:fsd fa2, 0(a5)<br> [0x80000528]:sd a7, 8(a5)<br>       |
|  16|[0x80002408]<br>0x0000000000000001|- rs1 : x10<br> - rd : f4<br>                                                                    |[0x80000534]:fcvt.d.l ft4, a0, dyn<br> [0x80000538]:csrrs a7, fflags, zero<br> [0x8000053c]:fsd ft4, 16(a5)<br> [0x80000540]:sd a7, 24(a5)<br>     |
|  17|[0x80002418]<br>0x0000000000000001|- rs1 : x15<br> - rd : f29<br>                                                                   |[0x80000558]:fcvt.d.l ft9, a5, dyn<br> [0x8000055c]:csrrs s5, fflags, zero<br> [0x80000560]:fsd ft9, 0(s3)<br> [0x80000564]:sd s5, 8(s3)<br>       |
|  18|[0x80002428]<br>0x0000000000000001|- rs1 : x9<br> - rd : f25<br>                                                                    |[0x8000057c]:fcvt.d.l fs9, s1, dyn<br> [0x80000580]:csrrs a7, fflags, zero<br> [0x80000584]:fsd fs9, 0(a5)<br> [0x80000588]:sd a7, 8(a5)<br>       |
|  19|[0x80002438]<br>0x0000000000000001|- rs1 : x23<br> - rd : f26<br>                                                                   |[0x80000594]:fcvt.d.l fs10, s7, dyn<br> [0x80000598]:csrrs a7, fflags, zero<br> [0x8000059c]:fsd fs10, 16(a5)<br> [0x800005a0]:sd a7, 24(a5)<br>   |
|  20|[0x80002448]<br>0x0000000000000001|- rs1 : x29<br> - rd : f5<br>                                                                    |[0x800005ac]:fcvt.d.l ft5, t4, dyn<br> [0x800005b0]:csrrs a7, fflags, zero<br> [0x800005b4]:fsd ft5, 32(a5)<br> [0x800005b8]:sd a7, 40(a5)<br>     |
|  21|[0x80002458]<br>0x0000000000000001|- rs1 : x5<br> - rd : f13<br>                                                                    |[0x800005c4]:fcvt.d.l fa3, t0, dyn<br> [0x800005c8]:csrrs a7, fflags, zero<br> [0x800005cc]:fsd fa3, 48(a5)<br> [0x800005d0]:sd a7, 56(a5)<br>     |
|  22|[0x80002468]<br>0x0000000000000001|- rs1 : x20<br> - rd : f21<br>                                                                   |[0x800005dc]:fcvt.d.l fs5, s4, dyn<br> [0x800005e0]:csrrs a7, fflags, zero<br> [0x800005e4]:fsd fs5, 64(a5)<br> [0x800005e8]:sd a7, 72(a5)<br>     |
|  23|[0x80002478]<br>0x0000000000000001|- rs1 : x19<br> - rd : f19<br>                                                                   |[0x800005f4]:fcvt.d.l fs3, s3, dyn<br> [0x800005f8]:csrrs a7, fflags, zero<br> [0x800005fc]:fsd fs3, 80(a5)<br> [0x80000600]:sd a7, 88(a5)<br>     |
|  24|[0x80002488]<br>0x0000000000000001|- rs1 : x31<br> - rd : f7<br>                                                                    |[0x8000060c]:fcvt.d.l ft7, t6, dyn<br> [0x80000610]:csrrs a7, fflags, zero<br> [0x80000614]:fsd ft7, 96(a5)<br> [0x80000618]:sd a7, 104(a5)<br>    |
|  25|[0x80002498]<br>0x0000000000000001|- rs1 : x11<br> - rd : f30<br>                                                                   |[0x80000624]:fcvt.d.l ft10, a1, dyn<br> [0x80000628]:csrrs a7, fflags, zero<br> [0x8000062c]:fsd ft10, 112(a5)<br> [0x80000630]:sd a7, 120(a5)<br> |
|  26|[0x800024a8]<br>0x0000000000000001|- rs1 : x13<br> - rd : f18<br>                                                                   |[0x8000063c]:fcvt.d.l fs2, a3, dyn<br> [0x80000640]:csrrs a7, fflags, zero<br> [0x80000644]:fsd fs2, 128(a5)<br> [0x80000648]:sd a7, 136(a5)<br>   |
|  27|[0x800024b8]<br>0x0000000000000001|- rs1 : x28<br> - rd : f15<br>                                                                   |[0x80000654]:fcvt.d.l fa5, t3, dyn<br> [0x80000658]:csrrs a7, fflags, zero<br> [0x8000065c]:fsd fa5, 144(a5)<br> [0x80000660]:sd a7, 152(a5)<br>   |
|  28|[0x800024c8]<br>0x0000000000000001|- rs1 : x22<br> - rd : f1<br>                                                                    |[0x8000066c]:fcvt.d.l ft1, s6, dyn<br> [0x80000670]:csrrs a7, fflags, zero<br> [0x80000674]:fsd ft1, 160(a5)<br> [0x80000678]:sd a7, 168(a5)<br>   |
|  29|[0x800024d8]<br>0x0000000000000001|- rs1 : x7<br> - rd : f22<br>                                                                    |[0x80000684]:fcvt.d.l fs6, t2, dyn<br> [0x80000688]:csrrs a7, fflags, zero<br> [0x8000068c]:fsd fs6, 176(a5)<br> [0x80000690]:sd a7, 184(a5)<br>   |
|  30|[0x800024e8]<br>0x0000000000000001|- rs1 : x2<br> - rd : f17<br>                                                                    |[0x8000069c]:fcvt.d.l fa7, sp, dyn<br> [0x800006a0]:csrrs a7, fflags, zero<br> [0x800006a4]:fsd fa7, 192(a5)<br> [0x800006a8]:sd a7, 200(a5)<br>   |
|  31|[0x800024f8]<br>0x0000000000000001|- rs1 : x21<br> - rd : f24<br>                                                                   |[0x800006b4]:fcvt.d.l fs8, s5, dyn<br> [0x800006b8]:csrrs a7, fflags, zero<br> [0x800006bc]:fsd fs8, 208(a5)<br> [0x800006c0]:sd a7, 216(a5)<br>   |
|  32|[0x80002508]<br>0x0000000000000001|- rs1 : x17<br> - rd : f11<br>                                                                   |[0x800006d8]:fcvt.d.l fa1, a7, dyn<br> [0x800006dc]:csrrs s5, fflags, zero<br> [0x800006e0]:fsd fa1, 0(s3)<br> [0x800006e4]:sd s5, 8(s3)<br>       |
