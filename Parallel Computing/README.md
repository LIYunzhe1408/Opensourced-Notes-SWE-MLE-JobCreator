### Processor and register
* Most application is <10% performance of peak.
* sequential -> parallel: 10x acceleration
* Load/write data is 100x the cost of +,*,&,etc.

How compilers wok?
* Check the program is legal
* translate into assembly code
* optimize the generated code

Compiler performs `register allocation` to decide when to load/store vs reuse.
* The compiler will build a graph, coloring the graph.

How they optimize?
* unrolls loops
* fuses loops(merge two together)
* reorder loops
* eliminates dead code
* reorder instructions to improve register reuse.

### Memory hierarchies
Two costs of memory access: 
  * Latency(cost to load/store, delay due to travel time)
  * Bandwidth(data throughput bytes/sec)

[On chip 1ns kB] Register in processors -> on-chip cache -> [Off the chip] SRAM(10ns MB) -> DRAM(100ns GB) -> Disk(10 ms TB) -> Cloud(10sec PB)
* Spatial locality: accessing things nearby previous accesses
* Temporary locality: reuse an item that was previously accessed

Cache is fast memory which keeps a copy of data based on the last second bits of memory address.
* cache hit - cheap

Approaches to handling memory latency
* Reuse values in fast memory(bandwidth filtering)
* Move larger chunks(achieve higher bandwidth)
* [Concurrency]Issue multiple read/write in singe instruction(higher bw)
* [Concurrency]Issue multiple read/write in parallel (hide latency)
$$Concurrency=latency\times{bandwidth}$$

Memory Benchmark - -CacheBench
* Allocate memory and load up data to see how long it takes
* Noise will be existing, run many times and take the average

Takeaway:
* Performance is complicated, depending on many factors
* Memory is hierarchical
* Trends: growing gap
* Little's Law: concurrency to overlap latency


### Parallelism
pipelining for laundry example.
* BW=loads/hour
* latency=wash+dry+fold
* [Questions] Each step is parallel or the step can be parallelized

Single Instruction Multiple Data
* Different data types or precisions are performed same instructions(add, multiply)

Another compiler optimization:
* Strip-mine: Turn one loop into nested one
* Strip-interchange=tiling

Takeaway
* Even serial processors use parallelism
* Compiler helps with this, but the programmer should do the right things

### Case study: matrix multiply
Why?
* Dominate training time in deep learning

Call a library like GEMM is the best way to do this except the hw.

Evaluate computational intensity

Naive -> Blocked Matrix Multiply (Turn N-by-N matrices into b-by-b subblocks)