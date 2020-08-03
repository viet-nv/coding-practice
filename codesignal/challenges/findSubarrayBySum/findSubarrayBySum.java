
int[] findSubarrayBySum(int s, int[] arr) {
    int[] sum =  new int[arr.length];
    sum[0] = arr[0];
    for (int i = 1; i < arr.length; i++) {
        sum[i] = arr[i] + sum[i-1];
    }

    for (int i = 0; i < arr.length; i++) {
        if (sum[i] == s) {
            return new int[] {1, i+1};
        };
        int  j = find(sum[i] - s, sum, 0, i);
        if (j != -1) {
            return new int[] {j+2, i+1};
        }
    }
    return new int[]{-1};
}

int find(int x, int[] arr, int i, int j) {
    int mid = (i + j) / 2;
    if (arr[mid] == x) return mid;
    if (j > i) {
        if (arr[mid] < x) return find(x, arr, mid+1, j);
        return find(x, arr, i, mid-1);
    }
    return -1;
}
