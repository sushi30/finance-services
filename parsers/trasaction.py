from datetime import datetime


class Transaction:
    def __init__(self, date, business, category, comments, value, **kwargs):
        self.date = date
        self.business = business
        self.category = category
        self.comments = comments
        self.value = value
        self.other = kwargs
        self.normalize()

    def normalize(self):
        self.date = datetime.fromisoformat(self.date)
        self.value = float(self.value)

    def dumps(self):
        d = self.__dict__
        d["date"] = d["date"].isoformat()
        return d
