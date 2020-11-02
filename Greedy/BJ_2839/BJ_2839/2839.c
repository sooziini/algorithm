#include <stdio.h>

int main(void) {
	int n;
	scanf("%d", &n);

	int count = -1;		// 배달하는 봉지의 최소 개수

	if (n % 5 == 0)
		count = n / 5;
	else {
		for (int i = (n / 5); i > 0; i--) {
			int j = n - (5 * i);
			if (j % 3 == 0) {
				count = i + (j / 3);
				break;
			}
		}
		if (count == -1) {
			if (n % 3 == 0)
				count = n / 3;
		}
	}
	
	printf("%d", count);
}