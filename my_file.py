from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from typing import List

def custom_filter(lst):
    new_lst = filter(lambda n: type(n) == int and n % 7 == 0, lst)
    return sum(new_lst) <= 83

some_list = [7, 14, 28, 32, 32, 56]


anonymous_filter = lambda s: s.lower().count('я') >= 23
# print(anonymous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))

admin_ids: List[int] = [173901673, 178876776, 197177271]

class IsAdmin(BoundFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message,*args, **kwargs):
        return message.from_user.id in self.admin_ids

print(type(admin_ids))