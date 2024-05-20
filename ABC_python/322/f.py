def n_ary(base, n, m):
    def from_base(num_str, base):
        """Convert a number from a given base to decimal (base 10)."""
        return int(num_str, base)
    
    def to_base(num, base):
        """Convert a decimal (base 10) number to a given base."""
        if num == 0:
            return "0"
        digits = []
        while num:
            digits.append(int(num % base))
            num //= base
        return ''.join(str(x) for x in digits[::-1])
    
    base_str = str(base)  # baseを文字列に変換
    decimal_number = from_base(base_str, n)
    result_num = to_base(decimal_number, m)
    
    return result_num
