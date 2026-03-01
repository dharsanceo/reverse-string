class Reverse:
    def rev(self, text):
        return " ".join(text.split()[::-1])
print(Reverse().rev("Hello how are you"))
