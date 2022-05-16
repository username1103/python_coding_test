def slice_two_dimensional_array(arr,rowStart,rowEnd,colStart,colEnd):
    return [row[colStart:colEnd] for row in arr[rowStart:rowEnd]]
