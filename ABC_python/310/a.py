class Order:
    def __init__(self, N, P, Q, D):
        self.N = N
        self.P = P
        self.Q = Q
        self.D = D
        self.total_min_money = 10 ** 20
        
    def get_total_min_money(self):
        self.total_min_money = min(self.P, self.total_min_money)
        for d in self.D:
            self.total_min_money = min(self.Q + d, self.total_min_money)
            
        return self.total_min_money


def main():
    N, P, Q = map(int, input().split())
    D = list(map(int, input().split()))
    order = Order(N, P, Q, D)
    print(order.get_total_min_money())

if __name__ == "__main__":
    main()