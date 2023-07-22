# Ch3

## 两种像素范围的拟合

### pixel range 1

- x     [0,4096]
- y     [0,4096]

拟合结果

coeff_Tx
Out[22]: array([ 2.90965330e-06,  6.67369481e-09, -5.98777934e-03])

coeff_Ty
Out[23]: array([-6.67369511e-09,  2.90963570e-06, -5.87289722e-03])

### pixel range 2

pixel range:

- x     [-2552,6648]
- y     [-2552,6648]

拟合结果

coeff_Tx
Out[32]: array([ 2.90956804e-06,  6.67335620e-09, -5.98760330e-03])

coeff_Ty
Out[33]: array([-6.67339369e-09,  2.90947941e-06, -5.87258305e-03])





# Ch4

SDO 正常工作期间 视角固定，就是说，图像每个像素的角度一成不变。

那我直接存一个4096*4096 * 2 （Tx，Ty 两个角度）都数组就完了















assignment:
df  cudf   np/cp..array

how to save?

noy   npz  pickle??



#### float 64 32 16



| `dtype`      | character code | description                           |
| :----------- | :------------- | :------------------------------------ |
| `int8`       | `i1`           | 8-bit signed integer                  |
| `int16`      | `i2`           | 16-bit signed integer                 |
| `int32`      | `i4`           | 32-bit signed integer                 |
| `int64`      | `i8`           | 64-bit signed integer                 |
| `uint8`      | `u1`           | 8-bit unsigned integer                |
| `uint16`     | `u2`           | 16-bit unsigned integer               |
| `uint32`     | `u4`           | 32-bit unsigned integer               |
| `uint64`     | `u8`           | 64-bit unsigned integer               |
| `float16`    | `f2`           | 16-bit floating-point number          |
| `float32`    | `f4`           | 32-bit floating-point number          |
| `float64`    | `f8`           | 64-bit floating-point number          |
| `float128`   | `f16`          | 128-bit floating-point number         |
| `complex64`  | `c8`           | 64-bit complex floating-point number  |
| `complex128` | `c16`          | 128-bit complex floating-point number |
| `complex256` | `c32`          | 256-bit complex floating-point number |
| `bool`       | `?`            | Boolean (`True` or `False`)           |
| `unicode`    | `U`            | Unicode string                        |
| `object`     | `O`            | Python objects                        |



https://numpy.org/doc/stable/reference/generated/numpy.finfo.html

1. **cp.float64 (CuPy's equivalent of NumPy's `np.float64`):**
   - Data type: 64-bit floating-point
   - Range: Approximately ±1.7 × 10^308 to ±2.2 × 10^-308
   - Precision: Approximately 15 to 17 significant decimal digits
2. **cp.float32 (CuPy's equivalent of NumPy's `np.float32`):**
   - Data type: 32-bit floating-point
   - Range: Approximately ±3.4 × 10^38 to ±1.2 × 10^-38
   - Precision: Approximately 6 to 9 significant decimal digits
3. **cp.float16 (CuPy's equivalent of NumPy's `np.float16`):**
   - Data type: 16-bit floating-point (half-precision)
   - Range: Approximately ±65504 to ±5.96 × 10^-8
   - Precision: Approximately 3 to 4 significant decimal digits



`f8` (64-bit floating-point) has the same range and precision as `float64` in Python





1. np.int16 (int16):

   - Range: -32,768 to 32,767
   - Precision: Exact representation of 4 significant digits

2. np.int32 (int32):

   - Range: -2,147,483,648 to 2,147,483,647
   - Precision: Exact representation of 9 significant digits

3. np.int64 (int64):

   - Range: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
   - Precision: Exact representation of 18 significant digits

   





#### numpy array save

- Load `npy` and `npz`: `np.load()`
- Save a single array as `npy`: `np.save()`
- Save multiple arrays as `npz`: `np.savez()`
- Save multiple arrays as compressed `npz`: `np.savez_compressed()`



#### Df save

1. **CSV (Comma-Separated Values):** A text-based format where each value in the DataFrame is separated by a comma. It is widely used for data exchange and can be easily read and written using various tools and programming languages.


   By default, when using the `DataFrame.to_csv()` method in Pandas, the time values will be stored as strings in the CSV file

   

2. **Excel (`.xlsx`, `.xls`):** Microsoft Excel files, which can store DataFrames with multiple sheets. Pandas provides built-in support for reading and writing Excel files.

3. **Pickle:** A binary serialization format native to Python. It allows you to store complex Python objects, including DataFrames, in a compact binary representation.

4. **Parquet:** A columnar storage file format designed for big data environments. Parquet files are efficient for large DataFrames and are used in distributed computing systems.

5. **HDF5 (Hierarchical Data Format 5):** A versatile data format suitable for large datasets with complex structures. It allows hierarchical storage of data and is supported by libraries like `h5py` in Python.

6. **Feather:** A fast and lightweight binary file format optimized for sharing data between Python and R. Feather files are ideal for inter-language data exchange.

7. **JSON (JavaScript Object Notation):** A lightweight and human-readable text format used for data interchange between systems.

8. **Msgpack:** A binary serialization format that is more compact and faster than JSON. It is often used for efficient data exchange between different programming languages.

9. **Avro:** A data serialization system using JSON schemas. Avro files are commonly used in big data environments.

10. **SQL Database (e.g., MySQL, PostgreSQL):** Storing DataFrames in SQL databases allows for efficient querying and data management using SQL queries.

11. **SQLite Database:** A lightweight, serverless database engine that can store DataFrames as tables within a single file.

12. **Gzip Compressed CSV or Pickle:** You can compress CSV or Pickle files using Gzip to reduce storage space.

13. **Apache Arrow:** A cross-language development platform for in-memory data that allows efficient transfer of data between different systems.





### cuDF

https://docs.rapids.ai/api/cudf/stable/user_guide/10min/















### time consumption diff



but pack in file   takes 300ms , excute in one cell takes 60ms........







The discrepancy in execution time between calling the function from a separate Python file and directly copying it into a timeit cell is likely due to differences in context and setup. Let's explore a few reasons why this could be happening:

1. **Imports and Context**: When you copy the function directly into a timeit cell, it runs within the context of your current environment, and all imports and variables might already be preloaded, leading to faster execution. However, when calling the function from a separate Python file, the function might need to import required libraries and set up the environment, which adds overhead and increases the execution time.
2. **GPU/CPU Switching**: If your function relies on GPU-accelerated libraries like Cupy, the time taken for initialization and switching between GPU and CPU modes can impact the execution time. When copying the function directly into a timeit cell, it might inherit the GPU settings already applied, which reduces initialization time.
3. **Function Call Overhead**: When calling a function from a separate file, there is a slight overhead associated with the function call, especially if the function is being called multiple times. This overhead might be less noticeable when you copy the function directly into a timeit cell.
4. **Caching**: Depending on your environment or how the function is called, there might be caching mechanisms in place that affect the execution time of the function.

Overall, when measuring the performance of a function using `timeit`, it's essential to ensure that the test conditions are consistent to obtain meaningful results. The recommended approach is to use `timeit` to measure the function's performance in a real-world scenario, where the function is called from the original Python file. This way, you can gauge its performance accurately in the intended context.