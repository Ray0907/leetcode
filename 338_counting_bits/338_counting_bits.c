/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
// Allocate memory to store the results
    int* result = (int*)malloc((n + 1) * sizeof(int));
    
    // Iterate from 0 to n
    for (int i = 0; i <= n; i++) {
        int num = i;
        int count = 0;
        
        // Count the number of set bits in the binary representation of the current number
        while (num) {
            count += num & 1;
            num >>= 1;
        }
        
        // Store the result in the result array
        result[i] = count;
    }
    
    // Set the size of the returned result
    *returnSize = n + 1;
    
    return result;
    
}
