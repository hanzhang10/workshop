// Team HE:: Han Zhang, Edwin Zheng
// SoftDev 
// K27 -- Basic functions in JavaScript
// 2022-02-03

function fact(n) {
	if (n <= 1)
		return 1;
	return (n * (fact (n - 1)));
}

function fibonacci(n) {
	if (n <= 2)
		return 1;
	return fibonacci(n-1) + fibonacci(n-2);
}
