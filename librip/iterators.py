@@ -0,0 +1,47 @@
# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        if type(items) is list:
            self.items = items
        else:
            self.generated_items = [i for i in items]
            self.items = self.generated_items

        self.limit = len(self.items)
        self.current = 0

        self.ignore_case = kwargs.get('ignore_case')

        if self.ignore_case:
            self.unique_dict = dict()
        else:
            self.unique = set()

    def __next__(self):
        if self.ignore_case:
            while self.items[self.current].lower() in self.unique_dict:
                if self.current < self.limit:
                    self.current += 1

                    if self.current >= self.limit:
                        raise StopIteration
                else:
                    break

            self.unique_dict.update({self.items[self.current].lower(): self.items[self.current]})
            return self.items[self.current]
        else:
            while self.items[self.current] in self.unique:
                if self.current < self.limit:
                    self.current += 1

                    if self.current >= self.limit:
                        raise StopIteration
                else:
                    break

            self.unique.add(self.items[self.current])
            return self.items[self.current]

    def __iter__(self):
        return self
