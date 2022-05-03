
# Data Propagation Report

- **STAT1** : Number of instructions that hit unique coverpoints and update the signature.
- **STAT2** : Number of instructions that hit covepoints which are not unique but still update the signature
- **STAT3** : Number of instructions that hit a unique coverpoint but do not update signature
- **STAT4** : Number of multiple signature updates for the same coverpoint
- **STAT5** : Number of times the signature was overwritten

| Param                     | Value    |
|---------------------------|----------|
| XLEN                      | 32      |
| TEST_REGION               | [('0x800000f8', '0x80000460')]      |
| SIG_REGION                | [('0x80002210', '0x80002310', '64 words')]      |
| COV_LABELS                | fclass_b1      |
| TEST_NAME                 | /home/riscv/RRF/Reports/2022-05-02_18:24:38.736136/fclass/work/fclass_b1-01.S/ref.S    |
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
Last Coverpoint : ['opcode : fclass.s', 'rd : x19', 'rs1 : f17', 'fs1 == 0 and fe1 == 0x00 and fm1 == 0x000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x8000011c]:fclass.s s3, fa7
	-[0x80000120]:csrrs a7, fflags, zero
	-[0x80000124]:sw s3, 0(a5)
Current Store : [0x80000128] : sw a7, 4(a5) -- Store: [0x80002214]:0x00000000




Last Coverpoint : ['rd : x27', 'rs1 : f30', 'fs1 == 1 and fe1 == 0x7f and fm1 == 0x000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000134]:fclass.s s11, ft10
	-[0x80000138]:csrrs a7, fflags, zero
	-[0x8000013c]:sw s11, 8(a5)
Current Store : [0x80000140] : sw a7, 12(a5) -- Store: [0x8000221c]:0x00000000




Last Coverpoint : ['rd : x6', 'rs1 : f16', 'fs1 == 0 and fe1 == 0x7f and fm1 == 0x000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x8000014c]:fclass.s t1, fa6
	-[0x80000150]:csrrs a7, fflags, zero
	-[0x80000154]:sw t1, 16(a5)
Current Store : [0x80000158] : sw a7, 20(a5) -- Store: [0x80002224]:0x00000000




Last Coverpoint : ['rd : x9', 'rs1 : f25', 'fs1 == 1 and fe1 == 0xff and fm1 == 0x2aaaaa and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000164]:fclass.s s1, fs9
	-[0x80000168]:csrrs a7, fflags, zero
	-[0x8000016c]:sw s1, 24(a5)
Current Store : [0x80000170] : sw a7, 28(a5) -- Store: [0x8000222c]:0x00000000




Last Coverpoint : ['rd : x24', 'rs1 : f9', 'fs1 == 0 and fe1 == 0xff and fm1 == 0x000001 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x8000017c]:fclass.s s8, fs1
	-[0x80000180]:csrrs a7, fflags, zero
	-[0x80000184]:sw s8, 32(a5)
Current Store : [0x80000188] : sw a7, 36(a5) -- Store: [0x80002234]:0x00000000




Last Coverpoint : ['rd : x8', 'rs1 : f1', 'fs1 == 1 and fe1 == 0xff and fm1 == 0x455555 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000194]:fclass.s fp, ft1
	-[0x80000198]:csrrs a7, fflags, zero
	-[0x8000019c]:sw fp, 40(a5)
Current Store : [0x800001a0] : sw a7, 44(a5) -- Store: [0x8000223c]:0x00000000




Last Coverpoint : ['rd : x10', 'rs1 : f28', 'fs1 == 0 and fe1 == 0xff and fm1 == 0x400001 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800001ac]:fclass.s a0, ft8
	-[0x800001b0]:csrrs a7, fflags, zero
	-[0x800001b4]:sw a0, 48(a5)
Current Store : [0x800001b8] : sw a7, 52(a5) -- Store: [0x80002244]:0x00000000




Last Coverpoint : ['rd : x3', 'rs1 : f8', 'fs1 == 1 and fe1 == 0xff and fm1 == 0x400000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800001c4]:fclass.s gp, fs0
	-[0x800001c8]:csrrs a7, fflags, zero
	-[0x800001cc]:sw gp, 56(a5)
Current Store : [0x800001d0] : sw a7, 60(a5) -- Store: [0x8000224c]:0x00000000




Last Coverpoint : ['rd : x30', 'rs1 : f27', 'fs1 == 0 and fe1 == 0xff and fm1 == 0x400000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800001dc]:fclass.s t5, fs11
	-[0x800001e0]:csrrs a7, fflags, zero
	-[0x800001e4]:sw t5, 64(a5)
Current Store : [0x800001e8] : sw a7, 68(a5) -- Store: [0x80002254]:0x00000000




Last Coverpoint : ['rd : x28', 'rs1 : f14', 'fs1 == 1 and fe1 == 0xff and fm1 == 0x000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800001f4]:fclass.s t3, fa4
	-[0x800001f8]:csrrs a7, fflags, zero
	-[0x800001fc]:sw t3, 72(a5)
Current Store : [0x80000200] : sw a7, 76(a5) -- Store: [0x8000225c]:0x00000000




Last Coverpoint : ['rd : x20', 'rs1 : f18', 'fs1 == 0 and fe1 == 0xff and fm1 == 0x000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x8000020c]:fclass.s s4, fs2
	-[0x80000210]:csrrs a7, fflags, zero
	-[0x80000214]:sw s4, 80(a5)
Current Store : [0x80000218] : sw a7, 84(a5) -- Store: [0x80002264]:0x00000000




Last Coverpoint : ['rd : x16', 'rs1 : f24', 'fs1 == 1 and fe1 == 0xfe and fm1 == 0x7fffff and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000230]:fclass.s a6, fs8
	-[0x80000234]:csrrs s5, fflags, zero
	-[0x80000238]:sw a6, 0(s3)
Current Store : [0x8000023c] : sw s5, 4(s3) -- Store: [0x8000226c]:0x00000000




Last Coverpoint : ['rd : x4', 'rs1 : f13', 'fs1 == 0 and fe1 == 0xfe and fm1 == 0x7fffff and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000254]:fclass.s tp, fa3
	-[0x80000258]:csrrs a7, fflags, zero
	-[0x8000025c]:sw tp, 0(a5)
Current Store : [0x80000260] : sw a7, 4(a5) -- Store: [0x80002274]:0x00000000




Last Coverpoint : ['rd : x25', 'rs1 : f23', 'fs1 == 1 and fe1 == 0x01 and fm1 == 0x055555 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x8000026c]:fclass.s s9, fs7
	-[0x80000270]:csrrs a7, fflags, zero
	-[0x80000274]:sw s9, 8(a5)
Current Store : [0x80000278] : sw a7, 12(a5) -- Store: [0x8000227c]:0x00000000




Last Coverpoint : ['rd : x12', 'rs1 : f10', 'fs1 == 0 and fe1 == 0x01 and fm1 == 0x000001 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000284]:fclass.s a2, fa0
	-[0x80000288]:csrrs a7, fflags, zero
	-[0x8000028c]:sw a2, 16(a5)
Current Store : [0x80000290] : sw a7, 20(a5) -- Store: [0x80002284]:0x00000000




Last Coverpoint : ['rd : x11', 'rs1 : f29', 'fs1 == 1 and fe1 == 0x01 and fm1 == 0x000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x8000029c]:fclass.s a1, ft9
	-[0x800002a0]:csrrs a7, fflags, zero
	-[0x800002a4]:sw a1, 24(a5)
Current Store : [0x800002a8] : sw a7, 28(a5) -- Store: [0x8000228c]:0x00000000




Last Coverpoint : ['rd : x7', 'rs1 : f12', 'fs1 == 0 and fe1 == 0x01 and fm1 == 0x000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800002b4]:fclass.s t2, fa2
	-[0x800002b8]:csrrs a7, fflags, zero
	-[0x800002bc]:sw t2, 32(a5)
Current Store : [0x800002c0] : sw a7, 36(a5) -- Store: [0x80002294]:0x00000000




Last Coverpoint : ['rd : x23', 'rs1 : f15', 'fs1 == 1 and fe1 == 0x00 and fm1 == 0x7fffff and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800002cc]:fclass.s s7, fa5
	-[0x800002d0]:csrrs a7, fflags, zero
	-[0x800002d4]:sw s7, 40(a5)
Current Store : [0x800002d8] : sw a7, 44(a5) -- Store: [0x8000229c]:0x00000000




Last Coverpoint : ['rd : x15', 'rs1 : f2', 'fs1 == 0 and fe1 == 0x00 and fm1 == 0x7fffff and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x800002f0]:fclass.s a5, ft2
	-[0x800002f4]:csrrs s5, fflags, zero
	-[0x800002f8]:sw a5, 0(s3)
Current Store : [0x800002fc] : sw s5, 4(s3) -- Store: [0x800022a4]:0x00000000




Last Coverpoint : ['rd : x31', 'rs1 : f6', 'fs1 == 1 and fe1 == 0x00 and fm1 == 0x7ffffe and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000314]:fclass.s t6, ft6
	-[0x80000318]:csrrs a7, fflags, zero
	-[0x8000031c]:sw t6, 0(a5)
Current Store : [0x80000320] : sw a7, 4(a5) -- Store: [0x800022ac]:0x00000000




Last Coverpoint : ['rd : x5', 'rs1 : f31', 'fs1 == 0 and fe1 == 0x00 and fm1 == 0x000002 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x8000032c]:fclass.s t0, ft11
	-[0x80000330]:csrrs a7, fflags, zero
	-[0x80000334]:sw t0, 8(a5)
Current Store : [0x80000338] : sw a7, 12(a5) -- Store: [0x800022b4]:0x00000000




Last Coverpoint : ['rd : x22', 'rs1 : f7', 'fs1 == 1 and fe1 == 0x00 and fm1 == 0x000001 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000344]:fclass.s s6, ft7
	-[0x80000348]:csrrs a7, fflags, zero
	-[0x8000034c]:sw s6, 16(a5)
Current Store : [0x80000350] : sw a7, 20(a5) -- Store: [0x800022bc]:0x00000000




Last Coverpoint : ['rd : x1', 'rs1 : f11', 'fs1 == 0 and fe1 == 0x00 and fm1 == 0x000001 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x8000035c]:fclass.s ra, fa1
	-[0x80000360]:csrrs a7, fflags, zero
	-[0x80000364]:sw ra, 24(a5)
Current Store : [0x80000368] : sw a7, 28(a5) -- Store: [0x800022c4]:0x00000000




Last Coverpoint : ['rd : x13', 'rs1 : f20', 'fs1 == 1 and fe1 == 0x00 and fm1 == 0x000000 and rm_val == 1  #nosat']
Last Code Sequence : 
	-[0x80000374]:fclass.s a3, fs4
	-[0x80000378]:csrrs a7, fflags, zero
	-[0x8000037c]:sw a3, 32(a5)
Current Store : [0x80000380] : sw a7, 36(a5) -- Store: [0x800022cc]:0x00000000




Last Coverpoint : ['rd : x21', 'rs1 : f5']
Last Code Sequence : 
	-[0x8000038c]:fclass.s s5, ft5
	-[0x80000390]:csrrs a7, fflags, zero
	-[0x80000394]:sw s5, 40(a5)
Current Store : [0x80000398] : sw a7, 44(a5) -- Store: [0x800022d4]:0x00000000




Last Coverpoint : ['rd : x0', 'rs1 : f19']
Last Code Sequence : 
	-[0x800003a4]:fclass.s zero, fs3
	-[0x800003a8]:csrrs a7, fflags, zero
	-[0x800003ac]:sw zero, 48(a5)
Current Store : [0x800003b0] : sw a7, 52(a5) -- Store: [0x800022dc]:0x00000000




Last Coverpoint : ['rd : x17', 'rs1 : f22']
Last Code Sequence : 
	-[0x800003c8]:fclass.s a7, fs6
	-[0x800003cc]:csrrs s5, fflags, zero
	-[0x800003d0]:sw a7, 0(s3)
Current Store : [0x800003d4] : sw s5, 4(s3) -- Store: [0x800022e4]:0x00000000




Last Coverpoint : ['rd : x26', 'rs1 : f21']
Last Code Sequence : 
	-[0x800003ec]:fclass.s s10, fs5
	-[0x800003f0]:csrrs a7, fflags, zero
	-[0x800003f4]:sw s10, 0(a5)
Current Store : [0x800003f8] : sw a7, 4(a5) -- Store: [0x800022ec]:0x00000000




Last Coverpoint : ['rd : x14', 'rs1 : f4']
Last Code Sequence : 
	-[0x80000404]:fclass.s a4, ft4
	-[0x80000408]:csrrs a7, fflags, zero
	-[0x8000040c]:sw a4, 8(a5)
Current Store : [0x80000410] : sw a7, 12(a5) -- Store: [0x800022f4]:0x00000000




Last Coverpoint : ['rd : x2', 'rs1 : f26']
Last Code Sequence : 
	-[0x8000041c]:fclass.s sp, fs10
	-[0x80000420]:csrrs a7, fflags, zero
	-[0x80000424]:sw sp, 16(a5)
Current Store : [0x80000428] : sw a7, 20(a5) -- Store: [0x800022fc]:0x00000000




Last Coverpoint : ['rd : x18', 'rs1 : f0']
Last Code Sequence : 
	-[0x80000434]:fclass.s s2, ft0
	-[0x80000438]:csrrs a7, fflags, zero
	-[0x8000043c]:sw s2, 24(a5)
Current Store : [0x80000440] : sw a7, 28(a5) -- Store: [0x80002304]:0x00000000




Last Coverpoint : ['rd : x29', 'rs1 : f3']
Last Code Sequence : 
	-[0x8000044c]:fclass.s t4, ft3
	-[0x80000450]:csrrs a7, fflags, zero
	-[0x80000454]:sw t4, 32(a5)
Current Store : [0x80000458] : sw a7, 36(a5) -- Store: [0x8000230c]:0x00000000





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

|s.no|        signature         |                                                           coverpoints                                                            |                                                    code                                                     |
|---:|--------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
|   1|[0x80002210]<br>0x00000010|- opcode : fclass.s<br> - rd : x19<br> - rs1 : f17<br> - fs1 == 0 and fe1 == 0x00 and fm1 == 0x000000 and rm_val == 1  #nosat<br> |[0x8000011c]:fclass.s s3, fa7<br> [0x80000120]:csrrs a7, fflags, zero<br> [0x80000124]:sw s3, 0(a5)<br>      |
|   2|[0x80002218]<br>0x00000002|- rd : x27<br> - rs1 : f30<br> - fs1 == 1 and fe1 == 0x7f and fm1 == 0x000000 and rm_val == 1  #nosat<br>                         |[0x80000134]:fclass.s s11, ft10<br> [0x80000138]:csrrs a7, fflags, zero<br> [0x8000013c]:sw s11, 8(a5)<br>   |
|   3|[0x80002220]<br>0x00000040|- rd : x6<br> - rs1 : f16<br> - fs1 == 0 and fe1 == 0x7f and fm1 == 0x000000 and rm_val == 1  #nosat<br>                          |[0x8000014c]:fclass.s t1, fa6<br> [0x80000150]:csrrs a7, fflags, zero<br> [0x80000154]:sw t1, 16(a5)<br>     |
|   4|[0x80002228]<br>0x00000100|- rd : x9<br> - rs1 : f25<br> - fs1 == 1 and fe1 == 0xff and fm1 == 0x2aaaaa and rm_val == 1  #nosat<br>                          |[0x80000164]:fclass.s s1, fs9<br> [0x80000168]:csrrs a7, fflags, zero<br> [0x8000016c]:sw s1, 24(a5)<br>     |
|   5|[0x80002230]<br>0x00000100|- rd : x24<br> - rs1 : f9<br> - fs1 == 0 and fe1 == 0xff and fm1 == 0x000001 and rm_val == 1  #nosat<br>                          |[0x8000017c]:fclass.s s8, fs1<br> [0x80000180]:csrrs a7, fflags, zero<br> [0x80000184]:sw s8, 32(a5)<br>     |
|   6|[0x80002238]<br>0x00000200|- rd : x8<br> - rs1 : f1<br> - fs1 == 1 and fe1 == 0xff and fm1 == 0x455555 and rm_val == 1  #nosat<br>                           |[0x80000194]:fclass.s fp, ft1<br> [0x80000198]:csrrs a7, fflags, zero<br> [0x8000019c]:sw fp, 40(a5)<br>     |
|   7|[0x80002240]<br>0x00000200|- rd : x10<br> - rs1 : f28<br> - fs1 == 0 and fe1 == 0xff and fm1 == 0x400001 and rm_val == 1  #nosat<br>                         |[0x800001ac]:fclass.s a0, ft8<br> [0x800001b0]:csrrs a7, fflags, zero<br> [0x800001b4]:sw a0, 48(a5)<br>     |
|   8|[0x80002248]<br>0x00000200|- rd : x3<br> - rs1 : f8<br> - fs1 == 1 and fe1 == 0xff and fm1 == 0x400000 and rm_val == 1  #nosat<br>                           |[0x800001c4]:fclass.s gp, fs0<br> [0x800001c8]:csrrs a7, fflags, zero<br> [0x800001cc]:sw gp, 56(a5)<br>     |
|   9|[0x80002250]<br>0x00000200|- rd : x30<br> - rs1 : f27<br> - fs1 == 0 and fe1 == 0xff and fm1 == 0x400000 and rm_val == 1  #nosat<br>                         |[0x800001dc]:fclass.s t5, fs11<br> [0x800001e0]:csrrs a7, fflags, zero<br> [0x800001e4]:sw t5, 64(a5)<br>    |
|  10|[0x80002258]<br>0x00000001|- rd : x28<br> - rs1 : f14<br> - fs1 == 1 and fe1 == 0xff and fm1 == 0x000000 and rm_val == 1  #nosat<br>                         |[0x800001f4]:fclass.s t3, fa4<br> [0x800001f8]:csrrs a7, fflags, zero<br> [0x800001fc]:sw t3, 72(a5)<br>     |
|  11|[0x80002260]<br>0x00000080|- rd : x20<br> - rs1 : f18<br> - fs1 == 0 and fe1 == 0xff and fm1 == 0x000000 and rm_val == 1  #nosat<br>                         |[0x8000020c]:fclass.s s4, fs2<br> [0x80000210]:csrrs a7, fflags, zero<br> [0x80000214]:sw s4, 80(a5)<br>     |
|  12|[0x80002268]<br>0x00000002|- rd : x16<br> - rs1 : f24<br> - fs1 == 1 and fe1 == 0xfe and fm1 == 0x7fffff and rm_val == 1  #nosat<br>                         |[0x80000230]:fclass.s a6, fs8<br> [0x80000234]:csrrs s5, fflags, zero<br> [0x80000238]:sw a6, 0(s3)<br>      |
|  13|[0x80002270]<br>0x00000040|- rd : x4<br> - rs1 : f13<br> - fs1 == 0 and fe1 == 0xfe and fm1 == 0x7fffff and rm_val == 1  #nosat<br>                          |[0x80000254]:fclass.s tp, fa3<br> [0x80000258]:csrrs a7, fflags, zero<br> [0x8000025c]:sw tp, 0(a5)<br>      |
|  14|[0x80002278]<br>0x00000002|- rd : x25<br> - rs1 : f23<br> - fs1 == 1 and fe1 == 0x01 and fm1 == 0x055555 and rm_val == 1  #nosat<br>                         |[0x8000026c]:fclass.s s9, fs7<br> [0x80000270]:csrrs a7, fflags, zero<br> [0x80000274]:sw s9, 8(a5)<br>      |
|  15|[0x80002280]<br>0x00000040|- rd : x12<br> - rs1 : f10<br> - fs1 == 0 and fe1 == 0x01 and fm1 == 0x000001 and rm_val == 1  #nosat<br>                         |[0x80000284]:fclass.s a2, fa0<br> [0x80000288]:csrrs a7, fflags, zero<br> [0x8000028c]:sw a2, 16(a5)<br>     |
|  16|[0x80002288]<br>0x00000002|- rd : x11<br> - rs1 : f29<br> - fs1 == 1 and fe1 == 0x01 and fm1 == 0x000000 and rm_val == 1  #nosat<br>                         |[0x8000029c]:fclass.s a1, ft9<br> [0x800002a0]:csrrs a7, fflags, zero<br> [0x800002a4]:sw a1, 24(a5)<br>     |
|  17|[0x80002290]<br>0x00000040|- rd : x7<br> - rs1 : f12<br> - fs1 == 0 and fe1 == 0x01 and fm1 == 0x000000 and rm_val == 1  #nosat<br>                          |[0x800002b4]:fclass.s t2, fa2<br> [0x800002b8]:csrrs a7, fflags, zero<br> [0x800002bc]:sw t2, 32(a5)<br>     |
|  18|[0x80002298]<br>0x00000004|- rd : x23<br> - rs1 : f15<br> - fs1 == 1 and fe1 == 0x00 and fm1 == 0x7fffff and rm_val == 1  #nosat<br>                         |[0x800002cc]:fclass.s s7, fa5<br> [0x800002d0]:csrrs a7, fflags, zero<br> [0x800002d4]:sw s7, 40(a5)<br>     |
|  19|[0x800022a0]<br>0x00000020|- rd : x15<br> - rs1 : f2<br> - fs1 == 0 and fe1 == 0x00 and fm1 == 0x7fffff and rm_val == 1  #nosat<br>                          |[0x800002f0]:fclass.s a5, ft2<br> [0x800002f4]:csrrs s5, fflags, zero<br> [0x800002f8]:sw a5, 0(s3)<br>      |
|  20|[0x800022a8]<br>0x00000004|- rd : x31<br> - rs1 : f6<br> - fs1 == 1 and fe1 == 0x00 and fm1 == 0x7ffffe and rm_val == 1  #nosat<br>                          |[0x80000314]:fclass.s t6, ft6<br> [0x80000318]:csrrs a7, fflags, zero<br> [0x8000031c]:sw t6, 0(a5)<br>      |
|  21|[0x800022b0]<br>0x00000020|- rd : x5<br> - rs1 : f31<br> - fs1 == 0 and fe1 == 0x00 and fm1 == 0x000002 and rm_val == 1  #nosat<br>                          |[0x8000032c]:fclass.s t0, ft11<br> [0x80000330]:csrrs a7, fflags, zero<br> [0x80000334]:sw t0, 8(a5)<br>     |
|  22|[0x800022b8]<br>0x00000004|- rd : x22<br> - rs1 : f7<br> - fs1 == 1 and fe1 == 0x00 and fm1 == 0x000001 and rm_val == 1  #nosat<br>                          |[0x80000344]:fclass.s s6, ft7<br> [0x80000348]:csrrs a7, fflags, zero<br> [0x8000034c]:sw s6, 16(a5)<br>     |
|  23|[0x800022c0]<br>0x00000020|- rd : x1<br> - rs1 : f11<br> - fs1 == 0 and fe1 == 0x00 and fm1 == 0x000001 and rm_val == 1  #nosat<br>                          |[0x8000035c]:fclass.s ra, fa1<br> [0x80000360]:csrrs a7, fflags, zero<br> [0x80000364]:sw ra, 24(a5)<br>     |
|  24|[0x800022c8]<br>0x00000008|- rd : x13<br> - rs1 : f20<br> - fs1 == 1 and fe1 == 0x00 and fm1 == 0x000000 and rm_val == 1  #nosat<br>                         |[0x80000374]:fclass.s a3, fs4<br> [0x80000378]:csrrs a7, fflags, zero<br> [0x8000037c]:sw a3, 32(a5)<br>     |
|  25|[0x800022d0]<br>0x00000010|- rd : x21<br> - rs1 : f5<br>                                                                                                     |[0x8000038c]:fclass.s s5, ft5<br> [0x80000390]:csrrs a7, fflags, zero<br> [0x80000394]:sw s5, 40(a5)<br>     |
|  26|[0x800022d8]<br>0x00000000|- rd : x0<br> - rs1 : f19<br>                                                                                                     |[0x800003a4]:fclass.s zero, fs3<br> [0x800003a8]:csrrs a7, fflags, zero<br> [0x800003ac]:sw zero, 48(a5)<br> |
|  27|[0x800022e0]<br>0x00000010|- rd : x17<br> - rs1 : f22<br>                                                                                                    |[0x800003c8]:fclass.s a7, fs6<br> [0x800003cc]:csrrs s5, fflags, zero<br> [0x800003d0]:sw a7, 0(s3)<br>      |
|  28|[0x800022e8]<br>0x00000010|- rd : x26<br> - rs1 : f21<br>                                                                                                    |[0x800003ec]:fclass.s s10, fs5<br> [0x800003f0]:csrrs a7, fflags, zero<br> [0x800003f4]:sw s10, 0(a5)<br>    |
|  29|[0x800022f0]<br>0x00000010|- rd : x14<br> - rs1 : f4<br>                                                                                                     |[0x80000404]:fclass.s a4, ft4<br> [0x80000408]:csrrs a7, fflags, zero<br> [0x8000040c]:sw a4, 8(a5)<br>      |
|  30|[0x800022f8]<br>0x00000010|- rd : x2<br> - rs1 : f26<br>                                                                                                     |[0x8000041c]:fclass.s sp, fs10<br> [0x80000420]:csrrs a7, fflags, zero<br> [0x80000424]:sw sp, 16(a5)<br>    |
|  31|[0x80002300]<br>0x00000010|- rd : x18<br> - rs1 : f0<br>                                                                                                     |[0x80000434]:fclass.s s2, ft0<br> [0x80000438]:csrrs a7, fflags, zero<br> [0x8000043c]:sw s2, 24(a5)<br>     |
|  32|[0x80002308]<br>0x00000010|- rd : x29<br> - rs1 : f3<br>                                                                                                     |[0x8000044c]:fclass.s t4, ft3<br> [0x80000450]:csrrs a7, fflags, zero<br> [0x80000454]:sw t4, 32(a5)<br>     |
