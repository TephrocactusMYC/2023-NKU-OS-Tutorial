lab4:进程管理
========================================


实验2/3完成了物理和虚拟内存管理，这给创建内核线程（内核线程是一种特殊的进程）打下了提供内存管理的基础。当一个程序加载到内存中运行时，首先通过ucore OS的内存管理子系统分配合适的空间，然后就需要考虑如何分时使用CPU来“并发”执行多个程序，让每个运行的程序（这里用线程或进程表示）“感到”它们各自拥有“自己”的CPU。
.. _本章内容:

本章内容
-------------------------------------

.. toctree::
   :maxdepth: 6

   lab4-1/lab4_1_goals
   lab4-2/index
   lab4-3/index
   lab4-4/lab4_4_labs_requirement

