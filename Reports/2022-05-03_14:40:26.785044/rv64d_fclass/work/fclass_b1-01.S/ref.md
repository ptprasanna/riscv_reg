
# Data Propagation Report

- **STAT1** : Number of instructions that hit unique coverpoints and update the signature.
- **STAT2** : Number of instructions that hit covepoints which are not unique but still update the signature
- **STAT3** : Number of instructions that hit a unique coverpoint but do not update signature
- **STAT4** : Number of multiple signature updates for the same coverpoint
- **STAT5** : Number of times the signature was overwritten

| Param                     | Value    |
|---------------------------|----------|
| XLEN                      | 64      |
| TEST_REGION               | [('0x80000390', '0x80000700')]      |
| SIG_REGION                | [('0x80002310', '0x80002510', '64 dwords')]      |
| COV_LABELS                | fclass_b1      |
| TEST_NAME                 | /home/riscv/RRF/Reports/2022-05-03_14:40:26.785044/rv64d_fclass/work/fclass_b1-01.S/ref.S    |
| Total Number of coverpoints| 93     |
| Total Coverpoints Hit     | 89      |
| Total Signature Updates   | 64      |
| STAT1                     | 32      |
| STAT2                     | 0      |
| STAT3                     | 0     |
| STAT4                     | 32     |
| STAT5                     | 0     |

## Details for STAT2:

```


```

## Details of STAT3

```


```

## Details of STAT4:

