import random, time, json
from typing import List, Dict

import sort


if __name__ == '__main__':
    results: Dict[str, List[float]] = {}
    types: List[str] = [
        'bubble sort', 
        'insertion sort',
        'selection sort',
        'merge sort',
        'quick sort',
        'heap sort',
        'radix sort',
        'custom sort',
    ]
    
    for type in types:
        results[type] = []
        
        for x in range(4):
            max_rand: int = 10**(x+2)
            end_val: int = int(max_rand / 10)
            array: List[int] = [random.randint(1, max_rand) for _ in range(end_val)]
        
            if type == 'bubble sort':
                start: float = time.time()
                sort.bubble_sort(array)
                res_time: float = time.time() - start
            elif type == 'insertion sort':
                start: float = time.time()
                sort.insertion_sort(array)
                res_time: float = time.time() - start
            elif type == 'selection sort':
                start: float = time.time()
                sort.selection_sort(array)
                res_time: float = time.time() - start
            elif type == 'merge sort':
                start: float = time.time()
                sort.merge_sort(array)
                res_time: float = time.time() - start
            elif type == 'quick sort':
                start: float = time.time()
                sort.quick_sort(array)
                res_time: float = time.time() - start
            elif type == 'heap sort':
                start: float = time.time()
                sort.heap_sort(array)
                res_time: float = time.time() - start
            elif type == 'radix sort':
                start: float = time.time()
                sort.radix_sort(array)
                res_time: float = time.time() - start
            elif type == 'custom sort':
                start: float = time.time()
                sort.custom_sort(array)
                res_time: float = time.time() - start
                
            results[type].append(res_time)
            
    print(json.dumps(results, indent=4))