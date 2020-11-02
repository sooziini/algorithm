#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define SWAP(x, y, t) ((t)=(x), (x)=(y), (y)=(t))

void bubble_sort(int arr[], int n) {
	int tmp;
	for (int i = n - 1; i > 0; i--) {
		for (int j = 0; j < i; j++)
			if (arr[j] > arr[j + 1])
				SWAP(arr[j], arr[j + 1], tmp);
	}
}

int main() {
	int n, sum = 0;
	scanf("%d", &n);
	int* a = malloc(sizeof(int) * n);
	
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);

	bubble_sort(a, n);		// 오름차순으로 정렬
	
	for (int i = 0; i < n; i++)
		for (int j = 0; j <= i; j++)
			sum += a[j];
	
	printf("%d", sum);
}