```
Last Coverpoint : ['opcode : fclass.d', 'rd : x25', 'rs1 : f31', 'fs1 == 0 and fe1 == 0x000 and fm1 == 0x0000000000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800003b4]:fclass.d s9, ft11
	-[0x800003b8]:csrrs a7, fflags, zero
	-[0x800003bc]:sd s9, 0(a5)
Current Store : [0x800003c0] : sd a7, 8(a5) -- Store: [0x80002318]:0x0000000000000000




Last Coverpoint : ['rd : x5', 'rs1 : f0', 'fs1 == 1 and fe1 == 0x3f8 and fm1 == 0x0000000000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800003cc]:fclass.d t0, ft0
	-[0x800003d0]:csrrs a7, fflags, zero
	-[0x800003d4]:sd t0, 16(a5)
Current Store : [0x800003d8] : sd a7, 24(a5) -- Store: [0x80002328]:0x0000000000000000




Last Coverpoint : ['rd : x18', 'rs1 : f20', 'fs1 == 0 and fe1 == 0x3ff and fm1 == 0x0000000000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800003e4]:fclass.d s2, fs4
	-[0x800003e8]:csrrs a7, fflags, zero
	-[0x800003ec]:sd s2, 32(a5)
Current Store : [0x800003f0] : sd a7, 40(a5) -- Store: [0x80002338]:0x0000000000000000




Last Coverpoint : ['rd : x21', 'rs1 : f16', 'fs1 == 1 and fe1 == 0x7ff and fm1 == 0x0000000000001 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800003fc]:fclass.d s5, fa6
	-[0x80000400]:csrrs a7, fflags, zero
	-[0x80000404]:sd s5, 48(a5)
Current Store : [0x80000408] : sd a7, 56(a5) -- Store: [0x80002348]:0x0000000000000000




Last Coverpoint : ['rd : x16', 'rs1 : f7', 'fs1 == 0 and fe1 == 0x7ff and fm1 == 0x0000000000001 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000420]:fclass.d a6, ft7
	-[0x80000424]:csrrs s5, fflags, zero
	-[0x80000428]:sd a6, 0(s3)
Current Store : [0x8000042c] : sd s5, 8(s3) -- Store: [0x80002358]:0x0000000000000000




Last Coverpoint : ['rd : x7', 'rs1 : f6', 'fs1 == 1 and fe1 == 0x7ff and fm1 == 0x8000000000001 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000444]:fclass.d t2, ft6
	-[0x80000448]:csrrs a7, fflags, zero
	-[0x8000044c]:sd t2, 0(a5)
Current Store : [0x80000450] : sd a7, 8(a5) -- Store: [0x80002368]:0x0000000000000000




Last Coverpoint : ['rd : x9', 'rs1 : f8', 'fs1 == 0 and fe1 == 0x7ff and fm1 == 0x8000000000001 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x8000045c]:fclass.d s1, fs0
	-[0x80000460]:csrrs a7, fflags, zero
	-[0x80000464]:sd s1, 16(a5)
Current Store : [0x80000468] : sd a7, 24(a5) -- Store: [0x80002378]:0x0000000000000000




Last Coverpoint : ['rd : x13', 'rs1 : f29', 'fs1 == 1 and fe1 == 0x7ff and fm1 == 0x8000000000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000474]:fclass.d a3, ft9
	-[0x80000478]:csrrs a7, fflags, zero
	-[0x8000047c]:sd a3, 32(a5)
Current Store : [0x80000480] : sd a7, 40(a5) -- Store: [0x80002388]:0x0000000000000000




Last Coverpoint : ['rd : x30', 'rs1 : f26', 'fs1 == 0 and fe1 == 0x7ff and fm1 == 0x8000000000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x8000048c]:fclass.d t5, fs10
	-[0x80000490]:csrrs a7, fflags, zero
	-[0x80000494]:sd t5, 48(a5)
Current Store : [0x80000498] : sd a7, 56(a5) -- Store: [0x80002398]:0x0000000000000000




Last Coverpoint : ['rd : x17', 'rs1 : f4', 'fs1 == 1 and fe1 == 0x7ff and fm1 == 0x0000000000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800004b0]:fclass.d a7, ft4
	-[0x800004b4]:csrrs s5, fflags, zero
	-[0x800004b8]:sd a7, 0(s3)
Current Store : [0x800004bc] : sd s5, 8(s3) -- Store: [0x800023a8]:0x0000000000000000




Last Coverpoint : ['rd : x1', 'rs1 : f28', 'fs1 == 0 and fe1 == 0x7ff and fm1 == 0x0000000000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800004d4]:fclass.d ra, ft8
	-[0x800004d8]:csrrs a7, fflags, zero
	-[0x800004dc]:sd ra, 0(a5)
Current Store : [0x800004e0] : sd a7, 8(a5) -- Store: [0x800023b8]:0x0000000000000000




Last Coverpoint : ['rd : x28', 'rs1 : f27', 'fs1 == 1 and fe1 == 0x7fe and fm1 == 0xfffffffffffff and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800004ec]:fclass.d t3, fs11
	-[0x800004f0]:csrrs a7, fflags, zero
	-[0x800004f4]:sd t3, 16(a5)
Current Store : [0x800004f8] : sd a7, 24(a5) -- Store: [0x800023c8]:0x0000000000000000




Last Coverpoint : ['rd : x26', 'rs1 : f25', 'fs1 == 0 and fe1 == 0x7fe and fm1 == 0xfffffffffffff and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000504]:fclass.d s10, fs9
	-[0x80000508]:csrrs a7, fflags, zero
	-[0x8000050c]:sd s10, 32(a5)
Current Store : [0x80000510] : sd a7, 40(a5) -- Store: [0x800023d8]:0x0000000000000000




Last Coverpoint : ['rd : x8', 'rs1 : f11', 'fs1 == 1 and fe1 == 0x001 and fm1 == 0x0000000000002 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x8000051c]:fclass.d fp, fa1
	-[0x80000520]:csrrs a7, fflags, zero
	-[0x80000524]:sd fp, 48(a5)
Current Store : [0x80000528] : sd a7, 56(a5) -- Store: [0x800023e8]:0x0000000000000000




Last Coverpoint : ['rd : x22', 'rs1 : f10', 'fs1 == 0 and fe1 == 0x001 and fm1 == 0x0000000000002 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000534]:fclass.d s6, fa0
	-[0x80000538]:csrrs a7, fflags, zero
	-[0x8000053c]:sd s6, 64(a5)
Current Store : [0x80000540] : sd a7, 72(a5) -- Store: [0x800023f8]:0x0000000000000000




Last Coverpoint : ['rd : x29', 'rs1 : f12', 'fs1 == 1 and fe1 == 0x001 and fm1 == 0x0000000000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x8000054c]:fclass.d t4, fa2
	-[0x80000550]:csrrs a7, fflags, zero
	-[0x80000554]:sd t4, 80(a5)
Current Store : [0x80000558] : sd a7, 88(a5) -- Store: [0x80002408]:0x0000000000000000




Last Coverpoint : ['rd : x15', 'rs1 : f30', 'fs1 == 0 and fe1 == 0x001 and fm1 == 0x0000000000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000570]:fclass.d a5, ft10
	-[0x80000574]:csrrs s5, fflags, zero
	-[0x80000578]:sd a5, 0(s3)
Current Store : [0x8000057c] : sd s5, 8(s3) -- Store: [0x80002418]:0x0000000000000000




Last Coverpoint : ['rd : x4', 'rs1 : f14', 'fs1 == 1 and fe1 == 0x000 and fm1 == 0xfffffffffffff and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000594]:fclass.d tp, fa4
	-[0x80000598]:csrrs a7, fflags, zero
	-[0x8000059c]:sd tp, 0(a5)
Current Store : [0x800005a0] : sd a7, 8(a5) -- Store: [0x80002428]:0x0000000000000000




Last Coverpoint : ['rd : x27', 'rs1 : f1', 'fs1 == 0 and fe1 == 0x000 and fm1 == 0xfffffffffffff and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800005ac]:fclass.d s11, ft1
	-[0x800005b0]:csrrs a7, fflags, zero
	-[0x800005b4]:sd s11, 16(a5)
Current Store : [0x800005b8] : sd a7, 24(a5) -- Store: [0x80002438]:0x0000000000000000




Last Coverpoint : ['rd : x12', 'rs1 : f3', 'fs1 == 1 and fe1 == 0x000 and fm1 == 0x0000000000002 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800005c4]:fclass.d a2, ft3
	-[0x800005c8]:csrrs a7, fflags, zero
	-[0x800005cc]:sd a2, 32(a5)
Current Store : [0x800005d0] : sd a7, 40(a5) -- Store: [0x80002448]:0x0000000000000000




Last Coverpoint : ['rd : x31', 'rs1 : f19', 'fs1 == 0 and fe1 == 0x000 and fm1 == 0x0000000000002 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800005dc]:fclass.d t6, fs3
	-[0x800005e0]:csrrs a7, fflags, zero
	-[0x800005e4]:sd t6, 48(a5)
Current Store : [0x800005e8] : sd a7, 56(a5) -- Store: [0x80002458]:0x0000000000000000




Last Coverpoint : ['rd : x10', 'rs1 : f22', 'fs1 == 1 and fe1 == 0x000 and fm1 == 0x0000000000001 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800005f4]:fclass.d a0, fs6
	-[0x800005f8]:csrrs a7, fflags, zero
	-[0x800005fc]:sd a0, 64(a5)
Current Store : [0x80000600] : sd a7, 72(a5) -- Store: [0x80002468]:0x0000000000000000




Last Coverpoint : ['rd : x23', 'rs1 : f17', 'fs1 == 0 and fe1 == 0x000 and fm1 == 0x0000000000001 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x8000060c]:fclass.d s7, fa7
	-[0x80000610]:csrrs a7, fflags, zero
	-[0x80000614]:sd s7, 80(a5)
Current Store : [0x80000618] : sd a7, 88(a5) -- Store: [0x80002478]:0x0000000000000000




Last Coverpoint : ['rd : x3', 'rs1 : f9', 'fs1 == 1 and fe1 == 0x000 and fm1 == 0x0000000000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000624]:fclass.d gp, fs1
	-[0x80000628]:csrrs a7, fflags, zero
	-[0x8000062c]:sd gp, 96(a5)
Current Store : [0x80000630] : sd a7, 104(a5) -- Store: [0x80002488]:0x0000000000000000




Last Coverpoint : ['rd : x19', 'rs1 : f5']
Last Code Sequence : 
	-[0x8000063c]:fclass.d s3, ft5
	-[0x80000640]:csrrs a7, fflags, zero
	-[0x80000644]:sd s3, 112(a5)
Current Store : [0x80000648] : sd a7, 120(a5) -- Store: [0x80002498]:0x0000000000000000




Last Coverpoint : ['rd : x14', 'rs1 : f18']
Last Code Sequence : 
	-[0x80000654]:fclass.d a4, fs2
	-[0x80000658]:csrrs a7, fflags, zero
	-[0x8000065c]:sd a4, 128(a5)
Current Store : [0x80000660] : sd a7, 136(a5) -- Store: [0x800024a8]:0x0000000000000000




Last Coverpoint : ['rd : x24', 'rs1 : f2']
Last Code Sequence : 
	-[0x8000066c]:fclass.d s8, ft2
	-[0x80000670]:csrrs a7, fflags, zero
	-[0x80000674]:sd s8, 144(a5)
Current Store : [0x80000678] : sd a7, 152(a5) -- Store: [0x800024b8]:0x0000000000000000




Last Coverpoint : ['rd : x0', 'rs1 : f23']
Last Code Sequence : 
	-[0x80000684]:fclass.d zero, fs7
	-[0x80000688]:csrrs a7, fflags, zero
	-[0x8000068c]:sd zero, 160(a5)
Current Store : [0x80000690] : sd a7, 168(a5) -- Store: [0x800024c8]:0x0000000000000000




Last Coverpoint : ['rd : x6', 'rs1 : f21']
Last Code Sequence : 
	-[0x8000069c]:fclass.d t1, fs5
	-[0x800006a0]:csrrs a7, fflags, zero
	-[0x800006a4]:sd t1, 176(a5)
Current Store : [0x800006a8] : sd a7, 184(a5) -- Store: [0x800024d8]:0x0000000000000000




Last Coverpoint : ['rd : x20', 'rs1 : f15']
Last Code Sequence : 
	-[0x800006b4]:fclass.d s4, fa5
	-[0x800006b8]:csrrs a7, fflags, zero
	-[0x800006bc]:sd s4, 192(a5)
Current Store : [0x800006c0] : sd a7, 200(a5) -- Store: [0x800024e8]:0x0000000000000000




Last Coverpoint : ['rd : x2', 'rs1 : f24']
Last Code Sequence : 
	-[0x800006cc]:fclass.d sp, fs8
	-[0x800006d0]:csrrs a7, fflags, zero
	-[0x800006d4]:sd sp, 208(a5)
Current Store : [0x800006d8] : sd a7, 216(a5) -- Store: [0x800024f8]:0x0000000000000000




Last Coverpoint : ['rd : x11', 'rs1 : f13']
Last Code Sequence : 
	-[0x800006e4]:fclass.d a1, fa3
	-[0x800006e8]:csrrs a7, fflags, zero
	-[0x800006ec]:sd a1, 224(a5)
Current Store : [0x800006f0] : sd a7, 232(a5) -- Store: [0x80002508]:0x0000000000000000





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

|s.no|            signature             |                                                               coverpoints                                                                |                                                     code                                                     |
|---:|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
|   1|[0x80002310]<br>0x0000000000000010|- opcode : fclass.d<br> - rd : x25<br> - rs1 : f31<br> - fs1 == 0 and fe1 == 0x000 and fm1 == 0x0000000000000 and rm_val == 1  #nosat<br> |[0x800003b4]:fclass.d s9, ft11<br> [0x800003b8]:csrrs a7, fflags, zero<br> [0x800003bc]:sd s9, 0(a5)<br>      |
|   2|[0x80002320]<br>0x0000000000000002|- rd : x5<br> - rs1 : f0<br> - fs1 == 1 and fe1 == 0x3f8 and fm1 == 0x0000000000000 and rm_val == 1  #nosat<br>                           |[0x800003cc]:fclass.d t0, ft0<br> [0x800003d0]:csrrs a7, fflags, zero<br> [0x800003d4]:sd t0, 16(a5)<br>      |
|   3|[0x80002330]<br>0x0000000000000040|- rd : x18<br> - rs1 : f20<br> - fs1 == 0 and fe1 == 0x3ff and fm1 == 0x0000000000000 and rm_val == 1  #nosat<br>                         |[0x800003e4]:fclass.d s2, fs4<br> [0x800003e8]:csrrs a7, fflags, zero<br> [0x800003ec]:sd s2, 32(a5)<br>      |
|   4|[0x80002340]<br>0x0000000000000100|- rd : x21<br> - rs1 : f16<br> - fs1 == 1 and fe1 == 0x7ff and fm1 == 0x0000000000001 and rm_val == 1  #nosat<br>                         |[0x800003fc]:fclass.d s5, fa6<br> [0x80000400]:csrrs a7, fflags, zero<br> [0x80000404]:sd s5, 48(a5)<br>      |
|   5|[0x80002350]<br>0x0000000000000100|- rd : x16<br> - rs1 : f7<br> - fs1 == 0 and fe1 == 0x7ff and fm1 == 0x0000000000001 and rm_val == 1  #nosat<br>                          |[0x80000420]:fclass.d a6, ft7<br> [0x80000424]:csrrs s5, fflags, zero<br> [0x80000428]:sd a6, 0(s3)<br>       |
|   6|[0x80002360]<br>0x0000000000000200|- rd : x7<br> - rs1 : f6<br> - fs1 == 1 and fe1 == 0x7ff and fm1 == 0x8000000000001 and rm_val == 1  #nosat<br>                           |[0x80000444]:fclass.d t2, ft6<br> [0x80000448]:csrrs a7, fflags, zero<br> [0x8000044c]:sd t2, 0(a5)<br>       |
|   7|[0x80002370]<br>0x0000000000000200|- rd : x9<br> - rs1 : f8<br> - fs1 == 0 and fe1 == 0x7ff and fm1 == 0x8000000000001 and rm_val == 1  #nosat<br>                           |[0x8000045c]:fclass.d s1, fs0<br> [0x80000460]:csrrs a7, fflags, zero<br> [0x80000464]:sd s1, 16(a5)<br>      |
|   8|[0x80002380]<br>0x0000000000000200|- rd : x13<br> - rs1 : f29<br> - fs1 == 1 and fe1 == 0x7ff and fm1 == 0x8000000000000 and rm_val == 1  #nosat<br>                         |[0x80000474]:fclass.d a3, ft9<br> [0x80000478]:csrrs a7, fflags, zero<br> [0x8000047c]:sd a3, 32(a5)<br>      |
|   9|[0x80002390]<br>0x0000000000000200|- rd : x30<br> - rs1 : f26<br> - fs1 == 0 and fe1 == 0x7ff and fm1 == 0x8000000000000 and rm_val == 1  #nosat<br>                         |[0x8000048c]:fclass.d t5, fs10<br> [0x80000490]:csrrs a7, fflags, zero<br> [0x80000494]:sd t5, 48(a5)<br>     |
|  10|[0x800023a0]<br>0x0000000000000001|- rd : x17<br> - rs1 : f4<br> - fs1 == 1 and fe1 == 0x7ff and fm1 == 0x0000000000000 and rm_val == 1  #nosat<br>                          |[0x800004b0]:fclass.d a7, ft4<br> [0x800004b4]:csrrs s5, fflags, zero<br> [0x800004b8]:sd a7, 0(s3)<br>       |
|  11|[0x800023b0]<br>0x0000000000000080|- rd : x1<br> - rs1 : f28<br> - fs1 == 0 and fe1 == 0x7ff and fm1 == 0x0000000000000 and rm_val == 1  #nosat<br>                          |[0x800004d4]:fclass.d ra, ft8<br> [0x800004d8]:csrrs a7, fflags, zero<br> [0x800004dc]:sd ra, 0(a5)<br>       |
|  12|[0x800023c0]<br>0x0000000000000002|- rd : x28<br> - rs1 : f27<br> - fs1 == 1 and fe1 == 0x7fe and fm1 == 0xfffffffffffff and rm_val == 1  #nosat<br>                         |[0x800004ec]:fclass.d t3, fs11<br> [0x800004f0]:csrrs a7, fflags, zero<br> [0x800004f4]:sd t3, 16(a5)<br>     |
|  13|[0x800023d0]<br>0x0000000000000040|- rd : x26<br> - rs1 : f25<br> - fs1 == 0 and fe1 == 0x7fe and fm1 == 0xfffffffffffff and rm_val == 1  #nosat<br>                         |[0x80000504]:fclass.d s10, fs9<br> [0x80000508]:csrrs a7, fflags, zero<br> [0x8000050c]:sd s10, 32(a5)<br>    |
|  14|[0x800023e0]<br>0x0000000000000002|- rd : x8<br> - rs1 : f11<br> - fs1 == 1 and fe1 == 0x001 and fm1 == 0x0000000000002 and rm_val == 1  #nosat<br>                          |[0x8000051c]:fclass.d fp, fa1<br> [0x80000520]:csrrs a7, fflags, zero<br> [0x80000524]:sd fp, 48(a5)<br>      |
|  15|[0x800023f0]<br>0x0000000000000040|- rd : x22<br> - rs1 : f10<br> - fs1 == 0 and fe1 == 0x001 and fm1 == 0x0000000000002 and rm_val == 1  #nosat<br>                         |[0x80000534]:fclass.d s6, fa0<br> [0x80000538]:csrrs a7, fflags, zero<br> [0x8000053c]:sd s6, 64(a5)<br>      |
|  16|[0x80002400]<br>0x0000000000000002|- rd : x29<br> - rs1 : f12<br> - fs1 == 1 and fe1 == 0x001 and fm1 == 0x0000000000000 and rm_val == 1  #nosat<br>                         |[0x8000054c]:fclass.d t4, fa2<br> [0x80000550]:csrrs a7, fflags, zero<br> [0x80000554]:sd t4, 80(a5)<br>      |
|  17|[0x80002410]<br>0x0000000000000040|- rd : x15<br> - rs1 : f30<br> - fs1 == 0 and fe1 == 0x001 and fm1 == 0x0000000000000 and rm_val == 1  #nosat<br>                         |[0x80000570]:fclass.d a5, ft10<br> [0x80000574]:csrrs s5, fflags, zero<br> [0x80000578]:sd a5, 0(s3)<br>      |
|  18|[0x80002420]<br>0x0000000000000004|- rd : x4<br> - rs1 : f14<br> - fs1 == 1 and fe1 == 0x000 and fm1 == 0xfffffffffffff and rm_val == 1  #nosat<br>                          |[0x80000594]:fclass.d tp, fa4<br> [0x80000598]:csrrs a7, fflags, zero<br> [0x8000059c]:sd tp, 0(a5)<br>       |
|  19|[0x80002430]<br>0x0000000000000020|- rd : x27<br> - rs1 : f1<br> - fs1 == 0 and fe1 == 0x000 and fm1 == 0xfffffffffffff and rm_val == 1  #nosat<br>                          |[0x800005ac]:fclass.d s11, ft1<br> [0x800005b0]:csrrs a7, fflags, zero<br> [0x800005b4]:sd s11, 16(a5)<br>    |
|  20|[0x80002440]<br>0x0000000000000004|- rd : x12<br> - rs1 : f3<br> - fs1 == 1 and fe1 == 0x000 and fm1 == 0x0000000000002 and rm_val == 1  #nosat<br>                          |[0x800005c4]:fclass.d a2, ft3<br> [0x800005c8]:csrrs a7, fflags, zero<br> [0x800005cc]:sd a2, 32(a5)<br>      |
|  21|[0x80002450]<br>0x0000000000000020|- rd : x31<br> - rs1 : f19<br> - fs1 == 0 and fe1 == 0x000 and fm1 == 0x0000000000002 and rm_val == 1  #nosat<br>                         |[0x800005dc]:fclass.d t6, fs3<br> [0x800005e0]:csrrs a7, fflags, zero<br> [0x800005e4]:sd t6, 48(a5)<br>      |
|  22|[0x80002460]<br>0x0000000000000004|- rd : x10<br> - rs1 : f22<br> - fs1 == 1 and fe1 == 0x000 and fm1 == 0x0000000000001 and rm_val == 1  #nosat<br>                         |[0x800005f4]:fclass.d a0, fs6<br> [0x800005f8]:csrrs a7, fflags, zero<br> [0x800005fc]:sd a0, 64(a5)<br>      |
|  23|[0x80002470]<br>0x0000000000000020|- rd : x23<br> - rs1 : f17<br> - fs1 == 0 and fe1 == 0x000 and fm1 == 0x0000000000001 and rm_val == 1  #nosat<br>                         |[0x8000060c]:fclass.d s7, fa7<br> [0x80000610]:csrrs a7, fflags, zero<br> [0x80000614]:sd s7, 80(a5)<br>      |
|  24|[0x80002480]<br>0x0000000000000008|- rd : x3<br> - rs1 : f9<br> - fs1 == 1 and fe1 == 0x000 and fm1 == 0x0000000000000 and rm_val == 1  #nosat<br>                           |[0x80000624]:fclass.d gp, fs1<br> [0x80000628]:csrrs a7, fflags, zero<br> [0x8000062c]:sd gp, 96(a5)<br>      |
|  25|[0x80002490]<br>0x0000000000000010|- rd : x19<br> - rs1 : f5<br>                                                                                                             |[0x8000063c]:fclass.d s3, ft5<br> [0x80000640]:csrrs a7, fflags, zero<br> [0x80000644]:sd s3, 112(a5)<br>     |
|  26|[0x800024a0]<br>0x0000000000000010|- rd : x14<br> - rs1 : f18<br>                                                                                                            |[0x80000654]:fclass.d a4, fs2<br> [0x80000658]:csrrs a7, fflags, zero<br> [0x8000065c]:sd a4, 128(a5)<br>     |
|  27|[0x800024b0]<br>0x0000000000000010|- rd : x24<br> - rs1 : f2<br>                                                                                                             |[0x8000066c]:fclass.d s8, ft2<br> [0x80000670]:csrrs a7, fflags, zero<br> [0x80000674]:sd s8, 144(a5)<br>     |
|  28|[0x800024c0]<br>0x0000000000000000|- rd : x0<br> - rs1 : f23<br>                                                                                                             |[0x80000684]:fclass.d zero, fs7<br> [0x80000688]:csrrs a7, fflags, zero<br> [0x8000068c]:sd zero, 160(a5)<br> |
|  29|[0x800024d0]<br>0x0000000000000010|- rd : x6<br> - rs1 : f21<br>                                                                                                             |[0x8000069c]:fclass.d t1, fs5<br> [0x800006a0]:csrrs a7, fflags, zero<br> [0x800006a4]:sd t1, 176(a5)<br>     |
|  30|[0x800024e0]<br>0x0000000000000010|- rd : x20<br> - rs1 : f15<br>                                                                                                            |[0x800006b4]:fclass.d s4, fa5<br> [0x800006b8]:csrrs a7, fflags, zero<br> [0x800006bc]:sd s4, 192(a5)<br>     |
|  31|[0x800024f0]<br>0x0000000000000010|- rd : x2<br> - rs1 : f24<br>                                                                                                             |[0x800006cc]:fclass.d sp, fs8<br> [0x800006d0]:csrrs a7, fflags, zero<br> [0x800006d4]:sd sp, 208(a5)<br>     |
|  32|[0x80002500]<br>0x0000000000000010|- rd : x11<br> - rs1 : f13<br>                                                                                                            |[0x800006e4]:fclass.d a1, fa3<br> [0x800006e8]:csrrs a7, fflags, zero<br> [0x800006ec]:sd a1, 224(a5)<br>     |