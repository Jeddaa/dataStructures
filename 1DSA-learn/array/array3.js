var addToArrayForm = function (num, k) {
  const leng = num.length;
  if (leng == 0) {
    return Array.from(String(k, Number));
  }
  const test = BigInt(num.join('')) + BigInt(k);
  console.log(test)
  return Array.from(String(test, Number));
};

console.log(addToArrayForm([1, 2, 3], 32));
