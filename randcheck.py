class RandomCracker:

    def __init__(self):
        self.mt = []
        self.counter = 0

    def submit(self, num):
        bits = self._to_bitarray(num)
        self.counter += 1
        self.mt.append(self._harden_inverse(bits))
        if self.counter == 624:
            self._regen()

    def _predict(self):
        if self.counter >= 624:
            self._regen()
    
def predict_getrandbits(self,k):
        if not self.state:
            print("Didn't recieve enough bits to predict")
            return 0
        if k == 0:
            return 0
        words = (k-1) // 32 + 1
        res = []
        for i in range(words):
            r = self._predict_32()
            if k < 32:
                r = [0]*(32-k) +r[:k]
            res = r + res
            k -= 32
        return self._to_int(res)
