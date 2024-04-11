class SampleClass:
    def __init__(self, attribute):
        self.__attribute = attribute
    def __method(self):
        print(self.__attribute)


sample_instance = SampleClass("Hello!")
print(vars(sample_instance))

print(sample_instance._SampleClass__attribute)