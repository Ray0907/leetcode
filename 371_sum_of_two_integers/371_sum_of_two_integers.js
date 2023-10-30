/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function (a, b) {
  while (b !== 0) {
    // 不帶進位的和
    var sum_without_carry = a ^ b;
    // 進位
    var carry = (a & b) << 1;
    a = sum_without_carry;
    b = carry;
  }
  return a;
};
