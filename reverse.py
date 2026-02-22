class Reverse:
    def rev(self, text):
        return " ".join(text.split()[::-1])
r = Reverse()
print(r.rev("Hello world this is Python"))